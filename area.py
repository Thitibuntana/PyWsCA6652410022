import math
def twoDigits(x):
    return format(x, ".2f")

def Square():
    print("""
    ******************************************** 
                        SQUARE
    ********************************************
      """)
    def doSquare():
        try:
            width = float(input("ป้อนความกว้าง: "))
            length = float(input("ป้อนความยาว: "))
            print(f"พื้นที่สี่เหลี่ยมที่คำนวณได้คือ: {twoDigits(width*length)}")
            print("**************************************")
        except ValueError:
            print("Please put in numbers...")
            doSquare()
    doSquare()

def Circle():
    print("""
    ******************************************** 
                        CIRCLE
    ********************************************
      """)
    def doCircle():
        try:
            radius = float(input("ป้อนรัศมี: "))
            print(f"พื้นที่วงกลมที่คำนวณได้คือ: {twoDigits(math.pi * radius**2)}")
            print("**************************************")
        except ValueError:
            print("Please put in numbers...")
            doCircle()  
    doCircle()