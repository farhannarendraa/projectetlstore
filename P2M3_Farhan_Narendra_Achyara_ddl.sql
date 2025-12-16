-- Create table dari dataset
CREATE TABLE global_superstore_data (
    Row_ID INTEGER PRIMARY KEY,
    Order_ID VARCHAR(50),
    Order_Date DATE,
    Ship_Date DATE,
    Ship_Mode VARCHAR(50),
    Customer_ID VARCHAR(50),
    Customer_Name VARCHAR(100),
    Segment VARCHAR(50),
    City VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100),
    Postal_Code VARCHAR(20),
    Market VARCHAR(50),
    Region VARCHAR(100),
    Product_ID VARCHAR(50),
    Category VARCHAR(50),
    Sub_Category VARCHAR(50),
    Product_Name TEXT,
    Sales NUMERIC(15,2),
    Quantity INTEGER,
    Discount NUMERIC(5,3),
    Profit NUMERIC(15,2),
    Shipping_Cost NUMERIC(15,2),
    Order_Priority VARCHAR(20)
);

-- Copy dataset dari local data
SET datestyle = 'ISO, DMY';
SET client_encoding TO 'LATIN1';
\copy global_superstore_data FROM '/Users/farhan/Downloads/P2M3_Farhan_Narendra_Achyara_raw_data.csv' DELIMITER ',' CSV HEADER;

