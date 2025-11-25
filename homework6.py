import csv

#Считываем purchases.csv и создаём словарь user_id -> category
purchases = {}

with open('purchases.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user_id = row['user_id']
        category = row['category']
        purchases[user_id] = category

#Построчно читаем visit_log.csv и пишем funnel.csv
with open('visit_log.csv', 'r', encoding='utf-8') as fin, \
     open('funnel.csv', 'w', newline='', encoding='utf-8') as fout:

    reader = csv.DictReader(fin)
    fieldnames = ['user_id', 'source', 'category']
    writer = csv.DictWriter(fout, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        user_id = row['user_id']
        if user_id in purchases:
            writer.writerow({
                'user_id': user_id,
                'source': row['source'],
                'category': purchases[user_id]
            })
