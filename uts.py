#bil kuat 
num = int(input("Masukkan sebuah bilangan: "))
temp = num
factorials = 0

while temp > 0:
    digit = temp % 10  
    factorial = 1  
    for i in range(1, digit + 1):
        factorial *= i
    factorials += factorial
    temp //= 10  
if factorials == num:
    print(f"{num} adalah bilangan kuat")
else:
    print(f"{num} bukan bilangan kuat")


#bilangan sempurna
num = int(input("Masukkan sebuah bilangan: "))
pembagi = 0

for i in range(1, num):
    if num % i == 0:
        pembagi += i

if pembagi == num:
    print(f"{num} adalah bilangan perfect")
else:
    print(f"{num} bukan bilangan perfect")

#palindrome
num = int(input("Masukkan sebuah bilangan: "))
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if original_num == reversed_num:
    print(f"{original_num} adalah bilangan palindrome")
else:
    print(f"{original_num} bukan bilangan palindrome")

#berat badan
weight = float(input("Masukkan berat badan (kg): "))
height = float(input("Masukkan tinggi badan (m): "))

bmi = weight / (height ** 2)

print(f"Indeks Massa Tubuh (BMI) adalah: {bmi:.2f}")

#pangkat sempurna
num = int(input("Masukkan sebuah bilangan: "))
is_perfect = False

for base in range(2, int(num ** 0.5) + 1):
    power = base
    while power <= num:
        power *= base
        if power == num:
            is_perfect = True
            break
    if is_perfect:
        break

if is_perfect:
    print(f"{num} adalah pangkat sempurna")
else:
    print(f"{num} bukan pangkat sempurna")

