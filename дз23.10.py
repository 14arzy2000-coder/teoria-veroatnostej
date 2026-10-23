```python
import math

print("Расчет перемещений")

x = float(input("Введите координату x точки A: "))
y = float(input("Введите координату y точки A: "))

ux = float(input("Введите координату x вектора u: "))
uy = float(input("Введите координату y вектора u: "))

vx = float(input("Введите координату x вектора v: "))
vy = float(input("Введите координату y вектора v: "))

rx = ux + vx
ry = uy + vy

bx = x + rx
by = y + ry

length_u = math.sqrt(ux ** 2 + uy ** 2)
length_v = math.sqrt(vx ** 2 + vy ** 2)
length = length_u + length_v

print("Результирующий вектор r:", rx, ry)
print("Координаты точки B:", bx, by)
print("Длина пути:", length)
```
