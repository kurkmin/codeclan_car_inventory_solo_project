from db.run_sql import run_sql
from models.model import Model
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

def delete_all(): 
    sql = "DELETE FROM models"
    run_sql(sql)

def delete(id): 
    sql = "DELETE FROM models WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(model): 
    sql = "INSERT INTO models (name, description, stock, buy_price, sell_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [model.name, model.description, model.stock, model.buy_price, model.sell_price, model.manufacturer.id]
    sql_results = run_sql(sql, values)
    id = sql_results[0]['id']
    model.id = id 
    return model

def select_all(): 
    models = []
    sql = "SELECT * FROM models"
    sql_results = run_sql(sql)

    for result in sql_results:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        model = Model(result['name'], result['description'], result["stock"], result["buy_price"], result["sell_price"], manufacturer, result['id'])
        models.append(model)
    
    return models

def select(id):
    model = None
    sql = "SELECT * FROM models WHERE id = %s"
    value = [id]
    sql_results = run_sql(sql, value)[0]

    if sql_results is not None:
        manufacturer = manufacturer_repository.select(sql_results['manufacturer_id'])
        model = Model(sql_results['name'], sql_results['description'], sql_results['stock'], sql_results['buy_price'], sql_results['sell_price'], manufacturer, sql_results['id'])

    return model

def update(model): 
    sql = "UPDATE models SET (name, description, stock, buy_price, sell_price, manufacturer_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [model.name, model.description, model.stock, model.buy_price, model.sell_price, model.manufacturer.id, model.id]
    run_sql(sql, values)
