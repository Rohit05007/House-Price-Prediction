CREATE DATABASE HousePriceDB;
USE HousePriceDB;

CREATE TABLE housing (
    longitude FLOAT,
    latitude FLOAT,
    housing_median_age FLOAT,
    total_rooms FLOAT,
    total_bedrooms FLOAT,
    population FLOAT,
    households FLOAT,
    median_income FLOAT,
    median_house_value FLOAT,
    ocean_proximity VARCHAR(20)
);

DESC housing;
SELECT COUNT(*) FROM housing;
SELECT * FROM housing LIMIT 10;
