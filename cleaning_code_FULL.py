import pandas as pd
import numpy as np
import seaborn as sns
import sqlite3
import sqlalchemy
import json
import requests
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

#open and read file
df = pd.read_csv("Jobs_NYC_Postings.csv")
pd.set_option('display.max_columns', None)

#Rename FT/PT columns for easier calculations
df =df.rename(columns={'Full-Time/Part-Time indicator': 'FT/PT'})

#Create new column to hold Base Salary Calculations
df['Base Salary'] = 0

#Calculate Daily salary rate to yearly, and copy Annual as yearly
df.loc[df['Salary Frequency'] == 'Daily', 'Base Salary'] = round(df['Salary Range From'].mul(210), 2)
df.loc[df['Salary Frequency'] == 'Annual', 'Base Salary'] = round(df['Salary Range From'], 2)

#calculate Base Salary for Hourly Employees dependent on their FT/PT Status
df['Base Salary'] = np.where((df['FT/PT'] == 'P') & (df['Salary Frequency'] == 'Hourly') , round(df['Salary Range From'].mul(20*52), 2), df['Base Salary'])
df['Base Salary'] = np.where((df['FT/PT'] == 'F') & (df['Salary Frequency'] == 'Hourly') , round(df['Salary Range From'].mul(40*52), 2), df['Base Salary'])

#move Base Salary column to desired location in table
column_to_move = df.pop("Base Salary")  
df.insert(12, "Annual Base Salary", column_to_move) 

#Drop unnecessary columns
df = df.drop(['Title Classification', 'Title Code No', 'Salary Range To', 'Salary Range From', 'Salary Frequency', 'Hours/Shift', 'Post Until', 'Posting Updated'], axis=1)
df = df.drop(['Preferred Skills', 'Additional Information', 'To Apply', 'Recruitment Contact', 'Work Location 1', 'Job Description', 'Process Date'], axis=1)

#rename columns for query managability 
df =df.rename(columns={'FT/PT': 'Ft_Pt', 'Minimum Qual Requirements' : 'Min_qual', 'Job ID' : 'Job_id', '# Of Positions' : 'Num_pos'})
df =df.rename(columns={'Business Title': 'Business_title', 'Civil Service Title' : 'Civil_title', 'Job Category' : 'Category', 'Career Level' : 'Career_level'})
df =df.rename(columns={'Posting Type': 'Posting_type', 'Annual Base Salary' : 'Yearly_salary', 'Work Location' : 'Location', 'Division/Work Unit' : 'Division'})
df =df.rename(columns={'Residency Requirement': 'Res_req', 'Posting Date' : 'Post_Date'})


#create local database
engine = create_engine('sqlite:///CAPSTONE_db.db')
df.to_sql('NYC_job_postings', con=engine, index=False, if_exists='replace')