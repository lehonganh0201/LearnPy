def bai1():
    n = int(input("Nhập một số nguyên dương: "))

    total = 0
    while n > 0:
        total += n % 10
        n //= 10

    print("Tổng các chữ số là:", total)

def bai2():
    n = int(input("Nhập một số nguyên dương: "))

    sum_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum_divisors += i

    print("Tổng các ước số là:", sum_divisors)
    
def bai3():
    a = int(input("Nhập cạnh a: "))
    b = int(input("Nhập cạnh b: "))
    c = int(input("Nhập cạnh c: "))

    if a + b > c and a + c > b and b + c > a:
    
        if a == b == c:
            triangle_type = "Tam giác đều"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            triangle_type = "Tam giác vuông"
        elif a == b or b == c or a == c:
            triangle_type = "Tam giác cân"
        else:
            triangle_type = "Tam giác nhọn hoặc tù"
    else:
        triangle_type = "Ba cạnh không tạo thành tam giác"

    print("Loại tam giác là:", triangle_type)
    
bai1()
bai2()
bai3()