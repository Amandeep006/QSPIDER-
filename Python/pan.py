# import pandas as pd

# # a=pd.Series([3,5,2], index=['a','b','c'])
# # print(a)




# data ={
#     "Name": ["AMANDEEP","NIKHIL SHARMA ","RAHUL"],
#     "ROLL_NO":[1,2,3],
#     "CLASS":["I","II","III"]
# }

# df=pd.DataFrame(data)
# # print(df)
# # print(data["Name"])
# # print(df["Name"]) # we are printing some column 
# # print(df["Name"][::-1]) # we will reverse the whole table using slcing and indexing methods.

# # print(df["ROLL_NO"])
# # help(pd.Series.loc)


# """ADD THE NEW COLUMN IN THE EXISTING DATABASE"""
# df["Course"]=["btech","bpharma","Nan"]
# # df["mobile"] = [1315,246464,231654]
# # df["Age"]=[12,35,68]
# # print(df)

# # df["Fees"]=["25k","30k","90k"]

# # print(df)

# """To read the csv file."""

# # tips=pd.read_csv("https://raw.githubusercontent.com/Taj1920/Data-Analysis-Datasets/refs/heads/main/Datasets-Practice/Dataset%20.csv")

# # print(tips["Restaurant ID"])

# # ama=pd.read_csv("https://github.com/Taj1920/Data-Analysis-Datasets/blob/main/Datasets-Practice/amazon_fires.csv",encoding="ISO-8859-1")
# # print(ama)

# # var.head() :- it is used to print the top five rows of the table 
# # var.tail() :- it is used to print all the last five rows of the table. 
# # var.info() :- it is used to fetch the information from the table.
# # var.describe() :-  it retuns statiscal information about dataframe and it will work only in numeric columns.



# # f=df.info()
# # print(f)

# d=df.describe()
# print(d)


"""*************************************************************************************************************"""

import pandas as pd
import numpy as np
# labels=['a','b','c']
# datas=[10,20,30]
# arr=np.array(datas)
# d={
#     'a':10,
#     'b':20,
#     'c':30
# }

# print(f"Labels : {labels}")
# print(f"Data : {datas}")
# print(f"Dictionary : {d}")

"""Series : It is a one dimesional array with index , it stores a single column and row of data in a dataframe."""
# s1=pd.Series(data=datas)
# print(s1)

# s2=pd.Series(data=datas, index=labels )
# print(s2)

# s3=pd.Series(arr, labels)
# print(s3)

# s4=pd.Series(d)
# print(s4)


"""DataFrame : It is a tabular spreedsheet like structure representing rows each of which contains one or multiple columns.
1D array- Series
2D array - DataFrame
"""
matrix_data=np.random.randint(1,20,size=20).reshape(5,4)
row_labels=['A','B','C','D','E']
column_headings=['W','X','Y','Z']

# df=pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)
# print(f"\n The data frame looks like :\n{df} ")

# d={
#     'a':[10,20], 
#     'b':[30,40],
#     'c':[50,60]  
#    }

# df2=pd.DataFrame(data=d, index=['X','Y'])
# print(df2)

matrix=np.random.randint(10,100,size=20).reshape(5,4)
# dbe=['a','d','f','g','n']
# clm=['w','e','r','t']

# df=pd.DataFrame(data=matrix,index=['a','d','f','g','n'],columns=['w','e','r','t'])
# print(df)


df3 = pd.read_csv("SQL\EMP_Table.csv")
# print(df3)

# head() : It is used to print top 5 rows 
# print(df3.head())
# tail() : It is used to print last 5 rows
# print(df3.tail())
# sample() : It is used to get sample data or only one random row.
# print(df3.sample())
# info() : It is used to provide the information about the dataset with the description of datatype of column.
# print(df3.info())
# describe() : It is used to describe the whole dataset while some statistical data.
# print(df3.describe())
# print(df3.describe().transpose())

# print(df3.transpose()) # transpose(): It is used to transpose the table which means rows convert into column and vice-versa.



"""Basic descriptive statistics on a DataFrame"""
# mean ()
# std ()
# var()
# min() and max()

"""Indexing, Slicing columns and rows of a DataFrame."""
# print("\n The 'EName_column \n","-"*25, sep=" ") # sep=" " defines the separator character used between multiple items printed in a single 

# print(df3["ENAME"][0:9])

# print(f"\n Type of the column {type (df3["ENAME"])}",sep=" ")

# print(f"THe 'Ename' and 'Salary' columns indexed by passign a list \n", "-"*50,sep=" ")
# print(df3[["ENAME","SAL","COMM"]])


# loc():- it is used to access a group of rows and columns in a DataFrame using labels or a boolean array.
# iloc() :- It is used to access a multiple group of rows and columns in a DataFrame labels or a boolean array.
# print(df3.loc["ENAME"])


""" CONDIITIONAL SUBSETTING """
# print(df3[df3["SAL"]>2530])
# print(df3[(df3["SAL"]>800) & (df3["SAL"]<8000)])

# print(df3["SAL"].std())
# print(df3["SAL"].mean())
# print(df3["SAL"].min())
# print(df3["SAL"].max())

# we can perform many operations in this datasets using pandas library.

"""Create a new columns as a function of mathematical operations on existing columns."""

"""Sum of two columns and assign to new column"""
# df3["SWC"]=df3["SAL"]+df3["COMM"]
# df3["SWC"]=df3[["SAL","COMM"]].sum(axis=1) # it sum both tha table 
# print(df3)

# Sorted by values :
# print(df3.sort_values(by="SWC"))

# Use "inplace=True" to make the changes reflected on the original DataFrame.
# print(df3.sort_values(by="SWC",inplace=True))
# print(df3)

# print(df3[df3["SAL"]>2000])
print(df3[df3["ENAME"]=="SMITH"])