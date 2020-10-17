#!/usr/bin/env python
# coding: utf-8

# In[113]:


# Import Dependencies
import pandas as pd
import csv


# In[114]:


# File to Load
books_clean = "Resources/books_clean.csv"
books_clean_df = pd.read_csv(books_clean)
books_clean_df.head()

# Read the modified GoodReads csv and store into Pandas DataFrame


# In[115]:


# Calculate the number of unique authors in the DataFrame
unique_authors = books_clean_df["Authors"].unique
unique_authors 


# In[116]:


# Calculate the earliest/latest year a book was published

earliest_year = books_clean_df['Publication Year'].min()
earliest_year



# In[117]:



latest_year = books_clean_df['Publication Year'].max()
latest_year


# In[118]:


# Calculate the total reviews for the entire dataset
# Hint: use the pandas' sum() method to get the sum for each row

total = (books_clean_df["One Star Reviews"].sum() + books_clean_df["Two Star Reviews"].sum() + books_clean_df["Three Star Reviews"].sum()+
books_clean_df["Four Star Reviews"].sum() + books_clean_df["Five Star Reviews"].sum())
total


# In[119]:


# Place all of the data found into a summary DataFrame
books_clean_df.describe()


# In[ ]:





# In[ ]:




