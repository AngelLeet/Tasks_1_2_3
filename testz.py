class Technic:
    __slot__ = ('title', 'price', 'availability')
    def __init__(self, title, price, availability=True):
        if (availability == True) or (availability == False):
            self.title = title
            self.price = price 
            self.availability = availability
        else:
            return None
    def __lt__(self,other):
        return len(self.title) < len(other.title)

