from google import genai
import json

client = genai.Client(api_key="AIzaSyB5_tWSNcYWooPrEJmE5dxoxoZSLY4dy3M")

print("--- ⚡ SHADOW: MODO GENERACIÓN MASIVA ⚡ ---")

prompt = """
Eres el experto en inventarios de Otto-market. 
Toma el archivo backup_otto.json y genera una lista completa de 100 productos.
Deben estar balanceados entre: Vehículos, Tecnología, Hogar, Servicios y Otros.
Incluye precios realistas y descripciones técnicas tipo Cyberpunk. 
Solo devuelve el JSON puro, nada de texto extra.
"""

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview", 
        contents=prompt
    )
    with open('backup_otto.json', 'w') as f:
        f.write(response.text)
    print("\n[SHADOW]: Misión cumplida, Arquitecto Otto Mendoza. 100 productos inyectados.")
except Exception as e:
    print(f"\n[ERROR]: {e}")

