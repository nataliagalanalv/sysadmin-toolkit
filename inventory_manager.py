import pandas as pd
import schedule
import time

def load_inventory(path: str = "inventory.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def filter_vulnerable_servers(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df["os"] == "Windows Server") | (df["ram_gb"] < 4)]


def count_by_department(df: pd.DataFrame) -> pd.Series:
    return df.groupby("department").size()

def export_to_excel(df: pd.DataFrame, path: str = "vulnerable_servers_report.xlsx") -> None:
    df.to_excel(path, index=False, sheet_name="Vulnerable Servers")

def generate_monthly_report() -> None:
    inventory = load_inventory()
    vulnerable = filter_vulnerable_servers(inventory)
    export_to_excel(vulnerable)
    print("Monthly report generated successfully.")


def run_scheduler() -> None:
    schedule.every(30).days.do(generate_monthly_report)

    print("Scheduler started. Waiting for the next scheduled run...")
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    inventory = load_inventory()

    vulnerable = filter_vulnerable_servers(inventory)
    print(f"Vulnerable servers found: {len(vulnerable)}")
    print(vulnerable.head())

    print("\nServers by department:")
    print(count_by_department(inventory))

    export_to_excel(vulnerable)
    print("\nExcel report generated: vulnerable_servers_report.xlsx")

    # run_scheduler() Only uncomment this line if you want to enable the scheduler for monthly reports
