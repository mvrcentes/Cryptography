import Utility

if __name__ == '__main__':
    
    utility = Utility.Utility()
    
    # ASCII to Binary 
    text = "Hola Mundo"
    utility.print_colored_text(text)
    utility.print_alternating_colored_binary(text)
    
    # Base64 to Binary
    base64_text = "SG9sYSBNdW5kbw=="
    decoded_text = utility.decode_base64(base64_text)
    print(f"Caracteres Base64: {base64_text}")
    print(f"Texto decodificado: {decoded_text}")

