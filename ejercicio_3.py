def mas_cercano_entre(numeros: list[int], query: int, limite_inf: int, limite_sup: int):
    """
    Busca en la lista `numeros` el valor más cercano a `query` entre las posiciones `limite_inf` y `limite_sup` (inclusivos).
    """

    # Asumimos que el primer número es el más cercano.
    print(
        f"Buscando en la lista {numeros}, el valor más cercano a {query}, entre los índices {limite_inf} y {limite_sup} ( o sea, en la lista {numeros[limite_inf : limite_sup + 1]} )"
    )

    # Asumimos un valor más cercano
    valor_mas_cercano = numeros[limite_inf]
    print(f"Asumimos que el valor más cercano es el primero de la lista, {valor_mas_cercano}, cualquier cosa, despues demostramos lo contrario")

    # Y obtenemos la distancia entre nuestra query, y el valor que asumimos que es el más cercano
    minima_distancia = abs(query - valor_mas_cercano)
    print(f"La distancia entre {query} y {valor_mas_cercano} es de {minima_distancia}")

    # Es más conciso usar slicing que un range
    # Hacemos limite_inf + 1 , porque sería al pedo evaluar el primer número, si ya lo asumimos cuando seteamos valor_mas_cercano
    for numero in numeros[limite_inf + 1 : limite_sup + 1]:
        distancia = abs(query - numero)
        print("---")
        print(f"Evaluando el número {numero}, la distancia es de {distancia}")
        if distancia < minima_distancia:
            print("Encontramos una distancia aún más corta!")
            print(f"Valor previo de minima_distancia: {minima_distancia}")
            minima_distancia = distancia
            print(f"Nuevo valor de minima_distancia: {minima_distancia}")
            valor_mas_cercano = numero
            print(f"El nuevo número más cercano es {valor_mas_cercano}")

    return valor_mas_cercano


print(mas_cercano_entre([2, 3, 4, 5, 6], 6, 1, 3))
print("### ### ### ###")
print(mas_cercano_entre([2, 3, 4, 5, 6], -2, 0, 2))
