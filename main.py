import subprocess
import os

# Full path to adb.exe
adb_path = "<Path\\to\\adb\\adb.exe"
destination_profile_id = 10


# Function to execute adb command and get output
def execute_adb_command(_command):
    _result = subprocess.run(_command, shell=True, capture_output=True, text=True)
    if _result.returncode != 0:
        print(f"Error executing command: {_command}")
        print(f"Error message: {_result.stderr.strip()}")
        return ""
    return _result.stdout.strip()


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
