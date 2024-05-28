# ADB Package Migrator

A script to migrate installed packages between Android user profiles using ADB.

## Description

This script lists all installed packages for a specified user profile on an Android device and installs those packages for another user profile. It utilizes ADB commands to achieve this.

## Acknowledgements
Thanks to u/Fenopy, a Reddit user, for the inspiration to create this script.

## Prerequisites

- Python 3.x
- ADB installed and configured
- Android device connected via USB with USB debugging enabled

## Usage

1. **Ensure ADB is Installed and Configured**:
   - Download and install ADB from the [Android developer site](https://developer.android.com/studio/releases/platform-tools).
   - Ensure `adb.exe` is accessible in your system PATH.

2. **Connect Your Android Device**:
   - Connect your device to your computer via USB.
   - Enable USB debugging on your device (Settings > Developer options > USB debugging).

3. **Clone the Repository**:

4. **Navigate to the Repository Folder**:
   - Navigate to the cloned repository folder:
     ```sh
     cd adb-package-migrator
     ```

5. **Get the List of Users on the Device**:
   - Use the following ADB command to list all users on the device:
     ```sh
     ./adb.exe shell pm list users
     ```
   - Note down the user IDs for the profiles you want to migrate packages between.

6. **Edit the Script**:
   - Open the `move_packages.py` file in a text editor or IDE.
   - Ensure the `adb_path` variable points to the correct path of `adb.exe` on your system.
   - Update the user IDs in the script as needed.

7. **Run the Script**:
   - Execute the script using Python:
     ```sh
     python move_packages.py
     ```

## Example Script

Here's the Python script included in this repository (`move_packages.py`):

```python
import subprocess
import os

# Full path to adb.exe
adb_path = "<Path\\to\\adb\\adb.exe"
destination_profile_id = <YOUR_PROFILE_ID>


# Function to execute adb command and get output
def execute_adb_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {command}")
        print(f"Error message: {result.stderr.strip()}")
        return ""
    return result.stdout.strip()


# Construct the command to get the list of installed packages for source profile (user ID 0)
command = f"{adb_path} shell pm list packages"
installed_packages = execute_adb_command(command)
if not installed_packages:
    print("No installed packages found or error in retrieving packages.")
else:
    print(f"Installed packages for source profile:\n{installed_packages}")

    # Extract package names
    package_names = [line.split(":")[1] for line in installed_packages.splitlines()]

    # Install each package in destination profile
    for package in package_names:
        command = f"{adb_path} shell pm install-existing --user {destination_profile_id} {package}"
        result = execute_adb_command(command)
        print(f"Installing {package} for user {destination_profile_id}: {result}")

    print("All packages moved from source profile to destination profile.")


