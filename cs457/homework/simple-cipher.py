# simple-cipher.py

alpha = [chr(i) for i in range(32, 127)]
alpha_size = 95
key = 4

def encipher(cleartext):
	global alpha, alpha_size, key
	cipher_str = ''

	for i in cleartext:
		cphr = (alpha.index(i) + key) % alpha_size
		cipher_str += alpha[cphr]

	return cipher_str


def decipher(ciphertext):
	global alpha, alpha_size, key
	clear_str = ''
	
	for i in ciphertext:
		clr = (alpha.index(i) - key) % alpha_size
		clear_str += alpha[clr]

	return clear_str

msg_clear = raw_input("Enter your cleartext:")
print 'ORIGINAL\t==>\t', msg_clear

msg_cipher = encipher(msg_clear)
print 'CIPHER\t\t==>\t', msg_cipher

msg_decipher = decipher(msg_cipher)
print 'CLEAR\t\t==>\t', msg_decipher


