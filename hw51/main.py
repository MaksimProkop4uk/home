def degree(num, deg):
    if (deg == 1):
        return (num)
    if (deg != 1):
        return (num * degree(num, deg - 1))
num = int(input("Введите число: "))
deg = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", degree(num, deg))
