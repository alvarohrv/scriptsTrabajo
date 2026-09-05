
def separar_valores(lineas, separador):
    izquierda = []
    derecha = []
    no_separados = []

    for linea in lineas:
        linea = linea.strip()

        # Ignorar líneas vacías
        if not linea:
            continue

        # Separar únicamente por la primera aparición
        partes = linea.split(separador, 1)

        # Si no encuentra el separador
        if len(partes) != 2:
            no_separados.append(linea)
            continue

        valor_izq = partes[0].strip()
        valor_der = partes[1].strip()

        izquierda.append(valor_izq)
        derecha.append(valor_der)

    # ========================================================
    # RESULTADOS
    # ========================================================

    print("=" * 70)
    print("CONJUNTO IZQUIERDO")
    print("=" * 70)

    print(",".join(f"'{valor}'" for valor in izquierda))

    print("\n" + "=" * 70)
    print("CONJUNTO DERECHO")
    print("=" * 70)

    print(",".join(f"'{valor}'" for valor in derecha))

    print("\n" + "=" * 70)
    print("CONJUNTO QUE NO SE LOGRA SEPARAR")
    print("=" * 70)

    print(",".join(f"'{valor}'" for valor in no_separados))

    print("\n" + "=" * 70)
    print("RESUMEN")
    print("=" * 70)

    print(f"Elementos procesados: {len(izquierda) + len(no_separados)}")
    print(f"Elementos separados: {len(izquierda)}")
    print(f"Elementos sin separar: {len(no_separados)}")

    return izquierda, derecha, no_separados


# ============================================================
# DATOS DE ENTRADA
# Pega aquí directamente desde Excel
# ============================================================

lineas = """
840781-320018997058
0WBOJP-320019010204
058851-320019238457
132919-320019288535
080645-320022611089
034730-320021665496
110831-320023950554
028721-320029503972
010063-320022013802
320255132903
""".strip().splitlines()


# ============================================================
# EJECUCIÓN
# ============================================================

izquierda, derecha, no_separados = separar_valores(lineas, '-')




# ======================================================================
# CONJUNTO IZQUIERDO
# ======================================================================
# '840781','0WBOJP','058851','132919','080645','034730','110831','028721','010063'
# ======================================================================
# CONJUNTO DERECHO
# ======================================================================
# '320018997058','320019010204','320019238457','320019288535','320022611089','320021665496','320023950554','320029503972','320022013802'
# ======================================================================
# CONJUNTO QUE NO SE LOGRA SEPARAR
# ======================================================================
# '320255132903'
# ======================================================================
# RESUMEN
# ======================================================================
# Elementos procesados: 10
# Elementos separados: 9
# Elementos sin separar: 1