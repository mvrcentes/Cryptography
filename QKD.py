#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/bin/python3
#!/bin/env python3


# # Ejercicio QKD

# In[2]:


import random
import pandas as pd


# In[3]:


BASES = ["+", "x"]  # + = recta, x = diagonal
BITS = [0, 1]


# In[4]:


def codificar_foton(bit, base):
    if base == "+":
        return "|" if bit == 0 else "—"
    elif base == "x":
        return "/" if bit == 0 else "\\"


# In[ ]:


def simular_bb84(n=10):
    resultados = []

    for i in range(n):
        bit_alice = random.choice(BITS)
        base_alice = random.choice(BASES)
        foton = codificar_foton(bit_alice, base_alice)

        base_bob = random.choice(BASES)

        if base_bob == base_alice:
            bit_bob = bit_alice
        else:
            bit_bob = random.choice(BITS)

        bases_coinciden = base_bob == base_alice
        usar_bit = "sí" if bases_coinciden else "no"

        resultados.append({
            "N°": i+1,
            "Bit de Alice": bit_alice,
            "Base de Alice (+/x)": base_alice,
            "Fotón enviado": foton,
            "Base de Bob (+/x)": base_bob,
            "Bit recibido": bit_bob,
            "¿Bases coinciden?": "sí" if bases_coinciden else "no",
            "¿Usar bit?": usar_bit
        })

    return pd.DataFrame(resultados)


# In[9]:


df = simular_bb84(n=20)  
df


# In[10]:


# Espía
def simular_bb84_con_eve(n=15, prob_intercepcion=0.5):
    resultados = []

    for i in range(n):
        bit_alice = random.choice(BITS)
        base_alice = random.choice(BASES)
        foton_original = codificar_foton(bit_alice, base_alice)

        fue_interceptado = random.random() < prob_intercepcion

        if fue_interceptado:
            base_eve = random.choice(BASES)
            if base_eve == base_alice:
                bit_eve = bit_alice
            else:
                bit_eve = random.choice(BITS)
            # Eve reenvía con su base y su medición
            base_bob = random.choice(BASES)
            if base_bob == base_eve:
                bit_bob = bit_eve
            else:
                bit_bob = random.choice(BITS)
        else:
            base_bob = random.choice(BASES)
            if base_bob == base_alice:
                bit_bob = bit_alice
            else:
                bit_bob = random.choice(BITS)

        bases_coinciden = base_bob == base_alice
        usar_bit = "sí" if bases_coinciden else "no"

        resultados.append({
            "N°": i+1,
            "Bit de Alice": bit_alice,
            "Base de Alice": base_alice,
            "Interceptado por Eve": "sí" if fue_interceptado else "no",
            "Base de Bob": base_bob,
            "Bit recibido por Bob": bit_bob,
            "¿Bases coinciden?": "sí" if bases_coinciden else "no",
            "¿Usar bit?": usar_bit
        })

    return pd.DataFrame(resultados)


# In[11]:


df_eve = simular_bb84_con_eve(n=20, prob_intercepcion=0.5)
df_eve


# ## Comparación

# In[19]:


# Filtrar bits válidos (donde las bases coinciden)
clave = df_eve[df_eve["¿Usar bit?"] == "sí"].reset_index(drop=True)

# Crear strings con los bits
bits_alice = "".join(map(str, clave["Bit de Alice"]))
bits_bob = "".join(map(str, clave["Bit recibido por Bob"]))

# Crear string de coincidencias visuales
coincidencias = "".join("✓" if a == b else "✗" for a, b in zip(bits_alice, bits_bob))

# Mostrar resultado
print("Bits de Alice: ", " ".join(bits_alice))
print("Bits de Bob:   ", " ".join(bits_bob))
print("Coincidencia:  ", " ".join(coincidencias))


# ## Analisis
# 
# 

# ### 1. ¿Cuántos bits finales obtuvieron de la clave?

# In[12]:


clave = df_eve[df_eve["¿Usar bit?"] == "sí"]
len(clave)


# ### 2. ¿Qué porcentaje representa respecto al total?

# In[13]:


porcentaje = len(clave) / len(df_eve) * 100
f"{porcentaje:.2f}%"


# ### 3. ¿Qué pasaría si Eve interceptara los fotones y usara bases incorrectas?
# 
# 
# Si Eve usa la base incorrecta, introduce errores: 
# * Al medir con la base incorrecta, modifica aleatoriamente el fotón
# * Bob podría recibir un bit diferente al que Alice envió, incluso cuando las bases coincidan.
# 
# Esto rompe la correlación esperada, haciendo que los errores aumenten en la clave final.

# ### 4. ¿Cómo se puede detectar su presencia?
# 
# Alice y Bob comparan una parte de sus bits finales

# In[15]:


error_rate = (clave["Bit de Alice"] != clave["Bit recibido por Bob"]).mean()
error_rate


# por ejemplo el error es del 11% significa que pudo haber un ataque

# ### 5. ¿Qué ventajas y desventajas tiene este protocolo frente a otros cifrados tradicionales?
# 
# Ventajas:
# * Seguridad cuántica: Basada en las leyes de la física, no en supuestos matemáticos
# * Detección de intrusos: Cualquier intento de espionaje deja rastro
# * Generación de claves perfectas (one-time pad)
# 
# Desventajas:
# * Costoso y difícil de implementar en la práctica
# * Requiere canal cuántico físico (fibra óptica o aire)
# * No cifra directamente, solo distribuye claves

# ## Referencias 
# * https://computerhoy.20minutos.es/reportajes/tecnologia/qkd-criptografia-cuantica-que-es-814885
# * https://www.gaussianos.com/criptografia-protocolo-de-distribucion-de-clave-bb84/
# 
# 
