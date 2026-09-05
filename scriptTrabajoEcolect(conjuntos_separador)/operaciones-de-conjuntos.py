
# 1. Definir los conjuntos
universo = {'632097','027805','009430','045506','050320','090686','004906','990453','190566','241774','011742','062744','089042','099563','038643','070128','070719','071247','422605','072922','955193','036648','715836','705901','075917','755173'}


muestra_a_validar_subConj = {'840781','0WBOJP','058851','749437','730912','105906','072039','033835','931675','132919','135435','002183','230940','162028','033239','087528','02993D','669148','401059','595054','916462','103003','010279','071808','312030','283827','031519','003406','682506','071556','668461','111546','094254','058128','070956','141146','141409','152826','099063','506964','153247','150656','373268','063255','051857','156706','641014'} 

                                        
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




# 🔵 El universo (fuente-de-verdad) son (26) elemento.
# ⚪ La muestra son (47) elemento.
# ⭕ Ojo: no encontados, elementos de muestra que ya NO cumplen con el universo son (47) elementos. {'682506', '058851', '283827', '072039', '162028', '010279', '003406', '916462', '135435', '401059', '071808', '152826', '0WBOJP', '002183', '156706', '105906', '132919', '063255', '595054', '153247', '931675', '669148', '058128', '033835', '840781', '103003', '087528', '749437', '033239', '02993D', '668461', '070956', '071556', '641014', '051857', '312030', '031519', '099063', '111546', '094254', '141146', '150656', '141409', '506964', '373268', '230940', '730912'}
# ✅ 'muestra-depurada' sin elementos que no cumplen con el universo (Intersección-inclunsiva) (0): set() 
# ⚠️ _ 'universo-resto' (Intersección-exclusiva) (26): {'050320', '070719', '004906', '075917', '990453', '070128', '090686', '955193', '715836', '099563', '071247', '705901', '038643', '036648', '045506', '062744', '632097', '755173', '027805', '072922', '089042', '422605', '011742', '190566', '241774', '009430'}
# ⚠️ _ validacion 'universo-resto'(26) + 'muestra-depurada(0)' (26)