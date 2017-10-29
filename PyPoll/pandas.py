
# coding: utf-8

# In[72]:


import pandas as pd 


# In[73]:


file_one = 'election_data_2.csv'


# In[74]:


file_one_df = pd.read_csv(file_one, encoding = 'UTF-8')
#file_one_df.head()


# In[75]:


# Check to see if data is clean 
counts = file_one_df.count()


# In[76]:


canditates = file_one_df['Candidate'].unique()
#canditates


# In[77]:


votes_per_candidate = file_one_df['Candidate'].value_counts()
#votes_per_candidate


# In[78]:


winning_candidates = file_one_df['Candidate'].value_counts().index.tolist()
#winning_candidates


# In[79]:


total_votes = counts.get_value(0)
#total_votes 


# In[80]:


percent_first = (votes_per_candidate.get_value(0)/total_votes)*100
first = round(percent_first, 2)
#first


# In[81]:


percent_second = (votes_per_candidate.get_value(1)/total_votes)*100
second = round(percent_second, 2)
#second


# In[82]:


percent_third = (votes_per_candidate.get_value(2)/total_votes)*100
third = round(percent_third, 2)
#third


# In[83]:


percent_forth = (votes_per_candidate.get_value(3)/total_votes)*100
forth = round(percent_forth, 2)
#forth


# In[84]:


percentages = [first, second, third, forth]
#percentages


# In[85]:


winner = winning_candidates[0]
#winner


# In[86]:


final = pd.DataFrame({'Candidates' : winning_candidates,
                      'Percentage of Votes' : percentages, 
                      "Winner" : winner,
                      "Total Votes" : total_votes,
                      "Votes per Candidate" : votes_per_candidate
  })
final

