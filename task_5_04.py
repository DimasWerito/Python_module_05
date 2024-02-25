"""
Повернемося до нашого завдання із телефонними номерами. 
Компанія розширюється та вийшла на ринок Азії. 
Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .

Компанія працює з наступними країнами

Країна	Код ISO	Префікс
Japan	JP	+81
Singapore	SG	+65
Taiwan	TW	+886
Ukraine	UA	+380
Щоб ми могли коректно виконати рекламну SMS кампанію, 
необхідно створити для кожної країни свій список телефонних номерів.

Напишіть функцію get_phone_numbers_for_сountries, яка буде:

Приймати список телефонних номерів.
Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
Сортувати телефонні номери за вказаними у таблиці країнами.
Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]
}
Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.
"""


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    sorted_phones = {
    "UA": [],
    "JP": [],
    "TW": [],
    "SG": []
    }
    for phone in list_phones:
        clean_phone = sanitize_phone_number(phone)
        if clean_phone.startswith("380"):
            sorted_phones["UA"].append(clean_phone)
        elif clean_phone.startswith("81"):
            sorted_phones["JP"].append(clean_phone)
        elif clean_phone.startswith("886"):
            sorted_phones["TW"].append(clean_phone)
        elif clean_phone.startswith("65"):
            sorted_phones["SG"].append(clean_phone)
        else:
            sorted_phones["UA"].append(clean_phone)
    return sorted_phones


list_phones = ["+38(063)27-64-273", "+8132892389238", "653829293983289", "+52-441-221-7882"]
print(get_phone_numbers_for_countries(list_phones))