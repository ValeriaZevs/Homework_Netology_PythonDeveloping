from datetime import datetime

print("Введите дату (или q для выхода):")

while True:
    s = input("> ").strip()
    if s.upper() == "q":
        break

    # пробуем оставить только правую часть после тире, если она есть
    if "—" in s:
        s = s.split("—", 1)[1].strip()

    dt = None

    # 1. The Moscow Times — Wednesday, October 2, 2002
    try:
        dt = datetime.strptime(s, "%A, %B %d, %Y")
    except ValueError:
        pass

    # 2. The Guardian — Friday, 11.10.13
    if dt is None:
        try:
            dt = datetime.strptime(s, "%A, %d.%m.%y")
        except ValueError:
            pass

    # 3. Daily News — Thursday, 18 August 1977
    if dt is None:
        try:
            dt = datetime.strptime(s, "%A, %d %B %Y")
        except ValueError:
            pass

    if dt is not None:
        print(dt)
    else:
        print("Формат не распознан, введите следующую строку.")