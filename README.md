# ADB Package Migrator

A script to migrate installed packages between Android user profiles using ADB.

## Description

This script lists all installed packages for a specified user profile on an Android device and installs those packages for another user profile. It utilizes ADB commands to achieve this.

## Acknowledgements
Thanks to [u/Fenopy](https://www.reddit.com/user/Fenopy/), a Reddit user, for the inspiration to create this script.

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
     - Linux/Mac:
     ```sh
     ./adb.exe shell pm list users
     ```
     - Windows:
     ```cmd
     adb.exe shell pm list users
     ```
   - Note down the user IDs for the profiles you want to migrate packages between.

6. **Edit the Script**:
   - Open the `move_packages.py` file in a text editor or IDE.
   - Ensure the `adb_path` variable points to the correct path of `adb.exe` on your system.

7. **Run the Script**:
   - Execute the script using Python:
     ```sh
     python move_packages.py <profile_id>
     ```

## Example Execution
   - Example:
     ```sh
     python move_packages.py 10
     ```
