

```python
<h> Anais Dotis-Georgiou </h>
```


      File "<ipython-input-3-0aea4e1dd56b>", line 1
        <h> Anais Dotis-Georgiou </h>
        ^
    SyntaxError: invalid syntax




```python
import pandas as pd
import numpy as np
```


```python
# Upload files
file_path = "students_complete copy.csv"
file_path_two = "schools_complete copy.csv"
```


```python
students = pd.read_csv(file_path)
schools = pd.read_csv(file_path_two)
#students.head()
```


```python
#rename columns to prepare for merge
students.columns = ['Student ID', 'student name', 'gender', 'grade', 'school', 'reading_score',
       'math_score']

```


```python
schools.columns = ['School ID', 'school', 'type', 'size', 'budget']
#schools.head()
```


```python
# Merge the two csv files
merged_df = pd.merge(schools, students, on="school")
#merged_df.head()
```


```python
# Create df with only district schools
district_df = merged_df.loc[merged_df['type'] == "District"]
#district_df.head()
```


```python
# Gather information on district schools

district_info = schools.loc[schools["type"] == "District"]
district_schools = len(district_info)
total_students = district_info['size'].sum()
budget = district_info['budget'].sum()
avg_math_score = round(district_df["math_score"].mean())
avg_reading_score = round(district_df["reading_score"].mean())
passing_math = (district_df["math_score"] >= 70).sum()
percent_passing_math = round((passing_math/total_students),2)
passing_reading = (district_df["reading_score"] >= 70).sum()
percent_passing_reading = round((passing_reading/total_students),2)
overall_passing_rate = round((np.mean([percent_passing_math, percent_passing_reading])),2)

```


```python
# Create df for district summary 

district_summary = pd.DataFrame({'Total Schools in District' : [district_schools],
'Total Students' : [total_students],
'Total Budget' : [budget],
'Average Math Score' : [avg_math_score],
'Average Reading Score' : [avg_reading_score],
'% Passing Math' : [percent_passing_math],
'% Passing Reading' : [percent_passing_reading],
'Overall Passing Rate' : [overall_passing_rate]})



```

# District Summary


```python
district_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>Overall Passing Rate</th>
      <th>Total Budget</th>
      <th>Total Schools in District</th>
      <th>Total Students</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.67</td>
      <td>0.81</td>
      <td>77</td>
      <td>81</td>
      <td>0.74</td>
      <td>17347923</td>
      <td>7</td>
      <td>26976</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Gather information...
student_count = merged_df.groupby('school')['student name'].count()

school_type = merged_df.groupby('school')['type'].unique()
school_budget = merged_df.groupby('school')['budget'].unique()

total_school_budget = school_budget.values.sum()
avg_math_score_all = round(merged_df.groupby('school')['math_score'].mean(),2)
avg_reading_score_all = round(merged_df.groupby('school')['reading_score'].mean(),2)

# .unique() returns values in [] need to contain within () and asign .str to the first/only column 
school_type = school_type.str[0]
school_budget = school_budget.astype(float)

per_student_budget = round(school_budget/student_count,2)


```


```python
# Create new df with only scores above 70 and gather information 
passing_df = merged_df.loc[(merged_df['math_score'] >= 70) & (merged_df['reading_score'] >60)]
passing_df.head()
passing_math_df = merged_df.loc[(merged_df['math_score'] >= 70)]
passing_reading_df = merged_df.loc[(merged_df['reading_score'] >= 70)]

passing_math_all = passing_math_df.groupby('school')['math_score'].count()
passing_reading_all = passing_reading_df.groupby('school')['reading_score'].count()

percent_math_all = passing_math_all/student_count
percent_reading_all = passing_reading_all/student_count

overall_passing_all = round((percent_math_all + percent_reading_all)/2, 2)

passing_math_all
student_count
percent_math_all
```




    school
    Bailey High School       0.666801
    Cabrera High School      0.941335
    Figueroa High School     0.659885
    Ford High School         0.683096
    Griffin High School      0.933924
    Hernandez High School    0.667530
    Holden High School       0.925059
    Huang High School        0.656839
    Johnson High School      0.660576
    Pena High School         0.945946
    Rodriguez High School    0.663666
    Shelton High School      0.938671
    Thomas High School       0.932722
    Wilson High School       0.938677
    Wright High School       0.933333
    dtype: float64




```python
# Need to Concatenate to get the followin df:

dataframes = [school_type, 
              student_count, 
              school_budget,
              per_student_budget,
              avg_math_score_all, 
              avg_reading_score_all, 
              percent_math_all, 
              percent_reading_all,
              overall_passing_all]

school_summary = pd.concat(dataframes, axis = 1)


# Reset index

school_summary = school_summary.reset_index()

```


```python
# Rename columns
school_summary.columns = ['School Name',
                          'School Type',
                          'Total Students',
                          'Total School Budget',
                          'Per Student Budget',
                          'Average Math Score',
                          'Average Reading Score',
                          '% Passing Math',
                          '% Passing Reading',
                          'Overall Passing Rate']

```

