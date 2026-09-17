from log_parser import parse_failed_ips
import tempfile
import os

def test_parse_failed_ips_counts_correctly() -> None:
    log_content = (
        "Jan 10 03:14:22 server sshd[1]: Failed password for root from 10.0.0.1 port 1 ssh2\n"
        "Jan 10 03:14:23 server sshd[2]: Failed password for root from 10.0.0.1 port 2 ssh2\n"
        "Jan 10 03:14:24 server sshd[3]: Failed password for root from 10.0.0.2 port 3 ssh2\n"
        "Jan 10 03:15:01 server sshd[4]: Accepted password for user from 10.0.0.3 port 4 ssh2\n"
    )

    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as temp_file:
        temp_file.write(log_content)
        temp_path = temp_file.name

    failed_attempts, unique_ips = parse_failed_ips(temp_path)
    os.remove(temp_path)

    assert failed_attempts["10.0.0.1"] == 2
    assert failed_attempts["10.0.0.2"] == 1
    assert "10.0.0.3" not in failed_attempts
    assert unique_ips == {"10.0.0.1", "10.0.0.2"}