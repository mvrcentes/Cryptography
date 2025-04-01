# 🏴‍☠️ Proyecto CTF – Cifrados de Flujo: One Piece Edition

Este proyecto tiene como objetivo resolver una serie de retos tipo CTF (Capture The Flag) enfocados en el uso, análisis y ruptura de cifrados de flujo simétricos, incluyendo XOR, RC4 y ChaCha20.

Cada reto representa una "isla" del universo de One Piece, en donde se encuentra una **piedra Poneglyph** cifrada que guarda una **flag secreta**. A través de técnicas de criptografía y reversing, se deben recuperar y documentar estos mensajes ocultos.

---

## 🎯 Objetivos

- Aplicar conceptos de cifrado de flujo como XOR, RC4 y ChaCha20.
- Identificar debilidades en generadores de clave.
- Romper cifrados personalizados usando ataques conocidos (plaintext, análisis de flujo).
- Documentar y organizar la información recuperada.

---

## 📁 Estructura del Proyecto

```
├── challenges/                # Retos generados
├── challenges_volumes/       # Volúmenes Docker montados
├── recovered_data/           # Datos extraídos desde los retos
│   ├── extracted_images/     # Imágenes poneglyph recuperadas
│   │   ├── poneglyph.jpeg              # Imagen base
│   │   ├── poneglyph_dec.jpeg          # Imagen procesada (OCR)
│   │   ├── poneglyph_zoro.jpeg         # Imagen RC4 (reto Zoro)
│   │   ├── poneglyph_usopp.jpeg        # Imagen XOR custom (Usopp)
│   │   ├── poneglyph_nami.jpeg         # Imagen ChaCha20 (Nami)
│   ├── flags/
│   │   └── flags.txt                   # Todas las flags encontradas
│   ├── poneglyphs/
│       └── poneglyphs.txt             # Textos extraídos de las imágenes
├── docker-compose.yml
├── generate_challenges.py
├── test.py                   # Scripts personalizados para análisis
└── README.md                 # Este archivo
```
## 🔧 Cómo ejecutar los retos

