import csv

def load_clients(csv_filename): ##Читает CSV и возвращает список словарей с полями
    clients = []
    with open(csv_filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            clients.append(row)
    return clients


def map_device(device_type): ##Преобразует тип устройства в фразу.
    mapping = {
        "mobile": "мобильного устройства",
        "tablet": "планшета",
        "laptop": "ноутбука",
        "desktop": "настольного компьютера",
    }
    return mapping.get(device_type, "устройства неизвестного типа")


def gender_words(sex): ##Возвращает строки для гендера
    if sex == "female":
        return "женского", "совершила"
    else:
        return "мужского", "совершил"


def build_description(client_row): ##Формирует одну строку описания покупателя по заданному шаблону.
    name = client_row["name"]
    device_type = client_row["device_type"]
    browser = client_row["browser"]
    sex = client_row["sex"]
    age = client_row["age"]
    bill = client_row["bill"]
    region = client_row["region"]

    gender_adj, verb = gender_words(sex)
    device_phrase = map_device(device_type)

    description = (
        f"Пользователь {name} {gender_adj} пола, {age} лет {verb} покупку "
        f"на {bill} у.е. с {device_phrase} в браузере {browser}. "
        f"Регион, из которого совершалась покупка: {region}."
    )
    return description


def write_descriptions(descriptions, txt_filename): ##Записывает все описания в текстовый файл, по одному в строке.
    with open(txt_filename, "w", encoding="utf-8") as f:
        for line in descriptions:
            f.write(line + "\n")


def main():
    input_csv = "web_clients_correct.csv"
    output_txt = "clients_descriptions.txt"

    clients = load_clients(input_csv)
    descriptions = []

    for client in clients:
        desc = build_description(client)
        descriptions.append(desc)

    write_descriptions(descriptions, output_txt)


if __name__ == "__main__":
    main()
