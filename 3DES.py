# 3DES

from Crypto.Cipher import DES3
import secrets

def pad_manual(text, block_size=8):
    """Agrega relleno manualmente para que el texto sea múltiplo de block_size (PKCS5 Padding)."""
    pad_len = block_size - (len(text) % block_size)
    padding = chr(pad_len) * pad_len  # Relleno con el número de bytes necesarios
    return text + padding

def unpad_manual(text):
    """Elimina el relleno manual después del descifrado."""
    pad_len = ord(text[-1])  # Último byte indica la cantidad de relleno
    return text[:-pad_len]  # Elimina los bytes de relleno

def generate_3des_key():
    """Genera una clave aleatoria de 16 o 24 bytes para 3DES."""
    key_length = 24  # Puede ser 16 o 24 bytes
    return secrets.token_bytes(key_length)

def validate_3des_key(key):
    """Verifica que la clave tenga exactamente 16 o 24 bytes."""
    if len(key) not in [16, 24]:
        raise ValueError("La clave 3DES debe tener exactamente 16 o 24 bytes.")

def generate_iv():
    """Genera un IV aleatorio de 8 bytes para 3DES en modo CBC."""
    return secrets.token_bytes(8)

def triple_des_encrypt_cbc(plaintext, key, iv):
    """Cifra un mensaje con 3DES en modo CBC."""
    validate_3des_key(key)  # Verifica la clave
    cipher = DES3.new(key, DES3.MODE_CBC, iv)  # Crear el cifrador con CBC
    padded_text = pad_manual(plaintext)  # Aplicar el padding manualmente
    ciphertext = cipher.encrypt(padded_text.encode())  # Cifrar
    return ciphertext.hex()  # Convertimos a hexadecimal para facilidad de almacenamiento

def triple_des_decrypt_cbc(ciphertext, key, iv):
    """Descifra un mensaje cifrado con 3DES en modo CBC."""
    validate_3des_key(key)  # Verifica la clave
    cipher = DES3.new(key, DES3.MODE_CBC, iv)  # Crear el descifrador con CBC
    decrypted_text = cipher.decrypt(bytes.fromhex(ciphertext))  # Convertir desde hex a bytes
    return unpad_manual(decrypted_text.decode())  # Decodificar y remover el relleno

# 🔹 Prueba del cifrado y descifrado con 3DES
if __name__ == "__main__":
    key = generate_3des_key()  # Generamos una clave 3DES aleatoria de 16 o 24 bytes
    iv = generate_iv()  # Generamos un IV aleatorio de 8 bytes
    message = "Hello, 3DES!"  # Mensaje de prueba

    encrypted = triple_des_encrypt_cbc(message, key, iv)
    decrypted = triple_des_decrypt_cbc(encrypted, key, iv)

    print(f"Clave (hex): {key.hex()}")
    print(f"IV (hex): {iv.hex()}")
    print(f"Mensaje original: {message}")
    print(f"Mensaje cifrado: {encrypted}")
    print(f"Mensaje descifrado: {decrypted}")


# https://pycryptodome.readthedocs.io/en/latest/src/cipher/des3.html
# https://www.geeksforgeeks.org/triple-des-3des/
# https://gist.github.com/komuw/83ddf9b4ae8f995f15af