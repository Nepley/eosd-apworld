import subprocess
import os
import hashlib
import time
from tkinter.filedialog import askopenfilename

process_already_checked_list = []

def calculate_file_checksum(file_path, hash_algorithm="sha1"):
    """Calculate the checksum of a given file."""
    hash_func = hashlib.new(hash_algorithm)
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except (FileNotFoundError, PermissionError):
        return None

def get_all_process():
    try:
        # PowerShell command to get all process executable paths and PIDs
        command = [
            "powershell",
            "-NoProfile",
            "-Command",
            "[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new();",
            "Get-Process | Where-Object { $_.Path -ne $null } | Select-Object -Property Id, Path"
        ]

        result = subprocess.check_output(command, universal_newlines=True, encoding="utf-8", errors="replace", shell=True)

        return result
    except Exception as e:
        print(f"Unexpected error: {e}")

def open_manually_process():
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    p = subprocess.Popen(filename)
    time.sleep(1)
    return p.pid

def find_process(name, target_checksum, hash_algorithm="sha1"):
    process = get_all_process()
    global process_already_checked_list

    pid_game = None
    # First check by name
    for line in process.splitlines():
         if line.strip() and not line.startswith("Id"):
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                pid, exe_path = parts
                exe_path = exe_path.strip()
                if name in exe_path:
                    pid_game = int(pid)
                    break

    # If not found by name, check by checksum
    if pid_game is None:
        for line in process.splitlines():
            if line.strip() and not line.startswith("Id"):
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    pid, exe_path = parts
                    exe_path = exe_path.strip()
                    if os.path.isfile(exe_path):
                        if pid not in process_already_checked_list:
                            checksum = calculate_file_checksum(exe_path, hash_algorithm)
                            if checksum == target_checksum:
                                pid_game = int(pid)
                            else:
                                process_already_checked_list.append(pid)

    if pid_game is None:
        pid_game = open_manually_process()

    return pid_game