from network_models.network_device import NetworkDevice
from network_models.router import Router
from network_models.server import Server
from network_models.router import Router
from os_utils import check_ping, check_disk_space
from log_parser import parse_failed_ips
from threat_intel import display_threat_table, get_ip_info

def show_menu() -> None:
    print("=== Sysadmin Toolkit ===")
    print("1. Check connectivity (ping)")
    print("2. Check disk space")
    print("3. Parse SSH log")
    print("4. Audit network device")
    print("5. Threat intel report (from SSH log)")
    print("6. Look up a single IP address")
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

        elif option == "4":
            device_type = input("Device type (router/server): ").strip().lower()
            hostname = input("Hostname: ")
            ip = input("IP address: ")
            mac = input("MAC address: ")

            device: NetworkDevice

            if device_type == "router":
                    firmware_version = input("Firmware version: ")
                    device = Router(hostname, ip, mac, firmware_version)
                    device.audit_device()
            elif device_type == "server":
                    os_type = input("Operating system: ")
                    device = Server(hostname, ip, mac, os_type)
                    device.audit_device()
            else:
                print("Unknown device type. Please enter 'router' or 'server'.")

        elif option == "5":
            log_path = input("Enter the path to the SSH log file: ")
            failed_ips, _ = parse_failed_ips(log_path)
            display_threat_table(failed_ips)

        elif option == "6":
            ip = input("Enter the IP address to look up: ")
            info = get_ip_info(ip)
            if info:
                print(f"IP: {ip}")
                print(f"Country: {info.get('country', 'Unknown')}")
                print(f"Organization: {info.get('org', 'Unknown')}")
            else:
                print("Could not retrieve information for the specified IP address.")

        else:
            print("Option not implemented yet")

if __name__ == "__main__":
    main()