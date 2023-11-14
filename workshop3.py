import math
import area
import cube

def twoDigits(x):
    return format(x, ".2f")

def Quit():
    print("ออกจากระบบเรียบร้อย...")
    exit

print("""
    ******************************************** 
                     AREA & CUBE
    ********************************************
      """)
print("""
1. พื้นที่สี่เหลี่ยม 
2. พื้นที่วงกลม 
3. ปริมาตรทรงสี่เหลี่ยม 
4. ปริมาตรทรงกลม 
0. ออกจากการทํางาน      
      """)

def inputNumber():
    print("    ********************************************")
    choice = input("เลือกเมนู: ")
    if choice == "0":
        Quit()
    elif choice == "1":
        area.Square()
    elif choice == "2":
        area.Circle()
    elif choice == "3":
        cube.vSquare()
    elif choice == "4":
        cube.vCircle()
    else:
        print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")
        print("    ********************************************")
        print("    ********************************************")
        inputNumber()

inputNumber()