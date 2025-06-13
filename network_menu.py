import os
import platform
import subprocess

def clear_screen():
    #Clear the terminal screen based on the operating system
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def ping_website(website):

    # Set the number of pings based on OS
    ping_count = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', ping_count, '4', website]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        print("\nPing Results:")
        print(result.stdout)
    except Exception as e:
        print(f"Oops! Something went wrong while pinging: {e}")

def traceroute_website(ip_or_hostname):

    try:
        if platform.system().lower() == 'windows':
            # Windows uses tracert command
            os.system(f'tracert {ip_or_hostname}')
        else:
            # On macOS and Linux, try with sudo first
            try:
                os.system(f'sudo traceroute {ip_or_hostname}')
            except:
                # If sudo fails, try without it
                os.system(f'traceroute {ip_or_hostname}')
                
    except Exception as e:
        print(f"Looks like we hit a snag while tracing: {e}")
        print("Let's try one more time...")
        try:
            if platform.system().lower() == 'windows':
                os.system(f'tracert {ip_or_hostname}')
            else:
                os.system(f'traceroute {ip_or_hostname}')
        except Exception as e2:
            print(f"Sorry, we couldn't complete the trace: {e2}")

def show_network_config():
    # Display detailed network configuration information.
    try:
        if platform.system().lower() == 'darwin':  # macOS
            print("\nNetwork Configuration:")
            
            # Show all network interfaces
            print("\n=== Network Interfaces ===")
            os.system('networksetup -listallhardwareports')
            
            # Show IP configuration
            print("\n=== IP Configuration ===")
            os.system('ifconfig')
            
            # Show DNS settings
            print("\n=== DNS Configuration ===")
            os.system('scutil --dns')
            
        elif platform.system().lower() == 'windows':
            # Windows network info
            os.system('ipconfig /all')
        else:
            # Linux network info
            os.system('ip addr')
                
    except Exception as e:
        print(f"Had trouble getting network info: {e}")
        print("Let's try a simpler approach...")
        try:
            if platform.system().lower() == 'darwin':
                os.system('ifconfig')
            elif platform.system().lower() == 'windows':
                os.system('ipconfig /all')
            else:
                os.system('ip addr')
        except Exception as e2:
            print(f"Sorry, couldn't get the network information: {e2}")

def display_menu():
    # Display and handle the main menu interface.
    while True:
        clear_screen()
        print("=== Network Tools Menu ===")
        print("1. Ping a website")
        print("2. Traceroute a website")
        print("3. Show Network Configuration")
        print("4. Exit")
        
        choice = input("\nWhat would you like to do? (1-4): ")
        
        if choice == '1':
            website = input("\nWhich website would you like to ping? (e.g., google.com): ")
            ping_website(website)
            input("\nPress Enter to continue...")
        elif choice == '2':
            ip_or_hostname = input("\nWhere would you like to trace? (e.g., 8.8.8.8 or google.com): ")
            traceroute_website(ip_or_hostname)
            input("\nPress Enter to continue...")
        elif choice == '3':
            show_network_config()
            input("\nPress Enter to continue...")
        elif choice == '4':
            print("\nThanks for using the Network Tools! Goodbye!")
            break
        else:
            print("\nThat's not a valid option. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    display_menu() 