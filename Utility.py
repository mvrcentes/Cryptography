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
    def ascii_to_binary(self, text):
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
            binary_values = self.ascii_to_binary(word)
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

    #region Base64 to ASCII
    def base64_to_ascii(self, base64_string):
        """Convierte una cadena Base64 a texto ASCII."""
        binary_string = self.decode_base64(base64_string)
        ascii_text = self.binary_to_ascii(binary_string)
        return ascii_text
    
    #region XOR 
    
    # https://stackoverflow.com/questions/19414093/how-to-xor-binary-with-python
    def xor_binary_strings(self, bin1=None, bin2=None, text1=None, text2=None):
        """Realiza la operación XOR entre dos cadenas binarias o de texto.

        Parámetros:
        - bin1, bin2: Cadenas binarias a operar (ejemplo: "1101").
        - text1, text2: Texto que se convertirá a binario antes del XOR.

        Retorna:
        - Cadena binaria con el resultado del XOR.
        """

        # Convertir texto a binario si se proporciona
        if text1 is not None:
            bin1 = ''.join(self.ascii_to_binary(text1))
        if text2 is not None:
            bin2 = ''.join(self.ascii_to_binary(text2))

        # Validar que ambas cadenas binarias estén definidas
        if bin1 is None or bin2 is None:
            raise ValueError("Se requieren bin1/bin2 o text1/text2 para realizar XOR.")

        # Asegurar que ambas cadenas binarias sean de la misma longitud
        max_len = max(len(bin1), len(bin2))
        bin1 = bin1.zfill(max_len)  # Rellenar con ceros a la izquierda
        bin2 = bin2.zfill(max_len)

        # Realizar el XOR bit a bit
        xor_result = ''.join(str(int(bin1[i]) ^ int(bin2[i])) for i in range(len(bin1)))

        return xor_result

    #region cypher ASCII k Fijo
    def encrypt_with_fixed_key(self, text, key):
        """Cifra un texto ASCII usando una clave fija mediante XOR.

        Parámetros:
        - text: Cadena de texto ASCII a cifrar.
        - key: Clave de tamaño fijo en ASCII.

        Retorna:
        - Texto cifrado en binario.
        """
        # Convertir texto y clave a binario
        binary_text = ''.join(self.ascii_to_binary(text))
        binary_key = ''.join(self.ascii_to_binary(key))

        # Repetir la clave hasta igualar la longitud del texto
        extended_key = (binary_key * (len(binary_text) // len(binary_key))) + binary_key[:len(binary_text) % len(binary_key)]

        # Aplicar XOR bit a bit
        encrypted_binary = ''.join(str(int(binary_text[i]) ^ int(extended_key[i])) for i in range(len(binary_text)))

        return encrypted_binary

    def decrypt_with_fixed_key(self, encrypted_binary, key):
        """Descifra un texto cifrado usando una clave fija mediante XOR.

        Parámetros:
        - encrypted_binary: Texto cifrado en binario.
        - key: Clave en ASCII usada en el cifrado.

        Retorna:
        - Texto original en ASCII.
        """
        # Convertir clave a binario
        binary_key = ''.join(self.ascii_to_binary(key))

        # Repetir la clave hasta igualar la longitud del texto cifrado
        extended_key = (binary_key * (len(encrypted_binary) // len(binary_key))) + binary_key[:len(encrypted_binary) % len(binary_key)]

        # Aplicar XOR para descifrar
        decrypted_binary = ''.join(str(int(encrypted_binary[i]) ^ int(extended_key[i])) for i in range(len(encrypted_binary)))

        # Convertir el binario descifrado a ASCII
        decrypted_text = self.binary_to_ascii(decrypted_binary)

        return decrypted_text