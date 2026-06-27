import calendar
from datetime import datetime, date 


def get_day_of_week(day, month, year):
    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    day_index = date(year, month, day)
    return days_of_week[day_index.weekday()]

def is_leap_year(year):
    return calendar.isleap(year)

def get_age(day, month, year):
    today = datetime.now()
    birthdate = datetime(year, month, day)
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

def print_date_styled(day, month, year):
    digit_art = {
    '0': ["*** ", "* * ", "* * ", "* * ", "*** "],
    '1': ["  * ", "  * ", "  * ", "  * ", "  * "],
    '2': ["*** ", "  * ", "*** ", "*   ", "*** "],
    '3': ["*** ", "  * ", "*** ", "  * ", "*** "],
    '4': ["* * ", "* * ", "*** ", "  * ", "  * "],
    '5': ["*** ", "*   ", "*** ", "  * ", "*** "],
    '6': ["*** ", "*   ", "*** ", "* * ", "*** "],
    '7': ["*** ", "  * ", "  * ", "  * ", "  * "],
    '8': ["*** ", "* * ", "*** ", "* * ", "*** "],
    '9': ["*** ", "* * ", "*** ", "  * ", "*** "],
}
    date_str = f"{day:02d}{month:02d}{year}"
    for i in range(5):
        line = []
        for digit in date_str:
            line.append(digit_art[digit][i])
        print(" ".join(line))

def main():
    print("Stylistic programmer adaption numbers")
    try:
        user_day = int(input("Введите день вашего рождения (1-31): "))
        user_month = int(input("Введите месяц вашего рождения (1-12): "))
        user_year = int(input("Введите год вашего рождения (1948-2031): "))
        print("\nРезультаты")
        weekday = get_day_of_week(user_day, user_month, user_year)
        print(f"День недели: {weekday}")
        leap_status = "високосный" if is_leap_year(user_year) else "не високосный"
        print(f"Этот год - {leap_status}")
        age = get_age(user_day, user_month, user_year)
        print(f"Вам сейчас: {age} лет")
        print("\nДата рождения на электронном табло:")
        print_date_styled(user_day, user_month, user_year)
    except ValueError:
        print("Error try again")
        return
    
if __name__ == "__main__":
    main()