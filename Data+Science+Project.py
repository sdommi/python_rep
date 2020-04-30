
# coding: utf-8

# In[144]:

import pandas as pd


# In[145]:

train = pd.read_csv("C:\\Users\\owner\\Desktop\\Titanic_Data\\train.csv")


# In[146]:

len(train)


# In[147]:

train.shape


# In[148]:

train.describe().round(2)


# In[149]:

train.style.highlight_max()


# In[150]:

train.sample()


# In[151]:

###Basic Visualization:crosstab,countplot,factorplot


# In[152]:

import seaborn as sbn


# In[153]:

df = pd.read_csv("C:\\Users\\owner\\Desktop\\Titanic_Data\\train.csv")


# In[154]:

##Work on crosstab


# In[155]:

df.columns


# In[156]:

pd.crosstab(df['Sex'],df['Survived'])


# In[157]:

df.head(20)


# In[158]:

###Check the Survived rate by age


# In[159]:

pd.crosstab(df['Age'],df['Survived'])


# In[160]:

##Check the Survived rate based upon Class


# In[161]:

pd.crosstab(df['Pclass'],df['Survived']) 


# In[162]:

###Basic visualization 


# In[163]:

import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt


# In[164]:

ax = sbn.countplot(x='Sex',hue='Survived',palette='Set1',data=df)
ax.set(title="Survivors According to Sex",xlabel="Sex",ylabel="Total")
plt.show()


# In[165]:

sbn.factorplot(x='Pclass',y='Survived',hue='Sex',data=df,aspect=0.9,size=3.5)


# In[166]:

plt.show()


# In[167]:

### 4 types of C's Machine Learning
"""
correcting--Update the vakues(corrct the age)
completing--Fill the Null values
Creating(Feature Enf=gineering, Means based on titles, we predict the gender)
Converting--Everything should be convert into Numbers
"""
### Basic Data Types in Data Science
"""
Dependent Vs Independent(Ex: Calucate the Survival rate(Dependent) based on Gender(Independent))
Categorical(Nominal(Order doesn't matter jut type like male or female or apple or pear) and Ordinal(Order is mater like percentage))
Numerical(Descret(Kind of Whole Number Ex: Throwing a dice get the some number ) and Continuos(Ex: Person height,speed of the car..))

"""


# In[168]:

###Example of one of the C : Creating(Feature ENgineering)


# In[169]:

train.columns


# In[170]:

train['Name'].sample(20)


# In[171]:

def get_titles(name):
    if '.' in name:
        return name.split(',')[1].split('.')[0].strip()
    else:
        return "No Titles"


# In[172]:

titles = set([x for x in train.Name.apply(lambda x:get_titles(x)) ])

print(titles)
# In[173]:

titles


# In[174]:

print(titles)


# In[175]:

train['Titles']=df['Name'].map(lambda x:get_titles(x))


# In[176]:

train


# In[177]:

train['Titles'].value_counts()


# In[178]:

def shorter_titles(x):
    title = x["Titles"]
    if title in ['Rev', 'Miss', 'Major', 'Capt', 'Master', 'Jonkheer']:
        return "Royality"
    elif title in ['Don', 'Col', 'the Countess']:
        return "oficer"
    elif title in ['Mlle', 'Mme', 'Mr']:
        return "Mr"
    else:
        return title
        


# In[179]:

train['Titles']=train.apply(shorter_titles,axis=1)


# In[180]:

train


# In[181]:

train['Titles'].value_counts()


# In[182]:

##Example of c: Completing


# In[213]:

train = pd.read_csv("C:\\Users\\owner\\Desktop\\Titanic_Data\\train.csv")


# In[185]:

train


# In[214]:

type(train)


# In[215]:

for column in train:
    print(column)


# In[216]:

for column in train:
    print(column ,":",train[column].isnull().sum())


# In[193]:

##NOte : Now we are filling the null values
## first fill the null of age with median of age


# In[217]:

train['Age'].median()


# In[218]:

train["Age"].fillna(train['Age'].median(),inplace=True)


# In[219]:

for column in train:
    print(column,":",train[column].isnull().sum())


# In[220]:

##Check what kind of data in Embarked  and fill witn it


# In[222]:

train['Embarked'].value_counts()


# In[223]:

train['Embarked'].fillna('S',inplace=True)


# In[224]:

for column in train:
    print(column,":",train[column].isnull().sum())


# In[229]:

## Delete the column of cabi since lot of nulls'
##Also delete the name column


# In[232]:

#del train['Cabin']
del train['Name']


# In[233]:

for column in train:
    print(column)


# In[234]:

train


# In[235]:

####Now one of the  C's example: COnverting to Numbers


# In[236]:

##Let's COnvert the sex (male,female to (0,1))


# In[237]:

train.Sex.replace(('male','female'),(0,1),inplace=True)


# In[238]:

train


# In[239]:

##also replace Embarked convert into Numbers


# In[240]:

train.Embarked.replace(('S','C','Q'),(0,1,2),inplace=True)


# In[ ]:




# In[241]:

train


# In[243]:

###Now One of the example of C's to correcting the data

df = pd.read_csv("C:\\Users\\owner\\Desktop\\Titanic_Data\\train.csv")


# In[244]:

df.head()


# In[252]:

graph = sbn.FacetGrid(df,col="Survived")
graph.map(plt.hist,"Fare",bins=20)


# In[253]:

plt.show()


# In[251]:

df.loc[df['Fare']>400,"Fare"]=1000 #df['Fare'].median()


# In[254]:

##Check any problems to correc the age


# In[256]:

graph_age = sbn.FacetGrid(df,col="Survived")
graph_age.map(plt.hist,"Age",bins=20)


# In[257]:

plt.show()


# In[ ]:



