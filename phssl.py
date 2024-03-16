import os
import subprocess
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()

# Function to check and install required library
def install_required_library(library):
    try:
        import importlib
        importlib.import_module(library)
    except ImportError:
        print(Fore.RED + f"Installing {library}..." + Style.RESET_ALL)
        subprocess.run(['pip', 'install', library], check=True)
        print(Fore.GREEN + f"{library} installed successfully." + Style.RESET_ALL)

def check_adb_devices():
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True)
        if "List of devices attached" in result.stdout:
            devices = result.stdout.split('\n')[1:]
            if len(devices) > 1 or (len(devices) == 1 and devices[0] != ''):
                print(Fore.GREEN + "Device details:" + Style.RESET_ALL)
                for device in devices:
                    if device:
                        print(Fore.CYAN + device + Style.RESET_ALL)
                return True
        print(Fore.RED + "No ADB devices found. Please connect your device." + Style.RESET_ALL)
        return False
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error checking ADB devices: {e}" + Style.RESET_ALL)
        return False

def list_files_with_numbers(files):
    print(Fore.GREEN + "Available files:" + Style.RESET_ALL)
    for i, file in enumerate(files, start=1):
        print(Fore.CYAN + f"{i}. {file}" + Style.RESET_ALL)

def select_file(files):
    while True:
        selection = input(Fore.YELLOW + "Enter the serial number of the file you want to push: " + Style.RESET_ALL)
        if selection.isdigit() and 1 <= int(selection) <= len(files):
            return files[int(selection) - 1]
        else:
            print(Fore.RED + "Invalid selection. Please enter a valid serial number." + Style.RESET_ALL)

def main():
    try:
        install_required_library('colorama')
        print(Fore.GREEN + ">>===========================================<<")
        print("||                                           ||")
        print("||  _  __     _ _         ____  _ _ _        ||")
        print("|| | |/ /__ _| | | __ _  | __ )(_) | | __ _  ||")
        print("|| | ' // _` | | |/ _` | |  _ \| | | |/ _` | ||")
        print("|| | . \ (_| | | | (_| | | |_) | | | | (_| | ||")
        print("|| |_|\_\__,_|_|_|\__,_| |____/|_|_|_|\__,_| ||")
        print("||                                           ||")
        print(">>===========================================<<" + Style.RESET_ALL)
        
        while True:
            if check_adb_devices():
                response = input(Fore.YELLOW + "Type 'satya' to proceed: " + Style.RESET_ALL)
                if response.lower() == 'satya':
                    print(Fore.GREEN + "Proceeding to the next step..." + Style.RESET_ALL)
                    # Check for .0 files
                    files = [file for file in os.listdir() if file.endswith(".0")]
                    if files:
                        list_files_with_numbers(files)
                        selected_file = select_file(files)
                        destination_path = "/sdcard/"
                        # Execute adb push command
                        push_result = subprocess.run(['adb', 'push', selected_file, destination_path], capture_output=True, text=True)
                        print(Fore.GREEN + push_result.stdout + Style.RESET_ALL)
                        print(Fore.RED + push_result.stderr + Style.RESET_ALL)
                        if push_result.returncode == 0:
                            print(Fore.GREEN + "ADB push executed." + Style.RESET_ALL)
                            # Execute mv command as adb shell
                            move_command = f"adb shell mv {destination_path}/{selected_file} /system/etc/security/cacerts/"
                            move_result = subprocess.run(move_command, capture_output=True, text=True, shell=True)
                            print(Fore.GREEN + move_result.stdout + Style.RESET_ALL)
                            print(Fore.RED + move_result.stderr + Style.RESET_ALL)
                            if move_result.returncode == 0:
                                print(Fore.GREEN + "File moved successfully." + Style.RESET_ALL)
                                # Execute chmod command as adb shell
                                chmod_command = f"adb shell chmod 644 /system/etc/security/cacerts/{selected_file}"
                                chmod_result = subprocess.run(chmod_command, capture_output=True, text=True, shell=True)
                                print(Fore.GREEN + chmod_result.stdout + Style.RESET_ALL)
                                print(Fore.RED + chmod_result.stderr + Style.RESET_ALL)
                                if chmod_result.returncode == 0:
                                    print(Fore.GREEN + "File permissions changed." + Style.RESET_ALL)
                                    # Execute adb reboot command
                                    reboot_result = subprocess.run(['adb', 'reboot'], capture_output=True, text=True)
                                    print(Fore.GREEN + reboot_result.stdout + Style.RESET_ALL)
                                    print(Fore.RED + reboot_result.stderr + Style.RESET_ALL)
                                    print(Fore.GREEN + "Rebooting device. You are all done, buddy!" + Style.RESET_ALL)
                                    break
                                else:
                                    print(Fore.RED + "Error changing file permissions." + Style.RESET_ALL)
                                    break
                            else:
                                print(Fore.RED + "Error moving file." + Style.RESET_ALL)
                                break
                        else:
                            print(Fore.RED + "Error pushing file to device." + Style.RESET_ALL)
                            break
                    else:
                        print(Fore.RED + "No .0 files found in the current directory." + Style.RESET_ALL)
                        break
                else:
                    print(Fore.RED + "Invalid input. Please type 'satya' to proceed." + Style.RESET_ALL)
            else:
                input(Fore.RED + "Please connect your ADB device and press Enter to continue..." + Style.RESET_ALL)
    except KeyboardInterrupt:
        print(Fore.RED + "\nYou killed kala billa!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
