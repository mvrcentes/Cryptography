import Utility
from KeyGen import ECCKeyGenerator

if __name__ == '__main__':
    
    utility = Utility.Utility()
    
    # ASCII to Binary 
    print("\nASCII to Binary")
    text = "Hola Mundo"
    utility.print_colored_text(text)
    utility.print_alternating_colored_binary(text)
    
    # Base64 to Binary
    print("\nBase64 to Binary")
    base64_text = "SG9sYSBNdW5kbw=="
    decoded_text = utility.decode_base64(base64_text)
    print(f"Caracteres Base64: {base64_text}")
    print(f"Texto decodificado: {decoded_text}")

    # Binary to Base64
    print("\nBinary to Base64")
    text = "me llamo marco"
    binary = "".join(utility.ascii_to_binary(text))
    print(f"Texto en binario" + ":\n" + binary)
    print(f"Texto en Base64: {utility.binary_to_base64(binary)}")
    
    # Binary to ASCII
    print("\nBinary to ASCII")
    text = "Esto es otra prueba"
    binary = "".join(utility.ascii_to_binary(text))
    print(f"Texto en binario" + ":\n" + binary)
    print(f"Texto decodificado: {utility.binary_to_ascii(binary)}")
    
    # Base64 to ASCII
    print("\nBase64 to ASCII")
    binary = "".join(utility.ascii_to_binary("una Prueba"))
    base64_text = utility.binary_to_base64(binary)
    print(f"Texto en Base64: {base64_text}")
    print(f"Texto decodificado: {utility.decode_base64(base64_text)}")
    
    # XOR Binary
    print("\nXOR Binary")
    text1 = "uno"
    text2 = "one"
    binary1 = "".join(utility.ascii_to_binary(text1))
    binary2 = "".join(utility.ascii_to_binary(text2))
    
    print(f"Texto 1 en binario: \t{binary1}")
    print(f"Texto 2 en binario: \t{binary2}")
    print(f"Resultado XOR: \t\t{utility.xor_binary_strings(bin1=binary1, bin2=binary2)}")
    
    
    # Dynamic key generation
    ecc = ECCKeyGenerator()
    
    text = "Hello "
    private_key, public_key = ecc.generate_key_pair(text)
    
    print(f"\nTexto: {text}")
    print(f"Llave privada: {private_key}")
    print(f"Llave pública: {public_key}")
    print(hex(public_key[0]), hex(public_key[1]))
    
    # Cypher with static K 
    text = "Hello World"
    key = "mysecretkey12345" # clave fija de 16 caracteres
    
    print(f"\nTexto: {text}")  
    print(f"Llave: {key}")
    
    # Cifrado
    encrypted_binary = utility.encrypt_with_fixed_key(text, key)
    print(f"Texto cifrado: {encrypted_binary}")
    
    # Descifrado
    decrypted_text = utility.decrypt_with_fixed_key(encrypted_binary, key)
    print(f"Texto descifrado: {decrypted_text}")
    
    # Cypher with dynamic K
    text = "Hello World"
    
    # Claves de diferente longitud
    keys = [
        "short",  
        "thisisalongerkey",  
        "1234567890123456",  
        "dynamic-key-size-test"
    ]

    for key in keys:
        print(f"\nTexto: {text}")
        print(f"Clave: {key}")
        
        # Cifrado
        encrypted_binary = utility.encrypt_with_fixed_key(text, key)
        print(f"Texto cifrado: {encrypted_binary}")
        
        # Descifrado
        decrypted_text = utility.decrypt_with_fixed_key(encrypted_binary, key)
        print(f"Texto descifrado: {decrypted_text}")
    