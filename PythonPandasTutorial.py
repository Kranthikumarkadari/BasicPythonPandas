#!/usr/bin/env python
# coding: utf-8

# # PART-01 Getting Started with Data Analysis - Installation and Loading Data

# In[61]:


import pandas as pd


# In[60]:


## loading the dataset of survey results public and schema

### If we wanted to ignore custom values when loading csv then we can simply passin an argument of a list of values
### that we wanna be treated as missing so here's how we would do this::
### if we had custom missing values here in this csv file then simply create a list of those missing values...
na_vals = ['NA','Missing']

df = pd.read_csv('survey_results_public.csv',na_values=na_vals)
schema_df = pd.read_csv('survey_results_schema.csv')


# In[62]:


df


# In[4]:


schema_df


# In[5]:


## setting ResponseId and Qname as index columns since they are unique identifiers
df = pd.read_csv('survey_results_public.csv',index_col = 'ResponseId')
schema_df = pd.read_csv('survey_results_schema.csv',index_col = 'qname')


# In[6]:


df


# In[7]:


## Let's go and see the column that doesn't make any sense
df.index


# In[8]:


df.loc[1,'Employment']


# In[9]:


schema_df


# In[10]:


## If you wanna sort the schema datafram alphabetically(ascending order) which will make bit easier to read 
## and identify them easily and to make it permanent changes just add in another argument called inplace = 'True'

schema_df.sort_index()


# In[11]:


## If you wanna sort the schema datafram alphabetically(ascending order) which will make bit easier to read 
## and identify them easily and to make it permanent changes just add in another argument called inplace = 'True'
schema_df.sort_index(inplace=True)
schema_df


# In[12]:


## If you wanna sort the schema datafram in descending order which will make bit easier to read and identify them easily
## what we are looking for and to make it permanent changes just add in another argument called inplace = 'True'

schema_df.sort_index(ascending = False)
schema_df.sort_index(ascending = False,inplace = True)


# In[13]:


## we wanna know what exactly  S1 means but we are not able to see the entire question row contains.
## if you wanna see full context just see following cell
schema_df.loc['S1']


# In[14]:


## to see the entire text of S1 row : just pass in s1 row and question column as a list into .loc
schema_df.loc['S1','question']


# In[15]:


## SETTING AN INDEX: deleting default index and setting ResponseID to index column 
## bcoz they are unique identifiers with the label

df.set_index('ResponseId',inplace=True)
df

## or df = pd.read_csv('survey_results_public.csv',index_col = 'ResponseId')


# In[ ]:


##info method gives total no.of.columns and rows & also data types of that columns
df.info()


# In[ ]:


## Shape is an attribute so you do not have to put parenthesis. It is not a METHOD/FUNCTION. 
## It gives tuple values with total number of rows and columns
## here in this Dataframe, we've got 89184 rows and 84 columns
df.shape


# In[ ]:


df.describe()


# In[ ]:


## To get first 5 Rows of DataFrame
df.head()


# In[ ]:


## we can also pass certain value to get the rows that you wanted
df.head(10)


# In[ ]:


## To get Last 5 Rows of DataFrame
df.tail()


# In[ ]:


## To get last 10 Rows of DataFrame
df.tail(10)


# In[63]:


## If we wanna see all of the columns in datafram then we have to change the settings:
pd.set_option('display.max_columns',84)
df


# In[ ]:


## if you are curious to know about the column definitions we do have schema csv file just upload and see the meaning
schema_df = pd.read_csv('survey_results_schema.csv')


# In[ ]:


schema_df


# In[64]:


pd.set_option('display.max_rows',78)
schema_df


# In[76]:


schema_df.iloc[16,2]


# In[77]:


schema_df.iloc[15,2]


# ## LET'S PERFORM SIMILAR OPERATIONS THAT WE LEARNT DOWN BELOW

# In[ ]:


df.columns


# In[ ]:


df['Employment']


# In[ ]:


## VALUE COUNTS IS A METHOD TO FIND OUT TOTAL COUNT OF EACH CATEGORY
df['Employment'].value_counts()


# In[ ]:


df.loc[[0, 1]]


# In[ ]:


df.loc[[0, 1],'Employment']


# In[ ]:


df.loc[4,'Employment']


# In[ ]:


df.loc[4,'Employment']


# In[ ]:


df.loc[[0, 1], ['Employment', 'Age']]


# In[ ]:


df.loc[[0,1,2,3], ['Employment', 'ResponseId','Age']]


# # SLICING - slicing is inclusive 

# In[ ]:


## We just looking at first 4 rows of specific columns
df.loc[0:3, ['Employment', 'ResponseId','Age']]


# In[ ]:


## do not have to put in brackets bcoz 
df.loc[0:3, 'ResponseId': 'EdLevel']


# ## # FILTERING OPERATIONS(AND, OR )

# In[ ]:


## FILTERING OPERATIONS(AND, OR )
high_salary = (df['ConvertedCompYearly'] > 70000)
high_salary


# In[ ]:


high_salary.value_counts()


# In[ ]:


df.loc[high_salary]


# # FILTERING MULTIPLE VALUES

# In[ ]:


df.loc[high_salary,['Country','ProfessionalTech','ConvertedCompYearly']]


# In[ ]:


