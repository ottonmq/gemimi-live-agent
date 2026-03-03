import os
import django
import google.generativeai as genai
from dotenv import load_dotenv

# 1. CARGA EL ENTORNO DE RENDER (.env)
load_dotenv()

# 2. SINCRONIZACIÓN CON TU PROYECTO
# Usamos 'market.settings' porque tu ROOT_URLCONF dice 'market.urls'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'market.settings')
django.setup()

# 3. IMPORTACIÓN DIRECTA DESDE TU APP
from marketapp.models import Publicacion

# 4. CONFIGURACIÓN DE IA CON TU GOOGLE_API_KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def sistema_shadow():
    # EL AGENTE SE CONECTA A 'otto-market-db' EN RENDER
    try:
        # Traemos solo lo que no está vendido
        stock_db = Publicacion.objects.filter(vendido=False)
        
        # Mapeamos los productos reales de tu base
        inventario = "\n".join([
            f"ID: {p.id} | {p.titulo} | {p.marca} | ${p.precio}" 
            for p in stock_db
        ])

        print("\n" + "—"*45)
        print("🦾 [SHADOW_AGENT]: ACCESO A RENDER DB EXITOSO")
        print(f"📡 BASE: otto-market-db | PRODUCTOS: {stock_db.count()}")
        print("—"*45)

        while True:
            orden = input("\n👤 OTTONMQ > ")
            if orden.lower() in ['salir', 'exit']: break

            # El Agente ahora maneja la data de tu base en Render
            prompt = f"""
            Eres Shadow, agente táctico de Otto-task. 
            Tu base de datos real en Render es:
            {inventario if inventario else 'Sin productos activos.'}
            
            Orden: {orden}
            Responde breve y con estilo neón.
            """
            
            res = model.generate_content(prompt)
            print(f"\n🤖 SHADOW > {res.text}")

    except Exception as e:
        print(f"\n[❌] ERROR DE CONEXIÓN A RENDER DB: {e}")

if __name__ == "__main__":
    sistema_shadow()

