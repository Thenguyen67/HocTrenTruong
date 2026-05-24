sampleList = [100, 50, 400, 500]

sampleList[1] = 200
print(f'Sau thay đổi : {sampleList}')

sampleList.append(600)
print(f'Sau thêm : {sampleList}')

sampleList.insert(2, 300)
print(f'Sau chèn : {sampleList}')

sampleList.remove(600)
print(f'Sau xóa bằng giá trị : {sampleList}')

sampleList.pop(0)
print(f'Sau xóa bằng chỉ số : {sampleList}')