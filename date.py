import re


class Date_Check:
    def __init__(self):
        self.date = self.date_work()

    def date_work(self):
        date = ''
        condn = '[0-9]'
        re_search = f"{condn * 4}-{condn * 2}-{condn * 2}"

        while not re.search(re_search, date):
            date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD :')

            month, day, year = int(date.split('-')[1]), int(date.split('-')[2]), int(date.split('-')[0])
            if month > 12 or day > 31:
                date = ''
                print('Incorrect Date')

            # Checking for >30 days on 30 day months
            if day > 30:
                for i in [2, 6, 9, 11]:
                    if month == i:
                        date = ''
                        print('Incorrect Date')
                        break
                        # leap year
            if month == 2:
                if year % 4 == 0 and day > 29:
                    date = ''
                    print('Incorrect Date')
                elif year % 4 != 0 and day > 28:
                    date = ''
                    print('Incorrect Date')
        return date
