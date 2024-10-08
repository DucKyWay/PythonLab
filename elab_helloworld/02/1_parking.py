# ให้เขียนโปรแกรมที่ทำหน้าที่คำนวนค่าจอดรถของลาดจอดรถอัตโนมัติแห่งหนึ่ง
# โดยให้รับตัวเลข 2 ค่าเข้ามาเป็น ชั่วโมง และ นาที ที่ใช้ในการจอดรถ ตามลำดับ
# หลังจากนั้นให้คำนวนค่าที่จอดรถ โดยกำหนดให้

# จอดฟรี 15 นาทีแรก
# 2 ชั่วโมงแรก 10 บาท
# ชั่วโมงถัดไปคิดชั่วโมงละ 10 บาท เศษของชั่วโมงคิดเป็น 1 ชั่วโมง
# ให้พิมพ์ราคาค่าที่จอดรถที่ต้องจ่าย

#------------------------------------------------------------------#
#------------------ Hello to python 101 elab yay ------------------#
#------------------------------------------------------------------#

import math

def main():
    hr = int(input("Input hours: "))
    m = int(input("Input minutes: "))

    m_total = (hr*60)+m
    total = 0
    
    if m_total <= 15:
        total = total
    elif m_total > 15: 
        total = total + 10

    if m_total >= 120:
        m_total = m_total - 120
        hr2 = math.ceil(m_total/60) * 10
        total = total + hr2

    print(f"Parking fee is {total} THB.")

main()