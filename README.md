# **Global Bike Sales Analysis Pipeline 🚴‍♂️🌍**

An end-to-end data pipeline for analyzing global bike sales data using PostgreSQL, Apache Airflow, Elasticsearch, and Kibana.

## **Introduction 🌐**

Bike sales are influenced by various factors, including product categories, geographic locations, discounts, and customer preferences. To enhance profitability, management requires detailed insights into sales performance to make strategic decisions. This dataset provides comprehensive sales information across dimensions like time, product categories, customer demographics, and geographic regions, enabling in-depth analysis.

## **Project Objectives 🎯**

The goal of this project is to provide insights into global bike sales trends, enabling stakeholders to make informed business decisions. Specific objectives include:

1. Deliver actionable insights into global bike sales trends and profitability factors.
2. Identify top-performing and underperforming products, categories, and regions.
3. Provide data-driven recommendations to enhance sales and optimize marketing strategies.
4. Improve operational efficiency in logistics, shipping, and discounting processes.

## **Dataset Overview 📂**

Sourced from [Kaggle](https://www.kaggle.com/datasets/hamedahmadinia/global-bike-sales-dataset-2013-2023), the dataset provides detailed records of global bike sales from 2013 to 2023.

### **Table Overview**

| No | Column Name       | Description                                                                 |
|----|-------------------|-----------------------------------------------------------------------------|
| 1  | Date              | Transaction date                                                           |
| 2  | Day               | Day of the transaction (1-31)                                              |
| 3  | Month             | Month of the transaction                                                   |
| 4  | Year              | Year of the transaction (2013-2023)                                        |
| 5  | Customer_Age      | Age of the customer at the time of purchase                                 |
| 6  | Age_Group         | Age group of the customer (e.g., Youth, Adults)                            |
| 7  | Customer_Gender   | Gender of the customer (Male, Female)                                       |
| 8  | Country           | Country where the transaction occurred                                     |
| 9  | State             | State/region for countries with subdivisions (e.g., US, Australia)         |
| 10 | Product_Category  | Category of the bike product                                               |
| 11 | Sub_Category      | Subcategory of the bike product                                            |
| 12 | Product           | Specific name or description of the product                                |
| 13 | Order_Quantity    | Number of units ordered                                                    |
| 14 | Unit_Cost         | Cost of producing one unit of the product                                  |
| 15 | Unit_Price        | Selling price per unit                                                     |
| 16 | Profit            | Net profit generated from the transaction                                  |
| 17 | Cost              | Total production cost of the product                                       |
| 18 | Revenue           | Total revenue generated from the transaction                               |
| 19 | Size              | Size of the product                                                       |
| 20 | Color             | Color of the product                                                      |
| 21 | Material          | Material of the product                                                   |
| 22 | Warranty          | Warranty provided for the product                                         |
| 23 | Manufacturer      | Manufacturer or brand of the product                                      |
| 24 | Rating            | Customer rating for the product                                           |
| 25 | Shipping_Weight   | Weight of the product during shipping                                      |
| 26 | Delivery_Time     | Delivery time in days                                                     |
| 27 | Discount          | Discount percentage applied to the transaction                            |
| 28 | Eco_Friendly      | Indicates if the product is eco-friendly (True/False)                     |
| 29 | Shipping_Cost     | Cost of shipping for the transaction                                       |
| 30 | Shipping_Company  | Company responsible for shipping                                           |
| 31 | Shipping_Type     | Type of shipping (e.g., standard, express)                                |
| 32 | Insurance         | Insurance type for the transaction                                        |
| 33 | Return_Policy     | Product return policy                                                     |

## **Methodology 🔧**

1. **Data Input to PostgreSQL**: Initial storage of raw data in PostgreSQL for structured management.
2. **ETL with Apache Airflow**: Airflow DAGs automate data extraction, transformation, and loading processes.
3. **Data Cleaning**: Handling missing values, removing duplicates, and standardizing formats for consistent data quality.
4. **Loading to Elasticsearch**: Cleaned data is indexed into Elasticsearch for efficient querying.
5. **Visualization with Kibana**: Interactive dashboards in Kibana for comprehensive data exploration and trend analysis.

## **Conclusion 📊**

**Sales Trends and Profitability**
- Seasonal trends indicate peak sales during holidays and cycling events. High-performing markets like the United States and Australia dominate profitability.
- The Bikes category generates the majority of profits, while Accessories contribute significantly in terms of quantity.

**Top-Performing Products and Locations**
- The United States and Australia are the most profitable regions, while some European markets underperform.

**Discount Impact**
- Discounts have diminishing returns beyond a threshold of 10–20%.

**Customer Segmentation**
- Adults (35–64) and Young Adults (25–34) generate 86% of revenue, highlighting key target demographics.

**Operational Efficiency**
- Consistent profit margins suggest opportunities for optimization in underperforming regions and categories.

## **Recommendations 💡**

**Enhance Revenue Growth**
- Leverage seasonal trends: Plan marketing campaigns and inventory restocking during high-demand periods.
- Focus on high-performing regions like the United States and Australia to maximize profitability.

**Optimize Product Strategy**
- Expand offerings in the Bikes category by introducing premium and entry-level models.
- Reassess underperforming categories like Clothing for strategic improvements.

**Fine-Tune Discount Strategies**
- Maintain discounts at an optimal level of 10–20% to balance order quantity and profitability.
- Use targeted discounts to stimulate growth in underperforming regions and product categories.

**Improve Customer Retention**
- Develop customer loyalty programs, emphasizing rewards for frequent purchases and referrals.

**Optimize Operations**
- Invest in logistics and supply chains for underperforming regions to reduce costs and improve efficiency.

## **Dependencies 📚**

- **Database**: PostgreSQL
- **ETL Tool**: Apache Airflow
- **Search Engine**: Elasticsearch
- **Visualization Tool**: Kibana
- **Libraries**: Pandas, Psycopg2, Pendulum, Great Expetations

## Author 👨‍💻
Ferryansa | [ferryansa.inbox@gmail.com](mailto:ferryansa.inbox@gmail.com) | [LinkedIn](https://www.linkedin.com/in/ferryansa) | [GitHub](https://github.com/ferryansa)