1. Clona el repositorio:
   ```bash
   git clone https://github.com/locano-uvg/ctf_onepice_symmetric_cipher.git
   cd ctf_onepice_symmetric_cipher


# CTF_ONEPICE_SYMMETRIC_CIPHER
<a id="readme-top"></a>

<!--
PROJECT DESCRIPTION
-->
## 📜 Descripción

CTF_ONEPICE_SYMMETRIC_CIPHER un repositorio diseñado para conocer y practicar conceptos básicos de cifrados simétricos como:
 
- XOR básico
- RC4
- Análisis estadístico
- PRNG inseguro
- Chacha20
- Cifrado combinado

Link:
https://locano-uvg.github.io/ctf_onepice_symmetric_cipher/

## 📦 Requisitos

- Comandos básicos de Linux
- Docker
- Docker Compose
- Python


## 🚀 Instalación y Ejecución
1. Clona este repositorio e instala los requistos:

```bash
git clone https://github.com/tu_usuario/CTF_INTRO_CIFRADOS.git
cd CTF_INTRO_CIFRADOS
```

2. Instalar dependencias
```bash
pip3 install -r scripts/requirements.txt
```

3. Ejecuta el script de python

```bash
python generate_challenges
```

4. Ejecuta el docker compose

```bash
sudo docker compose up -d
```

5. Valida que las imagenes esten activas

```bash
docker ps  
```

6. Dentro del contenedor se crearán 6 retos, ejecutalos individualmente

- luffy_challenge 🤠
- zoro_challenge 🏴‍☠️
- usopp_challenge 🎯
- nami_challenge 🌊
- sanji_challenge 🔥
- robin_challenge 📜

<!-- CREAR UNA TABLA -->
|**Usuario**|**Reto**|**Nivel**|**Objetivo**|
|-------------|-----------------------|-----------|---------------------------------------------------------------------------------------|
| Luffy 🤠| XOR | 🟢 Facil | Encontrar la flag cifrada en un poneglyph.txt, aplicando XOR con su carné como clave. |
| Zoro 🏴‍☠️ | Rompiendo RC4 | 🟡 Medio  | |
| Usopp 🎯| Stream Cipher Custom  | 🟡 Medio | |
| Nami 🌊 | ChaCha20 Playground   | 🟡 Medio | |
| Sanji 🔥| Ataque de correlación | 🔴 Alto | |
| Robin 📜| TRNG o PRNG inseguro  | 🔴 Alto | |

El primer reto a resolver es una aventura con Luffy, debes iniciar sesión utilizando la contraseña onepiece

```bash
su luffy
password: onepiece
```

```bash
docker exec -it {challengeX_ctf} bash
```

7. Al encontrar la imagen puedes extrarla usando un web server then enter to the mapping port

```bash
python3 -m http.server 8080
```
- luffy_challenge 8081
- zoro_challenge  8082
- nami_challenge 8083
- sanji_challenge 8084
- robin_challenge 8085
- usopp_challenge 8086


## 📝 Tips para Resolver los Desafíos
1. **Explora los archivos del sistema**
    - Muchas pistas pueden estar escondidas en lugares comunes como:
      - Mensajes del sistema (/etc/motd)
      - Logs de autenticación (/var/log/auth.log)
      - Archivos de configuración ocultos (/etc, /home)
    
2. **Revisa los usuarios y sus archivos**
    - Identifica los usuarios en el sistema:
      ```bash
      cat /etc/passwd
      ```
    - Explora los directorios personales en /home/ con:
      ```bash
      ls -la /home/<usuario>
      ```

3. **Busca archivos con permisos inusuales**
    - Archivos como `.flag.txt`, `.hidden`, `.instrucciones` pueden contener pistas valiosas.
    - Encuentra archivos con permisos de ejecución o escritura inusuales:
      ```bash
      find / -type f -perm -4000 2>/dev/null
      ```

4. **Analiza el tráfico de red**
    - Si el reto implica una comunicación cifrada, captura paquetes con:
      ```bash
      tcpdump -i eth0 -w captura.pcap
      ```
    - Luego examina los paquetes en Wireshark para encontrar patrones.

5. **Prueba herramientas criptográficas**
    - Usa `xxd` para ver contenido hexadecimal de archivos sospechosos:
      ```bash
      xxd archivo.bin | head
      ```
    - Usa `openssl` para intentar descifrar archivos cifrados:
      ```bash
      openssl enc -d -aes-256-cbc -in archivo.enc -out archivo.txt -k clave
      ```

6. **Busca texto cifrado en logs o configuraciones**
    - Si encuentras texto aparentemente aleatorio, intenta detectar el cifrado usado con `cyberchef` o scripts de Python.

## 👥 Contribuciones
Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:
1. Realiza un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## 📞 Contacto
Si tienes preguntas o comentarios, puedes contactarnos a través de nuestras redes sociales:

* [![Instagram][Instagram]][Instagram-url]
* [![Website][Website]][Website-url]

<p align="right">(<a href="#readme-top">Ir al inicio</a>)</p>



## 👥 Contribuciones
Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:
1. Realiza un fork del repositorio.
2.	Crea una nueva rama para tu funcionalidad (git checkout -b feature/nueva-funcionalidad).
3.	Haz commit de tus cambios (git commit -m 'Añadir nueva funcionalidad').
4.	Haz push a la rama (git push origin feature/nueva-funcionalidad).
5.	Abre un Pull Request.

### Developer's

<a href="https://github.com/locano">
  <img width='75' src="https://avatars.githubusercontent.com/u/16949087?v=4" alt="Ludwing Cano" />
</a>

* [![Linkedin][Linkedin]][Linkedin-lud]
* [![GitHub][GitHub]][GitHub-lud]

<p align="right">(<a href="#readme-top">Ir al inicio</a>)</p>

## 📞 Contacto
Si tienes preguntas o comentarios, puedes contactarnos a traves de nuestras redes sociales:

* [![Instagram][Instagram]][Instagram-url]
* [![Website][Website]][Website-url]

<p align="right">(<a href="#readme-top">Ir al inicio</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[Redux]: https://img.shields.io/badge/Redux-764ABC?style=flat&logo=redux&logoColor=white
[Redux-url]: https://redux.js.org/
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[MongoDB]: https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white
[MongoDB-url]: https://www.npmjs.com/package/mongodb
[Node.js]: https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white
[Node-url]: https://nodejs.org/en/
[Reveal-js]: https://img.shields.io/badge/Reveal.js-339933?style=flat&logo=reveal.js&logoColor=white
[Reveal-url]: https://revealjs.com/
[Python]: https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Instagram]: https://img.shields.io/badge/Instagram-E4405F?style=flat&logo=instagram&logoColor=white
[Instagram-url]: https://www.instagram.com/ludwing238/
[Instagram]: https://img.shields.io/badge/Instagram-E4405F?style=flat&logo=instagram&logoColor=white
[Instagram-url]: https://www.instagram.com/ludwing238/
[Website]: https://img.shields.io/website?url=https://lc2tech.com/
[Website-url]: https://lc2tech.com/
[AntDesign]: https://img.shields.io/badge/-Ant%20Design-333333?style=flat&logo=ant-design&logoColor=0170FE
[AntDesign-url]: https://ant.design/
[Chartjs]: https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white
[Chartjs-url]: https://github.com/reactchartjs/react-chartjs-2
[Linkedin-lud]: https://www.linkedin.com/in/ludwing-cano238
[Linkedin]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[Github-lud]: https://github.com/locano
[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
