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


тз2

print("Работа с матрицами")

x = []
print("Введите координаты вектора x")

for i in range(2):
    x.append(float(input("Введите координату: ")))

R = []
print("Введите матрицу R")

for i in range(2):
    row = []
    for j in range(2):
        row.append(float(input("Введите число: ")))
    R.append(row)

S = []
print("Введите матрицу S")

for i in range(2):
    row = []
    for j in range(2):
        row.append(float(input("Введите число: ")))
    S.append(row)

x1 = []

for i in range(2):
    a = 0
    for j in range(2):
        a = a + R[i][j] * x[j]
    x1.append(a)

x2 = []

for i in range(2):
    a = 0
    for j in range(2):
        a = a + S[i][j] * x1[j]
    x2.append(a)

T = []

for i in range(2):
    row = []
    for j in range(2):
        a = 0
        for k in range(2):
            a = a + S[i][k] * R[k][j]
        row.append(a)
    T.append(row)

print("x1 =", x1)
print("x2 =", x2)

print("Матрица T:")
for i in range(2):
    print(T[i])

result = []

for i in range(2):
    a = 0
    for j in range(2):
        a = a + T[i][j] * x[j]
    result.append(a)

print("Результат T * x =", result)

if abs(result[0] - x2[0]) < 0.000001 and abs(result[1] - x2[1]) < 0.000001:
    print("Результаты совпадают")
else:
    print("Результаты не совпадают")
