
# 1. Definir los conjuntos (pueden iniciar como tuplas o listas, los convertimos a set)
universo = {22534,17046,11693,21560,20201,19277,19651,21125,19121,20102,21080,20949,21123,20056,22633,17779,22470,8759,4901,18650,5133,5214,18912,11957,5026,20664,6690,22843,16852,17686,19547,18472,21084,20127,14272,20471,22160,15079,22701,4133,4134,4028,7067,8533,18775,20656,12655,16785,19783,18657,19043,17600,21056,22308,22309,22310,22311,19784,16894,15902,20610}

muestra_a_validar_subConj = {343006, 270139, 20201,19277, 5654, 654654 } 
                                        
                                        
# 2. Operaciones de conjuntos
encontrados = universo.intersection(muestra_a_validar_subConj)  # O también: universo & muestra_a_validar_subConj % # Intersección (&): Elementos que están en AMBOS conjuntos
ya_no_cumple = muestra_a_validar_subConj - encontrados
resto = universo.difference(muestra_a_validar_subConj)   # O también: universo - muestra_a_validar_subConj ## Diferencia (-): Elementos que están en 'universo' pero NO en 'muestra_a_validar_subConj'

print(f"🔵 El universo (fuente-de-verdad) son ({len(universo)}) elemento.")
print(f"⚪ La muestra son ({len(muestra_a_validar_subConj)}) elemento.")

if (len(ya_no_cumple) == 0):
    pass
else:
    print(f"⭕ Ojo: no encontados, elementos de muestra que ya NO cumplen con el universo son ({len(ya_no_cumple)}) elementos. {ya_no_cumple}")

if (len(ya_no_cumple) > 0):
    print(f"✅ 'muestra-depurada' sin elementos que no cumplen con el universo (Intersección-inclunsiva) ({len(encontrados)}): {encontrados} ")
else:
    print(f"✅ 'Todos los elementos de la muestra estan en el universo: cantidad de elementos igual a la muestra ({len(muestra_a_validar_subConj)})")
print(f"⚠️ _ 'universo-resto' (Intersección-exclusiva) ({len(resto)}): {resto}")
print(f"⚠️ _ validacion 'universo-resto'({len(resto)}) + 'muestra-depurada({len(encontrados)})' ({len(resto)+len(encontrados)})")
