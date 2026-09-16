import pandas as pd

def load_inventory(path: str = "inventory.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def filter_vulnerable_servers(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df["os"] == "Windows Server") | (df["ram_gb"] < 4)]


def count_by_department(df: pd.DataFrame) -> pd.Series:
    return df.groupby("department").size()

if __name__ == "__main__":
    inventory = load_inventory()

    vulnerable = filter_vulnerable_servers(inventory)
    print(f"Vulnerable servers found: {len(vulnerable)}")
    print(vulnerable.head())

    print("\nServers by department:")
    print(count_by_department(inventory))