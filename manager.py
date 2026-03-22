import os
import secrets
import string
import subprocess
import base64

## Sin soporte, se omite para su uso oficial por el momento.

def generar_clave_staff(longitud=10):
    caracteres = string.ascii_letters + string.digits
    return ''.join(secrets.choice(caracteres) for i in range(longitud))

def configurar_escudo_netlify(clave):
    
    os.makedirs(os.path.join("netlify", "edge-functions"), exist_ok=True)
    
    
    js_code = f"""
export default async (request, context) => {{
    const url = new URL(request.url);
    
    // Si la URL contiene "guia-de-moderacion", activamos el escudo
    if (url.pathname.toLowerCase().includes("guia-de-moderacion")) {{
        const authHeader = request.headers.get("authorization");
        // El usuario siempre será 'staff' y la clave es la generada
        const expectedAuth = "Basic " + btoa("staff:{clave}");

        if (authHeader !== expectedAuth) {{
            return new Response("Acceso Restringido al Staff de R-NET", {{
                status: 401,
                headers: {{
                    "WWW-Authenticate": 'Basic realm="Sistema R-NET (Usuario: staff)"'
                }}
            }});
        }}
    }}
    return context.next();
}};
"""
    with open(os.path.join("netlify", "edge-functions", "protect.js"), "w", encoding="utf-8") as f:
        f.write(js_code)
        
   
    toml_code = """
[[edge_functions]]
  path = "/guia-de-moderacion/*"
  function = "protect"
"""
    with open("netlify.toml", "w", encoding="utf-8") as f:
        f.write(toml_code)

def ejecutar():
    print("[1/4] Generando nueva credencial...")
    nueva_clave = generar_clave_staff()

    print("[2/4] Compilando la web con Retype...")
    subprocess.run("retype build", shell=True, capture_output=True, text=True, errors="replace")

    print("[3/4] Levantando escudo de servidor en Netlify...")
    configurar_escudo_netlify(nueva_clave)

    print("[4/4] Desplegando en Netlify...")
    deploy_res = subprocess.run("netlify deploy --prod --dir=site", shell=True, capture_output=True, text=True, errors="replace")

    if deploy_res.returncode != 0:
        print("--- ERROR EN NETLIFY DEPLOY ---")
        return

    print(f"CLAVE_GENERADA:{nueva_clave}")
    print("NETLIFY_OK: Sitio desplegado correctamente")
    print("--- PROCESO COMPLETADO CON EXITO ---")

if __name__ == "__main__":
    ejecutar()