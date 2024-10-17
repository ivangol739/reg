from pprint import pprint
import re
import csv


def format_name(contact):
	full_name = " ".join(contact[:3]).split()
	while len(full_name) < 3:
		full_name.append("")
	contact[:3] = full_name[:3]
	return contact


def format_phone(contact):
	pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
	sub = r'+7(\2)-\3-\4-\5 \6\7'
	phone = contact[-2]
	contact[-2] = re.sub(pattern, sub, phone)
	return contact


def merge_contacts(contacts):
	merged = {}
	for contact in contacts:
		name_key = (contact[0], contact[1])
		if name_key not in merged:
			merged[name_key] = contact
		else:
			for i in range(len(contact)):
				if not merged[name_key][i]:
					merged[name_key][i] = contact[i]
	return list(merged.values())


if __name__ == "__main__":
	with open("phonebook_raw.csv", encoding="utf-8",) as f:
		rows = csv.reader(f, delimiter=",")
		contacts_list = list(rows)

	contacts_list = [format_name(contact) for contact in contacts_list]
	contacts_list = [format_phone(contact) for contact in contacts_list]
	new_contacts_list = merge_contacts(contacts_list)

	with open("new_phonebook_raw.csv", "w", encoding="utf-8") as f:
		datawriter = csv.writer(f, delimiter=',')
		datawriter.writerows(new_contacts_list)
