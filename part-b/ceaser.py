import string
from colorama import init, Fore, Style
from dic import words  # Importamos el diccionario de palabras en español

# Inicializar colorama
init(autoreset=True)

# Definir el alfabeto en español con la "Ñ"
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Cargar el mensaje cifrado desde el archivo
with open("Cifrados/ceasar.txt", "r", encoding="utf-8") as file:
    mensaje_cifrado = file.read().strip().upper()

def descifrar_cesar(texto, shift):
    """Descifra un texto con un desplazamiento dado en el Cifrado César."""
    resultado = ""
    for char in texto:
        if char in ALFABETO:
            indice = (ALFABETO.index(char) - shift) % len(ALFABETO)
            resultado += ALFABETO[indice]
        else:
            resultado += char  # Mantener otros caracteres
    return resultado

def contar_palabras_validas(texto, diccionario):
    """Intenta encontrar palabras en el texto sin espacios comparando con un diccionario."""
    palabras_encontradas = 0
    for i in range(len(texto)):
        for j in range(i + 2, len(texto) + 1):  # Busca palabras de mínimo 2 letras
            if texto[i:j].lower() in diccionario:
                palabras_encontradas += 1
    return palabras_encontradas

def fuerza_bruta_cesar(mensaje):
    """Prueba todos los desplazamientos (0-26) y muestra resultados con colores."""
    
    mejor_shift = None
    mejor_texto = ""
    mejor_palabras = 0

    for shift in range(len(ALFABETO)):  
        texto_descifrado = descifrar_cesar(mensaje, shift)
        palabras_validas = contar_palabras_validas(texto_descifrado, words)

        # Determinar color basado en cantidad de palabras acertadas
        color = Fore.GREEN if palabras_validas > 5 else Fore.RED

        print(f"{Fore.CYAN}Probando shift: {shift}")
        print(f"{color}Palabras acertadas: {palabras_validas}")
        print(f"{color}Resultado: {texto_descifrado[:100]}...")  # Solo imprime los primeros 100 caracteres
        print(Style.RESET_ALL)

        # Guardar el mejor resultado
        if palabras_validas > mejor_palabras:
            mejor_palabras = palabras_validas
            mejor_shift = shift
            mejor_texto = texto_descifrado

    # Mostrar el mejor resultado encontrado
    if mejor_shift is not None:
        print(f"\n{Fore.YELLOW}🔹 Posible Clave: {mejor_shift}")
        print(f"{Fore.GREEN}🔓 Mensaje Descifrado: {mejor_texto}\n")

# Ejecutar la fuerza bruta
fuerza_bruta_cesar(mensaje_cifrado)

# Mejor shift encontrado: 23
# Mensaje descifrado: NNUESTROLABERINTODIGITALENCONSTANTEEVOLUCIONLAAGILIDADCRIPTOGRAFICACRIPTOAGILIDADPARAABREVIARESUNMECANISMODEDEFENSACRUCIALOSBRINDALACAPACIDADDEMODIFICARRAPIDAMENTEELUSODEALGORITMOSYCLAVESCRIPTOGRAFICOSUNAACCIONNECESARIAPARAANTICIPARNOSALASFUTURASAMENAZASDECIBERSEGURIDAD
# NUESTRO LABERINTO DIGITAL EN CONSTANTE EVOLUCIÓN


# Rerencias

# https://stackoverflow.com/questions/16291818/brute-force-caeser-cipher-python
# https://dev.to/cognivibes/hacking-the-caesar-cipher-3ic1
# GPT