## if you wanna get the information of the sepecific countries you are interested in:
countries = ['India','United Kingdom','United States of America','Canada','Australia']
filt_1 = df['Country'].isin(countries)


# In[ ]:


df.loc[filt_1,'Country']


# ### FILTER STRINGS

# In[ ]:


## if you are interested to get the rows with the DEVOPS FUNCTION we use string filters 
df['ProfessionalTech']


# In[ ]:


## we also see nan outlier as well which means not a number so we have to specify it as na = False
filt_2 = df['ProfessionalTech'].str.contains('DevOps function', na=False)


# In[ ]:


## we get the all rows which has DEVOPS FUNCTION
df.loc[filt_2,'ProfessionalTech']


# In[ ]:


df


# ####  Modifying AND Updating Column NAME using RENAME METHOD

# In[ ]:


df.rename(columns = {'ConvertedCompYearly':'SalaryUSD'},inplace=True)
df


# In[ ]:


df['SalaryUSD']


# In[ ]:


#### CONVERTING HOBBYIST COLUMN from YES / No to True/False
df['Q120']


# ###  SORTING DATA:

# In[ ]:


df.sort_values(by='Country',inplace=True)


# In[ ]:


df['Country'].head(50)


# In[ ]:


df[['Country','ConvertedCompYearly']].head(50)


# In[ ]:


### I am interested to get country column in ascending and convertedcompyearly column in descending order

df.sort_values(by=['Country','ConvertedCompYearly'],ascending=[True,False],inplace=True)


# In[ ]:


## And also I would like to get first 50 rows of the data
df[['Country','ConvertedCompYearly']].head(50)


# ####  TO FIND N LARGEST AND SMALLEST from data: nlargest and nsmallest

# In[ ]:


### i want to know 10 largest salaries from data
df['ConvertedCompYearly'].nlargest(10)


# In[ ]:


### i want to know 10 largest salaries from data with the complete details
df.nlargest(10,'ConvertedCompYearly')


# In[ ]:


### i want to know 10 smallest salaries from data 
df['ConvertedCompYearly'].nsmallest(10)


# In[ ]:


### i want to know 10 smallest salaries from data with the complete details
df.nsmallest(10,'ConvertedCompYearly')


# ####  GROUPING AND AGGREGATING THE DATA:

# In[ ]:


### In this column we can see NAN values which means Not A Number(Outliers). In this context which means they skipped 
## the question in the survey
df['ConvertedCompYearly'].head(15)


# In[ ]:


### we can see the median salary for the survey just by running median method on this series object
### It gives median salary of the survey by ignoring NAN values
### Probably this doesn't give us as much information as we'd really like to have so for example different countries 
### pays different amounts since there are different cost-of-livings and things like that
### it would by nice if we broken down median salary by countries that's where grouping comes into picture

df['ConvertedCompYearly'].median()


# In[ ]:


### if you wanna look at median values of entire dataframe it just gives us median of all numerical data columns
df.median()


# In[ ]:


### Describe method says us broad STATISTICAL OVERVIEW OF A DATAFRAME

### iT gives us different stats like COUNT,MEAN,STANDARD DEVIATION,MINIMUM,QUANTILES (25%,MEDIAN(50%),75%), MAXIMUM

### We are focused mainly on median not mean bcoz Mean is heavily affected by OUTLIERS(NAN). 

### its not really a good metric to use bcoz few outliers can heavily affect the average

### COUNT means it counts non missing rows that means Respondent didnt answer to that specific question

df.describe()


# In[ ]:


### we can also run descirbe method on a single column as well

df['ConvertedCompYearly'].describe()


# In[ ]:


### Only 48019 people are responded to that question out of 89184

df['ConvertedCompYearly'].count()


# In[ ]:


df['DatabaseHaveWorkedWith']


# In[ ]:


df['DatabaseHaveWorkedWith'].value_counts()


# ### CASTING AND CALCULATING AVERAGES

# ### Q1 : Calculate Avg No.of.Years Coding Experience among the Developers?

# In[78]:


schema_df.iloc[15]


# In[79]:


schema_df.iloc[15,2]


# In[80]:


### Lets look at the first 20 rows whether they are having different values or not to callculate average
### looks alright to perform average 

df['YearsCode'].head(20)


# In[81]:


### we've seen already this kinda error in our sample dataset and we know how to fix this issue???
df['YearsCode'].mean()


# In[84]:


### Lets typecast the data and then cal average
### But we got ValueError: could not convert string to float: 'Less than 1 year'
### LETS see the unique values in the series object of " YEARS CODE "

df['YearsCode'] = df['YearsCode'].astype(float)


# ### UNIQUE METHOD: To see unique values in the columns or series object

# In[85]:


### We can clearly see that we also have strings in our column : Less than 1 year & More than 50 years' mixed throughout 
### these numbers and we also has nan values but we're not gonna worry about those bcoz they are actually float 
### under the hood

df['YearsCode'].unique()


# In[86]:


type(np.nan)


# #### Replacing Strings to Numbers

# In[95]:


### Lets replace the strings:  Less than 1 year to 0 & More than 50 years to 51.
df['YearsCode'].replace('Less than 1 year',0,inplace=True)

df['YearsCode'].replace('More than 50 years',51,inplace=True)


# In[96]:


df['YearsCode'] = df['YearsCode'].astype(float)


# In[97]:


