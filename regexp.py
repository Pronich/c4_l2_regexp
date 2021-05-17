from pprint import pprint
import re
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

def normalize_fio(list):
    name = ','.join(list)
    pattern = r"(\w+)"
    result = re.findall(pattern, name)
    if len(result) < 3:
        result.append('')
    return result

def normalize_phone(phone):
    pattern = r"((\+7|8)?\s*\(*(\d{3})\)*\s*\-*(\d{3})\-*(\d{2})\-*(\d{2}))\s*\(*([а-я.]+)*\s*(\d{4})*\)*"
    subs = r"+7(\3)\4-\5-\6 \7\8"
    result = re.sub(pattern, subs, phone)
    return result

def duplicate_account(account, contact):
    if account[2] == '':
        account.insert(2, contact[2])
        account.pop(3)
    if account[3] == '':
        account.insert(3, contact[3])
        account.pop(4)
    if account[4] == '':
        account.insert(4, contact[4])
        account.pop(5)
    if account[5] == '':
        account.insert(5, contact[5])
        account.pop(6)
    if account[6] == '':
        account.insert(6, contact[6])
        account.pop()
    return account

namelist = []
phonebook = []

for raw in contacts_list:
    contact = normalize_fio(raw[:3])
    contact.append(raw[3])
    contact.append(raw[4])
    if raw == contacts_list[0]:
        contact.append(raw[5])
    else:
        contact.append(normalize_phone(raw[5]))
    contact.append(raw[6])
    if ','.join(contact[:2]) in namelist:
        i = namelist.index(','.join(contact[:2]))
        account = duplicate_account(phonebook[i], contact)
        phonebook.pop(i)
        phonebook.append(account)
    else:
        namelist.append(','.join(contact[:2]))
        phonebook.append(contact)
pprint(phonebook)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(phonebook)