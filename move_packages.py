import subprocess
import argparse

# Full path to adb.exe # modify to your adb path if desired (example- c:\Android\android-sdk\platform-tools\adb.exe)
adb_path = "adb.exe"


# Function to execute adb command and get output
def execute_adb_command(_command):
    _result = subprocess.run(_command, shell=True, capture_output=True, text=True)
    if _result.returncode != 0:
        print(f"Error executing command: {_command}")
        print(f"Error message: {_result.stderr.strip()}")
        return ""
    return _result.stdout.strip()

def main(destination_profile_id):
    # Construct the command to get the list of installed packages for source profile (user ID 0)
    command = f"{adb_path} shell pm list packages"
    installed_packages = execute_adb_command(command)
    if not installed_packages:
        print("No installed packages found or error in retrieving packages.")
    else:
        print(f"Installed packages for source profile:\n{installed_packages}")

        # Extract package names
        package_names = [line.split(":")[1] for line in installed_packages.splitlines()]

        # Ask user if they want to copy all packages
        user_input = input("Copy all installed packages to Destination Profile? (Y/N): ").strip().lower()
        
        if user_input == 'y':
            # Install each package in destination profile
            for package in package_names:
                command = f"{adb_path} shell pm install-existing --user {destination_profile_id} {package}"
                result = execute_adb_command(command)
                print(f"Installing {package} for user {destination_profile_id}: {result}")
        elif user_input == 'n':
            # Prompt for each package
            for package in package_names:
                user_input = input(f"Do you want to copy the package {package} to the Destination Profile? (Y/N): ").strip().lower()
                if user_input == 'y':
                    command = f"{adb_path} shell pm install-existing --user {destination_profile_id} {package}"
                    result = execute_adb_command(command)
                    print(f"Installing {package} for user {destination_profile_id}: {result}")
        
        print("Package installation process completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Copy installed packages to a destination profile.')
    parser.add_argument('destination_profile_id', type=str, help='Destination profile ID')

    args = parser.parse_args()

    main(args.destination_profile_id)
