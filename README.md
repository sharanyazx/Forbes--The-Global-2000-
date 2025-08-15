
# 📊 Forbes 2000 – 2025 Dashboard

An interactive **Python dashboard** that provides deep insights into the **Forbes Global 2000 companies for 2025**.  
It includes company-level metrics, clustering analysis, industry profit margins, and top market capitalisations.

---

## 🚀 Features
- **KPIs:** Total sales, profit, assets, and market value.
- **Data Cleaning:** Handles missing values, cleans numeric fields.
- **Charts:**
  - 📈 Top 10 companies by market capitalisation
  - 🏭 Top 10 industries by median profit margin
  - 🔍 Cluster analysis using t-SNE & K-Means
- **UI:** Fully interactive, clean, and responsive.

---

## 📸 Screenshots

### KPI Overview
![KPI Overview]()

### Top Companies by Market Cap
![Top Companies](screenshots/Screenshot_2025-08-15_223757.png)

### Industry Profit Margins
![Industry Profit Margins](screenshots/Screenshot_2025-08-15_223806.png)

---

## 🛠 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sharanyazx/Forbes--The-Global-2000-.git
cd Forbes--The-Global-2000-
````

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app locally

```bash
python app.py
```

---

## 📂 Project Structure

```
Forbes--The-Global-2000-/
│
├── app.py                  # Main Python application
├── data/
│   └── Forbes_2000_Companies_2025.csv
├── screenshots/
│   ├── Screenshot_2025-08-15_223738.png
│   ├── Screenshot_2025-08-15_223757.png
│   └── Screenshot_2025-08-15_223806.png
├── requirements.txt
└── README.md
```

---

## 📦 Requirements

Example `requirements.txt`:

```
pandas
numpy
matplotlib
seaborn
scikit-learn
```

---

## 🏷 Author

**Sharanya**
📅 2025 | Data source: **Forbes Global 2000 dataset**
