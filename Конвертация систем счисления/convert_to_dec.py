def is_in(sequence, digits):
    for digit in digits:
        if int(digit) not in sequence:
            return False
    return True
    
n=int(input("Введите число от 2 до 36: "))
while n not in range(2, 37):
    n=int(input("Введённое число не входит в указанный диапазон! Введите ещё раз: "))

n_sequence = list(range(0, n))
A=input(f"Введите число в системе счисления с основанием {n}: ")
while not is_in(n_sequence, set(A)):
    A=input(f"Введённое число содержит недопустимые цифры! Введите число в системе счисления с основанием {n}: ")

result = int(A, n)
print(result)