### Now we got the average value of coding experience have got for the developers who answered the survey
### Lets do some more Statistical Analysis if we wanna perform

df['YearsCode'].mean()


# In[98]:


df['YearsCode'].median()


# ###           PRACTISING ON CREATED DATASET

# # Part 2: DataFrame and Series Basics - Selecting Rows and Columns

# # CREATING A DATAFRAME

# In[ ]:


person = {
    "first": "Corey", 
    "last": "Schafer", 
    "email": "CoreyMSchafer@gmail.com"
}


# In[ ]:


people = {
    "first": ["Corey"], 
    "last": ["Schafer"], 
    "email": ["CoreyMSchafer@gmail.com"]
}


# In[ ]:


people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


# In[ ]:


people['email']


# In[ ]:


import pandas as pd


# In[ ]:


df = pd.DataFrame(people)


# In[ ]:


df


# # ACCESSING A SIGNLE COLUMN

# In[ ]:


## to access a single column with the key passing in it..
## This is the best way to use 
df['email']


# In[ ]:


## And ALSO we can access a single column by period(dot notation) which returns same series object of email values
## i would not recommend you to use dot because for an instance if you have a column called COUNT(df.count wont work)
df.email


# In[ ]:


type(df['email'])


# # what is a series?
# A series is a 1D ARRAY which means rows of a single column....
# A DATAFRAME is basically a container for multiple of these series objects
# ex: first column as a series, last column as a series and email column as series
# Note : Series also has an index as well just like we have for our dataframe

# # ACCESSING A MULTIPLE COLUMN 

# In[ ]:


df[['last', 'email']]


# In[ ]:


## To grab all the columns if you are interested to see
df.columns


# # To ACCESS ROWS:
#     using loc[specify column names] and iloc(specify INTEGER LOCATION since it is a ILOC(integer location))

# # a)ILOC

# In[ ]:


## TO ACCESS FIRST ROW OF A DATAFRAME
df.iloc[0]


# # Selecting multiple rows

# In[ ]:


## TO ACCESS FIRST TWO ROWS OF A DATAFRAME....again it will give us a dataframe 

df.iloc[[0, 1]]


# In[ ]:


## TO ACCESS FIRST two ROWs OF A DATAFRAME and also a single column
## it gives specific column object for specific rows that we wanted

df.iloc[[0, 1],2]


# In[ ]:


## TO ACCESS FIRST two ROWs OF A DATAFRAME and also two columns
## it gives specific column objects of last and email for specific rows that we wanted
df.iloc[[0, 1],[1,2]]


# # b) LOC

# In[ ]:


## TO ACCESS FIRST ROW OF A DATAFRAME
df.loc[0]


# In[ ]:


## TO ACCESS FIRST TWO ROWS OF A DATAFRAME....again it will give us a dataframe JUST LIKE ILOC

df.loc[[0, 1]]


# In[ ]:


## TO ACCESS FIRST two ROWs OF A DATAFRAME and also a single column HERE we pass column name as a key
## it gives specific column object for specific rows that we wanted
df.loc[[0, 1], 'email']


# In[ ]:


## TO ACCESS FIRST two ROWs OF A DATAFRAME and also two columns HERE we pass two column names(series) as a keys in a list
## it gives specific column object for specific rows that we wanted
df.loc[[0, 1], ['email', 'last']]


# #  PART-03 INDEXES (how to set, reset and use indexes)
# WE HAVE SEEN DEFAULT INDEXES IN THE PART-2 AND NOW WE WILL BE SEEING CUSTOM INDEXES AND BENEFIT OF DOING THIS

# In[ ]:


people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


# In[ ]:


import pandas as pd


# In[ ]:


df = pd.DataFrame(people)


# In[ ]:


## If we look at the dataframe we have DEFAULT indexes 0,1 and 2 that looks like a column without name which is an INDEX
## Index is a range of numbers that basically an INTEGER IDENTIFIERS for the rows
## It may have different identifiers for each row which basically be the LABEL for that row which is usually unique.
## here in our sample data 'EMAIL'address would be the index for this data bcoz that's usually a unique value for the people.

df


# # SETTING AN INDEX

# In[ ]:


## to view all of the emails 
df['email']


# In[ ]:


## Now Email column looks like a column
df.set_index('email')


# In[ ]:


## If we look our dataframe again then it didnt actually change. It still has the default index to the left
## this is because PANDAS DOES NOT DO A LOT OF THESE CHANGES in place unless we specifically tell it to do so.
## This is nice because it allows us to experiemnt without worrying about modifying our dataframe in unexpected ways.

df


# In[ ]:


## If we want to set EMAIL column to be as AN INDEX COLUMN and have those changes carryover into those future cells.
## To do so we have to pass in another argument inplace = True

df.set_index('email', inplace = True)


# In[ ]:


## Now if we look at our dataframe by running it. dataframe did modified and Email column set to INDEX COLUMN

df


# In[ ]:


## If you wanna look at the INDEX specifically
df.index


# In[ ]:


## WHY WOULD THIS ACCTUALLY BE USEFUL??
## Email address as the index gives us a nice UNIQUE IDENTIFIER for our rows
## We used '".LOC " to search our dataframe by "LABEL ".
## these indexs are Labels for these rows

## we've used df.loc[0] previously
## We get the row for that specific Email Index
df.loc['CoreyMSchafer@gmail.com']


