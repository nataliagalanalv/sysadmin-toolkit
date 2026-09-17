def parse_failed_ips(log_path: str) -> tuple[dict[str, int], set[str]]:
    unique_ips: set[str] = set()
    failed_attempts: dict[str, int] = {}

    try:
        with open(log_path, "r") as log_file:
            for line in log_file:
                line = line.strip()

                if "Failed password" in line:
                    parts = line.split()

                    if "from" in parts:
                        from_index = parts.index("from")
                        ip = parts[from_index + 1]

                        unique_ips.add(ip)
                        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    except FileNotFoundError:
        print(f"Error: the log file '{log_path}' was not found.")


    return failed_attempts, unique_ips
