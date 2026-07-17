#!/usr/bin/env python3
"""Creador de carpetas de tickets.
Uso:
    python crear_carpeta.py
    python crear_carpeta.py MiTicket-22859 AguasManizales 10444
"""
import os
import re
import shutil
import sys #
from datetime import datetime
from pathlib import Path #


# ============================================================
#  Utilidades
# ============================================================

def extraer_partes(entrada):
    """
    Extrae ticket, cliente y codigo de una entrada con orden variable.
    Formato del ticket: Texto-Numero  (ej: MiTicket-22859)
    """
    partes = entrada.strip().split()
    if len(partes) < 3:
        raise ValueError("Se necesitan 3 partes: ticket, cliente, codigo")

    ticket = None
    otros = []
    for p in partes:
        if re.search(r'-\d+$', p):
            ticket = p
        else:
            otros.append(p)

    if not ticket:
        raise ValueError("No se detecto un ticket valido (formato: Texto-12345)")

    codigo = None
    cliente = None
    for item in otros:
        if item.isdigit():
            codigo = item
        else:
            cliente = item

    if not codigo:
        raise ValueError("No se detecto un codigo numerico")
    if not cliente:
        raise ValueError("No se detecto el nombre del cliente")

    return ticket, cliente, codigo


def obtener_fecha():
    """Devuelve la fecha actual en formato YYMMDD (ej: 260715)."""
    ahora = datetime.now()
    return f"{ahora.year % 100:02d}{ahora.month:02d}{ahora.day:02d}"

def crear_carpeta(nombre_carpeta):
    try:
        os.makedirs(nombre_carpeta, exist_ok=False)
        print(f"      ✅ Carpeta creada.")
        return True
    except FileExistsError:
        print(f"      ⚠️ La carpeta ya existe: {nombre_carpeta}")
        return False
    except Exception as e:
        print(f"      ❌ Error al crear carpeta: {e}")
        return False
    
# ============================================================
#  Fases
# ============================================================

def fase01_crear_carpeta(nombre_carpeta):
    """Crea la carpeta principal. Retorna True si se creo, False si ya existia."""
    print(f"\n[01] Carpeta a crear: {nombre_carpeta}")
    return crear_carpeta(nombre_carpeta)


def fase02_copiar_md_in(destino, origen, file_name_md):
    """Copia MT.md (plantilla) dentro de la carpeta destino."""
    print(f"\n[02] Copiando plantilla MD")
    if not os.path.isfile(origen):
        print(f"      [ERROR] No existe la plantilla: {origen}")
        return False
    destino_path = os.path.join(destino, file_name_md)
    try:
        shutil.copy2(origen, destino_path)
        print(f"      [✅] Copiado  {destino_path}")
        return True
    except Exception as e:
        print(f"      [ERROR] {e}")
        return False

def fase03_modifica_md_in(
        destino,
        origen,
        file_name_md,
        marcador="Ticket",
        reemplazo=None,
        ):
    """
    En MT.md dentro de destino, reemplaza 'marcador' por 'reemplazo'.
    Por defecto 'reemplazo' es el nombre de la carpeta destino.
    Usa regex con \\b para que NO matchee 'Ticketid', 'TicketId', etc.
    """
    print(f"\n[03] Modificando MT.md (reemplazar palabra exacta '{marcador}')")

    if reemplazo is None:
        reemplazo = destino # se usa el nombre de la carpeta destino
    md_path = os.path.join(destino, file_name_md)
    if not os.path.isfile(md_path):
        print(f"      [ERROR] No existe: {md_path}")
        return False
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            contenido = f.read()
        # contenido_modificado = contenido.replace("Ticket", ticket_nombre)
        patron = r"\b" + re.escape(marcador) + r"\b"
        nuevo = re.sub(patron, reemplazo, contenido)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(nuevo)
        print(f"      [OK] {marcador} -> {reemplazo}")
        return True
    except Exception as e:
        print(f"      [ERROR] {e}")
        return False


def fase04_copiar_sql_in(destino, origen, file_name_sql):
    """Copia index.sql (plantilla) dentro de la carpeta destino."""
    print(f"\n[04] Copiando plantilla SQL")
    if not os.path.isfile(origen):
        print(f"      [ERROR] No existe la plantilla: {origen}")
        return False
    destino_path = os.path.join(destino, file_name_sql)
    try:
        shutil.copy2(origen, destino_path)
        print(f"      [✅] {destino_path}")
        return True
    except Exception as e:
        print(f"      [ERROR] {e}")
        return False


