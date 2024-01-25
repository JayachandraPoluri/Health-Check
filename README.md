# HTTP Endpoint Health Checker
Overview
The HTTP Endpoint Health Checker is a Python script designed to monitor the health of specified HTTP endpoints. The script checks each endpoint at regular intervals, logging their availability status and response times.

Features
Periodic health checks for multiple HTTP endpoints.
Configurable via a YAML file.
Option for detailed output in test mode.
Cumulative availability percentage calculation for each domain.
Command-line argument support for easy usage.

Requirements
Python 3
requests library
pyyaml library
argparse library

Installation
Ensure Python 3 is installed on your system.
Install required Python libraries:
pip install requests pyyaml


Usage
Run the script with the path to the configuration file [rplace input.yaml file with desired yaml configured file]. Optionally, enable test mode for detailed output:

bash
python health_check.py input.yaml [--test]


Author
Jayachandra Poluri
