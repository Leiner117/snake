from functools import reduce

def miembro(ele, lista):
    return any(filter(lambda x: x == ele, lista))

def remove_if(fun, lista):
    return list(filter(lambda x: not fun(x), lista))


def vecinos(nodo, obstaculos, fin):
    x, y = nodo
    neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    valid_neighbours = list(filter(lambda coord: coord[0] >= 0 and coord[1] >= 0 and coord not in obstaculos, neighbours))
    sorted_neighbours = sorted(valid_neighbours, key=lambda coord: abs(coord[0] - fin[0]) + abs(coord[1] - fin[1]))
    return sorted_neighbours

def extender(ruta, obstaculos, visitados, fin):
    return remove_if(lambda x: miembro(x, ruta) or miembro(x, visitados), vecinos(ruta[-1], obstaculos, fin))

def prof(ini, fin, obstaculos):
    return prof_aux(fin, [(ini,)], obstaculos, set())

def prof_aux(fin, rutas, obstaculos, visitados):
    if not rutas:
        return None  # No se encontró ninguna ruta válida
    elif fin == rutas[0][-1]:
        return list(reversed(rutas[0]))  # Se encontró una ruta válida
    else:
        nuevas_rutas = reduce(lambda acc, ruta: acc + [ruta + (vecino,) for vecino in extender(ruta, obstaculos, visitados, fin)], rutas, [])
        nuevos_visitados = visitados.union(reduce(lambda acc, ruta: acc.union({ruta[-1]}), nuevas_rutas, set()))
        mejor_ruta = min(nuevas_rutas, key=lambda ruta: sum(map(lambda coord: abs(coord[0] - fin[0]) + abs(coord[1] - fin[1]), ruta)))
        return prof_aux(fin, [mejor_ruta], obstaculos, nuevos_visitados)
