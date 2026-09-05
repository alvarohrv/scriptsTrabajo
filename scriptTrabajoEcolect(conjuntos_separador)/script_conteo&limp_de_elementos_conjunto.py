from collections import Counter


def analizar_conjunto(conjunto):
    # Convertir a lista para poder contar el total
    elementos = list(conjunto)

    # Cantidad total SIN limpiar
    cantidad_total = len(elementos)

    # Contar frecuencia de cada elemento
    frecuencias = Counter(elementos)

    # Conjunto de duplicados
    duplicados = [
        elemento
        for elemento, cantidad in frecuencias.items()
        if cantidad > 1
    ]

    # Eliminar duplicados conservando el orden original
    elementos_limpios = list(dict.fromkeys(elementos))

    # Cantidad limpia
    cantidad_limpia = len(elementos_limpios)

    # Contar cantidad de caracteres por elemento
    conteo_caracteres = Counter(
        len(str(elemento))
        for elemento in elementos_limpios
    )

    # ========================================================
    # MOSTRAR RESULTADOS
    # ========================================================

    print("=" * 50)
    print("ANÁLISIS DEL CONJUNTO")
    print("=" * 50)

    print(f"\nCantidad total sin limpiar: {cantidad_total}")
    print(f"Cantidad limpia de duplicados: {cantidad_limpia}")
    print(f"Duplicados eliminados: {cantidad_total - cantidad_limpia}")

    # ========================================================
    # DUPLICADOS
    # ========================================================

    print("\nDUPLICADOS ENCONTRADOS")
    print("-" * 40)

    if duplicados:
        print(",".join(
            f"'{elemento}'"
            if isinstance(elemento, str)
            else str(elemento)
            for elemento in duplicados
        ))

        print(f"\nCantidad de valores duplicados: {len(duplicados)}")
    else:
        print("No se encontraron duplicados.")

    # ========================================================
    # DESGLOSE POR CARACTERES
    # ========================================================

    print("\nDESGLOSE POR CANTIDAD DE CARACTERES")
    print("-" * 40)

    for cantidad_caracteres in sorted(conteo_caracteres):
        cantidad = conteo_caracteres[cantidad_caracteres]
        print(f"{cantidad_caracteres} caracteres: {cantidad}")

    # ========================================================
    # LISTADO LIMPIO
    # ========================================================

    print("\nLISTADO LIMPIO (SIN DUPLICADOS)")
    print("-" * 40)

    print(",".join(
        f"'{elemento}'"
        if isinstance(elemento, str)
        else str(elemento)
        for elemento in elementos_limpios
    ))

    return elementos_limpios


# ============================================================
# EJEMPLO
# ============================================================

conjunto = ('632097','027805','009430','045506','050320','090686','090686','990453','190566','241774','011742','062744','089042','099563','038643','070128','070719','071247','422605','072922','955193','036648','715836','705901','075917','755173','081147','083730','083951','093958','005502','011261','050856','648848','158886','006714')


analizar_conjunto(conjunto)