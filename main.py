import subprocess
import sys
import os
from colorama import init, Fore, Style

def install_required_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}. Exiting.")
        sys.exit(1)

def display_menu():
    print("\nMenu:")
    print("0. Back")
    print("1. Run cert.py")
    print("2. Run phssl.py")

def get_script_path(script_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_dir, script_name)
    return script_path

def main():
    try:
        # Check if colorama is installed
        try:
            import colorama
        except ImportError:
            print("colorama is not installed. Installing...")
            install_required_package("colorama")
            import colorama  # Import again after installation

        # Import colorama after installation
        init()

        # ASCII art for "Kalla Billa" logo
        logo = """
        >>===========================================<<
        ||                                           ||
        ||  _  __     _ _         ____  _ _ _        ||
        || | |/ /__ _| | | __ _  | __ )(_) | | __ _  ||
        || | ' // _` | | |/ _` | |  _ \| | | |/ _` | ||
        || | . \ (_| | | | (_| | | |_) | | | | (_| | ||
        || |_|\_\__,_|_|_|\__,_| |____/|_|_|_|\__,_| ||
        ||                                           ||
        >>===========================================<<
        """

        # Your main code here
        print(Fore.CYAN + logo + Style.RESET_ALL)
        print(Fore.GREEN + "Hello, Buddy,I am Kalla Billa" + Style.RESET_ALL)

        while True:
            display_menu()
            choice = input("Enter your choice: ")

            if choice == "0":
                print("Going back...")
                break
            elif choice == "1":
                print("Running cert.py...")
                subprocess.run(["python", "cert.py"])
            elif choice == "2":
                print("Running phssl.py...")
                subprocess.run(["python", "phssl.py"])
            else:
                print(Fore.RED + "Invalid choice. Please enter a valid option." + Style.RESET_ALL)

    except KeyboardInterrupt:
        print(Fore.RED + "\nYou killed Kala Billa! How dare you?!" + Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    main()
