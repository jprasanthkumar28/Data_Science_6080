#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests


# In[17]:


request = requests.get("https://en.wikipedia.org/wiki/Harvard_University")


# In[18]:


request


# In[20]:


type(request)


# In[21]:


dir(request)


# In[22]:


pageText = request.text
pageText


# In[24]:


from bs4 import BeautifulSoup


# In[25]:


bs_soup = BeautifulSoup(pageText, 'html.parser')


# In[26]:


bs_soup


# In[27]:


type(bs_soup)


# In[28]:


print(bs_soup.prettify())


# In[29]:


"title" in dir(bs_soup)


# In[30]:


len(bs_soup.find_all("p"))


# In[32]:


#finding the class attribute and also can find the class of a single element
bs_soup.table["class"]


# In[33]:


#checking all the tables that have class attributes
[each["class"] for each in bs_soup.find_all("table") if each.get("class")]


# In[34]:


#the above code is similar to 
result = []
for each in bs_soup.find_all("table"):
    if each.get("class"):
        result.append(each["class"])
result


# In[35]:


#displaying content of a particulat table
tableText = str(bs_soup.find_all("table","wikitable")[2])


# In[36]:


from IPython.core.display import HTML
HTML(tableText)


# In[37]:


#extracting tr elements 
rows = [row for row in bs_soup.find_all("table","wikitable")[2].find_all("tr")]
rows


# In[43]:


#lambda expression basically replaces a character in string
"Lambda Expression"
string = lambda s:s.replace("\n","")


# In[44]:


"Function"
#functions in python
def product(a,b):
    return a*b;
product(10,5)


# In[45]:


#no argument functions
def printName():
    return "Prashu"
print(printName())


# In[46]:


#functions with default parameters. It can be called with both the values and also single value if other parameters
#are defaultly given
def defaultValues(x,y=1):
    return x*y
print(defaultValues(2))
print(defaultValues(2,3))


# In[47]:


#if multiple default values
def multipleDValues(x,y="Sum is",z=1):
    print(y, x+z)
multipleDValues(2)
multipleDValues(2, "Sum of two numbers", 4)


# In[48]:


def printAll(name, *listV):
    print(name, "has the following values:")
    for i in listV:
        print(i)
    print
        
printAll("List", 80, 4, 5)
printAll("List", 123)
printAll("List")


# In[51]:


def printAll(name, **listV):
    print(name, "has the following values:")
    for i in listV:
        print(i, ":", listV[i])
    print
printAll("List", ONE=1, TWO=2, THREE=3)


# In[52]:


columns = [string(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
columns


# In[53]:


indexes = [string(row.find("th").get_text()) for row in rows[1:]]
indexes


# In[54]:


#in original table also have the same rows attributes
HTML(tableText)


# In[55]:


to_num = lambda s: s[-1] == "%" and int(s[:-1]) or None


# In[56]:


#getting the values of the columns
values = [to_num(string(value.get_text())) for row in rows[1:] for value in row.find_all("td")]
# values = [to_num(value.get_text()) for row in rows[1:] for value in row.find_all("td")]
values


# In[57]:


#arranging the value of each row in tupples
stacked_values = zip(*[values[i::3] for i in range(len(columns))])
list(stacked_values)


# In[58]:


#lets check with the table
HTML(tableText)


# In[59]:


#while passing parameter to a function we can pass any type
def exampleParameter(a,b,c):
    print(a,b,c)
exampleParameter(1,2,3)
exampleParameter([1,2], [3,4], [5,6])


# In[60]:


List = [1,2,3]
a = List[0]
b = List[1]
c = List[2]
exampleParameter(a,b,c)


# In[61]:


a1,a2,a3 = List
exampleParameter(a1,a2,a3)


# In[62]:


#can also send the address of the variable
exampleParameter(*List)


# In[64]:


import pandas as panda


# In[65]:


stacked_values = zip(*[values[i::3] for i in range(len(columns))])
pText = panda.DataFrame(stacked_values, columns=columns, index=indexes)
pText


# In[66]:


#converting into key value pair
columns = [string(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
stacked_values = zip(*[values[i::3] for i in range(len(columns))])
data_dicts = [{col: val for col, val in zip(columns, col_values)} for col_values in stacked_values]
data_dicts    


# In[67]:


panda.DataFrame(data_dicts, index=indexes)


# In[68]:


#lets write the value in column wise
stacked_colValues = [values[i::3] for i in range(len(columns))]
stacked_colValues


# In[69]:


#lets write in key as rows name and values as list
data_lists = {col: val for col, val in zip(columns, stacked_colValues)}
data_lists


# In[70]:


panda.DataFrame(data_lists, index=indexes)


# In[71]:


pText.dtypes


# In[72]:


#dropping the column with null values
pText.dropna()


# In[73]:


#let us drop the column that has null value
pText.dropna(axis=1)


# In[74]:


#instead of dropping the values let us manually keep the value as zero
pTextOpti = pText.fillna(0).astype(int)
pTextOpti


# In[75]:


pTextOpti.dtypes


# In[76]:


#finding some of the insights from table
pTextOpti.describe()


# In[77]:


import numpy as nump


# In[78]:


#geeting row wise values using numpy
pTextOpti.values


# In[79]:


#checking for the type
type(pTextOpti.values)


# In[80]:


#calculating mean for a particular column
nump.mean(pTextOpti.Undergrad)


# In[81]:


nump.std(pTextOpti)


# In[82]:


#geting the values of a undergrad as a dict table
pTextOpti["Undergrad"]


# In[83]:


#can also be written as
pTextOpti.Undergrad


# In[84]:


#getting the values of a particular row w.r.t column
pTextOpti.loc["Asian/Pacific Islander"]


# In[85]:


#also as. iloc[index] will give required column
pTextOpti.iloc[0]


# In[86]:


#below also serves the same
pTextOpti.ix["Asian/Pacific Islander"]


# In[87]:


pTextOpti.ix[0]


# In[88]:


#finding the value of a row at particular column 
pTextOpti.loc["White/non-Hispanic", "Graduate"]


# In[89]:


pTextOpti.ix[3, "Graduate"]


# In[90]:


pTextOpti.loc[3, 1]


# In[91]:


#displaying in order instead of table naming the columns individually
sequenceTable = pTextOpti.stack().reset_index()
sequenceTable.columns = ["race", "source", "percentage"]
sequenceTable


# In[92]:


#grouping the data as per the race
groupedData = sequenceTable.groupby("race")
groupedData.groups


# In[93]:


#checking the type
type(groupedData)


# In[95]:


#calculating the mean of each race in the table
meanTable = groupedData.mean()
meanTable


# In[96]:


#checking for the type
type(meanTable)


# In[97]:


#printing the groups individually
for name, group in sequenceTable.groupby("source", sort=True):
    print(name)
    print(group)


# In[98]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[100]:


#plotting the mean of each race
meanTable.plot(kind="bar",color = "black");


# In[ ]:




