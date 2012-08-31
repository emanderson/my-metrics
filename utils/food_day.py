class FoodDay(object):
    def __init__(self, date):
        self.date = date
        self.food_entries = []
    
    def total_calories(self):
        return sum(map(lambda x: x.calories, self.food_entries))
    
    def to_dict(self):
        return {
            'date': self.date.strftime('%Y%m%d'),
            'entries': map(lambda x: x.to_dict(), self.food_entries),
            'total_calories': self.total_calories()
        }
        
    # ASSUMES ENTRIES FROM THE SAME DAY ARE GROUPED
    @classmethod
    def group_days(self, food_entries):
        food_days = []
        for entry in food_entries:
            if len(food_days) == 0 or food_days[-1].date != entry.date:
                food_day = FoodDay(entry.date)
                food_days.append(food_day)
            food_days[-1].food_entries.append(entry)
        return food_days