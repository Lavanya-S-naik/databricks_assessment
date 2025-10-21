## Databricks Data Engineering Assessment
### Project Summary<br>
`This project demonstrates key data engineering tasks using Databricks and Python. The workflow covers automated CSV file generation, smart file filtering, and table creation with Spark SQL.`

---

## Task List
### Create a Databricks account and explore its features
  `Workspace explored, notebooks and folders created and organized.`

### Write SQL to create a Delta table from an existing table
  `Delta table created using SQL below.`

### Python: Use list comprehension to filter .csv files from a list
  `Script filters all files in a folder and selects those ending with .csv.`

---

## Project Steps
### 1. Set Up Your Environment

  Create a free Databricks account at databricks.com.<br>
  Launch your first workspace and explore key features: compute, SQL editor, notebooks, and workspace file browser.<br>

### 2. Generate Synthetic Data Files (Locally)

  Use the given Python script(generate_csv) code file to create 10 CSV files with sample employee data.

### 3. Upload CSV Files to Databricks
  
  Move the generated .csv files into Databricks.
  Or Use Databricks UI "Data"/"Upload Data" if available.

### 4. List and Filter Files Using Python
  In a Databricks notebook cell, filter for .csv files using python code given in folder.

### 5. Create a Delta Table from Existing Table using SQL
  Use the SQL editor or notebook cell, and run:

 <code>
  sql
  CREATE TABLE delta_employee
  USING delta
  AS SELECT * FROM employee_data;
  </code>
  
### 6. Review Outputs
  Check the printed list of CSV files in your notebook output.<br>
  Creation of the delta_employee table in SQL or workspace table browser.
  **Snapshots**
  

## Happy coding!!!...
 

