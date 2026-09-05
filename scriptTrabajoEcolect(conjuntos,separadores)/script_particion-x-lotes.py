from collections import Counter

# ============================================================
# ANALIZAR CONJUNTO
# ============================================================

def analizar_conjunto(conjunto):
    elementos = list(conjunto)

    # Cantidad total original
    cantidad_total = len(elementos)

    # Eliminar duplicados conservando el orden
    elementos_limpios = list(dict.fromkeys(elementos))

    # Cantidad después de eliminar duplicados
    cantidad_limpia = len(elementos_limpios)

    # Cantidad de caracteres por elemento
    conteo_caracteres = Counter(
        len(str(elemento))
        for elemento in elementos_limpios
    )

    print("=" * 60)
    print("ANÁLISIS DEL CONJUNTO")
    print("=" * 60)

    print(f"\nCantidad total sin limpiar: {cantidad_total}")
    print(f"Cantidad limpia de duplicados: {cantidad_limpia}")
    print(f"Duplicados eliminados: {cantidad_total - cantidad_limpia}")

    print("\nDESGLOSE POR CANTIDAD DE CARACTERES")
    print("-" * 60)

    for caracteres in sorted(conteo_caracteres):
        cantidad = conteo_caracteres[caracteres]
        print(f"{caracteres} caracteres: {cantidad}")

    print("\nLISTADO LIMPIO (SIN DUPLICADOS)")
    print("-" * 60)

    print(formatear_elementos(elementos_limpios))

    return elementos_limpios


# ============================================================
# SEPARAR EN LOTES
# ============================================================

def separar_en_lotes(conjunto, tamano, unico=False):
    elementos = list(conjunto)

    # Eliminar duplicados si unico=True
    if unico:
        elementos = list(dict.fromkeys(elementos))

    if tamano <= 0:
        raise ValueError("El tamaño del lote debe ser mayor que 0.")

    print("\n" + "=" * 60)
    print("SEPARACIÓN EN LOTES")
    print("=" * 60)

    print(f"\nTotal de elementos: {len(elementos)}")
    print(f"Tamaño de cada lote: {tamano}")
    print(
        f"Duplicados eliminados: {'SÍ' if unico else 'NO'}"
    )

    cantidad_lotes = (
        (len(elementos) + tamano - 1) // tamano
    )

    print(f"Cantidad de lotes: {cantidad_lotes}")

    print("\nDESGLOSE")
    print("-" * 60)

    for numero, inicio in enumerate(
        range(0, len(elementos), tamano),
        start=1
    ):
        lote = elementos[inicio:inicio + tamano]

        print(f"Lote {numero}: {len(lote)} elementos")

    print("\nLOTES")
    print("-" * 60)

    for numero, inicio in enumerate(
        range(0, len(elementos), tamano),
        start=1
    ):
        lote = elementos[inicio:inicio + tamano]

        print(f"\nLOTE {numero} ({len(lote)} elementos)")
        print(formatear_elementos(lote))

    return [
        elementos[inicio:inicio + tamano]
        for inicio in range(0, len(elementos), tamano)
    ]


# ============================================================
# FORMATEAR ELEMENTOS
# ============================================================

def formatear_elementos(elementos):
    """
    Strings:
        '632097','027805','009430'

    Números:
        632097,27805,9430
    """

    return ",".join(
        f"'{elemento}'"
        if isinstance(elemento, str)
        else str(elemento)
        for elemento in elementos
    )


# ============================================================
# INPUT
# ============================================================

conjunto = (
'632097','027805','009430','045506','050320','090686','004906','070128','070719','071247','422605','072922','955193','023045','0WBOJP','154872','0WBOJP'
)


# ============================================================
# EJECUCIÓN
# ============================================================

# Analizar y obtener listado limpio
conjunto_limpio = analizar_conjunto(conjunto)


# Separar en lotes
# True  = elimina duplicados
# False = conserva duplicados
separar_en_lotes(conjunto, 8, True)  # seg parametro cantidad por lote