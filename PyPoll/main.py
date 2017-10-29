
# coding: utf-8

# In[69]:


import os 
import csv


# In[70]:


file_to_open = "election_data_2 copy.csv"
with open(file_to_open, 'r') as election_data:
    reader = csv.DictReader(election_data)
    contents= set()
    [contents.add(x["Candidate"]) for x in reader]
    list_contents = list(contents)
    #votes = []
    #[votes.append(y["Candidate"]) for y in reader]
    #total_votes = len(votes)
    #print(votes)
  
    
with open(file_to_open, 'r') as election_data:
    content = election_data.read()
    ind_votes = []
    total_votes=0 
    for i in range(0, len(list_contents)):
        count = content.count(list_contents[i])
        total_votes = total_votes + count
        ind_votes.append(count)
    percent_votes=[]
    for x in range(0, len(ind_votes)):
        percent = round((ind_votes[x]/total_votes)*100)
        percent_votes.append(percent)
        
    print(f' The Winner Is:                  {list_contents[0]}')
    print(f' The Candidates Are:             {list_contents}')
    print(f' Respective Percent Won:         {percent_votes}')
    print(f' Respective Votes Per Candidate: {ind_votes}')

   
 
    
   
   
  

