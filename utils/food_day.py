class FoodDay(object):
    def __init__(self, date):
        self.date = date
        self.food_entries = []
    
    def total_calories(self):
        return sum(map(lambda x: x.calories, self.food_entries))
        
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