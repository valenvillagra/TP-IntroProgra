# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase
    if i >= n - 1:
        return {"done": True}
    
    if fase == "buscar":
        a = min_idx
        b = j   
        if items[b] < items[min_idx]:
            min_idx = b
        j += 1
        if j >= n:
            fase = "swap"
        return{"a": a, "b": b, "swap": False, "done": False}
    
    if fase == "swap":
        a = i
        b = min_idx

        items[a], items[b] = items[b], items[a]

        i += 1
        j = i + 1
        min_idx = i
        fase = "buscar"
        return {"a": a, "b": b, "swap": True, "done": False}