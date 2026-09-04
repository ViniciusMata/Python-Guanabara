import hashlib

# SHA = Security Hash Algorithm
texto = "Gafonhoto"
cod = texto.encode('utf-8')
hash1 = hashlib.sha1(cod).hexdigest()
hash2 = hashlib.sha256(cod).hexdigest()
hash3 = hashlib.sha512(cod).hexdigest()


#SHA256 or SHA512= melhor hash de segurança até o momento

print(cod)
print(hash1)
print(hash2)
print(hash3)
