from db.run_sql import run_sql
from models.manufacturer import Manufacturer

def delete_all(): 
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id): 
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(manufacturer): 
    sql = "INSERT INTO manufacturers (name, position, country) VALUES (%s, %s, %s) RETURNING id"
    values = [manufacturer.name, manufacturer.position, manufacturer.country]
    sql_results = run_sql(sql, values)
    id = sql_results[0]['id']
    manufacturer.id = id 

def select_all(): 
    manufacturers = []
    sql = "SELECT * FROM manufacturers"
    sql_results = run_sql(sql)

    for result in sql_results:
        manufacturer = Manufacturer(result['name'], result['position'], result['country'], result['id'])
        manufacturers.append(manufacturer)
    return manufacturers

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    value = [id]
    sql_results = run_sql(sql, value)[0]

    if sql_results is not None:
        manufacturer = Manufacturer(sql_results['name'], sql_results['position'], sql_results['country'], sql_results['id'])
    return manufacturer

def update(manufacturer): 
    sql = "UPDATE manufacturers SET (name, position, country) = (%s, %s, %s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.position, manufacturer.country, manufacturer.id]
    run_sql(sql, values)

def models(manufacturers):
    models = []

    sql = "SELECT * FROM models WHERE manufacturer_id = %s"
    values = [manufacturers.id]
    results = run_sql(sql, values)

    for row in results:
        model = Model(row['name'], row['description'], row['stock'], row['buy_price'], row['sell_price'], row['manufacturer_id'], row['id'])
        models.append(model)
    return models

