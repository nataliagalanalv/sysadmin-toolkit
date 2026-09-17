import subprocess
import schedule
import time

def run_tests() -> None:
    print("Running scheduled tests...")
    result = subprocess.run(["pytest", "test_toolkit.py", "-v"])

    if result.returncode == 0:
        print("All tests passed.")
    else:
        print("Some tests failed. Check the output above.")


def run_test_scheduler() -> None:
    schedule.every(1).hour.do(run_tests)

    print("Test scheduler started. Waiting for the next scheduled run...")
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    run_test_scheduler()