# HTTP Endpoint Health Checker

## *Overview:*
The HTTP Endpoint Health Checker is a Python script designed to monitor the health of specified HTTP endpoints. The script checks each endpoint at regular intervals, logging their availability status and response times.

## *Features:*
- Periodic health checks for multiple HTTP endpoints.
- Configurable via a YAML file.
- Option for detailed output in test mode.
- Cumulative availability percentage calculation for each domain.
- Command-line argument support for easy usage.

## *Requirements:*
- Python 3 
- requests library 
- pyyaml library 
- argparse library 

## *Installation:*
- Ensure Python 3 is installed on your system.
- Install required Python libraries:
```bash
- pip install requests pyyaml
```

## *Usage:*
Run the script with the path to the configuration file [replace input.yaml file with path of desired yaml configured file].

```bash
python health_check.py input.yaml
```
Optionally, enable test mode for detailed output:
 ```bash
python health_check.py input.yaml --test
```
*Note:* I used input.yaml in same folder for testing the code, you can replace it with path of you desired configured yaml file.

## *Author*
Jayachandra Poluri
