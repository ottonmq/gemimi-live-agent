from google import genai

# LLAVE MAESTRA
client = genai.Client(api_key="AIzaSyCh3gVJA1t_wUlz0wwRo2fhDSkkdXRRArg")

print("📡 [SISTEMA]: INYECTANDO NÚCLEO GEMMA 3 (BAJA LATENCIA)...")

try:
    # Gemma 3 es ligero y rara vez da 503
    response = client.models.generate_content(
        model="models/gemma-3-27b-it", 
        contents="Shadow, confirma al Arquitecto Dmfhdilyd que el motor Gemma 3 está vivo."
    )

    print("\n" + "—"*45)
    print(f"✅ [SHADOW GEMMA]: {response.text}")
    print("—"*45)
    print("\n🚀 [STATUS]: NÚCLEO INDEPENDIENTE SOLDADO.")

except Exception as e:
    print(f"\n💀 [REPORTE FINAL]: {e}")

