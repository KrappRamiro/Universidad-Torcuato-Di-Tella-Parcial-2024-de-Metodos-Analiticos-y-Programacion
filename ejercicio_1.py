# El nombre de la función DEBERÍA estar en imperativo
def son_mago_goma(p1: str, p2: str, mapeo_silabas: dict[str, tuple[str, ...]]) -> bool:
    """
    Recibe dos palabras, `p1` y `p2`, y se fija si son _mago goma_.

    Para que dos palabras sean _mago goma_, la sílaba final de `p1` tiene que ser la sílaba final de `p2`.

    Args:
        p1 (str): La primera palabra a analizar
        p2 (str): La segunda palabra a analizar
        mapeo_silabas (dict[str, tuple[str, ...]]):
            Un diccionario el cual tiene, como `key`'s, todas las palabras del idioma español.
            A cada `key`, le corresponde un value, el cual es una tupla con las sílabas de la palabra.

            **Podemos asumir que todas las palabras que recibimos están en este diccionario**

    Returns:
        - `True`, si `p1` y `p2` son mago goma
        - `False`, si `p1` y `p2` NO son mago goma


    Example:
        ```
        # Definimos nuestras palabras
        mapeo_silabas = {
            "persiana": ("per", "sia", "na"),
            "navaja": ("na", "va", "ja"),
            "reloj": ("re", "loj"),
        }

        # p1 y p2 SI son mago goma, porque:
        # - persiana termina con na
        # - navaja empieza con na
        p1 = "persiana"
        p2 = "navaja"

        # Pero p2 y p3 NO son mago goma, porque
        # - navaja termina con ja
        # - reloj empieza con re
        # En este caso, para que sean mago goma, p3 tendría que empezar con ja, pero en cambio empieza con re
        p3 = "reloj"

        # Con assert afirmamos que lo que esté adentro de () sea verdadero
        assert son_mago_goma(p1, p2, mapeo_silabas)
        assert not son_mago_goma(p2, p3, mapeo_silabas)

        ```
    """

    # Lo primero que debería hacer nuestra función es buscar p1 y p2 en mapeo_silabas
    # Si p1 o p2 no estan en el diccionario de mapeo_silabas,
    # vamos a terminar la función devolviendo False
    # Al usar return, la función se deja de ejecutar
    if p1 not in mapeo_silabas:
        print("ERROR: p1 NO existe en mapeo_silabas.")
        return False

    if p2 not in mapeo_silabas:
        print("ERROR: p2 NO existe en mapeo_silabas.")
        return False

    # Ahora que sabemos que p1 y p2 si estan en el diccionario, procedemos a obtener sus mapeo_silabas !

    p1_silabas = mapeo_silabas.get(p1)
    p2_silabas = mapeo_silabas.get(p2)

    # Ahora lo que tenemos que hacer es:
    # - obtener la última sílaba de p1
    # - obtener la primera sílaba de p2
    # - Retornar True si son iguales, o False si son distintas

    p1_ultima_silaba = p1_silabas[-1]
    p2_primera_silaba = p2_silabas[0]

    return p1_ultima_silaba == p2_primera_silaba


# El nombre de la función DEBERÍA estar en imperativo
def posiciones_invalidas(palabras: list[str], mapeo_silabas: dict[str, tuple[str, ...]]) -> list[int]:
    """
    Recibe una lista de palabras y una lista de mapeo_silabas, y devuelve una lista con las posiciones en donde alguien dijo una palabra invalida

    Args:
        palabras: tuple[str, ...]: La lista de palabras que se dijeron
        mapeo_silabas (dict[str, tuple[str, ...]]):
            Un diccionario el cual tiene, como `key`'s, todas las palabras del idioma español.
            A cada `key`, le corresponde un value, el cual es una tupla con las sílabas de la palabra.

            **Podemos asumir que todas las palabras que recibimos están en este diccionario**

    Returns:
        Una lista con las posiciones en donde alguien dijo una palabra invalida

    Example:
        ```
        nuestras_silabas = {
            "mago": ("ma", "go"),
            "goma": ("go", "ma"),
            "persiana": ("per", "sia", "na"),
            "reloj": ("per", "sia", "na"),
            "naranja": ("na", "ran", "ja"),
            "carne": ("car", "ne"),
            "neto": ("ne", "to"),
            "hola": ("ho", "la"),
            "lave": ("la", "ve"),
            "veces": ("ve", "ces"),
            "cesped": ("ces", "ped"),
            "queso": ("que", "so"),
            "sordo": ("sor", "do"),
            "donde": ("don", "de"),
            "delta": ("del", "ta"),
        }

        nuestras_palabras_1 = [
            "mago",
            "goma",
            "carne",
            "neto",
        ]

        nuestras_palabras_2 = [
            "hola",
            "lave",
            "veces",
            "cesped",
        ]
        nuestras_palabras_3 = [
            "queso",
            "sordo",
            "donde",
            "delta",
        ]

        assert posiciones_invalidas(nuestras_palabras_1, nuestras_silabas) == [2]

        assert posiciones_invalidas(nuestras_palabras_2, nuestras_silabas) == []

        assert posiciones_invalidas(nuestras_palabras_3, nuestras_silabas) == [1, 2, 3]
        ```
    """

    # Lo primero que vamos a hacer, es tener una lista vacia, en donde vamos a ir poniendo toooodas
    # las veces que alguien dice una combinación invalida
    combinaciones_invalidas = []

    # qué hace palabras[1:] ? crea una nueva lista iniciando desde el segundo elemento de palabras
    # Y nuestro zip pone en pares el primero elemento de palabras, con el primer elemento de palabras[1:], el segundo con el segundo, y asi
    # Esto crea pares como (palabras[0], palabras[1]), (palabras[1], palabras[2]), etc.
    # Tambien usamos enumerate para obtener el índice, el cual usamos para saber dónde se equivocaron
    for indice, (p1, p2) in enumerate(zip(palabras, palabras[1:])):
        # Si es una combinación inválida
        if not son_mago_goma(p1, p2, mapeo_silabas):
            # El índice empieza en 0, pero recordemos que la primera palabra nunca puede estar mal!
            # Eso ya nos da un indicio de que debemos poner el índice + 1
            combinaciones_invalidas.append(indice + 1)

    # Una vez terminado, devolvemos las combinaciones invalidas
    return combinaciones_invalidas


