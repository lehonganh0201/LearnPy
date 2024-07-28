N = int(input("Nhập số lượng phần tử N: "))
lst = []
for _ in range(N):
    lst.append(int(input("Nhập phần tử: ")))

X = int(input("Nhập số X: "))
print(f"Số lần {X} xuất hiện trong list: {lst.count(X)}")

if len(lst) >= 8:
    lst[2:8] = [8, 5, 4, 0, 1, 3]
else:
    lst[2:] = [8, 5, 4, 0, 1, 3][:len(lst) - 2]

max_value = max(lst)
min_value = min(lst)
print(f"Số lớn nhất trong list: {max_value}")
print(f"Số nhỏ nhất trong list: {min_value}")

Y = int(input("Nhập số Y: "))
lst.insert(0, Y)

if lst == sorted(lst):
    print("TĂNG")
elif lst == sorted(lst, reverse=True):
    print("GIẢM")
else:
    print("NO")

new_lst = [sum(lst[:i+1]) for i in range(N)]
print("List mới với các phần tử là tổng i phần tử đầu tiên của list cũ:", new_lst)

lst2 = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
sorted_lst2 = sorted(lst2)
sorted_lst2_abs = sorted(lst2, key=abs)

print("List mới sắp xếp theo thứ tự tăng dần của giá trị:", sorted_lst2)
print("List mới sắp xếp theo thứ tự tăng dần của giá trị tuyệt đối:", sorted_lst2_abs)
