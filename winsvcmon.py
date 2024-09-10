import subprocess
import argparse
import os

def get_services_with_paths():
    """Retrieve a list of all Windows services along with their executable paths."""
    services = []
    try:
        # Run the WMIC command to get services and their paths
        result = subprocess.run(
            ["wmic", "service", "get", "name,pathname"],
            capture_output=True, text=True, check=True
        )
        output = result.stdout.strip()
        lines = output.split('\n')[1:]  # Skip the header line

        # Process each line to extract service names and paths
        for line in lines:
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                service_name, service_path = parts
                services.append((service_name.strip(), service_path.strip()))
    except subprocess.CalledProcessError as e:
        print(f"Error executing WMIC command: {e}")
    return services

def save_baseline(filename):
    """Save the current list of services and their paths to a specified file."""
    services = get_services_with_paths()
    with open(filename, "w") as file:
        for name, path in services:
            file.write(f"{name}|{path}\n")

def load_baseline(filename):
    """Load a list of services and paths from a specified file."""
    if not os.path.isfile(filename):
        return set()
    with open(filename, "r") as file:
        return {tuple(line.strip().split('|', 1)) for line in file}

def compare_services(baseline_filename):
    """Compare current services against those in the baseline file and display differences."""
    baseline_services = load_baseline(baseline_filename)
    current_services = set(get_services_with_paths())

    added_services = current_services - baseline_services
    removed_services = baseline_services - current_services

    if added_services:
        print("New services detected:")
        for name, path in added_services:
            print(f" - {name}: {path}")

    if removed_services:
        print("Removed services detected:")
        for name, path in removed_services:
            print(f" - {name}: {path}")

    if not added_services and not removed_services:
        print("No changes detected.")

def main():
    """Handle user input and execute the appropriate actions based on arguments."""
    parser = argparse.ArgumentParser(description="Windows Services Analysis Tool")
    parser.add_argument(
        "--create-baseline",
        action="store_true",
        help="Create and save a baseline of Windows services."
    )
    parser.add_argument(
        "--compare",
        type=str,
        metavar="BASELINE_FILE",
        help="Compare current services with a baseline file."
    )

    args = parser.parse_args()

    if args.create_baseline:
        save_baseline("baseline_services.txt")
        print("Baseline created and saved to baseline_services.txt")
    elif args.compare:
        compare_services(args.compare)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
