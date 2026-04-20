<<<<<<< HEAD
#  Smart Crop Analytics System

A web-based data analysis application built with **Django** that allows users to explore Canadian agricultural data.
The system provides insights into crop production and yield trends through **interactive charts and dynamic filtering**.

---

# Features includes:

## Interactive Charts (Chart.js)
=======
# 🌱 Smart Crop Analytics System

A Django web application built for analyzing and visualizing Canadian crop data using a preloaded dataset. The system provides insights through interactive charts and dynamic filtering.

---

# 📌 Features

##  Interactive Charts (Chart.js)
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

* Production by Crop
* Yield Over Time
* Production by Region

<<<<<<< HEAD
## Dynamic Filtering
=======
##  Dynamic Filtering
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

* Filter by year
* Filter by region
* Search crops or regions
* Sort results

<<<<<<< HEAD
## Database Storage

* Uses **SQLite** (no external setup required)
* Data is **preloaded into the database**
* No CSV upload required (per project requirements)

## Data Analysis

* Aggregations using Django ORM (`Sum`, `Avg`)
* Charts update dynamically based on filters

---

#  Key Questions & How Charts Answer Them

This application is designed to answer specific analytical questions.

---

##  Chart 1: Production by Crop

**Questions:**

* Which crops have the highest production in Canada?
* How does production compare across crops?

**Explanation:**

* Displays total production per crop
* Higher bars = higher production
* Helps identify dominant crops

---

##  Chart 2: Yield Over Time

**Questions:**

* How has crop yield changed over time?
* Are there improvements in agricultural productivity?

**Explanation:**

* Shows average yield per year
* X-axis = Year
* Y-axis = Yield
* Reveals trends over time

---

##  Chart 3: Production by Region

**Questions:**

* Which regions produce the most crops?
* How does production vary by province?

**Explanation:**

* Compares production across regions
* Helps identify high-producing areas

---

## Supporting Features (Filters & Table)

**Questions:**

* What happens when filtering by year or region?
* How can users explore specific crops?

**Explanation:**

* Filters refine the dataset
* Charts update automatically
* Table shows detailed records

---

# Technologies Used

* Python 3.13.7
* Django 5.x
=======
##  Database Storage

* Uses SQLite (no external setup required)
* Data is preloaded into the database

##  Data Analysis

* Aggregations using Django ORM (`Sum`, `Avg`)
* Real-time updates based on filters

---
#  Key Questions and How the Charts Answer Them

This application is designed to answer specific analytical questions using visualizations. 
Each chart directly corresponds to a key question.

---

## 📊 Chart 1: Production by Crop (Bar Chart)

### ❓ Question:

* Which crops have the highest production in Canada?
* How does production compare across different crops?

### 📈 How the Chart Answers This:

* The bar chart displays total production for each crop.
* Taller bars represent crops with higher production levels.
* Users can quickly identify dominant crops such as wheat or canola.

---

## 📈 Chart 2: Yield Over Time (Line Chart)

### ❓ Question:

* How has crop yield changed over time?
* Are there trends or improvements in agricultural productivity?

### 📉 How the Chart Answers This:

* The line chart plots average yield for each year.
* The X-axis represents time (years), while the Y-axis shows yield.
* Upward or downward trends reveal changes in productivity over time.

---

## 🗺️ Chart 3: Production by Region (Bar Chart)

### ❓ Question:

* Which regions contribute the most to crop production?
* How does production differ between provinces?

###  How the Chart Answers This:

* The chart compares total production across regions.
* Each bar represents a province or region.
* This helps identify high-producing areas and regional differences.

---

##  Supporting Features (Filters & Table)

### ❓ Questions:

* How does production or yield change when filtering by year?
* What patterns appear when focusing on a specific region?
* How can users explore specific crops?

### How the App Answers This:

* Filters allow users to refine data dynamically.
* Charts update automatically based on selected filters.
* The table provides detailed records for deeper inspection.

---

### Summary

Each visualization in the application is designed to answer a specific analytical question, making the system not just a data display tool, but a decision-support dashboard.


#  Technologies Used

* Python 3
* Django
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e
* SQLite
* HTML / CSS
* JavaScript
* Chart.js

---

<<<<<<< HEAD
#  Project Structure
=======
# 📁 Project Structure
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

