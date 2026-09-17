# Sysadmin Toolkit

A command-line toolkit for system administrators, built in Python as part of the Corner Estudios ASIR Bootcamp. It combines SSH log auditing, network inventory reporting, device auditing through OOP, and external threat intelligence lookups into a single interactive menu.

## Features

- **Connectivity check** — pings a given IP address and reports whether it responds.
- **Disk space check** — reports free disk space percentage for a given path and warns when it drops below 20%.
- **SSH log parsing** — scans an `auth.log`-style file and counts failed login attempts per IP address.
- **Network device auditing** — models routers and servers as objects with their own security audit behavior.
- **Threat intelligence lookup** — queries [ipinfo.io](https://ipinfo.io) to enrich suspicious IPs with country and organization data, either as a single lookup or as a full report cross-referenced with the SSH log.
- **Inventory generation & analysis** — generates a fake but realistic 1000-row server inventory and filters/aggregates it with Pandas.
- **Excel reporting** — exports the list of vulnerable servers to a real `.xlsx` file.
- **Scheduling** — two independent background schedulers: one for monthly Excel report generation, another for periodic test execution.
- **Unit testing** — automated verification of the SSH log parsing logic with `pytest`.

## Tech stack

- Python 3.14
- `requests` — external API calls
- `pandas` + `openpyxl` — data analysis and Excel export
- `faker` — synthetic data generation
- `schedule` — task scheduling
- `pytest` — unit testing
- `mypy` — static type checking

## Project structure

sysadmin-toolkit/
├── network_models/
│ ├── init.py
│ ├── network_device.py
│ ├── router.py
│ └── server.py
├── docs/
│ ├── python-sysadmin.md
│ ├── oop-explanation.md
│ └── pytest-output.md
├── sys_toolkit.py
├── os_utils.py
├── log_parser.py
├── threat_intel.py
├── generate_inventory.py
├── inventory_manager.py
├── test_toolkit.py
├── test_scheduler.py
├── requirements.txt
└── .gitignore


## Setup

```bash
python -m venv venv
venv\Scripts\Activate.ps1        # Windows PowerShell
pip install -r requirements.txt
```

## Usage

Run the interactive menu:

```bash
python sys_toolkit.py
```

Run the unit tests:

```bash
pytest test_toolkit.py -v
```

Run the monthly Excel report scheduler (blocks indefinitely until stopped with `Ctrl+C`):

```bash
python inventory_manager.py
# uncomment run_scheduler() inside the __main__ block first
```

Run the periodic test scheduler (also blocks indefinitely):

```bash
python test_scheduler.py
```

## Known limitations

- `check_ping` only distinguishes between "responded" and "did not respond" via the process exit code; it does not currently differentiate between an unreachable IP and a malformed IP address.
- The `ipinfo.io` integration does not use an API token, so it is subject to the service's unauthenticated rate limits.
- Scheduler intervals in the code are illustrative for demonstration purposes; production use would require a persistent process (e.g. a system service) rather than a foreground script.

## Author

Natalia Galán — Corner Estudios ASIR Bootcamp