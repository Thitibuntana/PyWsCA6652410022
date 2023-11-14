import random
print("""
    ******************************************** 
          ทายตัวเลขที่มีค่าอยู่ที่ 1 -100 กันเถอะ
    ********************************************
      """)
try:
    correctNumber = random.randint(1, 100)
    def inputNumber():
        try:
            n = int(input("ป้อนตัวเลขที่ต้องการทาย (1-100): "))
            if n == correctNumber:
                print("ยินดีด้วยคุณทายถูก")
            elif n > correctNumber:
                print("คุณทายผิดตัวเลขที่ป้อนมากไป")
                inputNumber()
            elif n < correctNumber:
                print("คุณทายผิดตัวเลขที่ป้อนน้อยไป")
                inputNumber()
        except ValueError:
           print("Please put in numbers...")
           inputNumber()

    inputNumber()
except Exception:
   print("Exception found...")
