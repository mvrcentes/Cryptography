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
    binary = "".join(utility.BinaryRepresentation(text))
    print(f"Texto en binario" + ":\n" + binary)
    print(f"Texto en Base64: {utility.binary_to_base64(binary)}")