import subprocess


def get_IPv4_external_address(interface_name):

	cmd = ["ip", "address", "show", interface_name]

	keywargs = {
		"capture_output" : True,
		"text"  : True,
		"check" : True
	}

	try:
		# chamada de sistema para executar o comando acima:
		result = subprocess.run(cmd, **keywargs)

		for line in result.stdout.splitlines():
			if "inet " in line:
				IPv4 = line.split()[1]
				IPv4 = IPv4.split("/")[0]
				return IPv4

	except subprocess.CalledProcessError as e:
		print(f"Erro ao executar comando 'ip': {e}")
		raise