# In[ ]:


## We can still pass in values for the specific columns
df.loc['CoreyMSchafer@gmail.com','last']


# In[ ]:


## We actually NO LONGER HAVE those default integers index bcoz we're using Email index
## We gonna get TYPE ERROR
df.loc[0]


# In[ ]:


## IF YOU STILL WANNA USE INTEGER LOCATION WITHOUT LABELS. WE STILL HAVE ILOC index still available
df.iloc[0]


# In[ ]:


## first row but second column
df.iloc[0,1]


# # HOW TO RESET AN INDEX?

# In[ ]:


## Now we will get back to email as a column but not an index column and will get default range of index
df.reset_index(inplace=True)


# In[ ]:


df


# # PART-04 FILTERING - USING CONDITIONALS TO FILTER ROWS AND COLUMNS:
# Filtering is very essential to filter the data from the dataset that we are intersted into..

# In[ ]:


people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


# In[ ]:


pd.DataFrame(people)


# In[ ]:


df = pd.DataFrame(people)
df


# In[ ]:


## If I wanna to get the rows with the Last name " Doe" but it gave series of boolean values that we might not be expected
## True values are the rows that met filter criteria and False values that didnt meet our filter criteria
df['last'] == 'Doe'


# In[ ]:


## If I wanna to get the rows with the Last name " Doe" but it gave series of boolean values
## you can assign it to the variable called as FILT(Note: don't use FILTER bcoz pandas has existed FILTER variable)
## use parenthesis so that you can read easily and understand.
filt = (df['last'] == 'Doe')


# # FILTER MASK

# In[ ]:


df[filt]


# In[ ]:


## we can also use this way but its littel more difficult to read and understand
df[df['last'] == 'Doe']


# # FILTER DATAFRAME

# In[ ]:


## this is nother way to filter out the data and best way to use it 
df.loc[filt]


# In[ ]:


## you can get the specifi column from filt variable
df.loc[filt,'email']


# # USING AND (&), OR(|) operators

# In[ ]:


## i am interested to get the email id  by filtering out USING AND OPERATOR
filt = (df['last'] == 'Doe') & (df['first'] == 'John')


# In[ ]:


df.loc[filt]


# In[ ]:


df.loc[filt,'email']


# In[ ]:


## i am interested to get the email ids by filtering out using OR OPERATOR
filt = (df['last'] == 'Schafer') | (df['first'] == 'John')


# In[ ]:


df.loc[filt,'email']


# In[ ]:


## To get  opposite of those results WE SIMPLY usE TILDE SIGN(~)
## IT prints out without Schafer and John
df.loc[~filt,'email']


# # PART-05 Updating Rows and Columns - Modifying Data Within DataFrames
# we will be learning how to modify the data within our DataFrames.
# We will use some of the filtering techniques we learned in the last part to update values conditionally, 
# and we will also be learning how to use the apply, map, and applymap method. Let's get started...
# 

# ### let's learn how to modify the columns first:

# In[ ]:


people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


# In[ ]:


df = pd.DataFrame(people)


# In[ ]:


df.columns


# In[ ]:


## I would like to modify the column names to more specific
## we can do it simply by assigning new column names passing in list
df.columns = ['first_name','last_name','email_id']
df.columns


# In[ ]:


df


# In[ ]:


## if we wanna change the column names to be upper case or lower case or vice versa
## maybe if column names have spaces if we wanna replace them with the underscore
## In this case we use LIST COMPREHENSION
df.columns = [x.upper() for x in df.columns]
df


# In[ ]:


## if we wanna change the column names to be upper case or lower case or vice versa
## maybe if column names have spaces if we wanna replace them with the underscore
## In this case we use LIST COMPREHENSION
df.columns = [x.lower() for x in df.columns]
df


# In[ ]:


## we can replace undersore and just leave it a space using string replace method 
df.columns = df.columns.str.replace('_', ' ')
df


# In[ ]:


## we can replace space and replace it back with underscore using string replace method 
df.columns = df.columns.str.replace(' ', '_')
df


# In[ ]:


## if we wanted to change some columns we can use RENAME METHOD
## AND just pass in dictionary of the columns that we want to change


# In[ ]:


df


# In[ ]:


df.rename(columns = {'first_name':'first','last_name':'last'})


# In[ ]:


## but the changes didn't went through in our dataframe 
df


# In[ ]:


## if we want the changes to take place permanently just add an argument inplace = True 
df.rename(columns = {'first_name':'first','last_name':'last'}, inplace=True)
df


# ### UPDATING THE DATA IN ROWS:

# In[ ]:


people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


# In[ ]:


df = pd.DataFrame(people)
df


# ### UPDATING A SINGLE ROW

# In[ ]:


df.loc[2]


# In[ ]:


## updating the second row 
df.loc[2] = ['John','Smith', 'JohnSmith@email.com']
df.loc[2]


# In[ ]:


## if you wanna update only two columns in a second row
df.loc[2,['last','email']] = ['Doe','JohnDoe@email.com']
df.loc[2]


# In[ ]:


## if you wanna change single value(one row and one column)
df.loc[2,'last'] = 'Smith'
df.loc[2]


# In[ ]:


df


# In[ ]:


## We can also change a single value by using "at " but best way is to use " LOC ""
df.at[2,'last'] = 'Doe'
df


