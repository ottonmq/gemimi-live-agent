import os
from google import genai

# CARGA DE VARIABLE DE ENTORNO (SEGURIDAD DE NIVEL BÚNKER)
# La API KEY ahora se jala del sistema, no se escribe en el código.
api_key_env = os.getenv("GOOGLE_API_KEY")

if not api_key_env:
    print("⚠️ [ALERTA]: No se detectó la variable GOOGLE_API_KEY. Configúrala en el entorno.")
else:
    client = genai.Client(api_key=api_key_env)

    print("📡 [SISTEMA]: INYECTANDO NÚCLEO GEMMA 3 (MODO SEGURO)...")

    try:
        # Usando Gemma 3 para validación de acceso
        response = client.models.generate_content(
            model="models/gemma-3-27b-it",
            contents="Shadow, confirma al Arquitecto Dmfhdilyd que el motor está operando bajo protocolos de seguridad."
        )

        print("\n" + "—"*45)
        print(f"✅ [SHADOW GEMMA]: {response.text}")
        print("—"*45)
        print("\n🚀 [STATUS]: NÚCLEO PROTEGIDO Y OPERATIVO.")

    except Exception as e:
        print(f"\n💀 [REPORTE FINAL]: Error de conexión o credenciales. Detalles: {e}")

