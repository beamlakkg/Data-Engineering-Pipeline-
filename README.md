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

Create and activate a virtual environment first:

```
python3 -m venv .venv
source .venv/bin/activate
```

Then install the packages inside that environment:

```
pip install -r requirements.txt
```

### Step 2b: Configure BigQuery credentials

Choose one of these options before running the script:

1. Put your service account file at the project root as `key.json`.
2. Or set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the full path of your key file.

Example on Linux/macOS:

```
export GOOGLE_APPLICATION_CREDENTIALS="/full/path/to/key.json"
```

Example on Windows PowerShell:

```
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\full\path\to\key.json"
```

### Step 3: Run the ETL pipeline

```
.venv/bin/python src/src_main.py
```

If the credentials are configured correctly, the script will read the CSV, build the `Revenue` column, save the cleaned file, and then load the data into BigQuery without raising an authentication error.

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
