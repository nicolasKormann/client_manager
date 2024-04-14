# Example of relationship between tables and creation of records

CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE contact (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);


INSERT INTO customer (full_name, email, phone)
VALUES ('João da Silva', 'joao_silva@gmail.com', '999999999')

INSERT INTO contact (full_name, email, phone, customer_id)
VALUES ('Maria da Silva', 'maria_silva@gmail.com', '888888888', 1)