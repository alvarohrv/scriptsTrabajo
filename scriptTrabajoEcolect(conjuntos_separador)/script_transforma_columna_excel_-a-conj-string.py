def transformar(lineas):
    # Limpiar espacios y eliminar líneas vacías
    elementos = [
        linea.strip()
        for linea in lineas
        if linea.strip()
    ]

    # Convertir al formato deseado
    resultado = ",".join(
        f"'{elemento}'"
        for elemento in elementos
    )

    print("=" * 60)
    print("RESULTADO")
    print("=" * 60)

    print(resultado)

    print("\n" + "=" * 60)
    print(f"Cantidad de elementos: {len(elementos)}")


# ============================================================
# DATOS DE ENTRADA
# ============================================================

lineas = """
632097
027805
009430
045506
050320
224453
886370
225727
225759
045248
056398
231328
081716
265796
233246
""".strip().splitlines()


# ============================================================
# EJECUTAR
# ============================================================

transformar(lineas)



# ============================================================
# RESULTADO
# ============================================================
# '632097','027805','009430','045506','050320','224453','886370','225727','225759','045248','056398','231328','081716','265796','233246'
# ============================================================
# Cantidad de elementos: 15