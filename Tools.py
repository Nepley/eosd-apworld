import subprocess
import asyncio
import os
import hashlib
import json

process_already_checked_list = []

async def calculate_file_checksum(file_path, hash_algorithm="sha1"):
	"""Calculate the checksum of a given file."""
	hash_func = hashlib.new(hash_algorithm)
	try:
		with open(file_path, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hash_func.update(chunk)
		return hash_func.hexdigest()
	except (FileNotFoundError, PermissionError):
		return None

async def get_all_process():
	try:
		# PowerShell command to get all process executable paths and PIDs
		command = [
			"powershell",
			"-NoProfile",
			"-Command",
			"[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new();",
			"Get-Process | Where-Object { $_.Path -ne $null } | Select-Object -Property Id, Path | ConvertTo-Json"
		]

		pw = await asyncio.create_subprocess_exec("powershell", "-NoProfile", "-Command", "[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new();", "Get-Process | Where-Object { $_.Path -ne $null } | Select-Object -Property Id, Path | ConvertTo-Json", stdout=asyncio.subprocess.PIPE)

		await asyncio.sleep(1)
		result, errors = await pw.communicate()

		return json.loads(result)
	except Exception as e:
		print(f"Unexpected error: {e}")

async def find_process(name = "東方紅魔郷", target_checksum = "e61b4f4fea3802e926ef307f45166599c3e86555", hash_algorithm="sha1"):
	processes = await get_all_process()
	global process_already_checked_list

	pid_game = None
	# First check by name
	for process in processes:
		if name in process['Path'].split("\\")[-1]:
			pid_game = int(process['Id'])
			break

	# If not found by name, check by checksum
	if pid_game is None:
		for process in processes:
			if os.path.isfile(process['Path']):
				if process['Id'] not in process_already_checked_list:
					checksum = await calculate_file_checksum(process['Path'], hash_algorithm)
					await asyncio.sleep(0.01)
					if checksum == target_checksum:
						pid_game = int(process['Id'])
					else:
						process_already_checked_list.append(process['Id'])

	return pid_game