# School Summary


```python
school_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928.0</td>
      <td>628.0</td>
      <td>77.05</td>
      <td>81.03</td>
      <td>0.666801</td>
      <td>0.819333</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356.0</td>
      <td>582.0</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>0.941335</td>
      <td>0.970398</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411.0</td>
      <td>639.0</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>0.659885</td>
      <td>0.807392</td>
      <td>0.73</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916.0</td>
      <td>644.0</td>
      <td>77.10</td>
      <td>80.75</td>
      <td>0.683096</td>
      <td>0.792990</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500.0</td>
      <td>625.0</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>0.933924</td>
      <td>0.971390</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020.0</td>
      <td>652.0</td>
      <td>77.29</td>
      <td>80.93</td>
      <td>0.667530</td>
      <td>0.808630</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087.0</td>
      <td>581.0</td>
      <td>83.80</td>
      <td>83.81</td>
      <td>0.925059</td>
      <td>0.962529</td>
      <td>0.94</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635.0</td>
      <td>655.0</td>
      <td>76.63</td>
      <td>81.18</td>
      <td>0.656839</td>
      <td>0.813164</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650.0</td>
      <td>650.0</td>
      <td>77.07</td>
      <td>80.97</td>
      <td>0.660576</td>
      <td>0.812224</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858.0</td>
      <td>609.0</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>0.945946</td>
      <td>0.959459</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363.0</td>
      <td>637.0</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>0.663666</td>
      <td>0.802201</td>
      <td>0.73</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600.0</td>
      <td>600.0</td>
      <td>83.36</td>
      <td>83.73</td>
      <td>0.938671</td>
      <td>0.958546</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130.0</td>
      <td>638.0</td>
      <td>83.42</td>
      <td>83.85</td>
      <td>0.932722</td>
      <td>0.973089</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574.0</td>
      <td>578.0</td>
      <td>83.27</td>
      <td>83.99</td>
      <td>0.938677</td>
      <td>0.965396</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400.0</td>
      <td>583.0</td>
      <td>83.68</td>
      <td>83.96</td>
      <td>0.933333</td>
      <td>0.966111</td>
      <td>0.95</td>
    </tr>
  </tbody>
</table>
</div>



# Top Schools by Passing Rate


```python
top_schools=school_summary.sort_values("Overall Passing Rate", axis=0, ascending=False, inplace=False)
top_schools.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356.0</td>
      <td>582.0</td>
      <td>83.06</td>
      <td>83.98</td>
      <td>0.941335</td>
      <td>0.970398</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500.0</td>
      <td>625.0</td>
      <td>83.35</td>
      <td>83.82</td>
      <td>0.933924</td>
      <td>0.971390</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858.0</td>
      <td>609.0</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>0.945946</td>
      <td>0.959459</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600.0</td>
      <td>600.0</td>
      <td>83.36</td>
      <td>83.73</td>
      <td>0.938671</td>
      <td>0.958546</td>
      <td>0.95</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130.0</td>
      <td>638.0</td>
      <td>83.42</td>
      <td>83.85</td>
      <td>0.932722</td>
      <td>0.973089</td>
      <td>0.95</td>
    </tr>
  </tbody>
</table>
</div>



# Bottom Schools by Passing Rate


```python
bottom_schools=school_summary.sort_values("Overall Passing Rate", axis=0, ascending=True, inplace=False)
bottom_schools.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411.0</td>
      <td>639.0</td>
      <td>76.71</td>
      <td>81.16</td>
      <td>0.659885</td>
      <td>0.807392</td>
      <td>0.73</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363.0</td>
      <td>637.0</td>
      <td>76.84</td>
      <td>80.74</td>
      <td>0.663666</td>
      <td>0.802201</td>
      <td>0.73</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928.0</td>
      <td>628.0</td>
      <td>77.05</td>
      <td>81.03</td>
      <td>0.666801</td>
      <td>0.819333</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916.0</td>
      <td>644.0</td>
      <td>77.10</td>
      <td>80.75</td>
      <td>0.683096</td>
      <td>0.792990</td>
      <td>0.74</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020.0</td>
      <td>652.0</td>
      <td>77.29</td>
      <td>80.93</td>
      <td>0.667530</td>
      <td>0.808630</td>
      <td>0.74</td>
    </tr>
  </tbody>
</table>
</div>



# Math Scores by Grade


```python
math_scores_df = round(students.groupby(["school","grade"])["math_score"].mean().unstack(level=1),2)
#math_scores_df = math_scores_df[sorted(math_scores_df.columns)]
math_scores_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>grade</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.00</td>
      <td>77.52</td>
      <td>76.49</td>
      <td>77.08</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.15</td>
      <td>82.77</td>
      <td>83.28</td>
      <td>83.09</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.54</td>
      <td>76.88</td>
      <td>77.15</td>
      <td>76.40</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.67</td>
      <td>76.92</td>
      <td>76.18</td>
      <td>77.36</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>84.23</td>
      <td>83.84</td>
      <td>83.36</td>
      <td>82.04</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.34</td>
      <td>77.14</td>
      <td>77.19</td>
      <td>77.44</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.43</td>
      <td>85.00</td>
      <td>82.86</td>
      <td>83.79</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>75.91</td>
      <td>76.45</td>
      <td>77.23</td>
      <td>77.03</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>76.69</td>
      <td>77.49</td>
      <td>76.86</td>
      <td>77.19</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.37</td>
      <td>84.33</td>
      <td>84.12</td>
      <td>83.63</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.61</td>
      <td>76.40</td>
      <td>77.69</td>
      <td>76.86</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>82.92</td>
      <td>83.38</td>
      <td>83.78</td>
      <td>83.42</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.09</td>
      <td>83.50</td>
      <td>83.50</td>
      <td>83.59</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.72</td>
      <td>83.20</td>
      <td>83.04</td>
      <td>83.09</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>84.01</td>
      <td>83.84</td>
      <td>83.64</td>
      <td>83.26</td>
    </tr>
  </tbody>
