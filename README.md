# Data Engineering ETL Pipeline Project

## 📌 Project Overview

This project demonstrates a simple **ETL (Extract, Transform, Load) pipeline** using Python. The pipeline processes sales data and prepares it for visualization in Power BI.

---

## 🎯 Objective

The goal of this project is to:

* Extract raw data from a CSV file
* Transform the data by cleaning and computing new metrics
* Load the processed data into a new file for analysis and visualization

---

## ⚙️ Tools Used

* Python (Pandas)
* CSV / Excel
* Power BI (for visualization)

---

## 🔄 ETL Process

### 1. Extract

The pipeline reads raw sales data from:

```
data/input/sales_data_sample.csv
```

### 2. Transform

* Cleans missing values
* Calculates **Revenue** using:

```
Revenue = PRICEEACH × QUANTITYORDERED
```

### 3. Load

* Saves processed data to:

```
data/output/cleaned_sales.csv
```

---

## ▶️ How to Run the Project

### Step 1: Clone the repository

```
git clone <your-repo-link>
cd project-folder
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

### Step 3: Run the ETL pipeline

```
python src/src_main.py
```

---

## 📊 Output

The cleaned dataset is saved in:

```
data/output/
```

This file can be used in Power BI to create dashboards such as:

* Revenue by Product Line
* Revenue over Time
* Revenue by Country

---

## 📈 Project Outcome

This project successfully demonstrates a working ETL pipeline and prepares data for business intelligence and analytics.

---

## ✅ Conclusion

The ETL pipeline automates data processing and enables efficient data analysis, fulfilling the requirements of a data engineering workflow.
