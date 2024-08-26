import csv
import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def split_name(fname):
    fio = " ".join(fname[:3]).split()
    while len(fio) < 3:
        fio.append("")
    return fio + fname[3:]


def f_phone(phone):
    pattern = re.compile(
        r"(\+7|8)?\s*\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(?:\s*\(?(доб\.\s*\d{4})\)?)?")
    formatted_phone = pattern.sub(r"+7(\2)\3-\4-\5 \6", phone)
    return formatted_phone



grouped_contacts = {}
normalized_contacts = []
for contact in contacts_list:
    normalized_contact = split_name(contact)
    normalized_contact[5] = f_phone(normalized_contact[5])
    normalized_contacts.append(normalized_contact)

for contact in normalized_contacts:
    key = (contact[0], contact[1])
    if key in grouped_contacts:
        exist = grouped_contacts[key]
        for f in range(3, len(exist)):
            if not exist[f] and contact[f]:
                exist[f] = contact[f]
    else:
        grouped_contacts[key] = contact

    final_contacts = list(grouped_contacts.values())

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(final_contacts)
pprint(final_contacts)
