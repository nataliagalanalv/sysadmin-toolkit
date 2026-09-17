import subprocess
import platform
import shutil

def check_ping(ip: str) -> bool:
    
    system = platform.system()
    if system == "Windows":
        command = ["ping", "-n", "1", ip]
    else:
        command = ["ping", "-c", "1", ip]

    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def check_disk_space(path: str = "C:\\") -> float | None:

    try: 
        total, used, free = shutil.disk_usage(path)
        percentage_free = (free / total) * 100
        return percentage_free
    except FileNotFoundError:
        print(f"Error: The path '{path}' does not exist.")
        return None 
    
