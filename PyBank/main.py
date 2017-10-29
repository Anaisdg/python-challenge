
# coding: utf-8

# In[1]:


import os 
import csv


# In[10]:


file_to_load = "budget_data_1.csv"


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)
    #total_months = sum(1 for row in reader)
    revenue=[]
    total=0
    for row in reader:
        revenue.append(int(row["Revenue"]))
        total_revenue = total + int(row["Revenue"])
    total_months =  len(revenue)
    
    count=0 
    difference = []
    for i in range(1,len(revenue)): 
        difference.append(revenue[i]-revenue[i-1])
    
    total  = sum(difference)
    average = sum(difference) / len(difference)
    max_rev = max(difference)
    min_rev = min(difference)
    
    print(f'Total Months: {total_months}' )
    print(f'Total Revenue: ${total_revenue}')
    print(f'Average Revenue Change: ${average}')
    print(f'List of Monthly Difference: {difference}')
    print(f'Greatest Increase in Revenue: ${max_rev}')
    print(f'Greatest Decrease in Revenue: ${min_rev}')

        
        
   

