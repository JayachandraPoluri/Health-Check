import yaml
import requests
import time
import threading
from urllib.parse import urlparse
from datetime import datetime

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

def check_endpoint(endpoint):
    url = endpoint['url']
    method = endpoint.get('method', 'GET')
    headers = endpoint.get('headers', {})
    body = endpoint.get('body', None)
    starttime = datetime.now()
    response = requests.request(method, url, headers=headers, data=body)
    latency = ((datetime.now() - starttime).total_seconds())*1000
    #print(latency)
    # latency = response.elapsed.total_seconds() * 10  # Convert to milliseconds
    is_up = response.status_code in range(200, 300) and latency < 500
    return urlparse(url).netloc, is_up

def monitor_endpoints(endpoints):
    total_requests = {}  # Total number of requests for each domain
    successful_requests = {}  # Number of successful ('UP') requests for each domain

    while True:
        for endpoint in endpoints:
            domain = urlparse(endpoint['url']).netloc
            try:
                _, is_up = check_endpoint(endpoint)
                total_requests[domain] = total_requests.get(domain, 0) + 1
                if is_up:
                    successful_requests[domain] = successful_requests.get(domain, 0) + 1
            except Exception as e:
                print(f"Error checking endpoint {endpoint['name']}: {e}")

        # Log the cumulative availability percentage for each domain
        for domain in total_requests:
            if total_requests[domain] > 0:
                avail_percent = round(100 * successful_requests.get(domain, 0) / total_requests[domain])
                print(f"{domain} has {avail_percent}% availability percentage")
        
        time.sleep(15)



def main(file_path):
    endpoints = load_config(file_path)
    monitor_thread = threading.Thread(target=monitor_endpoints, args=(endpoints,))
    monitor_thread.start()

if __name__ == "__main__":
    file_path = "input.yaml" 
    main(file_path)
