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

manu_repo.select_all()

model1 = Model("5series", "sedan", 3, 50000, 60000, manufacturer1)
model_repo.save(model1)
model2 = Model("Explorer", "suv", 1, 40000, 50000, manufacturer2)
model_repo.save(model2)

model_repo.select_all()

pdb.set_trace()