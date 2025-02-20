# Ejercicio Stream Cipher
📌 **Laboratorio de Criptografía - Implementación de un Cifrado de Flujo**

## 📖 Objetivos
- Comprender el concepto de un **keystream** y su importancia en los cifrados de flujo.
- Implementar un esquema básico de **cifrado y descifrado utilizando XOR**.
- Analizar las implicaciones de la **reutilización del keystream** y su longitud en la seguridad.

## 📂 Contenido del Proyecto  
El laboratorio está desarrollado en un **Jupyter Notebook (`.ipynb`)** e incluye los siguientes pasos:

1. **Generación del Keystream**  
   - Implementación de un **Generador de Números Pseudoaleatorios (PRNG)**.  
   - Uso de una **clave (seed/nonce)** para inicializar el PRNG.  
   - Garantizar que el keystream tenga la misma longitud que el mensaje.

2. **Cifrado del Mensaje**  
   - Conversión del mensaje en una representación en bytes.  
   - Aplicación de la operación **XOR** con el keystream para cifrar el mensaje.  

3. **Descifrado del Mensaje**  
   - Aplicación de la operación **XOR** con el mismo keystream para recuperar el mensaje original.  
   - Comparación entre mensaje original y descifrado para validar la correcta implementación.

4. **Pruebas de Seguridad**  
   - Evaluación de qué sucede al cambiar la **clave (seed)** del PRNG.  
   - Análisis de los riesgos de **reutilizar el keystream en diferentes mensajes**.  
   - Validación de cómo la **longitud del keystream afecta la seguridad**.

## 📌 Requisitos  
Para ejecutar el laboratorio, asegúrate de tener instaladas las siguientes bibliotecas de Python:

```bash
pip install -r requirements.txt
```

## 🚀 Cómo ejecutar el laboratorio  
1. Descarga el archivo `stream-cipher.ipynb`.  
2. Asegúrate de tener instaladas las bibliotecas necesarias.  
3. Abre el **Jupyter Notebook** y ejecuta las celdas en orden.  
4. Analiza los resultados y responde las preguntas de seguridad.  

## 🔬 Ejemplos de Entrada y Salida  
El laboratorio incluye pruebas con los siguientes ejemplos:

1. **Mensaje corto**: `"Hola"`  
2. **Frase mediana**: `"Stream Cipher"`  
3. **Mensaje más largo**: `"Cifrado de flujo seguro"`  

Cada uno es **cifrado y luego descifrado**, asegurando que el mensaje original se recupere correctamente.  

## 🛠 Pruebas Unitarias  
El laboratorio incluye pruebas unitarias para validar que el cifrado y descifrado funcionan correctamente:

- **Se verifica que al cifrar y descifrar se recupere el mensaje original.**  
- **Se prueba que el keystream generado tenga la longitud adecuada.**  
- **Se evalúa que la misma semilla genera el mismo keystream.**  
- **Se verifica que semillas distintas generen keystreams diferentes.**  

## 📊 Consideraciones de Seguridad  
- **Nunca reutilizar el keystream** en diferentes mensajes.  
- **Usar un PRNG fuerte** para evitar patrones predecibles.  
- **Proteger la clave (seed) y el vector de inicialización (IV).**  
- **Garantizar que la longitud del keystream sea igual o mayor que el mensaje.**  

## 🏆 Conclusión  
Después de implementar y analizar el cifrado de flujo, se concluye que:  
- **El uso de XOR es sencillo pero inseguro si se reutiliza el keystream.**  
- **El PRNG básico no es lo suficientemente fuerte para criptografía real.**  
- **El keystream debe generarse de forma única para cada mensaje.**  

## 📅 Información del Proyecto  
✉️ **Autor:** *Marco Ramírez*  
📅 **Fecha:** *20 de febrero del 2025*  
🔗  *[**Repositorio**](https://github.com/mvrcentes/Cryptography/tree/stream-cipher)*  