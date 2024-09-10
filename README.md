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


