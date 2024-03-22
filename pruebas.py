from functools import reduce

def miembro(ele, lista):
    return any(x == ele for x in lista)

def remove_if(fun, lista):
    return list(filter(lambda x: not fun(x), lista))

def vecinos(nodo, obstaculos, fin):
    x, y = nodo
    neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    valid_neighbours = list(filter(lambda coord: coord not in obstaculos and coord[0] >= 0 and coord[1] >= 0, neighbours))
    return sorted(valid_neighbours, key=lambda coord: abs(coord[0] - fin[0]) + abs(coord[1] - fin[1]))

def extender(ruta, obstaculos, visitados, fin):
    return remove_if(lambda x: miembro(x, ruta) or miembro(x, visitados), vecinos(ruta[-1], obstaculos, fin))

def prof(ini, fin, obstaculos):
    return prof_aux(fin, [(ini,)], obstaculos, set())

def prof_aux(fin, rutas, obstaculos, visitados):
    return (None if not rutas else
            list(reversed(rutas[0])) if fin == rutas[0][-1] else
            prof_aux(fin, reduce(lambda acc, ruta: acc + list(map(lambda vecino: ruta + (vecino,), extender(ruta, obstaculos, visitados, fin))), rutas, []), obstaculos, visitados.union(set(ruta[-1] for ruta in rutas))))

# Definición de la función para imprimir el resultado de manera más legible
def print_path(path):
    print("Ruta encontrada:")
    for coord in path:
        print(coord)
    print()

# Definición de las coordenadas de salida y llegada, así como los obstáculos
inicio = (0, 0)
final = (17, 19)
obstaculos = [(1, 0), (2, 2), (3, 3),]

# Ejecución de la búsqueda de la ruta más corta
ruta_corta = prof(inicio, final, obstaculos)

# Imprimir la ruta encontrada
if ruta_corta:
    print_path(ruta_corta)
else:
    print("No se encontró una ruta válida.")
