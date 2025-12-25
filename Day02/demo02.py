#python code is used to analyze employee data stored in a csv file by
 #1. reading the csv into a pandas dataframe
 #2. inspecting the sturcture of the data
 #3. running sql queries directly on the dataframe
 #4. producing summarized result (total salary per job role)

import pandas as pd
import pandasql as ps

filepath = "emp_hdr.csv"

df = pd.read_csv(filepath)

print("Dataframe Column Types: ")  #Shows the type of each column
print(df.dtypes)                    #Helps avoid SQL mistakes


print("\nEmp Data: ")
print(df)

# query = "SELECT * FROM data WHERE sal BETWEEN 1000 AND 2000 ORDER BY sal"

query = "Select job, Sum(sal) total FROM data GROUP BY job"

result = ps.sqldf(query, {"data": df})  #sqldf() - executes SQL
                                        #"data" - is the sql table name 
                                        #df is the actual dataframe

print("\n Query Result: ")
print(result)