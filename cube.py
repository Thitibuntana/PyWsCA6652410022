import math
def twoDigits(x):
    return format(x, ".2f")

def vSquare():
    print("""
    ******************************************** 
                    SQUARE VOLUME
    ********************************************
      """)
    def doSquare():
       try:
           width = float(input("ป้อนความกว้าง: "))
           length = float(input("ป้อนความยาว: "))
           height = float(input("ป้อนความสูง: "))
           print(f"ปริมาตรทรงสี่เหลี่ยมที่คำนวณได้คือ: {twoDigits(width*length*height)}")
           print("**************************************")
       except ValueError:
            print("Please put in numbers...")
            doSquare()
    doSquare()

def vCircle():
    print("""
    ******************************************** 
                    SPHERE VOLUME
    ********************************************
      """)
    def doCircle():
        try:
           radius = float(input("ป้อนรัศมี: "))
           print(f"ปริมาตรทรงกลมที่คำนวณได้คือ: {twoDigits(4/3 * math.pi * radius**3)}")
           print("**************************************")
        except ValueError:
            print("Please put in numbers...")
            doCircle()
    doCircle()