from colorama import Fore, Style, init

class Utility:
    def __init__(self):
        self.colors = [Fore.RED, Fore.YELLOW]  

    #region ASCII to Binary
    # https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
    def DecimalToBinary(self, decimal):
        if decimal == 0:
            return "0"
        if decimal == 1:
            return "1"
        return self.DecimalToBinary(decimal // 2) + str(decimal % 2)

    # https://www.geeksforgeeks.org/python-program-to-convert-ascii-to-binary/
    def BinaryRepresentation(self, text):
        binary_strings = []
        for char in text:
            number = ord(char)
            b_repr = self.DecimalToBinary(number).zfill(8)  # Asegurar 8 bits por carácter
            binary_strings.append(b_repr)
        return binary_strings

    def print_colored_text(self, text):
        words = text.split()
        colored_text = ""
        for i, word in enumerate(words):
            colored_text += self.colors[i % len(self.colors)] + word + " " + Style.RESET_ALL
        print(f"Cadena Original:\n {colored_text}")

    def print_alternating_colored_binary(self, text):
        words = text.split()
        for i, word in enumerate(words):
            binary_values = self.BinaryRepresentation(word)
            binary_colored = " ".join(
                (self.colors[i % len(self.colors)] + b + Style.RESET_ALL)
                if j % 2 == 0 else b  
                for j, b in enumerate(binary_values)
            )
            print(f"Resultado de binario para {self.colors[i % len(self.colors)]}{word}{Style.RESET_ALL}:")
            print(binary_colored)
            print()
    
    #region Base64 to Binary
    def generate_base64_alphabet(self):
        """Genera la tabla Base64 estándar dinámicamente."""
        return (
            [chr(i) for i in range(ord('A'), ord('Z') + 1)] +  # A-Z
            [chr(i) for i in range(ord('a'), ord('z') + 1)] +  # a-z
            [chr(i) for i in range(ord('0'), ord('9') + 1)] +  # 0-9
            ['+', '/']  # Caracteres adicionales de Base64
        )

    # https://minyak128.medium.com/learning-base64-without-using-modules-14983582f969
    def decode_base64(self, encoded_string):
        """Decodifica una cadena Base64 a texto utilizando las funciones existentes."""
        base64_chars = self.generate_base64_alphabet()
        encoded_string = encoded_string.replace('=', '')  # Eliminar el padding

        # Convertir cada carácter a su valor binario de 6 bits usando DecimalToBinary
        binary_str = ""
        for char in encoded_string:
            if char in base64_chars:
                index = base64_chars.index(char)
                binary_str += self.DecimalToBinary(index).zfill(6)

        # Dividir la cadena binaria en bloques de 8 bits
        binary_chunks = [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]
        
        # Eliminar el último bloque si no tiene 8 bits completos
        if len(binary_chunks[-1]) != 8:
            binary_chunks.pop()

        # Convertir cada bloque binario en su carácter ASCII correspondiente
        decoded_text = "".join(chr(int(b, 2)) for b in binary_chunks)

        return decoded_text
    
    #region Binary to Base64
    def binary_to_base64(self, binary_string):
        """Convierte una cadena binaria a Base64 utilizando la tabla generada dinámicamente."""
        base64_chars = self.generate_base64_alphabet()

        # Asegurar que la longitud de la cadena binaria sea múltiplo de 6
        padding_length = (6 - len(binary_string) % 6) % 6
        binary_string += '0' * padding_length  # Rellenar con ceros si es necesario

        # Dividir la cadena binaria en bloques de 6 bits
        binary_chunks = [binary_string[i:i + 6] for i in range(0, len(binary_string), 6)]

        # Convertir cada bloque de 6 bits a decimal y luego a Base64
        base64_result = ""
        for chunk in binary_chunks:
            decimal_value = int(chunk, 2)
            base64_result += base64_chars[decimal_value]

        # Agregar padding si la longitud original del binario no era múltiplo de 24 bits
        if padding_length > 0:
            base64_result += "=" * (padding_length // 2)

        return base64_result
    
    #region Binary to ASCII
    def binary_to_ascii(self, binary_string):
        """Convierte una cadena binaria a texto ASCII."""
        
        # Asegurar que la longitud del binario sea múltiplo de 8
        if len(binary_string) % 8 != 0:
            raise ValueError("La longitud de la cadena binaria debe ser múltiplo de 8 bits.")

        # Dividir la cadena binaria en bloques de 8 bits
        binary_chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

        # Convertir cada bloque de 8 bits a un carácter ASCII
        ascii_chars = [chr(int(chunk, 2)) for chunk in binary_chunks]

        # Unir todos los caracteres para formar la cadena ASCII final
        ascii_text = ''.join(ascii_chars)

        return ascii_text
    #endregion
    