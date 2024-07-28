s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")

reversed_s1 = s1[::-1]
print("Đảo ngược của chuỗi s1:", reversed_s1)

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
while not (1 <= a < b <= len(s2)):
    print("Giá trị a và b không hợp lệ. Vui lòng nhập lại.")
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))

s2_reversed_substring = s2[:a-1] + s2[a-1:b][::-1] + s2[b:]
print("Chuỗi s2 sau khi đảo ngược từ vị trí {} đến {}: {}".format(a, b, s2_reversed_substring))

s3 = s1[::2]
print("Chuỗi s3 sau khi xóa các kí tự vị trí chẵn:", s3)

s4 = ''.join([i + j for i, j in zip(s1, s2)])
s4 += s1[len(s2):] if len(s1) > len(s2) else s2[len(s1):]
print("Chuỗi s4 đan xen các kí tự của s1 và s2:", s4)

if len(s1) > 1 and len(s2) > 1:
    swapped_s1 = s2[:2] + s1[2:]
    swapped_s2 = s1[:2] + s2[2:]
else:
    swapped_s1 = s2 + s1[1:]
    swapped_s2 = s1 + s2[1:]

print("Chuỗi s1 sau khi đổi chỗ 2 ký tự đầu tiên với s2:", swapped_s1)
print("Chuỗi s2 sau khi đổi chỗ 2 ký tự đầu tiên với s1:", swapped_s2)
