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

model_repo.select_all()

pdb.set_trace()