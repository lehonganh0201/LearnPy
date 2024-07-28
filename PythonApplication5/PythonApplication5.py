
N = int(input("Nhập số lượng số N: "))

numbers = list(map(int, input("Nhập các số: ").split()))

liked_last_digits = {1, 3, 5, 7, 9}

liked_numbers = [num for num in numbers if num % 10 in liked_last_digits]

liked_numbers.sort()

print(len(liked_numbers))


print(" ".join(map(str, liked_numbers)))
