import os
import base64

from PIL import Image
import piexif
from zoro_rc4 import rc4_decrypt

def extraer_texto_metadata(imagen_path):
    # Abrir la imagen
    img = Image.open(imagen_path)
    
    # Obtener los metadatos EXIF
    exif_dict = piexif.load(img.info.get('exif', b''))
    
    # Obtener el texto almacenado en 'Artist' (o en el campo que elegimos)
    texto = exif_dict['0th'].get(piexif.ImageIFD.Artist)
    if texto:
        return texto.decode('utf-8')
    return None

    
# Uso del código para descifrar la imagen
# Ejemplo de uso
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
image_path = os.path.join(base_dir, "recovered_data/extracted_images", "poneglyph.jpeg")
student_id = input("Introduce tu carné para descifrar el mensaje: ")

texto_cifrado_b64 = extraer_texto_metadata(image_path)
if texto_cifrado_b64 is None:
    print("No se encontró texto cifrado en los metadatos.")
else:
    try:
        # Asegurar padding correcto para base64
        missing_padding = len(texto_cifrado_b64) % 4
        if missing_padding != 0:
            texto_cifrado_b64 += '=' * (4 - missing_padding)

        texto_cifrado = base64.b64decode(texto_cifrado_b64)
        decrypted_text = rc4_decrypt(texto_cifrado, student_id)
        print(decrypted_text.decode('utf-8', errors='replace'))
    except Exception as e:
        print("Error al decodificar o descifrar:", e)

print(decrypted_text)
