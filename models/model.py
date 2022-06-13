class Model:
    def __init__(self, name, description, stock, buy_price, sell_price, manufacturer, id=None):
        self.name = name 
        self.description = description 
        self.stock = stock 
        self.buy_price = buy_price 
        self.sell_price = sell_price 
        self.manufacturer = manufacturer
        self.id = id 