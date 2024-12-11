import subprocess
import os
import hashlib

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

def find_process_by_checksum(target_checksum, hash_algorithm="sha1"):
    """Find a process by matching the checksum of its executable using PowerShell, handling Unicode paths."""
    try:
        # PowerShell command to get all process executable paths and PIDs
        command = [
            "powershell",
            "-NoProfile",
            "-Command",
            "[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new();",
            "Get-Process | Where-Object { $_.Path -ne $null } | Select-Object -Property Id, Path"
        ]
        
        # Run the command and ensure the output is captured in UTF-8
        result = subprocess.check_output(command, universal_newlines=True, encoding="utf-8", errors="replace")
        
        for line in result.splitlines():
            if line.strip() and not line.startswith("Id"):
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    pid, exe_path = parts
                    exe_path = exe_path.strip()
                    if os.path.isfile(exe_path):
                        checksum = calculate_file_checksum(exe_path, hash_algorithm)
                        if checksum == target_checksum:
                            print(f"Found process with PID {pid}, Executable: {exe_path}, Checksum: {checksum}")
                            return int(pid)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")