```
smart-crop-analytics/
│
├── crop_project/
│   ├── crop_project/      # Project settings
│   ├── crops/             # App (models, views, templates)
<<<<<<< HEAD
│   ├── db.sqlite3         # Database (preloaded)
│   ├── manage.py
│   ├── import_data.py     # Data import script (not required to run)
=======
│   ├── db.sqlite3         # Database
│   ├── manage.py
│   ├── import_data.py     # Script to load data
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e
│
├── README.md
```

---

<<<<<<< HEAD
#  Development Environment Setup

Ensure your system meets the following requirements:

* Python: **3.13.7**
* Django: **5.x**
* Database: SQLite (included with Django)
* Browser: Chrome / Edge / Firefox

---

# Installation & Setup Guide

## 1. Install Python

Check version:
=======
# ⚙️ Installation & Setup Guide

## 1. Install Python

Check if Python is installed:
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

```bash
python --version
```

<<<<<<< HEAD
Expected:

```
Python 3.13.7
```

Download if needed:
=======
If not installed, download from:
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e
https://www.python.org/downloads/

---

<<<<<<< HEAD
## 2. Clone the Repository
=======
## 2. Clone or Download Project
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

```bash
git clone <your-repo-url>
cd smart-crop-analytics/crop_project
```

<<<<<<< HEAD
=======
Or download the ZIP and extract it.

>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e
---

## 3. Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

<<<<<<< HEAD
Activate:

**Windows**
=======
### Activate it:

**Windows:**
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

```bash
venv\Scripts\activate
```

<<<<<<< HEAD
**Mac/Linux**
=======
**Mac/Linux:**
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

```bash
source venv/bin/activate
```

---

<<<<<<< HEAD
## 4. Install Dependencies
=======
## 4. Install Django
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

```bash
pip install django
```

---

<<<<<<< HEAD
## 5. Apply Migrations
=======
## 5. Run Migrations
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

```bash
python manage.py migrate
```

---

<<<<<<< HEAD
## 6. Database Setup

This project includes a **preloaded SQLite database (`db.sqlite3`)**.

✔ No manual data import required
✔ Application is ready after migrations

---

## 7. Run the Server
=======
## 6. Load Data into Database

```bash
python manage.py shell
```

Then run:

```python
exec(open('import_data.py').read())
```

Exit:

```python
exit()
```

---

## 7. Start the Server
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

```bash
python manage.py runserver
```

---

## 🌐 8. Open in Browser

Go to:

<<<<<<< HEAD
```
http://127.0.0.1:8000/
```

---

# How to Use the App

## Filters

* Select year
* Select region
* Enter search text
* Click **Filter**

 Charts update automatically

---

## Charts Overview
=======
http://127.0.0.1:8000/

---

#  How to Use the App

##  Filters

* Select Year
* Select Region
* Enter search text
* Click Filter

👉 Charts update automatically based on filters

---

## 📈 Charts
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

| Chart                | Description                |
| -------------------- | -------------------------- |
| Production by Crop   | Total production per crop  |
| Yield Over Time      | Average yield per year     |
| Production by Region | Total production by region |

---

##  Table

* Displays filtered crop data
<<<<<<< HEAD
* Limited to improve performance
=======
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e
* Updates dynamically

---

<<<<<<< HEAD
# How Data Works

* Data stored in **SQLite (`db.sqlite3`)**
* Originally processed from CSV
* Managed using Django ORM:

  * `Sum()` → Production
  * `Avg()` → Yield

---

# Troubleshooting

## Charts not showing

Ensure Chart.js is included:
=======
#  How Data Works

* Data is stored in SQLite (`db.sqlite3`)
* Imported using `import_data.py`
* Uses Django ORM:

  * `Sum()` for production
  * `Avg()` for yield

---

#  Troubleshooting

## Charts not showing

Make sure Chart.js is included:
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

---

## Server not starting

<<<<<<< HEAD
Make sure you're in the correct folder:

```bash
cd crop_project
=======
Make sure you're inside the project folder:

```bash
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e
python manage.py runserver
```

---

## Data not appearing

<<<<<<< HEAD
If needed (optional):
=======
Re-run import:
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

```bash
python manage.py shell
exec(open('import_data.py').read())
```
<<<<<<< HEAD

---

# License
=======
# 📄 License
>>>>>>> d4ae991899efc288e6aa4c0cd63821351202807e

Educational use only
