milk = [0, 0, 0, 0]
milk[0] = int(input("ราคานมต่อขวด: "))
milk[1] = int(input("จำนวนฝาที่นำมาแลกนม: "))
milk[2] = int(input("จำนวนนมที่แลกได้: "))
milk[3] = int(input("เงินที่ลูกค้าจ่าย: "))

if milk[1] == 0:
    print("ไม่มีโปรโมชั่นนี้")
elif milk[1] != 0:
    