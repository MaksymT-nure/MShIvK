import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

train=pd.read_csv(r'C:\Users\Admin\Documents\Pandas\train.csv')
df=train.copy()

print("Head:")
print(df.head(),"\n\n")
print("Tail:")
print(df.tail(),"\n\n")
print("Shape:", df.shape,)
print("Columns:", list(df.columns),"\n\n")
print("Index:", df.index,"\n\n")
print("Pclass value counts:")
print(df['Pclass'].value_counts(),"\n\n")


print("Describing", df.describe())


df_empty=pd.DataFrame()
df_empty.head()


student_dict={'Name':['A','B','C'],'Age':[24,18,17],'Roll':[1,2,3]}
df_student=pd.DataFrame(student_dict).reset_index(drop=True)
print(df_student.head(),"\n\n\n\n")


print("Head:")
print(df.head(),"\n\n")


print("Nulls:")
print(df.isnull().sum(),"\n\n")


print("on a particular column Age - ",df['Age'].isnull().sum())


df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Age'].isnull().sum()
df['Sex'].fillna(df['Sex'].mode(),inplace=True)
df['Sex'].isnull().sum()


print("Head:")
print(df.head(),"\n\n")
df['Sex']=df['Sex'].map({"male":'0',"female":"1"})
print("Modified:")
print(df.head(),"\n\n")


df['last_name']=df['Name'].apply(lambda x: x.split(',')[0])
df['first_name']=df['Name'].apply(lambda x: ' '.join(x.split(',')[1:]))
print("Added first names and surnames:")
print(df.head(),"\n\n")


print("Added category:")
df['Third&Men']=df.apply(lambda row: int(row['Pclass']==3 and row['Sex']=="0"),axis=1)
print(df.head(),"\n\n")


def findAgeGroup(age):
    if age<18:
        return 1
    elif age>=18 and age<40:
        return 2
    elif age>=40 and age<60:
        return 3
    else:
        return 4
df['Age_group']=df['Age'].apply(lambda x: findAgeGroup(x))
print("Added age groups:")
print(df.head(),"\n\n")

df=df.drop(['PassengerId'],axis=1)
print("Deleted passenger ids:")
print(df.head(),"\n\n")


df=df.rename(columns={'Sex':'Gender','Name':'Full Name','last_name':'Surname','first_name':'Name'})
print("Renamed columns:")
print(df.head(),"\n\n\n\n")

print("Slicing DataFrame p1")
print(df.head(),"\n\n")


print("All rows with pclass==3")
df_third_class=df[df['Pclass']==3].reset_index(drop=True)
print(df_third_class.head(),"\n\n")


print("Females with age > 60")
df_aged=df[(df['Age']>60) & (df['Gender']=="1")]
df_aged.head()
print(df_aged.head(),"\n\n")


print("Selecting some columns")
df1=df[['Age','Pclass','Gender']]
print(df1.head(),"\n\n")


print("Select numerical columns only")
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
df_num = df.select_dtypes(include=numerics)
print(df_num.head(),"\n\n")

print("Categorical columns")
df_cat=df.select_dtypes(include=['object'])
print(df_cat.head(),"\n\n\n\n")


print("Slicing dataframe p2")
print(df.head(),"\n\n")


print("First 100 rows & all columns")
df_sub1=df.iloc[0:100,:]
print(df_sub1.head(),"\n\n")


print("First 250 rows with a subset of columns")
df_sub2=df.iloc[:250,[1,8]]
print(df_sub2.head(),"\n\n")


print("loc")
print(df.head(),"\n\n")


print("Gender and age of age >50")
df_sub4=df.loc[(df['Age']>50),['Gender','Age']]
print(df_sub4.head(),"\n\n")

row=dict({'Age':24,'Full Name':'Peter','Survived':'Y'})
df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)


print("Added row")
print(df.tail(),"\n\n")


print("Deleting last row")
df=df.drop(df.index[-1],axis=0) # Deletes last row
print(df.head(),"\n\n")


print("Sorting by age say in decreasing order")
df=df.sort_values(by=['Age'],ascending=False)
print(df.head(),"\n\n")


print("Joins")

sno=[i+1 for i in range(100)]
marks=np.random.randint(100,size=100)
print(len(marks))
marks_df=pd.DataFrame({'Sno':sno,'Marks':marks})
print(marks_df.head())


sno=[i+1 for i in range(100)]
age=np.random.randint(100,size=100)
print(len(marks))
age_df=pd.DataFrame({'Sno':sno,'Age':age})
print(age_df.head())

print("Cross")
cross_join=pd.merge(marks_df,age_df,how='cross')
print(cross_join.shape)
print(cross_join.head())



print("Inner")
inner_join=pd.merge(age_df,marks_df,how='inner',on='Sno')
print(inner_join.shape)
print(inner_join.head())


print("ADding some rows")
age_df.loc[len(age_df.index)]={'Sno':101,'Age':23}
age_df.loc[len(age_df.index)]={'Sno':102,'Age':27}
age_df.loc[len(age_df.index)]={'Sno':104,'Age':29}
age_df.loc[len(age_df.index)]={'Sno':103,'Age':32}
age_df.loc[len(age_df.index)]={'Sno':105,'Age':53}


print("Left")
left_join=pd.merge(age_df,marks_df,how='left',on='Sno')
print(left_join.shape)
print(left_join.tail())


print("Right")
right_join=pd.merge(marks_df,age_df,how='right',on='Sno')
print(right_join.shape)
print(right_join.tail())


print("Full outer")
out_join=pd.merge(marks_df,age_df,how='outer',on='Sno')
print(out_join.shape)
print(out_join.tail(10),"\n\n\n\n")


print("groupby","\n")
print(df.head(),"\n\n")

print("Only class 3")
groups=df.groupby(['Pclass'])
print(groups.get_group(3),"\n\n")


print("Avg age oer class")
df_grp1=df.groupby(['Pclass'])
print(df_grp1['Age'].mean(),"\n\n")

print("Min&max age")
print(df_grp1['Age'].min(),"\n\n")
print(df_grp1['Age'].max(),"\n\n")

print("Age count")
print(df_grp1['Age'].count(),"\n\n")


print("Using agg() function","\n")
df=train.copy()
print(df.head(),"\n\n")

print("Average per Pclass using 'agg' this time")
df_grp2=df.groupby(['Pclass']).agg({'Age':lambda x: np.mean(x)})
print(df_grp2.head(),"\n\n")

print("Min/Max,count,Sum for each Pclass usign agg function")
df_grp3=df.groupby(['Pclass']).agg({'Age':'min'}).rename(columns={'Age':'Min Age'})
print(df_grp3.head(),"\n\n")

print("Names of all the pasengers in that class.")
df_grp4=df.groupby(['Pclass']).agg({'Name':lambda x:', '.join(x)})
print(df_grp4.head(),"\n\n")








