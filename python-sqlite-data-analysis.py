# ---------------------------------------
# 1. Import Required Libraries
# ---------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


# ---------------------------------------
# 2. Read CSV File into Pandas
# ---------------------------------------
df = pd.read_csv('survey_data.csv')
#data_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv'

print("First 5 rows of the dataset:")
print(df.head())


# ---------------------------------------
# 3. Create SQLite Database & Insert Data
# ---------------------------------------
conn = sqlite3.connect('survey-data.sqlite')

# Store DataFrame as SQL table
df.to_sql('main', conn, if_exists='replace', index=False)

print("\nData successfully stored in SQLite database.")


# ---------------------------------------
# 4. Verify Data in the Database
# ---------------------------------------
QUERY_VERIFY = "SELECT * FROM main LIMIT 5"
df_check = pd.read_sql_query(QUERY_VERIFY, conn)

print("\nFirst 5 rows from SQL database:")
print(df_check)


# ---------------------------------------
# 5. SQL Demo – Count Number of Rows
# ---------------------------------------
QUERY_COUNT = "SELECT COUNT(*) AS total_rows FROM main"
df_count = pd.read_sql_query(QUERY_COUNT, conn)

print("\nTotal number of rows in the database:")
print(df_count)


# ---------------------------------------
# 6. SQL Demo – List All Tables
# ---------------------------------------
QUERY_TABLES = """
SELECT name AS table_name
FROM sqlite_master
WHERE type = 'table'
"""
df_tables = pd.read_sql_query(QUERY_TABLES, conn)

print("\nTables in the database:")
print(df_tables)


# ---------------------------------------
# 7. SQL Group By Query (Age Distribution)
# ---------------------------------------
QUERY_AGE = """
SELECT Age, COUNT(*) AS count
FROM main
GROUP BY Age
ORDER BY count DESC
"""
age_distribution = pd.read_sql_query(QUERY_AGE, conn)

print("\nAge distribution:")
print(age_distribution)


# ---------------------------------------
# 7. SQL Group By Query (Age Distribution)
# ---------------------------------------
QUERY_AGE = """
SELECT Age, COUNT(*) AS count
FROM main
GROUP BY Age
ORDER BY count DESC
"""
age_distribution = pd.read_sql_query(QUERY_AGE, conn)

print("\nAge distribution:")
print(age_distribution)


# ---------------------------------------
# 8. Visualize Age Distribution
# ---------------------------------------
plt.figure(figsize=(10, 6))
plt.bar(age_distribution['Age'], age_distribution['count'])
plt.title("Survey Respondents by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Respondents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ---------------------------------------
# 9. Describe Table Structure (Schema)
# ---------------------------------------
QUERY_SCHEMA = """
SELECT sql
FROM sqlite_master
WHERE name = 'main'
"""
schema = pd.read_sql_query(QUERY_SCHEMA, conn)

print("\nTable schema:")
print(schema.iloc[0, 0])


# ---------------------------------------
# 10. Close Database Connection
# ---------------------------------------
conn.close()
print("\nDatabase connection closed.")
