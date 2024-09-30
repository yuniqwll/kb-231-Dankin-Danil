import math

def discriminant(a, b, c): # Функція для обчислення дискримінанту
    return b**2-4*a*c


def find_roots(a, b, c):  # Функція для знаходження коренів квадратного рівняння
    D = discriminant(a, b, c)

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"два корені: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x= -b / (2*a)
        print(f"Один корінь: x = {x1}")
    else:
        print("Дійсних коренів немає")

a = int(input ("введіть коофіцієнт a: ")) 
b = int(input ("введіть коофіцієнт b: "))
c = int(input ("введіть коофіцієнт с: "))
find_roots(a, b, c)