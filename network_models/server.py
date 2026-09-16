from network_models.network_device import NetworkDevice

class Server(NetworkDevice):
    def __init__(self, hostname: str, ip: str, mac: str, os_type: str) -> None:
        super().__init__(hostname, ip, mac)
        self.os_type = os_type

    def audit_device(self) -> None:
        print(f"Server {self.hostname} ({self.os_type}): review security patches and open ports")