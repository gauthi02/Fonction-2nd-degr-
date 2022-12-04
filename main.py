from math import *
import re

def second_degres(a: float, b: float, c: float) -> any:
    delta = b**2-4*a*c
    if delta < 0:
        return "Il n'y a pas de solution"
    elif delta == 0:
        return f"Il y a une solution : {-b/2*a}"
    else:
        return f"Il y a 2 solutions: {(-b + sqrt(delta))/(2*a)} et {(-b - sqrt(delta))/(2*a)}"
    
def abc_auto() -> any:
    print("tapez votre équation du 2nd degres dans le bon ordre et avec des espaces en utilisant uniquement des nombres entiers")
    print("voici deux exemples: -3 x² +2 x -14 = 0 et 1x² - 3x + 13 = 5")
    
    equation = input("equation : ")
    numbers = re.compile('-?\d+')
    ts = equation
    result = list(map(int, numbers.findall(ts)))
    
    a, b, c, d, e = result[0], result[1], result[2], result[3], 0
    
    if d != 0:
        e = d
        d = 0
        c += e
    
    print(f"{a} x² {b} x {c} = 0")
    print(f"a = {a} b = {b} c = {c}")
    
    delta = (b**2)-4*a*c
    print(f"delta = {delta}")
    
    if delta < 0:
        return "Il n'y a pas de solution"
    elif delta == 0:
        return f"Il y a une solution : {-b/2*a}"
    else:
        return f"Il y a 2 solutions: {(-b + sqrt(delta))/(2*a)} et {(-b - sqrt(delta))/(2*a)}"

if __name__ == "__main__":
    print(abc_auto())

# utilisez la fonction second_degrès() si vous connaissez votre a, b, c et que l'équation est = 0 (veuillez coller les  signes - s'il y en a aux nombres)
# utilisez la fonction abc_auto() si vous ne savez pas ce qu'est a, b c ou ou si elle n'est pas = à 0 (veuillez coller les  signes - s'il y en a aux nombres)
