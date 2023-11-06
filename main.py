from datetime import date, datetime,timedelta


def get_birthdays_per_week(users: list):
    RESULT = {'Monday':[],'Tuesday"':[],'Wednesday':[],'Thursday':[],'Friday':[]}
    TODAY = date.today() 

    # Empty table exception
    if len(users) < 1:
        return {}
    for dic in users:
        tmp_date = dic["birthday"]
        tmp_delta = timedelta(days=(7))
        #Changing year to compare properly
        if tmp_date.year < TODAY.year:
            tmp_date = tmp_date.replace(year=(TODAY.year + 1))
        #Checking if we are not out of bounds(aka the next week)
        if (tmp_date >= TODAY) and (tmp_date - TODAY) <= tmp_delta:
                if tmp_date.weekday() < 5:
                    RESULT[tmp_date.strftime("%A")].append(dic["name"])
                elif tmp_date.weekday() >= 5:
                    RESULT['Monday'].append(dic["name"])

    #Removing leftover (empty) days.
    to_remove = []
    for k,v in RESULT.items():
        if v == []:
            to_remove.append(k)
    for i in to_remove:
        del RESULT[i]
    
    return(RESULT)


if __name__ == "__main__":
    users = [
            {
                "name": "John",
                "birthday": (datetime(2023, 12, 26) + timedelta(days=-5)).date(),
            },
            {
                "name": "Doe",
                "birthday": (datetime(2023, 12, 26) + timedelta(days=-6)).date(),
            },
            {
                "name": "Alice",
                "birthday": (datetime(2021, 1, 1)).date(),
            },
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

