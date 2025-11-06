import sys

def validfloat(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def getcoeff(prompt, default_value=None):
    while True:
        try:
            value = input(f"{prompt}: ").strip()
            if validfloat(value):
                return float(value)
            else:
                print("Ошибка: введите действительное число!")
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            sys.exit(0)

def solvebiquadratic(a, b, c):
    """Решает биквадратное уравнение ax⁴ + bx² + c = 0"""
    if a == 0:
        print("Ошибка: коэффициент A не может быть равен 0 для биквадратного уравнения!")
        return []

    D = b**2 - 4*a*c

    if D < 0:
        print("Действительных корней нет")
        return []

    roots = []

    t1 = (-b + D**0.5) / (2*a)
    if t1 >= 0:
        roots.extend([t1**0.5, -t1**0.5])

    if D > 0:
        t2 = (-b - D**0.5) / (2*a)
        if t2 >= 0:
            roots.extend([t2**0.5, -t2**0.5])

    roots = sorted(list(set(roots)))
    return roots

def main():
    args = sys.argv[1:]
    a_arg = b_arg = c_arg = None

    if len(args) >= 1 and validfloat(args[0]):
        a_arg = args[0]
    if len(args) >= 2 and validfloat(args[1]):
        b_arg = args[1]
    if len(args) >= 3 and validfloat(args[2]):
        c_arg = args[2]

    print("Решение биквадратного уравнения: Ax⁴ + Bx² + C = 0")
    print("=" * 50)

    a = getcoeff("Введите коэффициент A", a_arg)
    b = getcoeff("Введите коэффициент B", b_arg)
    c = getcoeff("Введите коэффициент C", c_arg)

    print(f"\nУравнение: {a}x⁴ + {b}x² + {c} = 0")

    roots = solvebiquadratic(a, b, c)

    if roots:
        print(f"Действительные корни: {roots}")
        print(f"Количество действительных корней: {len(roots)}")
    else:
        print("Действительных корней нет")

main()
