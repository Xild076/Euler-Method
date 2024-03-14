import math

dx = float(input("dx: "))
firstx = float(input("first x: "))
firsty = float(input("first y: "))
steps = int(input("steps: "))
equation = input("Equation ({x} for x and {y} for y): ")

def mathequation(x: float, y: float) -> float:
    return eval(eval("f'{}'".format(equation)))

for _ in range(steps + 1):
    dydx = mathequation(firstx, firsty)
    dy = dydx * dx
    base_str = f"x: {firstx} | y: {round(firsty, 6)} | dy/dx: {round(dydx, 6)} | dy: {round(dy, 6)}"
    print(base_str)
    firstx += dx
    firsty += dy