# In[ ]:


## LET'S TRY USING filters to grab that specific row
filt = (df['email'] == 'JohnDoe@email.com')
df[filt]


# In[ ]:


## if you are interested to get second row last column 
df[filt]['last']


# In[ ]:


## this doesn't work bcoz filt is a temp variable that we set just click the link below to get in detail information
df[filt]['last'] = 'Smith'


# In[ ]:


## that didn't work out as we can see same dataframe even if tried to change the last name to smith by assignment method
df


# In[ ]:


## By using loc index on filt variable it did go through and changed our column name to smith
filt = (df['email'] == 'JohnDoe@email.com')
df.loc[filt,'last'] = 'Smith'


# In[ ]:


df


# ### UPDATING MULTIPLE ROWS

# In[ ]:


## if you wanna update all email addresses to the lower case since it has mixed casing issue.
## This is the one WAY to change multiple rows at once
df['email'].str.lower()


# In[ ]:


## but still we can see emails as mixed casing to make changes we just assign to df['email']
df


# In[ ]:


## By doing this way we can change all the rows at a single time

df['email']=df['email'].str.lower()
df


# In[ ]:


## Let's see a little more advanced to change the multiple rows: 
## FOUR POPULAR METHODS most of the people do get confused because they are very similar in what they do
## 1. APPLY 2. MAP 3. APPLYMAP 4.REPLACE


# ### 1.APPLY METHOD
# APPLY - used for calling a function on our VALUES. IT can work on either a DATAFRAME and SERIES OBJECT.
# Behaviour might be little different than what we expect for each of those different objects

# In[ ]:


## LET'S LOOK AT HOW APPLY WORKS FOR SERIES so when we use this on a series it can apply a function to every value in series
## let's see the length of all our email addresses

df['email'].apply(len)


# In[ ]:


### We can also use this to update the values.. lets create a simple function that returns uppercase version of our email
### but the function can be as complicated as you wanna be
### don't wanna put parenthesis just pass in function without parenthesis

def update_email(email):
    return email.upper()

df['email'].apply(update_email)


# In[ ]:


df['email'] = df['email'].apply(update_email)


# In[ ]:


df


# In[ ]:


### added all the above cells in a single cell to execute in a single stretch
def update_email(email):
    return email.upper()

df['email'].apply(update_email)
df['email'] = df['email'].apply(update_email)
df


# In[ ]:


### We may also see people using LAMBDA FUNCTIONs as well which means anonymous functions without a specific name 
### that we use for things like this..we can see down below that's little complicated but 
### if you are familiar and more comfortable writing regular functions then you can do that way.... 
### if you're comfortable writing LAMBDA functions then u can do this way...
### All the methods do work on numerical data as well since we are working on string data 

df['email'] = df['email'].apply(lambda x: x.lower())
df


# ### LETS LOOK AT HOW APPLY WORKS ON DATAFRAME: 

# In[ ]:


### apply method worked well for series object
df['email'].apply(len)


# In[ ]:


### But apply method doesn't work for dataframe: it's not applying length function to every value in the dataframe..it's 
### actually applying to each series in the dataframe specifically the columns i.e., first column has 3 values, second has 3
### and third column has 3 values...
df.apply(len)


# In[ ]:


### OOPS rows is the default one needless to mention!!!
### counting downwards (vertically)
df.apply(len,axis = 'rows')


# In[ ]:


### counting horizontally
df.apply(len,axis = 'columns')


# In[ ]:


### if we wanna check manually the length of the column it gives same result 
len(df['email'])


# In[ ]:


### series objects have a min method since our df has string data it gave us ALPHABETICALLY
### Obviously Numerical data makes more sense
df.apply(pd.Series.min)


# In[ ]:


### we can also use LAMBDA FUNCTION TO GET MIN VALUE OF A DATAFRAME
df.apply(lambda x: x.min())


# #### 2. APPLY MAP
# APPLY MAP works only on DATAFRAME...it applies every individual element in the dataframe...
# SERIES Object don't have APPLYMAP method

# In[ ]:


### now this built-in length function applies for each individual element in our dataframe
df.applymap(len)


# In[ ]:


### If i wanted to get our entire dataframe to lower case using LOWER FUNCTION AND APPLYMAP METHOD
df.applymap(str.lower)


# ### 3. MAP METHOD- It only works on series objects
# It is used for substituting each value in a series with another value

# In[ ]:


## i wanted to substitute two new values into first column by passing in two dictionaries into map function
## But the problem is the values which we didn't substitute that converted to NAN value which may not be what we want
df['first'].map({'Corey':'Chris','Jane':'Mary'})


# ### 4. REPLACE METHOD- It only works on series objects
# It is ALSO used for substituting each value in a series with another value without NAN values

# In[ ]:


df['first'].replace({'Corey':'Chris','Jane':'Mary'})


# In[ ]:


### Replaced Version of the dataframe
df['first'] = df['first'].replace({'Corey':'Chris','Jane':'Mary'})
df


# ## PART-06: Add/Remove Rows and Columns From DataFrames
# how to add and remove rows and columns from dataframes using the append and drop methods. 
# We will also see how we can create new columns by combining elements from existing ones. 
# Let's get started...

# In[ ]:


people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


# In[ ]:


pd.DataFrame(people)