</table>
</div>



# Reading Scores by Grade


```python
reading_scores_df = round(students.groupby(["grade","school"])["reading_score"].mean().unstack(level=0),2)
reading_scores_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>grade</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>80.91</td>
      <td>80.95</td>
      <td>80.91</td>
      <td>81.30</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>84.25</td>
      <td>83.79</td>
      <td>84.29</td>
      <td>83.68</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.41</td>
      <td>80.64</td>
      <td>81.38</td>
      <td>81.20</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>81.26</td>
      <td>80.40</td>
      <td>80.66</td>
      <td>80.63</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.71</td>
      <td>84.29</td>
      <td>84.01</td>
      <td>83.37</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.66</td>
      <td>81.40</td>
      <td>80.86</td>
      <td>80.87</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.32</td>
      <td>83.82</td>
      <td>84.70</td>
      <td>83.68</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.51</td>
      <td>81.42</td>
      <td>80.31</td>
      <td>81.29</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>80.77</td>
      <td>80.62</td>
      <td>81.23</td>
      <td>81.26</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.61</td>
      <td>84.34</td>
      <td>84.59</td>
      <td>83.81</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.63</td>
      <td>80.86</td>
      <td>80.38</td>
      <td>80.99</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.44</td>
      <td>84.37</td>
      <td>82.78</td>
      <td>84.12</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>84.25</td>
      <td>83.59</td>
      <td>83.83</td>
      <td>83.73</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>84.02</td>
      <td>83.76</td>
      <td>84.32</td>
      <td>83.94</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.81</td>
      <td>84.16</td>
      <td>84.07</td>
      <td>83.83</td>
    </tr>
  </tbody>
</table>
</div>



# Scores by School Spending
Average Math Score

Average Reading Score

% Passing Math

% Passing Reading

Overall Passing Rate (Average of the above two)


```python

#school_summary.groupby("Spending Summary")
bins = [0,585,615,645,675]
group_names = ["<$585","$585-$615","$615-$645","$645-$675"]
pd.cut(school_summary["Per Student Budget"], bins, labels = group_names)
school_summary["Spending Summary"]=pd.cut(school_summary["Per Student Budget"], bins, labels = group_names)
scores_df = school_summary[["School Name","Spending Summary", "Average Math Score","Average Reading Score", "% Passing Math", "% Passing Reading"]]
scores_df = scores_df.groupby("Spending Summary").max()
scores_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
    </tr>
    <tr>
      <th>Spending Summary</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;$585</th>
      <td>Wright High School</td>
      <td>83.80</td>
      <td>83.99</td>
      <td>0.941335</td>
      <td>0.970398</td>
    </tr>
    <tr>
      <th>$585-$615</th>
      <td>Shelton High School</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>0.945946</td>
      <td>0.959459</td>
    </tr>
    <tr>
      <th>$615-$645</th>
      <td>Thomas High School</td>
      <td>83.42</td>
      <td>83.85</td>
      <td>0.933924</td>
      <td>0.973089</td>
    </tr>
    <tr>
      <th>$645-$675</th>
      <td>Johnson High School</td>
      <td>77.29</td>
      <td>81.18</td>
      <td>0.667530</td>
      <td>0.813164</td>
    </tr>
  </tbody>
</table>
</div>



# Scores by School Size

# Scores by School Type


```python
scores_df = school_summary[["School Name","School Type", "Average Math Score","Average Reading Score", "% Passing Math", "% Passing Reading"]]
scores_df = scores_df.groupby("School Type").max()
scores_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Name</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>Wright High School</td>
      <td>83.84</td>
      <td>84.04</td>
      <td>0.945946</td>
      <td>0.973089</td>
    </tr>
    <tr>
      <th>District</th>
      <td>Rodriguez High School</td>
      <td>77.29</td>
      <td>81.18</td>
      <td>0.683096</td>
      <td>0.819333</td>
    </tr>
  </tbody>
</table>
</div>


