import yaml
import re
from datetime import datetime, date
import locale
import logging
import shutil
import os

# Configurar idioma local a español
try:
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, "Spanish_Spain.1252")
    except locale.Error:
        logging.warning("No se pudo establecer el locale en español. Los meses pueden aparecer en inglés.")

# Diccionario de meses en español (respaldo)
MESES_ES = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

def formatear_fecha_es(fecha_obj):
    try:
        return fecha_obj.strftime("%d de %B, %Y")
    except Exception:
        
        return f"{fecha_obj.day:02d} de {MESES_ES[fecha_obj.month-1]}, {fecha_obj.year}"

# Configurar el logger
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Constantes 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMBIOS_YAML = os.path.join(BASE_DIR, "cambios.yaml")
CHANGELOG_MD = os.path.join(BASE_DIR, "Changelog.md")
ORDENAR_POR = "version" 
SEMVER_REGEX = r"^\d+\.\d+\.\d+$"

# Diccionario de emojis por sección
EMOJIS_SECCIONES = {
    "mejoras": "✨",
    "correcciones": "🔧",
    "cambios": "🛠",
    "novedades": "🆕",
    "eliminado": "🗑",
    "documentación": "📚",
    "otros": "🔧"
}

# Claves aceptadas para imágenes
IMAGE_SINGLE_KEYS = ["imagen", "image"]
IMAGE_LIST_KEYS = ["imagenes", "images"]

def parsear_fecha(fecha_str):
    if isinstance(fecha_str, (datetime, date)):
        return datetime.combine(fecha_str, datetime.min.time())
    formatos = ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"]
    for formato in formatos:
        try:
            return datetime.strptime(fecha_str, formato)
        except ValueError:
            continue
    raise ValueError(f"Formato de fecha no válido: {fecha_str}")

def _agregar_imagenes(entry: dict) -> str:
    """Devuelve markdown con una o varias imágenes según el contenido del entry."""
    bloques = []

    # 1) Una sola imagen
    for k in IMAGE_SINGLE_KEYS:
        if k in entry and isinstance(entry[k], str) and entry[k].strip():
            ruta = entry[k].strip()
            bloques.append(f"![Evidencia]({ruta})\n")
            break  

    
    for k in IMAGE_LIST_KEYS:
        if k in entry and isinstance(entry[k], list):
            for ruta in entry[k]:
                if isinstance(ruta, str) and ruta.strip():
                    bloques.append(f"![Evidencia]({ruta.strip()})\n")
            break

    return "\n".join(bloques)

def procesar_entrada(entry, fecha_formateada):
    version = entry["version"]
    contenido = f"### 🛠 Versión {version} — *{fecha_formateada}*\n"

    # Secciones con bullets 
    for clave in EMOJIS_SECCIONES:
        if clave in entry:
            emoji = EMOJIS_SECCIONES[clave]
            titulo = clave.capitalize()
            contenido += f"\n**{emoji} {titulo}**\n\n"
            if isinstance(entry[clave], list):
                for item in entry[clave]:
                    contenido += f"- {item}\n"
            else:
                logging.warning(f"La clave '{clave}' no es una lista en la versión {entry['version']}")

    # Bloque de imágenes 
    imagenes_md = _agregar_imagenes(entry)
    if imagenes_md:
        contenido += f"\n{imagenes_md}"

    contenido += "\n---\n\n"
    return contenido

# Cargar YAML
try:
    logging.info("Cargando archivo YAML...")
    with open(CAMBIOS_YAML, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
except Exception as e:
    logging.error(f"Error al leer YAML: {e}")
    exit(1)

if not data:
    logging.error("El archivo YAML está vacío o malformado.")
    exit(1)

# Validar y ordenar entradas
entradas_validas = []
for entry in data:
    if "version" not in entry or "fecha" not in entry:
        logging.warning(f"Entrada inválida: {entry}")
        continue

    version = str(entry["version"])
    if not re.match(SEMVER_REGEX, version):
        logging.warning(f"Versión inválida: {version}")
        continue

    try:
        fecha_obj = parsear_fecha(entry["fecha"])
        fecha_formateada = formatear_fecha_es(fecha_obj)
        entradas_validas.append((entry, fecha_formateada))
    except ValueError as ve:
        logging.error(str(ve))

# Ordenar
if ORDENAR_POR == "version":
    entradas_validas.sort(key=lambda x: list(map(int, x[0]["version"].split("."))), reverse=True)
else:
    entradas_validas.sort(key=lambda x: parsear_fecha(x[0]["fecha"]), reverse=True)

# Backup previo
if os.path.exists(CHANGELOG_MD):
    shutil.copy(CHANGELOG_MD, CHANGELOG_MD + ".bak")

# Generar changelog
try:
    with open(CHANGELOG_MD, "w", encoding="utf-8") as out:
        out.write("# 🌐 ***Actualizaciones Web***\n\n")
        out.write("En este canal se registrarán las actualizaciones importantes de la guía. "
                  "Si deseas agregar contenido adicional o realizar alguna corrección, no dudes en contactarme por MD para implementar los cambios.\n\n")

        for entry, fecha_fmt in entradas_validas:
            contenido = procesar_entrada(entry, fecha_fmt)
            out.write(contenido)

    logging.info(f"✅ Changelog.md generado exitosamente con {len(entradas_validas)} entradas.")
except IOError as e:
    logging.error(f"Error al escribir el archivo: {e}")
    exit(1)
