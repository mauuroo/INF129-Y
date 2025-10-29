# Ejercicio 5: Red Social ⭐⭐⭐

Crear una funcion `informe(lista)` que  dada una lista de relaciones `[seguidor, seguido]` retorne:
1. Un diccionario `siguiendo` donde cada persona tenga una lista con las personas que sigue.
2. Un diccionario `seguidores` donde cada persona tenga una lista con quienes lo siguen.

**Ejemplo de entrada:**
```python
relaciones = [
    ["Ana", "Luis"], ["Luis", "Marta"], ["Marta", "Ana"], 
    ["Ana", "Marta"], ["Sofía", "Luis"], ["Carlos", "Ana"],
    ["Luis", "Sofía"], ["Marta", "Sofía"], ["Sofía", "Ana"],
    ["Carlos", "Luis"], ["Ana", "Carlos"]
]
```

**Salida esperada:**
```python

  siguiendo = {
    "Ana": ["Luis", "Marta", "Carlos"],
    "Luis": ["Marta", "Sofía"],
    "Marta": ["Ana", "Sofía"],
    "Sofía": ["Luis", "Ana"],
    "Carlos": ["Ana", "Luis"]
  }

  seguidores = {
    "Ana": ["Marta", "Carlos", "Sofía"],
    "Luis": ["Ana", "Sofía", "Carlos"],
    "Marta": ["Luis", "Ana"],
    "Sofía": ["Luis", "Marta"],
    "Carlos": ["Ana"]
  }
```

**Pista:**
- Recorre la lista de listas y actualizar ambos diccionarios simultaneamente.
---

