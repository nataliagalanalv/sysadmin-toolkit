import csv
from faker import Faker
import random

def generate_inventory(path: str = "inventory.csv", rows: int = 1000) -> None:
    fake = Faker()

    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["hostname", "ip", "os", "ram_gb", "department"])
        

        for _ in range(rows):
            writer.writerow([
                fake.hostname(),
                fake.ipv4(),
                random.choice(["Ubuntu", "Windows Server", "Debian", "CentOS"]),
                random.choice([2, 4, 8, 16, 32]),
                random.choice(["IT", "Sales", "HR", "Finance"])
            ])
            

if __name__ == "__main__":
    generate_inventory()
    