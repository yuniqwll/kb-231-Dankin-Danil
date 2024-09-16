def findD(a,b,c):
    return b**2-4*a*c
a=int(input("Введіть коофіцієнт a: "))
b=int(input("Введіть коофіцієнт b: "))
c=int(input("Введіть коофіцієнт c: "))
print("Дискримінант:", findD(a, b ,c))