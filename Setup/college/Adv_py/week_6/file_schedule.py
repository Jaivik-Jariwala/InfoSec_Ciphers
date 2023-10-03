import schedule 
import shutil
import time
from datetime import datetime

def backup_files(source_dir, backup_dir):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_folder = f"{backup_dir}/backup_{timestamp}"

    try:
        shutil.copytree(source_dir, backup_folder)
        print(f"backup created at{backup_folder}")
    except Exception as e:
        print("Error ", e)
if __name__ == "__main__":
    source_directory="/home/jaivikjariwala/Desktop/Advanced_py"
    backup_directory="/home/jaivikjariwala/Desktop/Advanced_py/week_6/backup"

    schedule.every().day.at("09:50").do(backup_files, source_directory, backup_dir=backup_directory)
