# 📊 Survey Data Analysis (Python + SQLite)

This project shows how to take survey data from a **CSV file 📄**, save it into a **SQLite database 🗄️**, run **SQL queries 🔍**, and create a **simple chart 📈** using Python.

Perfect for **beginners** learning data analysis, SQL, and Python together 🚀

---

## ✨ What This Project Does

✅ Reads survey data from a CSV file  
✅ Stores the data in a SQLite database  
✅ Runs SQL queries using Python  
✅ Counts and groups survey responses  
✅ Creates a bar chart (Age Distribution)  
✅ Shows database tables and schema  

---

## 📁 Project Files

```

📂 project-folder
├── 📄 survey_data.csv        # Survey data file
├── 🗄️ survey-data.sqlite     # SQLite database (auto-created)
├── 🐍 main.py                # Python script
└── 📝 README.md              # Project explanation

````

---

## 🧰 Tools & Libraries Used

🐍 **Python 3**  
📊 **Pandas** – data handling  
🗄️ **SQLite (sqlite3)** – database  
📈 **Matplotlib** – charts  

---


## ▶️ How to Run the Project

Make sure `survey_data.csv` is in the folder, then run:

```bash
python main.py
```

---

## 🧠 Step-by-Step Explanation

### 📥 1. Load CSV Data

Reads the survey data into a Pandas DataFrame and prints the first 5 rows.

---

### 🗄️ 2. Create SQLite Database

Creates a SQLite database and saves the data into a table called `main`.

---

### 🔍 3. Check the Database

Runs SQL queries to:

* Preview data
* Count total rows
* List all tables

---

### 👥 4. Analyze Age Distribution

Uses SQL `GROUP BY` to count how many people belong to each age group.

---

### 📊 5. Visualize Data

Creates a **bar chart** showing:

* **X-axis:** Age Groups
* **Y-axis:** Number of Respondents

---

### 🧱 6. View Table Schema

Displays the SQL structure (columns and types) of the `main` table.

---

### 🔒 7. Close Database

Safely closes the SQLite database connection.

---

## 📈 Output Example

📊 Bar chart showing **Survey Respondents by Age Group**
This helps quickly understand the age distribution of participants.

---

## 🎯 Who Is This For?

✔️ Beginners learning Python
✔️ Students practicing SQL
✔️ Data analysis learners
✔️ Portfolio / practice projects

---

## 📚 What You’ll Learn

🧠 How Pandas works with SQL
🧠 Basic SQL queries (`SELECT`, `COUNT`, `GROUP BY`)
🧠 How to store data in databases
🧠 How to visualize data using Python

---

## 🔮 Future Improvements

🚀 Add more charts
🚀 Analyze more survey columns
🚀 Export SQL results to CSV
🚀 Convert project to Jupyter Notebook


---

## 💡 Final Notes

This project is a **simple end-to-end data analysis example** that connects CSV → SQL → Python → Visualization.

Happy coding! 🎉🐍

---

## 📜 Author

📄 Varrun Vashisht

