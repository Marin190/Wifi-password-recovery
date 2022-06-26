try:
	import subprocess
	lis = {}
	a = subprocess.check_output('netsh wlan show profiles').replace(b'\r\n', b'').replace(b'Profil Tous les utilisateurs', b"").replace(b'\xff', b'').replace(b'Current User Profile', b"").split(b":")
	name = []
	for i in range(len(a) - 2):
		name.append(str(a[i + 2]).replace("b'", "").replace("'", "").replace(" ", "", 1).replace("        ", "", 1))

	for i in name:
		o = subprocess.check_output(f'netsh wlan show profile name="{i}" key=clear').replace(b'\r', b' ').split(b' ')
		for f in range(len(o)):
			if f + 3 < len(o):
				if o[f + 2] == b'\nParam\x8atres':
					l = str(o[f]).replace("b'", "").replace("'", "")
					lis[i] = l
				elif o[f + 2] == b'Cost' and o[f + 3] == b'settings':
					l = str(o[f]).replace("b'", "").replace("'", "")
					lis[i] = l


	print(f"\n  {len(lis)} wifi passwords found :")
	for key, value in lis.items():
		print(f"\n\n    wifi name : {key}\n    password : {value}")
	input('\n\n  Press "Enter" to exit : ')
except Exception as e:
	print(f"\n  An error occured please send it to me (Marin#9044) :\n  {e}")
	input('\n\n  Press "Enter" to exit : ')