# In[ ]:


df = pd.DataFrame(people)
df


# #### ADDING NEW COLUMN TO OUR DATAFRAME:

# In[ ]:


df['first']+' '+df['last']


# In[ ]:


df['full_name'] = df['first']+' '+df['last']
df


# #### REMOVING COLUMNS TO OUR DATAFRAME:  USING DROP METHOD

# In[ ]:


df.drop(columns = ['first','last'])


# In[ ]:


df


# In[ ]:


df.drop(columns = ['first','last'],inplace=True)
df


# ####  ADDING MULTIPLE COLUMNS FROM OUR DATAFRAME: USING string split method and expand

# In[ ]:


df['full_name'].str.split(' ')


# In[ ]:


df['full_name'].str.split(' ',expand=True)


# In[ ]:


df[['first','last']] = df['full_name'].str.split(' ',expand=True)
df


# ### ADDING single row to our dataframe : APPEND METHOD
# We may wanna add a single row to our data frame of new data and second maybe we wanna combine two dataframes together
# by single dataframe by APPENDING the rows of one to another

# In[ ]:


### TypeError: Can only append a dict if ignore_index=True
df.append({'first':'Tony'})


# In[ ]:


## Now if we pass in type error: ignore_index=True then it ran successfully without throwing an error 
df.append({'first':'Tony'},ignore_index=True)


# In[ ]:


## Passing a complete row details into our dataframe
df.append({'email':'TonyPony@email.com','full_name':'Tony Pony','first':'Tony','last':'Pony'},ignore_index=True)


# In[ ]:


people_1 = {
    "first": ["Tony", 'Steve'], 
    "last": ["Stark", 'Rogers'], 
    "email": ["IronMan@avenge.com", 'Cap@avenge.com']
}


# In[ ]:


df2 = pd.DataFrame(people_1)
df2


# In[ ]:


df.append(df2,ignore_index=True)


# In[ ]:


df


# In[ ]:


df = df.append(df2,ignore_index=True)


# In[ ]:


df


# #### NOTE: If you wanna make the changes permanent  theAPPEND METHOD doesn't have inplace = TRUE method to use
# #### istead we just have to set the dataframe to this returned data frame 
# df = df.append(df2,ignore_index=True)

# #### REMOVING ROWS IN A DATAFRAME: Using index method

# In[ ]:


df = df.drop(index=4)
df


# In[ ]:


### little more complicated way: using filters and conditionals
df.drop(index=df[df['last'] == 'Doe'].index)

## or
filt = df['last'] == 'Doe'
df.drop(index=df[filt].index)
        


# # PART-07: SORTING DATA

# In[ ]:


people = {
    "first": ["Corey", 'Jane', 'John','Adam'], 
    "last": ["Schafer", 'Doe', 'Doe','Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com','Adam@email.com']
}


# In[ ]:


import pandas as pd


# In[ ]:


df  = pd.DataFrame(people)
df


# ### sort values method

# In[ ]:


### if you wanna sort the last column in the dataframe by ascending order
df.sort_values(by='last')


# In[ ]:


### if you wanna sort the last column in the dataframe by descending order

df.sort_values(by='last', ascending=False)


# In[ ]:


### if you wanna sort the multiple columns in the dataframe in ascending order
df.sort_values(by=['first','last'])


# In[ ]:


### if you wanna sort the multiple columns in the dataframe by decreasing order
df.sort_values(by=['last','first'],ascending=False)


# In[ ]:


### if you wanna sort the one column in ascending and other column in descending order in the dataframe by passing booleans
df.sort_values(by=['first','last'],ascending=[True,False])


# In[ ]:


### to make permanent changes
df.sort_values(by=['last','first'],ascending=[False,True],inplace=True)
df


# In[ ]:


df['last'].sort_values()


# #### SORT INDEX METHOD: SET BACK TO THE DATA  how it was before

# In[ ]:


##If we wanna set this back to how it was before we can simply use SORT INDEX METHOD
df.sort_index()


# ####  SORTING SINGLE COLUMN OR SERIES OBJECT IN A DATAFRAME

# In[ ]:


### usindg sort values method
df['first'].sort_values()


# # Part 8: Grouping and Aggregating - Analyzing and Exploring Your Data
# -- Aggregating means combining multiple pieces of data into a single result ex: Mean, Median and Mode are aggregate functions
# because they take Multiple values and gives us either mean,median or mode of those results
# 
# -- GroupBy Function in the pandas documentation it says that groupby operation involves some combination of the
#    SPLITTING THE OBJECT    APPLYING A FUNCTION   & COMBINING A RESULTS
# 

# In[ ]:


df['Country']


# In[ ]:


### Majority of this survey was answered by the United States of America and in second place Germany, 
### third place Indian and  so on & so forth 

df['Country'].value_counts()


# In[ ]:


### Now WE look at how to use the group by function on our country column
### Firstly we're going to SPLIT THE FUNCTION and then We're gonna APPLY A FUNCTION and then It'll COMBINE THOSE RESULTS

df.groupby(['Country'])


# In[ ]:


### Now set this to a variable so that we can reuse this and not have to retype our code over and over 
### and also easier to read

country_grp = df.groupby(['Country'])


# In[ ]:


### Let's grab the group for USA by using GET_GROUP METHOD
### doesnt look like anything special yet but if i look at the country name for each of these survey results are from USA
country_grp.get_group('United States of America')


