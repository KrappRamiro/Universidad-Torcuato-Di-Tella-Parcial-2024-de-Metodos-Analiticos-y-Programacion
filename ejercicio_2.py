def diccionario_minimal(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    """
    En base a dos diccionarios (`d1` y `d2`), retorna un nuevo diccionario llamado `dm`.

    Las keys de `dm` son las keys que `d1` y `d2` tienen en comun.

    El valor de cada key es el menor valor entre `d1` y `d2`
    """
    # dm la vamos a usar para ir creando nuestro diccionario
    dm = {}
    # Y vamos a iterar toooodas las keys de d1
    for key in d1:
        # Si hay una key que NO está en d2, ya sabemos que no va a pertenecer a dm, y podemos usar continue para pasar al siguiente loop
        if key not in d2:
            continue
        # Luego, obtenemos el valor de esta clave en d1 y d2
        valor_d1 = d1[key]
        valor_d2 = d2[key]
        # Y comparamos ambos valores para saber cuál es el menor.
        # recordemos que el menor valor es el que va en dm
        if valor_d1 < valor_d2:
            dm[key] = valor_d1
        else:
            dm[key] = valor_d2
    # Una vez iteradas todas las keys, retornamos nuestro diccionario dm
    return dm


mydict_1 = {
    "uno": 1,
    "dos": 3,
    "tres": 3,
}


mydict_2 = {
    "cuatro": 4,
    "uno": 1,
    "dos": 2,
}

assert diccionario_minimal(mydict_1, mydict_2) == {"uno": 1, "dos": 2}
