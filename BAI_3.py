name = input("Nhập tên của bệnh nhân")
patient_age = int(input("Nhập tuổi của bệnh nhân"))



if name == "":
    print("Vui lòng nhập tên")
elif patient_age <= 0 or patient_age > 100:
    print("Tuổi khong hợp lệ")
  
elif patient_age >= 80 and patient_age <= 100:
    print("ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa.")
    print(f"Bệnh nhân {name} \nTuổi {patient_age} ")
else:
    print("KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh.")
    print(f"Bệnh nhân {name} \nTuổi {patient_age} ")

# đầu tiên ta sẽ kiểm tra họ tên trước sau rồi đó đến tuổi 