# In[ ]:


country_grp.get_group('India')


# In[ ]:


#### This would be similar to RUNNING A FILTER on our dataframe so I shoul be able to 
#### get the same results for a single country

filt = (df['Country'] == 'United States of America')
df.loc[filt]


# In[ ]:


### If we wanna know that What are the Top most languages have worked with by USA using FILTER METHOD
### we are applying value count method on filt variable

filt = (df['Country'] == 'United States of America')
df.loc[filt]['LanguageHaveWorkedWith'].value_counts()


# In[ ]:


### If we wanna know that What are the Top most languages have worked with by INDIA using FILTER METHOD
### we are applying value count method on filt variable

filt = (df['Country'] == 'India')
df.loc[filt]['LanguageHaveWorkedWith'].value_counts()


# In[ ]:


### For that country group we wanna look at top languages that they have worked with
### this actually cuts off a little early
country_grp['LanguageHaveWorkedWith'].value_counts()


# In[ ]:


### For that country group we wanna look at top languages that they have worked with
### This actually returing a series and this series has a  multiple indexes it has Country and LanguageHaveWorkedWith indexe

country_grp['LanguageHaveWorkedWith'].value_counts().head(50)


# In[ ]:


### if you are interested to know specific countries we can just simply use loc method
country_grp['LanguageHaveWorkedWith'].value_counts().loc['India']


# In[ ]:


#### If you wanna look at PERCENTAGE RESULTS instead of raw numbers using NORMALIZE
country_grp['LanguageHaveWorkedWith'].value_counts(normalize = True).loc['India']


# In[ ]:


#### Now Lets see how we can do AGGREGATE functions like Mean, MEDIAN,and things like that on Specific Countrygroup and 
### we did calculated median on entire survey dataframe before but now lets look at country group

country_grp['ConvertedCompYearly'].median()


# In[ ]:


### If you wanna see MEDIAN SALARY IN place like GERMANY
country_grp['ConvertedCompYearly'].median().loc['Germany']


# In[ ]:


### If you wanna know MEDIAN AND MEAN FOR THE COUNTRIES we use AGG METHOD
country_grp['ConvertedCompYearly'].agg(['median','mean'])


# In[ ]:


### If you wanna know MEDIAN AND MEAN FOR THE Specific COUNTRy we use AGG METHOD

country_grp['ConvertedCompYearly'].agg(['median','mean']).loc['India']


# In[ ]:


### If you wanna know the SPECIFIC country who specifically worked with Python USING STRING METHOD

filt = (df['Country'] == 'United States of America')
df.loc[filt]['LanguageHaveWorkedWith'].str.contains('Python')


# In[ ]:


### If you wanna know the SPECIFIC country who specifically worked with Python USING STRING METHOD
### If you wanna total number of respondents who worked with Python Using SUM METHOD
### Sum Method not only works with Numerical but also works with Boolean Values(True 1 or False 0)

filt = (df['Country'] == 'United States of America')
df.loc[filt]['LanguageHaveWorkedWith'].str.contains('Python').sum()


# In[ ]:


filt = (df['Country'] == 'India')
df.loc[filt]['LanguageHaveWorkedWith'].str.contains('Python').sum()


# In[ ]:


country_grp['LanguageHaveWorkedWith'].str.contains('Python').sum()


# In[ ]:


### We can resolve above issue by using APPLY METHOD and LAMBDA FUNCTION

country_grp['LanguageHaveWorkedWith'].apply(lambda x: x.str.contains('Python').sum())


# #### Q: What % of People from each country Know Python?
#  1. find out Total Number of Respondants/People from each country
#  2. Total Number of People from each Country who Knows Python 
#  3. combine these two variable by creating nother variable using CONCAT function

# In[ ]:


### Let's find out Total Number of Respondants/People from each country
country_respondents  = df['Country'].value_counts()
country_respondents


# In[ ]:


### Total Number of People from each Country who Knows Python 

country_uses_python = country_grp['LanguageHaveWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
country_uses_python


# In[ ]:


#### Now lets combine these two variable by creating nother variable using CONCAT function

python_df = pd.concat([country_respondents,country_uses_python],axis='columns',sort=False)
python_df


# In[ ]:


#### Now lets combine these two variable by creating nother variable using CONCAT function 
#### And also rename the object names to look more specific

python_df.rename(columns={'Country':'NumRespondents','LanguageHaveWorkedWith':'NumKnowsPython'})


# In[ ]:


python_df.rename(columns={'Country':'NumRespondents','LanguageHaveWorkedWith':'NumKnowsPython'},inplace=True)
python_df


# In[ ]:


#### Now we have total no.of people from each country and total no.of people who knows Python in each country in one df
#### So we have all the information we need to calculate a Percentage
#### All we need to do is to create a column and calculate it.

python_df['PerKnowsPython'] = (python_df['NumKnowsPython']/python_df['NumRespondents'])*100
python_df


# #### Q1.  Sort the countries by largest percentage of respondents
# 

# In[ ]:


python_df.sort_values(by='PerKnowsPython',ascending=False)


# In[ ]:


python_df.sort_values(by='PerKnowsPython',ascending=False,inplace=True)
python_df


# In[ ]:


### If you wanna look at specific country 
### we get specific statistcs for that country

python_df.loc['India']


# #### Q2: What is the most common Education Level for the people who answered survey?

# In[ ]:


df['EdLevel']


# In[ ]:


Common_EdLevel = df['EdLevel'].value_counts(ascending=False)
Common_EdLevel


# # Part 9: Cleaning Data - Casting Datatypes and Handling Missing Values
# we will be learning how to clean our data. We will be learning how to handle and remove missing values, fill missing values, cast datatypes, and more. This is an essential skill in Pandas because we will frequently need to modify our data to our needs. 
# 
# -- Every dataset that we are going to be working with is likely gonna have missing data or data that we'd to like to clean up 
# or convert to a different datatype
# 

# ### Lets talk about how to drop MISSING VALUES

# In[16]:


import pandas as pd
import numpy as np


# In[17]:


people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}


