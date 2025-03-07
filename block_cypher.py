from Crypto.Cipher import DES
import secrets

def pad_manual(text, block_size=8):
    """Agrega relleno manualmente para que el texto sea múltiplo de block_size (8 bytes para DES)."""
    pad_len = block_size - (len(text) % block_size)
    padding = chr(pad_len) * pad_len  # Relleno con el número de bytes necesarios
    return text + padding

def unpad_manual(text):
    """Elimina el relleno manualmente después del descifrado."""
    pad_len = ord(text[-1])  # Último byte indica la cantidad de relleno
    return text[:-pad_len]  # Elimina los bytes de relleno

def generate_des_key():
    """Genera una clave DES aleatoria de 64 bits (8 bytes)."""
    return secrets.token_bytes(8)  # 8 bytes = 64 bits

def validate_key(key):
    """Verifica que la clave tenga exactamente 8 bytes (64 bits)."""
    if not isinstance(key, bytes) or len(key) != 8:
        raise ValueError("La clave DES debe tener exactamente 8 bytes (64 bits).")

def des_encrypt_ecb(plaintext, key):
    """Cifra un mensaje con DES en modo ECB."""
    validate_key(key)  # Verifica la clave antes de usarla
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad_manual(plaintext)
    ciphertext = cipher.encrypt(padded_text.encode())  # Convertir a bytes antes de cifrar
    return ciphertext.hex()  # Convertimos a hexadecimal para facilidad de almacenamiento

def des_decrypt_ecb(ciphertext, key):
    """Descifra un mensaje cifrado con DES en modo ECB."""
    validate_key(key)  # Verifica la clave antes de usarla
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(bytes.fromhex(ciphertext))  # Convertir desde hex a bytes
    return unpad_manual(decrypted_text.decode())  # Decodificar y remover el relleno

# 🔹 Prueba del cifrado y descifrado con ECB
if __name__ == "__main__":
    key = generate_des_key()  # Generamos una clave DES aleatoria de 64 bits
    message = "Hello, DES!"  # Mensaje de prueba (menos de 8 bytes para probar el relleno)

    encrypted = des_encrypt_ecb(message, key)
    decrypted = des_decrypt_ecb(encrypted, key)

    print(f"Clave (hex): {key.hex()}")
    print(f"Mensaje original: {message}")
    print(f"Mensaje cifrado: {encrypted}")
    print(f"Mensaje descifrado: {decrypted}")