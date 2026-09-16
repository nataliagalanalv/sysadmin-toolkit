from network_models.network_device import NetworkDevice

class Router(NetworkDevice):
    def __init__(self, hostname: str, ip: str, mac: str, firmware_version: str) -> None:
        super().__init__(hostname, ip, mac)
        self.firmware_version = firmware_version

    def audit_device(self) -> None:
        print(f"Router {self.hostname}: check firmware version {self.firmware_version} is up to date and disable UPnP")