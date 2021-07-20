""" Написать функцию xor_cipher принимающую 2 аргумента: строку, которую нужно зашифровать
 и ключ шифрования, который возвращает строку, зашифрованную путем применения
   функции XOR (^)  над символами строки и ключом. Написать также функцию xor_uncipher
   которая по зашифрованной строке и ключу восстонавливает исходную строку"""

a = input('Введи слово для шифрования: ')
key = input('Введи ключ шифрования: ')
# переводим ключ в число
keyBin = 0
for letter in key:
	keyBin += ord(letter)

print(keyBin)

# функция шифрования
def XOR_cipher(a, keyBin):
	encripted = ''
	for letter in a:
		encripted += chr(ord(letter) ^ keyBin)
	return encripted

x = XOR_cipher(a, keyBin)


# функция дешифрования
def XOR_uncipher(x, keyBin):
	uncripted = ''
	for symbol in x:
		uncripted += chr(ord(symbol) ^ keyBin)
	return uncripted
y = XOR_uncipher(x, keyBin)

print(x)
print(y)

