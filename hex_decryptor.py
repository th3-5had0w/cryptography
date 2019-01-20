def decrypt():
	ciphertext=raw_input("[*] Type in something : ");
	reverse_ciphertext=ciphertext.replace("0x","");
	print("[*] Secret Message : "+reverse_ciphertext.decode("hex"));
decrypt();
