# 📞 Call Center Performance Dashboard

![Dashboard]((https://github.com/patelmuqarrab/Dashboards/blob/main/Call%20Center%20Dashboard/frame.png))

This project is a comprehensive **Call Center Performance Dashboard** built using **Power BI**. It provides detailed visual insights into call center metrics such as call volume, channel effectiveness, and agent performance. The dashboard is powered by a synthetic dataset that simulates realistic call center operations.

---

## 📊 Project Overview

### 🎯 Business Problem

Call centers are often overwhelmed with large volumes of customer queries through multiple communication channels. This creates challenges in identifying performance bottlenecks, measuring channel effectiveness, and optimizing resource allocation.

### ✅ Objective

The goal of this project is to develop an interactive Power BI dashboard to help stakeholders:

- Monitor overall call center activity and performance
- Analyze the effectiveness of each communication channel
- Identify agent and department-level performance
- Make data-driven decisions for improved service delivery

---

## 🔍 Insights & Business Impact

- 📈 **Channel Effectiveness:** Visual comparison of call volumes and resolutions across phone, email, chat, and social media.
- 👥 **Agent & Team Productivity:** Identification of top-performing and underperforming agents.
- ⏱️ **Response Times & SLAs:** Visualization of average handling time, wait time, and resolution efficiency.
- 🧠 **Actionable Insights:** Enables operations managers to reallocate resources, train specific teams, or optimize channels based on real-time data.

---

## 🗂️ Folder Structure

📁 call-center-dashboard/
│
├── 📄 README.md
├── 📊 callCenter.pbix # Power BI file
├── 📁 assets/ # UI Icons used in dashboard
│ ├── callCenter.png
│ ├── home.png
│ ├── grid.png
│ └── table.png
│
├── 📁 dashboard_backgrounds/ # Dashboard background images
│ ├── 1.png
│ ├── 2.png
│ └── 3.png
│
├── 📁 dashboard_views/ # Final dashboard images
│ ├── Overview.png
│ ├── Channel Effectiveness.png
│ └── Details.png
│
├── 📁 data/
│ ├── call_center_data.csx # Synthetic dataset (CSV format)
│ └── call_center_data_generation.py # Python script used to generate data


---

## 🧪 Dataset

The dataset contains:

- ID
- CALL CENTER LOCATION
- DATE OF CALL
- REASON OF CALL
- CLIENT CALL
- CALL SENTIMENT
- CALL DURATION(MIN)
- CSAT SCORE
- CHANNEL(CALL CENTER, CHAT BOT, WEBSITE, EMAIL)

> The dataset was generated using `call_center_data_generation.py` and stored in `call_center_data.csv`.

---

## 🛠️ Tools & Technologies

- **Power BI**: For data visualization and interactive dashboard creation  
- **Python**: To generate synthetic call center data  
- **Pandas**: Used in the data generation process  
- **DAX**: For custom measures and calculated columns in Power BI  

---

## 📷 Dashboard Snapshots

| Overview | Channel Effectiveness | Agent & Details |
|---------|------------------------|-----------------|
| ![Overview](https://github.com/patelmuqarrab/Dashboards/blob/main/Call%20Center%20Dashboard/Overview.png) | ![Channel](https://github.com/patelmuqarrab/Dashboards/blob/main/Call%20Center%20Dashboard/Channel%20Effectiveness.png) | ![Details](https://github.com/patelmuqarrab/Dashboards/blob/main/Call%20Center%20Dashboard/Details.png) |

---

## 🚀 Getting Started

1. Clone or download this repository.
2. Open `callCenter.pbix` in Power BI Desktop.
3. Replace or update data source if needed (`call_center_data.csv`).
4. Customize or expand the dashboard as required.
   
---

