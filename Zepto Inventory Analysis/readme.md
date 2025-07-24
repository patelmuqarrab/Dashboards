# Zepto Grocery Data Analysis

This project analyzes Zepto's grocery product data to provide insights on inventory management, pricing strategies, and category performance. The SQL script performs comprehensive data exploration and business analysis on a simulated grocery delivery dataset. A Power BI dashboard was developed to visualize key metrics and extract actionable insights.

---

## 📸 Dashboard Preview
![Zepto Dashboard 1](https://github.com/patelmuqarrab/Dashboards/blob/main/Zepto%20Inventory%20Analysis/1.png)
![Zepto Dashboard 2](https://github.com/patelmuqarrab/Dashboards/blob/main/Zepto%20Inventory%20Analysis/2.png) 

---

## 🧩 Business Problem

Zepto, a rapid grocery delivery service in India, manages a vast inventory across multiple product categories. With increasing product diversity and varying discount strategies, the company faces challenges in:
- Managing stockouts and overstock situations
- Identifying underperforming categories
- Balancing discounting practices with profitability
- Monitoring inventory value tied up in specific product segments

---

## 🎯 Goal of the Dashboard

The objective of the dashboard is to:
- Monitor product availability and stock status by category
- Track total inventory value and category-wise contributions
- Analyze the impact of discounting on sales and margins
- Identify high-value and high-discount products
- Support decision-making in pricing, inventory, and procurement

---

## 💡 Business Impact and Key Insights

- 📉 **Out-of-Stock Rate**: The overall stockout rate is 12.14%, with categories like *Cooking Essentials* and *Munchies* having the highest out-of-stock instances. Addressing this can improve service reliability.
- 💰 **Inventory Value**: A significant portion of the inventory value ($249M) is concentrated in just three categories: *Cooking Essentials*, *Munchies*, and *Paan Corner*, each contributing $30M–$38M. Diversifying inventory allocation could reduce risk.
- 🏷️ **Discount Strategy**: Products like *Zorabian Chicken Smoked Ham* have high discount amounts despite moderate average discount percentages, indicating bulk discounting or high-priced product markdowns.
- 🔎 **Premium Products**: 874 products were flagged as premium, indicating opportunities for luxury segment marketing and upselling.
- 📦 **Category Distribution**: Categories like *Personal Care* and *Paan Corner* are product-dense, while *Fruits & Vegetables* have minimal inventory—highlighting areas for inventory expansion or reevaluation.

---

## 📊 Data Source

The dataset used in this analysis is available on Kaggle:  
🔗 [Zepto Grocery Product Dataset](https://www.kaggle.com/datasets/palvinder2006/zepto-inventory-dataset/data?select=zepto_v2.csv)

**Dataset Features:**
- 1600+ grocery products
- 14 categories
- Pricing, discounts, and inventory data
- Product weights and stock status

---

## 🛠️ SQL & Dashboard Analysis Highlights

### 1. Data Quality Assurance
- NULL value detection
- Invalid price record removal
- Data range verification

### 2. Category Analysis
- Product distribution across categories
- Out-of-stock rates by category
- Inventory value analysis

### 3. Pricing Strategy
- Price tier segmentation
- Discount effectiveness analysis
- Premium product identification

### 4. Business Insights
- Revenue potential by category
- Profit margin analysis
- Stock optimization recommendations
- Discount impact on revenue

---

📌 *This dashboard empowers Zepto to make informed operational and financial decisions based on real-time product, pricing, and inventory data.*

