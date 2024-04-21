import re

raw_numbers = [
    "067\\t123 4567",
     "(095) 234-5678\\n",
     "+380 44 123 4567",
     "380501234567",
     " +38(050)123-32-34",
     " 0503451234 ",
     "(050)8889900",
     "38050-111-22-22",
     "38050 111 22 11 ",
]
for phone in raw_numbers:
    cleaned_number = re.sub(r'[^0-9]', '', phone)
    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number
    print(cleaned_number)