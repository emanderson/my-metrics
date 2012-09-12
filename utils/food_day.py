class FoodDay(object):
    def __init__(self, date):
        self.date = date
        self.food_entries = []
    
    def total_calories(self):
        return sum(map(lambda x: x.calories, self.food_entries))
    
    def entries_by_tag(self):
        by_tag = {}
        for entry in self.food_entries:
            #TODO: handle untagged foods or multiple tags
            if entry.food.food_tags:
                tag = entry.food.food_tags[0]
                by_tag.setdefault(tag.id, [])
                by_tag[tag.id].append(entry.to_dict())
            else:
                by_tag.setdefault(0, [])
                by_tag[0].append(entry.to_dict())
        return by_tag
    
    def to_dict(self):
        return {
            'date': self.date.strftime('%Y%m%d'),
            'entries': map(lambda x: x.to_dict(), self.food_entries),
            'by_tag': self.entries_by_tag(),
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