from colorama import Fore, Style, init

class Utility:
    def __init__(self):
        self.colors = [Fore.RED, Fore.YELLOW]  

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
    
    


# 