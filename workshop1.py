try :
    sentence = input("ป้อนข้อความ : ")
    sList = sentence.split()
    print(f"มีคำรวมทั้งหมด {len(sList)} คำ")
    sameText = list()

    for i in sList:
        num = sList.count(i)
        if num > 1 :
            sameText.append(i) 

    sameTextS = set(sameText)
    print(f"มีคำซํ้ากันรวม {len(sameTextS)} คำคือ {' '.join(str(i) for i in sameTextS)}")  #Researched for this one..

    filterList = list()
    for i in sList:
        num = sList.count(i)
        if num > 1 and not filterList.count(i) > 0:
            filterList.append(i)
            print(f"คำว่า {i} ซํ้ากัน {num} ครั้ง")

except Exception:
    print("Exception Found.")