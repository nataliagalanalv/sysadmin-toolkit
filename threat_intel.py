import requests

def get_ip_info(ip: str) -> dict | None:
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None


def display_threat_table(ip_attempts: dict[str, int]) -> None:
    print(f"{'IP':<20}{'Attempts':<12}{'Country':<10}{'Organization'}")
    print("-" * 70)

    for ip, count in ip_attempts.items():
        info = get_ip_info(ip)

        if info is None:
            country = "N/A"
            organization = "N/A (private or unreachable IP)"
        else:
            country = info.get("country", "Unknown")
            organization = info.get("org", "Unknown")

        print(f"{ip:<20}{count:<12}{country:<10}{organization}")