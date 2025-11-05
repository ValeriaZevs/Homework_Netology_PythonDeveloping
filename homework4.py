# исходные данные
documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_owner(doc_number: str, docs: list): #Возвращает имя владельца по номеру документа.
    for doc in docs:
        if doc.get('number') == doc_number:
            return doc.get('name')
    return None


def get_shelf(doc_number: str, dirs: dict): #Возвращает номер полки, на которой лежит документ.
    for shelf, numbers in dirs.items():
        if doc_number in numbers:
            return shelf
    return None


def main_loop(docs: list, dirs: dict):
    while True:
        command = input("Введите команду (p - владелец, s - полка, q - выход): ").strip().lower()
        if command == 'q':
            print("Завершение работы")
            break
        elif command == 'p':
            doc_number = input("Введите номер документа: ").strip()
            owner = get_owner(doc_number, docs)
            if owner:
                print(f"Владелец документа: {owner}")
            else:
                print("Документ не найден")
        elif command == 's':
            doc_number = input("Введите номер документа: ").strip()
            shelf = get_shelf(doc_number, dirs)
            if shelf:
                print(f"Документ хранится на полке: {shelf}")
            else:
                print("Документ не найден на полках")

        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main_loop(documents, directories)