# In[18]:


df=pd.DataFrame(people)
df


# #### a) DROPNA METHOD
# 
#  -- We will remove missing values by using DROPNA method
#  -- dropna will use default arguments in the background

# In[19]:


### We will remove missing values by using DROPNA method
### But we do have custom missing values that wont get dropped

df.dropna()


# In[20]:


## we will be getting same results by passing arguments like axis='index',how='any'
## if the axis = index which means row and how method means it is a condition how you want to drop the values(any,all)
## down below rows 3,4, and 5 were dropped because of missing values

df.dropna(axis='index',how='any')


# In[21]:


## if the axis = index which means row and how method means it is a condition how you want to drop the values(all)
## down below rows 4 were dropped because of all  missing values in the row but row 5 has email id so its not dropped

df.dropna(axis='index',how='all')


# In[22]:


## if the axis = columns  and how = all then it didn't drop the column becuase no column has all missing values

df.dropna(axis='columns',how='all')


# In[23]:


## if the axis = columns  and how = any then it will drop all columns becuase 4th column has all missing values(nan,none)
## which is an empty data so it gives empty dataframe

df.dropna(axis='columns',how='any')


# #### USING SUBSET ARGUMENT

# In[24]:


### USING SUBSET argument
### It's fine if they don't have first name or last name but we really need email address and 
### if they don't have an email address then we need to just drop those rows
### doesn't matter if we use any or all output remains same
### In order to this just use subset argument with the list or just a series object

### it drops rows 3,4 bcoz it has missing values
### it ain't dropped 5 even if it has first name as None and Last name as Nan bcoz that row has email address
### row 6 has customized sample we will discuss later

df.dropna(axis='index',how='any',subset=['email'])


# In[25]:


df.dropna(axis='index',how='all',subset=['email'])


# In[26]:


### we bothered having missing values in email but aint bothered in first name column
### row3 has email address none so it dropped
### row4 last name has Nan so it dropped
### row5 last name has Nan so it dropped

### if you wanna set the modified dataframe as permanent just passin argument inplce = True

df.dropna(axis='index',how='any',subset=['email','last'])


# ### b) CUSTOM MISSING VALUES:

# In[27]:


import pandas as pd
import numpy as np


# In[28]:


people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}


# In[29]:


df = pd.DataFrame(people)

df.replace('NA',np.nan,inplace=True)
df.replace('Missing',np.nan,inplace=True)


# In[30]:


df


# In[31]:


###LET'S run all the similar lines of code which we ran above and find out difference::

df.dropna()


# In[32]:


df.dropna(axis='index',how='any')


# In[33]:


df.dropna(axis='index',how='all')


# In[34]:


df.dropna(axis='columns',how='all')


# In[35]:


df.dropna(axis='columns',how='any')


# In[36]:


df.dropna(axis='index',how='any',subset=['email'])


# In[37]:


df.dropna(axis='index',how='all',subset=['email'])


# In[38]:


df.dropna(axis='index',how='all',subset=['email','last'])


# In[39]:


df.dropna(axis='index',how='any',subset=['email','last'])


# #### ISNA METHOD
# isna method is used to get a MASK OF VALUES as to whether or not these classify as na or not

# In[40]:


df.isna()


# In[41]:


### SINCE WE ARE WORKING ON STRNG DATA SO WE'VE PASSED STRING VALUE
### IF YOU'RE WORKING ON NUMERICAL DATA THEN PASS 0 OR -1

df.fillna('MISSING')


# In[42]:


### if you want those changes to be permanent and just simply add that inplace argument by setting it to True

df.fillna(0)


# In[43]:


df.dtypes


# In[44]:


### since age is an Object(which means string or mix of different th)
df['age'].mean()


# In[45]:


### lets see what is the nan datatype 
type(np.nan)


# #### CASTING : Using ASTYPE

# In[46]:


###CHANGE DATATYPE OBJECT TO FLOAT SINCE DATAYPE OF NAN IS FLOAAAAAT if you change to int it will throw an error
df['age']=df['age'].astype(int)


# In[47]:


### Now age data type is converted to float from object dtype
df['age']=df['age'].astype(float)


# In[59]:


### when we check datatypes of columns age column is converted to FLOAT

df.dtypes


# In[58]:


### Now we can calculate average of age

df['age'].mean()


# In[ ]:


### WE can aslo convert all the columns at a single time but we have mixed columns like strings and numerical 
### so it won't work for us.

df.astype(float)


# In[ ]:





# In[ ]:




