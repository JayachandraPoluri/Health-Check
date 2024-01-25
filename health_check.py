import yaml
import requests
import time
import threading
from urllib.parse import urlparse
import argparse

def load_config(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}")
        return []
    except Exception as exc:
        print(f"An unexpected error occurred: {exc}")
        return []

def check_endpoint(endpoint, test_mode=False):
    url = endpoint['url']
    method = endpoint.get('method', 'GET')
    headers = endpoint.get('headers', {})
    body = endpoint.get('body', None)

    response = requests.request(method, url, headers=headers, data=body)
    latency = (response.elapsed).total_seconds() * 1000  # Convert to milliseconds

    is_up = response.status_code in range(200, 300) and latency < 500
    status = "UP" if is_up else "DOWN"

    if test_mode:
        print(f"Endpoint with name {endpoint['name']} has HTTP response code {response.status_code} and response latency is {latency:.2f} ms = {status}")

    return urlparse(url).netloc, is_up

def monitor_endpoints(endpoints, test_mode=False):
    total_requests = {}
    successful_requests = {}

    cycle = 1
    while True:
        if test_mode:
            print(f"Test cycle #{cycle} begins at time = {datetime.now().strftime('%H:%M:%S')}")

        for endpoint in endpoints:
            domain, is_up = check_endpoint(endpoint, test_mode)
            total_requests[domain] = total_requests.get(domain, 0) + 1
            if is_up:
                successful_requests[domain] = successful_requests.get(domain, 0) + 1

        if test_mode:
            print(f"Test cycle #{cycle} ends. The program logs to the console:")

        for domain in total_requests:
            if total_requests[domain] > 0:
                avail_percent = round(100 * successful_requests.get(domain, 0) / total_requests[domain])
                print(f"{domain} has {avail_percent}% availability percentage")

        cycle += 1
        time.sleep(15)

def main(file_path, test_mode):
    endpoints = load_config(file_path)
    monitor_thread = threading.Thread(target=monitor_endpoints, args=(endpoints, test_mode))
    monitor_thread.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Endpoint Health Checker")
    parser.add_argument("file_path", type=str, help="Path to the YAML configuration file")
    parser.add_argument("--test", action="store_true", help="Enable test mode for detailed output")
    args = parser.parse_args()

    main(args.file_path, args.test)
