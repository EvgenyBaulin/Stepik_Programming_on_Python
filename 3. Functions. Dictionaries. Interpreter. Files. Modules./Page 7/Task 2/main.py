def substitution_cipher(plain_alphabet, cipher_alphabet, message):
	cipher_dict = dict(zip(plain_alphabet, cipher_alphabet))

	encrypted_message = ''.join(cipher_dict.get(char, char) for char in message)
	return encrypted_message


def decrypt_substitution_cipher(plain_alphabet, cipher_alphabet, encrypted_message):
	decrypt_dict = dict(zip(cipher_alphabet, plain_alphabet))

	decrypted_message = ''.join(decrypt_dict.get(char, char) for char in encrypted_message)
	return decrypted_message


plain_alphabet = input().strip()
cipher_alphabet = input().strip()
to_encrypt = input().strip()
to_decrypt = input().strip()

print(substitution_cipher(plain_alphabet, cipher_alphabet, to_encrypt))
print(decrypt_substitution_cipher(plain_alphabet, cipher_alphabet, to_decrypt))
