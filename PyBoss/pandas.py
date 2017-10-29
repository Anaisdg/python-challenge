
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file_one = "employee_data1.csv"
file_two = "employee_data2.csv"


# In[3]:


file_one_df = pd.read_csv(file_one, encoding = "UTF-8")
file_two_df = pd.read_csv(file_two, encoding = "UTF-8")
#file_one_df.head()


# In[4]:


#file_two_df.head()


# In[5]:


# To ensure that data is clean
#file_one_df.count()


# In[6]:


# To ensure that data is clean
#file_two_df.count()


# In[7]:


# Create two new columns and split into first and last name 
file_one_df[['First Name', 'Last Name']] = file_one_df['Name'].str.split(expand=True)
#file_one_df.head()


# In[8]:


# Create two new columns and split 'Name' into first and last name 
file_two_df[['First Name', 'Last Name']] = file_two_df['Name'].str.split(expand=True)
#file_two_df.head()


# In[9]:


# Create three new columns and split 'SSN' by hyphen 
file_one_df[['First part of SSN', 'Middle part of SSN', 'Last part of SSN']] = file_one_df['SSN'].str.split("-", expand=True)
#file_one_df.head()


# In[10]:


# Create three new columns and split 'SSN' by hyphen 
file_two_df[['First part of SSN', 'Middle part of SSN', 'Last part of SSN']] = file_one_df['SSN'].str.split("-", expand=True)
#file_two_df.head()


# In[11]:


file_one_df['Last part of SSN'] = '***-**-' + file_one_df['Last part of SSN'].astype(str)
#file_one_df.head()


# In[12]:


file_two_df['Last part of SSN'] = '***-**-' + file_two_df['Last part of SSN'].astype(str)
#file_two_df.head()


# In[13]:


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# In[14]:


file_one_df['State'].replace(us_state_abbrev, inplace = True)
#file_one_df.head()


# In[15]:


file_two_df['State'].replace(us_state_abbrev, inplace = True)
#file_two_df.head()


# In[16]:


organized_one = file_one_df[['Emp ID', 'First Name', 'Last Name', 'DOB', 'Last part of SSN', 'State']]
organized_one.head()


# In[17]:


organized_two = file_two_df[['Emp ID', 'First Name', 'Last Name', 'DOB', 'Last part of SSN', 'State']]
organized_two.head()

