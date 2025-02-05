import string
from colorama import init, Fore, Style
from dic import words  # Importamos el diccionario de palabras en español

# Inicializar colorama
init(autoreset=True)

# Definir el alfabeto en español con la "Ñ"
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
UMBRAL_PALABRAS = 200  # Umbral para detenerse si hay muchas palabras acertadas

def extended_gcd(a, b):
    """Algoritmo de Euclides Extendido para encontrar el MCD y los coeficientes."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modular_inverse(a, m):
    """Calcula el inverso modular de 'a' módulo 'm'."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None  # No tiene inverso modular
    return x % m

def decrypt_affine(texto, a, b):
    """Descifra un texto cifrado con el cifrado Afín."""
    resultado = ""
    a_inv = modular_inverse(a, len(ALFABETO))
    if a_inv is None:
        return None  # Saltar si no tiene inverso

    for char in texto:
        if char in ALFABETO:
            indice = (a_inv * (ALFABETO.index(char) - b)) % len(ALFABETO)
            resultado += ALFABETO[indice]
        else:
            resultado += char  # Mantener otros caracteres
    return resultado

def contar_palabras_validas(texto, diccionario):
    """Cuenta cuántas palabras del diccionario aparecen en el texto sin espacios."""
    palabras_encontradas = 0
    for palabra in diccionario:
        if palabra in texto.lower():
            palabras_encontradas += 1
    return palabras_encontradas

def brute_force_affine(texto_cifrado):
    """Prueba todas las combinaciones de 'a' y 'b' y se detiene si encuentra palabras."""

    mejor_a, mejor_b = None, None
    mejor_texto = ""
    mejor_palabras = 0

    print(Fore.YELLOW + "\n🔹 Iniciando Fuerza Bruta para el Cifrado Afín...")

    for a in range(1, 17):  # Recorrer 'a' en el rango permitido
        if extended_gcd(a, len(ALFABETO))[0] != 1:
            continue  # Saltar si 'a' no es coprimo con el tamaño del alfabeto

        for b in range(1, 17):  # Recorrer 'b' en el rango permitido
            texto_descifrado = decrypt_affine(texto_cifrado, a, b)
            if texto_descifrado is None:
                continue  # Saltar si no se pudo descifrar

            palabras_validas = contar_palabras_validas(texto_descifrado, words)

            # Determinar color basado en cantidad de palabras acertadas
            color = Fore.GREEN if palabras_validas > 10 else Fore.RED

            print(f"{Fore.CYAN}🔹 Probando (a={a}, b={b})")
            print(f"{color}✅ Palabras acertadas: {palabras_validas}")
            print(f"{color}🔓 Resultado: {texto_descifrado[:150]}...")  # Solo primeros 150 caracteres
            print(Style.RESET_ALL)

            # Guardar el mejor resultado
            if palabras_validas > mejor_palabras:
                mejor_palabras = palabras_validas
                mejor_a, mejor_b = a, b
                mejor_texto = texto_descifrado

            # 🚨 **Solo preguntar si supera el umbral de palabras encontradas**
            if palabras_validas >= UMBRAL_PALABRAS:
                print(f"{Fore.YELLOW}\n🔹 Se encontraron muchas palabras en el intento (a={a}, b={b})")
                print(f"{Fore.GREEN}🔓 Texto: {texto_descifrado[:300]}...\n")  # Mostrar hasta 300 caracteres
                
                print("¿Quieres continuar con más claves?")
                print("[1] Continuar probando más claves")
                print("[2] Detenerse y mostrar el mejor resultado")
                
                opcion = input("Selecciona una opción: ").strip()
                
                if opcion == "2":
                    print(f"\n{Fore.YELLOW}🔹 Mejor Clave Encontrada: (a={mejor_a}, b={mejor_b})")
                    print(f"{Fore.GREEN}🔓 Mensaje Descifrado: {mejor_texto[:300]}\n")  # Mostrar hasta 300 caracteres
                    return  # Salir de la función

    # Mostrar el mejor resultado encontrado si no se detuvo antes
    if mejor_a is not None:
        print(f"\n{Fore.YELLOW}🔹 Mejor Clave Encontrada: (a={mejor_a}, b={mejor_b})")
        print(f"{Fore.GREEN}🔓 Mensaje Descifrado: {mejor_texto[:300]}\n")  # Mostrar hasta 300 caracteres

# Cargar el mensaje cifrado desde el archivo
with open("Cifrados/afines.txt", "r", encoding="utf-8") as file:
    mensaje_cifrado = file.read().strip().upper()

# Ejecutar la fuerza bruta
brute_force_affine(mensaje_cifrado)

# https://thepythoncode.com/article/how-to-crack-the-affine-cipher-in-python
# https://github.com/sukhdev01/Attacks-on-Affine-Cipher/blob/master/Brute_force_attacks_on_Affine_cipher.ipynb
# 