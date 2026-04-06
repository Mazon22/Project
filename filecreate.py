def createTXT():
    with open("SS.txt", "w+") as SSS:
        try:
            print("enter text for file")
            st = input("ввод:")
            SSS.write(st)
        finally:
            print("ваш текст сохранен:)")
            SSS.close()

def main():
    print("привет, хочешь ли создать текстовый файл?")
    choice = input("y/n")

    if choice == "y":
        createTXT()
    else:
        return
    
main()