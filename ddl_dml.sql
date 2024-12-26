-- Create a new database
CREATE DATABASE bike_sales_database;

-- Begin a transactional block
BEGIN;

-- Create the table
CREATE TABLE "bike_sales_table" (
    "Date" DATE,
    "Day" INT,
    "Month" VARCHAR(50),
    "Year" INT,
    "Customer_Age" INT,
    "Age_Group" VARCHAR(50),
    "Customer_Gender" VARCHAR(50),
    "Country" VARCHAR(50),
    "State" VARCHAR(50),
    "Product_Category" VARCHAR(50),
    "Sub_Category" VARCHAR(50),
    "Product" VARCHAR(50),
    "Order_Quantity" INT,
    "Unit_Cost" INT,
    "Unit_Price" INT,
    "Profit" INT,
    "Cost" INT,
    "Revenue" INT,
    "Size" VARCHAR(50),
    "Color" VARCHAR(50),
    "Material" VARCHAR(50),
    "Warranty" VARCHAR(50),
    "Manufacturer" VARCHAR(50),
    "Rating" INT,
    "Shipping_Weight" FLOAT,
    "Delivery_Time" INT,
    "Discount" INT,
    "Eco_Friendly" BOOLEAN,
    "Shipping_Cost" FLOAT,
    "Shipping_Company" VARCHAR(50),
    "Shipping_Type" VARCHAR(50),
    "Insurance" VARCHAR(50),
    "Return_Policy" VARCHAR(50)
);

-- Create a savepoint after successfully creating the table
SAVEPOINT create_table_savepoint;

-- Import all data from a CSV file into the created table
COPY "bike_sales_table"(
    "Date", "Day", "Month", "Year", "Customer_Age", "Age_Group", "Customer_Gender", "Country", "State", 
    "Product_Category", "Sub_Category", "Product", "Order_Quantity", "Unit_Cost", "Unit_Price", 
    "Profit", "Cost", "Revenue", "Size", "Color", "Material", "Warranty", "Manufacturer", "Rating", 
    "Shipping_Weight", "Delivery_Time", "Discount", "Eco_Friendly", "Shipping_Cost", 
    "Shipping_Company", "Shipping_Type", "Insurance", "Return_Policy"
)
FROM '/tmp/data_raw.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ','
);

-- If there is an error in the table creation process, rollback to the previous savepoint
-- ROLLBACK TO SAVEPOINT create_table_savepoint;

-- Commit the transactional block
COMMIT;

-- To revert all changes, rollback to before the transactional block started
-- ROLLBACK;

-- Verify that the table and its data have been successfully added to the database
SELECT * FROM bike_sales_table;
