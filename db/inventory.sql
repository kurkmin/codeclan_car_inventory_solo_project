DROP TABLE IF EXISTS models; 
DROP TABLE IF EXISTS manufacturers; 

CREATE TABLE manufacturers (
    name VARCHAR(255),
    position VARCHAR(255), 
    country VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE models (
    name VARCHAR(255),
    description VARCHAR(255), 
    stock INT, 
    buy_price FLOAT, 
    sell_price FLOAT,
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE,
    id SERIAL PRIMARY KEY
); 

