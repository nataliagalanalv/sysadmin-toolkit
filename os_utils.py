import subprocess
import platform
import shutil

def check_ping(ip: str) -> bool:
    
    sistema = platform.system()
    if sistema == "Windows":
        param = ["ping", "-n", "1", ip]
    else:
        param = ["ping", "-c", "1", ip]

    try:
        subprocess.run(param, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False


def check_disk_space(path: str = "C:\\") -> float:
    
    total, used, free = shutil.disk_usage(path)
    percentage_free = (free / total) * 100
    return percentage_free
