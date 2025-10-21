# Databricks notebook source
# Example: read a CSV and append to Delta table
# csv_path = "/Workspace/Users/lavanyaattisalu@gmail.com/csv-files"

# df = spark.read.option("header", True).csv(csv_path)
# df.write.format("delta").mode("append").saveAsTable("workspace.default.delta_employee")

# df.show()

import os

folder_path = "/Workspace/Users/lavanyaattisalu@gmail.com/csv-files" 
file_list = os.listdir(folder_path)
csv_files = [f for f in file_list if f.endswith('.csv')]
print(csv_files)
