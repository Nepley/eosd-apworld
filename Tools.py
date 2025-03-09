import asyncio
import os
import hashlib
import json
from .Variables import *
from .Mapping import CHAR_MAP, RED_CHAR_MAP

process_already_checked_list = [] # For performance reasons, we don't want to check the same process multiple times

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
	"""Get all running processes."""
	try:
		# PowerShell command to get all process executable paths and PIDs
		command = [
			"powershell",
			"-NoProfile",
			"-Command",
			"[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new();",
			"Get-Process | Where-Object { $_.Path -ne $null } | Select-Object -Property Id, Path | ConvertTo-Json"
		]

		pw = await asyncio.create_subprocess_exec("powershell", "-NoProfile", "-Command", "[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new();", "Get-Process | Where-Object { $_.Path -ne $null } | Select-Object -Property Id, Path | ConvertTo-Json", stdout=asyncio.subprocess.PIPE, creationflags=0x08000000)

		await asyncio.sleep(1)
		result, errors = await pw.communicate()

		return json.loads(result)
	except Exception as e:
		print(f"Unexpected error: {e}")

async def find_process(name = GAME_NAME, target_checksum = GAME_HASH, hash_algorithm="sha1"):
	"""Find a process by name or checksum."""
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

def textToBytes(text: str, red = False):
	bytes = []
	current_char_map = RED_CHAR_MAP if red else CHAR_MAP

	for char in text:
		bytes.append(current_char_map[char])

	return bytes