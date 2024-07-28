
input_name = input("Nhập họ và tên: ")

def chuan_hoa_ho_ten(name):
    words = name.strip().split()
    words = [word.capitalize() for word in words]
    return ' '.join(words)

normalized_name = chuan_hoa_ho_ten(input_name)
print("Chuỗi họ tên chuẩn hóa:", normalized_name)
