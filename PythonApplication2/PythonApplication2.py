k = int(input("Nhập số lượng phần tử k: "))
a = []
for _ in range(k):
    a.append(int(input("Nhập phần tử: ")))

n = int(input("Nhập số dòng n: "))
m = int(input("Nhập số cột m: "))

if n * m <= k:
    matrix = []
    for i in range(n):
        row = a[i*m:(i+1)*m]
        matrix.append(row)
    print("Ma trận X({} × {}):".format(n, m))
    for row in matrix:
        print(row)
else:
    print("NO")
