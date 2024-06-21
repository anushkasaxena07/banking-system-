CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    balance DECIMAL(10, 2)
);
CREATE TABLE transfers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender_id INT,
    receiver_id INT,
    amount DECIMAL(10, 2),
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES customers(id),
    FOREIGN KEY (receiver_id) REFERENCES customers(id)
);
INSERT INTO customers (name, email, balance) VALUES
('Anushka', 'anushka@gmail.com', 1000.00),
('Aditi', 'Aditi@gmail.com', 1500.00),
('Anshika', 'Anshika@gmail.com', 2000.00),

;
