# Windows Services Analysis Tool

## Description

The **Windows Services Analysis Tool** is a Python script designed to help you manage and monitor Windows services. It provides essential functionalities for system administrators and security professionals to:

- **Create a Baseline Snapshot**: Capture a snapshot of currently running Windows services and their executable paths. This snapshot is saved to a file, serving as a reference for future comparisons.
  
- **Compare Service States**: Compare the current list of Windows services against a previously saved baseline to detect any changes, such as newly added or removed services.

## Features

- **Service Snapshot**: Uses the `wmic` command to retrieve a list of services and their executable paths.
- **Baseline Creation**: Saves the current service state to a text file for future reference.
- **Change Detection**: Compares current services with a baseline to identify additions or removals.
- **Command-Line Interface**: Easy-to-use commands for creating baselines and performing comparisons.

## Use Cases

- **System Monitoring**: Track changes in Windows services to ensure system integrity and security.
- **Security Auditing**: Identify unauthorized changes to services for enhanced security posture.
- **Compliance**: Maintain a record of service states for auditing and compliance purposes.

## Installation
1. **Clone the repository**:

    ```bash
    git clone https://github.com/username/repository.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd repository
    ```

3. **Ensure Python is installed**: This script requires Python 3.6 or later. You can download Python from [python.org](https://www.python.org/downloads/).

## Usage

### Create a Baseline

To create and save a baseline of Windows services, run:

```bash
python script_name.py --create-baseline
```
This command will generate a file named baseline_services.txt containing the list of current services and their paths.

### Compare Services
To compare the current list of services with a previously saved baseline, use:

```bash
python script_name.py --compare baseline_services.txt
```
Replace baseline_services.txt with the path to your baseline file if it is named differently.

## Error Handling
If there is an issue executing the wmic command, the script will print an error message. Ensure you have appropriate permissions and that the wmic command is available on your system.

