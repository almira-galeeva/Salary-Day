from datetime import datetime, date
import numpy as np

class SalaryDay:
    def __init__(self):
        # today's date
        self.today = datetime.date(datetime.now()) 
        self.today_day = self.today.day
        self.today_month = self.today.month
        self.today_year = self.today.year
        
        # possible varints of coming paycheck
        self.variants = [date(self.today_year, self.today_month, 5),
            date(self.today_year, self.today_month, 20),
            date(self.today_year, self.today_month+1, 5),
            date(self.today_year+1, 1, 5)]
        
        # variants of days left
        self.days_variants = []
        self.days = None
        self.word_days = f"Hello my poor friend!\n\nToday's date: {self.today}\n\nDay of week: {self.today.strftime('%A')}\n\nSalary:\t"
        
    def day_res(self):
        # if weekends
        for variant in self.variants:
            if variant.weekday == 6:
                variants.pop(variant)
                variants.append(variant-1)
            elif variant.weekday == 7:
                variants.pop(variant)
                variants.append(variant-2)
                
         # final variants of days left     
        self.days_variants = np.array([(var-self.today).days for var in self.variants])
        # get minimal days number
        self.days = min(self.days_variants[self.days_variants >= 0])

    def res_phrase(self):
        self.day_res()
            
        if self.days == 1:
            self.word_days += f'{self.days} day left'
        elif self.days > 1:
            self.word_days += f'{self.days} days left'
        else:
            self.word_days += 'Today!'