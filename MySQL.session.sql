DROP TABLE drinks;

CREATE TABLE drinks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(7, 2) NOT NULL,
    category VARCHAR(50),
    available BOOLEAN DEFAULT TRUE
);
ALTER TABLE drinks MODIFY price DECIMAL(7, 2);
INSERT INTO drinks (name, description, price, category, available) VALUES
('Cà phê sữa', 'Cà phê pha với sữa đặc', 25000, 'Cà phê', TRUE),
('Cà phê đen', 'Cà phê nguyên chất, không đường', 20000, 'Cà phê', TRUE),
('Trà đào', 'Trà vị đào với miếng đào tươi', 30000, 'Trà', TRUE),
('Trà sữa', 'Trà sữa trân châu', 35000, 'Trà', TRUE),
('Sinh tố xoài', 'Sinh tố xoài nguyên chất', 40000, 'Sinh tố', TRUE),
('Nước chanh', 'Nước chanh tươi', 20000, 'Nước ép', TRUE);

SELECT * FROM drinks;

SELECT * FROM drinks


