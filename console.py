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

model1 = Model("X3", "suv", 1, 15000, 20000, 1)
model_repo.save(model1)
model2 = Model("5", "sedan", 1, 17000, 22000, 1)
model_repo.save(model2)

manu_repo.select_all()
model_repo.select_all()

pdb.set_trace()