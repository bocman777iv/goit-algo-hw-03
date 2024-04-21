from datetime import datetime
def get_days_from_today(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    current_date = datetime.today().date()
    delta_days = (date_obj - current_date).days
    return delta_days
date_str = '2025-04-17'
days_diff = get_days_from_today(date_str)
print(f'Количество дней от {date_str} до текущей даты: {days_diff}')
