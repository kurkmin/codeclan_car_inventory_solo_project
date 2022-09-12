class Model:
    def __init__(self, name, description, stock, buy_price, sell_price, manufacturer, id=None):
        self.name = name 
        self.description = description 
        self.stock = stock 
        self.buy_price = buy_price 
        self.sell_price = sell_price 
        self.manufacturer = manufacturer
        self.id = id 

    def get_markup(self):
        markup = float(self.stock * (self.sell_price - self.buy_price))
        return markup 

    # create a method called 'get_markup', which takes self parameter (in this case, model) 
    #   markup is calculated by model's stock times the difference between model's sell_price and model's buy_price
    #   it returns markup finally 
