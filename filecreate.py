def create_file():
    print("\n--- Создание файла ---")
    print("Введите содержимое файла (пустая строка для завершения):")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    content = "\n".join(lines)
    
    path = input("\nПуть сохранения (например, output.txt): ")
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Файл сохранён: {path}\n")

def menu():
    while True:
        print("===== МЕНЮ =====")
        print("1. Создать файл")
        print("2. Выход")
        choice = input("\nВыбор: ")
        
        if choice == "1":
            create_file()
        elif choice == "2":
            print("Пока!")
            break
        else:
            print("Неверный пункт, попробуй снова.\n")

if __name__ == "__main__":
    menu()
