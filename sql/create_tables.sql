CREATE DATABASE IF NOT EXISTS fanvoice;
USE fanvoice;
CREATE TABLE IF NOT EXISTS reviews(
 id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
 name varchar(100) NOT NULL,
 email varchar(100) NOT NULL,
 comment text NOT NULL,
 order_id varchar(50) NOT NULL,
 seatgeek_message text NOT NULL,
 created int NOT NULL
);

CREATE TABLE IF NOT EXISTS curated_reviews(
 id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
 review_id int NOT NULL,
 comment text NOT NULL,
 name varchar(256) NOT NULL,
 gender varchar(32) NOT NULL,
 FOREIGN KEY (review_id) REFERENCES reviews(id)
);