# El nombre de la función DEBERÍA estar en imperativo
def posiciones_repeticiones(palabras: list[str]) -> list[int]:
    """
    Un jugador no puede repetir inmediatamente la palabra que acaba de decir.
    Por ejemplo, si yo digo `"mago"` y mi contrincante dice `"goma"`, no puedo volver a decir `"mago"`.
    Por eso, esta función recibe una lista `palabras` y retorna una lista de las posiciones donde un
    jugador repitió su última palabra

    Args:
        palabras: tuple[str, ...]: La lista de palabras que se dijeron
    Returns:
        Una lista con las posiciones en donde se repitió una palabra
    Example:
        ```
        nuestras_palabras_4 = [
            "mago",
            "goma",
            "mago",
            "goma",
        ]

        nuestras_palabras_5 = [
            "ropero",
            "ropero",
            "ropa",
            "paro",
            "ropero",
        ]

        assert posiciones_repeticiones(nuestras_palabras_4) == [2, 3]
        assert posiciones_repeticiones(nuestras_palabras_5) == []
        ```
    """

    # Aca guardamos las repeticiones que hubieron
    repeticiones = []

    # Comenzamos desde el índice 2 porque es el primer turno posible donde un jugador podría repetir una palabra (su segundo turno).
    for i in range(2, len(palabras)):
        # Si la palabra que dijo, es IGUAL a la palabra que dijo en su turno anterior (dos elementos antes)
        # Agregamos el índice a la lista de repeticiones
        if palabras[i] == palabras[i - 2]:
            repeticiones.append(i)
    return repeticiones


def es_valida(palabras: list[str], silabas: dict[str, tuple[str, ...]]) -> bool:
    """Retorna True si se cumplen las reglas y False si no cumple alguna"""
    if posiciones_invalidas(palabras, silabas):
        return False
    if posiciones_repeticiones(palabras):
        return False
    return True


nuestras_silabas = {
    "mago": ("ma", "go"),
    "goma": ("go", "ma"),
    "persiana": ("per", "sia", "na"),
    "reloj": ("per", "sia", "na"),
    "naranja": ("na", "ran", "ja"),
    "carne": ("car", "ne"),
    "neto": ("ne", "to"),
    "hola": ("ho", "la"),
    "lave": ("la", "ve"),
    "veces": ("ve", "ces"),
    "cesped": ("ces", "ped"),
    "queso": ("que", "so"),
    "sordo": ("sor", "do"),
    "donde": ("don", "de"),
    "delta": ("del", "ta"),
}

assert son_mago_goma("mago", "goma", nuestras_silabas)
assert not son_mago_goma("mago", "reloj", nuestras_silabas)
assert son_mago_goma("persiana", "naranja", nuestras_silabas)

nuestras_palabras_1 = [
    "mago",
    "goma",
    "carne",
    "neto",
]

nuestras_palabras_2 = [
    "hola",
    "lave",
    "veces",
    "cesped",
]
nuestras_palabras_3 = [
    "queso",
    "sordo",
    "donde",
    "delta",
]

assert posiciones_invalidas(nuestras_palabras_1, nuestras_silabas) == [2]

assert posiciones_invalidas(nuestras_palabras_2, nuestras_silabas) == []

assert posiciones_invalidas(nuestras_palabras_3, nuestras_silabas) == [1, 2, 3]

nuestras_palabras_4 = [
    "mago",
    "goma",
    "mago",
    "goma",
]

nuestras_palabras_5 = [
    "ropero",
    "ropero",
    "ropa",
    "paro",
    "ropero",
]

assert posiciones_repeticiones(nuestras_palabras_4) == [2, 3]
assert posiciones_repeticiones(nuestras_palabras_5) == []
