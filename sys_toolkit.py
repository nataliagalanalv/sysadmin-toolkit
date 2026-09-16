from os_utils import check_ping, check_disk_space
from log_parser import parse_failed_ips

def show_menu() -> None:
    print("=== Sysadmin Toolkit ===")
    print("1. Check connectivity (ping)")
    print("2. Check disk space")
    print("3. Parse SSH log")
    print("4. Audit network device")
    print("5. Look up suspicious IP")
    print("0. Exit")

def main() -> None:
    while True:
        show_menu()
        option: str = input("Choose an option: ")

        if option == "0":
            print("Exiting program...")
            break

        elif option == "1":
            ip: str = input("Enter the IP address to check: ")
            if check_ping(ip):
                print(f"Connectivity to {ip} successful.")
            else:
                print(f"Could not establish connectivity to {ip}.")

        elif option == "2":
            path: str = input("Enter the disk path to check (default C:\\): ") or "C:\\"
            percentage_free = check_disk_space(path)
            if percentage_free >= 20:
                print(f"Disk space at {path} is sufficient.")
            else:
                print(f"Warning: less than 20% free disk space at {path}.")

        elif option == "3":
            log_path: str = input("Enter the path to the SSH log file: ")
            failed_ips, unique_ips = parse_failed_ips(log_path)
            print(f"Unique IPs detected: {unique_ips}")
            print("IPs with failed connection attempts:")
            for ip, count in failed_ips.items():
                print(f"{ip}: {count} failed attempt(s)")

        else:
            print("Option not implemented yet") 

if __name__ == "__main__":
    main()