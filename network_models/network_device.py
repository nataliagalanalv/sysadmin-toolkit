class NetworkDevice:
    def __init__(self, hostname: str, ip: str, mac: str) -> None:
        self.hostname = hostname
        self.ip = ip
        self.mac = mac

    def audit_device(self) -> None:
        print(f"Auditing generic device: {self.hostname}")