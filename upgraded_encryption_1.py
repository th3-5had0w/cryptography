def encrypt():
	plaintext=raw_input("[*] Type in something : ");
	ciphertext="";
	for i in plaintext:
		try:
			ciphertext+=str(hex(ord(i)));
		except ValueError:
			print("[!] Invalid Character Found !");
			exit();
	print(ciphertext);


def encrypt():
	plaintext=raw_input("[*] Type in something : ");
	ciphertext="";
	for i in plaintext:
		try:
			ciphertext+=str(hex(ord(i)));
		except ValueError:
			print("[!] Invalid Character Found !");
			exit();
	print(ciphertext);
encrypt();
