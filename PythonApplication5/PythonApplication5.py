def is_armstrong_3(num):
    digits = [int(d) for d in str(num)]
    sum_of_powers = sum(d ** 3 for d in digits)
    return sum_of_powers == num

def armstrong_numbers(n):
    armstrong_nums = [num for num in range(1, n + 1) if is_armstrong_3(num)]
    return armstrong_nums

def is_perfect(num):
    sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
    return sum_of_divisors == num

def perfect_numbers(n):
    perfect_nums = [num for num in range(1, n + 1) if is_perfect(num)]
    return perfect_nums

n = int(input("Nhập số n: "))
print(f"Các số Armstrong bậc 3 từ 1 đến {n} là: {armstrong_numbers(n)}")
print(f"Các số hoàn hảo từ 1 đến {n} là: {perfect_numbers(n)}")

