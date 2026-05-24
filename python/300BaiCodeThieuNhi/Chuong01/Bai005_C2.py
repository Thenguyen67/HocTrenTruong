#Chương trình tính điểm trung bình và xếp loại học sinh

# Sử dụng hàm sum() để tính tổng điểm và chia cho độ dài
# len() của danh sách scores để lấy điểm trung bình.
def hamTinhTBC(scores):
    return sum(scores) / len(scores) #Độ dài mảng

def hamPhanLoaiHS(trungBinhCong):
    if trungBinhCong >= 8.5:
        return "Xuất sắc"
    elif trungBinhCong >= 7.0:
        return "Giỏi"
    elif trungBinhCong >= 5.5:
        return "Khá"
    elif trungBinhCong >= 4.0:
        return "Trung bình"
    else:
        return "Yếu"

try:
    mangMonHoc = [] 
    soMonHoc = int(input("Nhập số lượng môn học: "))
    if soMonHoc <= 0:
        print("Số lượng môn học phải lớn hơn 0.")
    else:
        for i in range(soMonHoc):
            monHoc = float(input(f"Nhập điểm môn học thứ {i+1} : "))
            if monHoc < 0 or monHoc > 10:
                print("Điểm số phải từ 0 đến 10. Vui lòng nhập lại.")
                break
            mangMonHoc.append(monHoc)
            
        if len(mangMonHoc) == soMonHoc:
            trungBinhCong = hamTinhTBC(mangMonHoc)
            phanLoaiHS = hamPhanLoaiHS(trungBinhCong)
            print(f"Điểm trung bình: {trungBinhCong:.2f}")
            print(f"Xếp loại: {phanLoaiHS}")
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
