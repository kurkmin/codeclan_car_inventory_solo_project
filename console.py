import pdb 

from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manu_repo

from models.model import Model
import repositories.model_repository as model_repo

manu_repo.delete_all()
model_repo.delete_all()

manufacturer1 = Manufacturer("Bmw", "luxury", "Germany")
manu_repo.save(manufacturer1)
manufacturer2 = Manufacturer("Ford", "standard", "USA")
manu_repo.save(manufacturer2)
manufacturer3 = Manufacturer("Hyundai", "standard", "Korea")
manu_repo.save(manufacturer3)
manufacturer4 = Manufacturer("Toyota", "standard", "Japan")
manu_repo.save(manufacturer4)
manufacturer5 = Manufacturer("Kia", "standard", "Korea")
manu_repo.save(manufacturer5)
manufacturer6 = Manufacturer("Porsche", "luxury", "Germany")
manu_repo.save(manufacturer6)
manufacturer7 = Manufacturer("Audi", "luxury", "Germany")
manu_repo.save(manufacturer7)
manufacturer8 = Manufacturer("Mercedes", "luxury", "German")
manu_repo.save(manufacturer8)
manufacturer9 = Manufacturer("Honda", "luxury", "Germany")
manu_repo.save(manufacturer9)

manu_repo.select_all()

model1 = Model("5series", "sedan", 3, 50000, 60000, manufacturer1)
model_repo.save(model1)
model2 = Model("Explorer", "suv", 1, 40000, 50000, manufacturer2)
model_repo.save(model2)
model3 = Model("i30", 'hatchback', 0, 20000, 30000, manufacturer3)
model_repo.save(model3)
model4 = Model("Prius", "hatchback", 2, 20000, 30000, manufacturer4) 
model_repo.save(model4)
model5 = Model("X5", "suv", 1, 60000, 70000, manufacturer1)
model_repo.save(model5)
model6 = Model("911", 'sports-car', 1, 100000, 120000, manufacturer6)
model_repo.save(model6)
model7 = Model("RS5", "gran-coupe", 3, 70000, 80000, manufacturer7)
model_repo.save(model7)
model8 = Model("S350", "sedan", 1, 200000, 240000, manufacturer8)
model_repo.save(model8)
model9 = Model("Civic", "hatchback", 1, 20000, 21000, manufacturer9)
model_repo.save(model9)
model10 = Model("Ceed", "hatchback", 2, 15000, 17000, manufacturer5)
model_repo.save(model10)

model_repo.select_all()

pdb.set_trace()