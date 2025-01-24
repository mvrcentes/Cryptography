import Utility

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