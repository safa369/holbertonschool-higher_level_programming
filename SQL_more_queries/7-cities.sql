-- cities table.
USE hbtn_0d_usa; 
CREATE TABLE IF NOT EXISTS cities(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    state_id INT NOT NULL ,
    name VARCHAR(256) NOT NULL,
    UNIQUE (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);