def fase05_modifica_sql_in(destino, origen, file_name_sql, marcador="Ticket", reemplazo=None):
    """
    En index.sql dentro de destino, reemplaza 'marcador' por 'reemplazo'.
    Por defecto 'reemplazo' es el nombre de la carpeta destino.
    Usa regex con \\b para que NO matchee 'Ticketid', 'TicketId', etc.
    """
    print(f"\n[05] Modificando {file_name_sql} (reemplazar palabra exacta '{marcador}')")
    if reemplazo is None:
        reemplazo = destino
    sql_path = os.path.join(destino, file_name_sql)
    if not os.path.isfile(sql_path):
        print(f"      [ERROR] No existe: {sql_path}")
        return False
    try:
        with open(sql_path, "r", encoding="utf-8") as f:
            contenido = f.read()
        patron = r"\b" + re.escape(marcador) + r"\b"
        nuevo = re.sub(patron, reemplazo, contenido)
        with open(sql_path, "w", encoding="utf-8") as f:
            f.write(nuevo)
        print(f"      [OK] {marcador} -> {reemplazo}")
        return True
    except Exception as e:
        print(f"      [ERROR] {e}")
        return False


def fase06_crear_empty_folder_in(destino, subcarpeta):
    """Crea una subcarpeta vacia dentro de destino."""
    print(f"\n[06] Creando subcarpeta '{subcarpeta}'")
    path = os.path.join(destino, subcarpeta)
    try:
        os.makedirs(path, exist_ok=True)
        print(f"      [OK] {path}")
        return True
    except Exception as e:
        print(f"      [ERROR] {e}")
        return False


def fase07_crear_file_in(destino_padre, subcarpeta, nombre_archivo, contenido=""):
    """
    Crea un archivo dentro de destino_padre/subcarpeta/.
    :::: carpeta_destino/adjuntos/NOMBRE_ARCHIVO
    Pensado para 'adjuntos/MITICKET-xxxxx.txt'.
    """
    print(f"\n[07] Creando archivo '{nombre_archivo}' en '{subcarpeta}'") 
    carpeta_adj = os.path.join(destino_padre, subcarpeta) #Construir la ruta
    if not os.path.isdir(carpeta_adj):
        print(f"      [ERROR] No existe la carpeta: {carpeta_adj}")
        return False
    path = os.path.join(carpeta_adj, nombre_archivo)
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"      [OK] {path}")
        return True
    except Exception as e:
        print(f"      [ERROR] {e}")
        return False


# ============================================================
#  Main
# ============================================================

def main():
    if len(sys.argv) > 1:
        entrada = " ".join(sys.argv[1:])
    else:
        entrada = input("Ingresa el ticket y cliente (ej: MiTicket-22859 AguasManizales 10444): ")

    if not entrada.strip():
        print("No ingresaste ningun dato.")
        sys.exit(1)

    try:
        ticket, cliente, codigo = extraer_partes(entrada)
    except ValueError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

    fecha = obtener_fecha()
    # Orden confirmado: ticket-fecha-cliente-codigo
    nombre_carpeta = f"{ticket}-{fecha}-{cliente}-{codigo}"

    if not fase01_crear_carpeta(nombre_carpeta):
        # Si la carpeta ya existe, no pisamos nada. Salimos.
        print("\n⚠️ Proceso abortado: la carpeta ya existe.")
        sys.exit(2)

    # Plantillas
    base = "Base_MiTicket"
    md_origen = os.path.join(base, "MT.md")
    sql_origen = os.path.join(base, "index.sql")
    file_name_md = f"MT-{codigo}.md"
    file_name_sql = f"index-{codigo}.sql"
    folder_aux = "adjuntos"

    file_name_ticket = f"{ticket.upper()}.txt"
    contenido_ticket = f"Ticket: {ticket}\nCodigo: {codigo}\nCliente: {cliente}\nFecha: {fecha}\n"

    # Fases 2-7
    fase02_copiar_md_in(nombre_carpeta, md_origen,file_name_md)
    fase03_modifica_md_in(nombre_carpeta, md_origen, file_name_md)
    fase04_copiar_sql_in(nombre_carpeta, sql_origen, file_name_sql)
    fase05_modifica_sql_in(nombre_carpeta, sql_origen, file_name_sql)
    fase06_crear_empty_folder_in(nombre_carpeta, folder_aux)
    fase07_crear_file_in(
        nombre_carpeta,
        folder_aux,
        file_name_ticket,
        contenido=contenido_ticket
    )

    print(f"\n[OK] Carpeta '{nombre_carpeta}' lista en {os.getcwd()}")


if __name__ == "__main__":
    main()
