import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as pl
import seaborn as sns
import plotly.express as px
from PIL import Image

# adding image 
image3 = Image.open(r'C:\Users\User\Desktop\stroke.png')
st.image(image3)

# reading data
stroke = pd.read_csv(r'C:\Users\User\Desktop\healthcare-dataset-stroke-data.csv')
stroke1 = pd.read_csv(r'C:\Users\User\Desktop\file_stroke.csv')

st.title('Stroke Analysis')
st.header('explaning the data')

st.write('In this project we analysis a data about having stroke.')

# create box for showing data
if st.checkbox('show the data'):
   st.write('The Data is:')
   st.write(stroke.head(5))

# creat box for showing more info
if st.button('More information'):
   st.write('Shape of our data is:',stroke.shape)
   st.write('Columns are:',stroke.columns)
   st.write('How many type every columns?',stroke.nunique())


# basic info about data
st.subheader('Details about our data:')
hadstroke = stroke[stroke['stroke']==1]
hadntstroke = stroke[stroke['stroke']==0]
st.write('total number of persons are: ' , len(stroke))
st.write('number of people who had stroke are: ' ,len(hadstroke) )
st.write('number of people who hadnot stroke are: ' ,len(hadntstroke) )


# countplot for some items
opt= st.sidebar.radio('Data visualisation (Count of the items)' , options=('number of the each type of the gender','number of the each type of the work',
                                                                           'number of the each type of smoking status'))
if opt == 'number of the each type of the gender': 
   st.write('number of the each type of the gender:')
   fig= plt.figure(figsize=(8,6))
   a=stroke.gender.value_counts().plot.barh(color='pink')
   st.write(fig)
elif opt == 'number of the each type of the work':
   st.write('number of the each type of the work type :')
   fig= plt.figure(figsize=(8,6))
   b=stroke.work_type.value_counts().plot.barh()
   st.write(fig)
else:
   st.write('number of the each type of the smoking status :')
   fig= plt.figure(figsize=(8,6))
   c=stroke.smoking_status.value_counts().plot.barh(color='green')
   st.write(fig)

# showing the count in details
st.subheader('comparing the items')
names_crosstab = ['gender and smoking status' , 'gender and work type' , 'gender and Residence_type' , 'working type and smoking status']
crossing = st.radio('compare the number of items' , names_crosstab)

if crossing == 'gender and smoking status':
   st.write(pd.crosstab(stroke["gender"] , stroke["smoking_status"]))
elif crossing == 'gender and work type':   
   st.write(pd.crosstab(stroke["gender"] , stroke["work_type"]))
elif crossing == 'gender and Residence_type':   
   st.write(pd.crosstab(stroke["gender"] , stroke["Residence_type"]))
else:
   st.write(pd.crosstab(stroke["work_type"] , stroke["smoking_status"]))

# showing pie plots
if st.checkbox('show pie plots'):
   opt= st.sidebar.radio('Select a graph' , options=('smoking status on piechart' ,'work on piechart'))
   if opt == 'smoking status on piechart': 
      st.write('count of smoking status:')
      fig= plt.figure(figsize=(8,6))
      lab = stroke['smoking_status'].value_counts()
      labels = lab.index
      plt.pie(stroke['smoking_status'].value_counts().head(5),labels= labels, autopct='%.2f%%', startangle=90)
      st.write(fig)
   elif opt == 'work on piechart':
      st.write('count of work type :')
      fig= plt.figure(figsize=(8,6))
      lab = stroke['work_type'].value_counts()
      labels = lab.index
      plt.pie(stroke['work_type'].value_counts().head(5),labels= labels, autopct='%.2f%%', startangle=90)
      st.write(fig)

# create a radio for more plots
st.subheader('Showing more plots')
names_plot = ['boxplot for different items','count of age divided by stroke',
              'density distributain for age']
ploting = st.radio('Select one plot' , names_plot)

if ploting == 'boxplot for different items':
    fig = plt.figure(figsize=[20,6])
    plt.subplot(131)
    sns.boxplot(x='gender' , y='age' , data=stroke)
    plt.subplot(132)
    sns.boxplot(x='work_type' , y='age' , data=stroke)
    plt.subplot(133)
    sns.boxplot(x='smoking_status' , y='age' , data=stroke)
    st.write(fig)

elif ploting == 'count of age divided by stroke':
    fig=plt.figure(figsize=[24,6])
    sns.countplot(x='age' ,hue='stroke', data=stroke)  
    st.write(fig)
else:
   fig=plt.figure(figsize=[8,6])
   sns.kdeplot(x=stroke['age'])   
   st.write(fig)


# ibm details charts
if st.checkbox('showing bmi graph'):
   opt= st.sidebar.radio('Select a graph related to bmi' , options=('age , bmi , smoking status' ,'age , bmi , stroke','age , bmi , work type'))
   if opt == 'age , bmi , smoking status':
      fig = plt.figure(figsize=[12,8])
      sns.scatterplot(x='age', y='bmi', hue='smoking_status',style='smoking_status',data=stroke)
      st.write(fig)
   elif opt == 'age , bmi , stroke':
      fig = plt.figure(figsize=[12,8])
      sns.scatterplot(x='age', y='bmi', hue='stroke',style='stroke',data=stroke)
      st.pyplot(fig)
   else:
      fig = plt.figure(figsize=[12,8])
      sns.scatterplot(x='age', y='bmi', hue='work_type',style='work_type',data=stroke)
      st.pyplot(fig) 

# showing correlation 
st.subheader('Correlation graph')
fig= plt.figure(figsize=[12,8])
sns.heatmap(stroke.corr(), annot=True)
st.pyplot(fig)

# starting to show details about people who had stroke
st.subheader('Details about people who had stroke :')

names_plot1= ['gender' , 'age' , 'heart disease' , 'ever married' , 'work type','smoking status','residence']
stroking = st.radio('Select one plot' , names_plot1)

if stroking == 'gender':
    fig = plt.figure(figsize=[8,6])
    plt.bar([120,89],[120,89],tick_label=['female','male'], width=12  ,color=['pink','green'])
    st.pyplot(fig)
elif stroking == 'age':
    fig = plt.figure(figsize=[8,6])
    plt.bar([20,10],[188,18],tick_label=['more than 50','less than 50'], width=12  ,color=['black','pink'])
    st.pyplot(fig)
   
elif stroking == 'heart disease':
    fig = plt.figure(figsize=[8,6])
    plt.bar([10,20],[169,40],tick_label=['doesnot have heart disease','has heart disease'], width=12  ,color=['black','pink'])
    st.pyplot(fig)
elif stroking == 'ever married':
    fig = plt.figure(figsize=[8,6])
    plt.bar([10,20],[23,186],tick_label=['not married','married'], width=12  ,color=['black','blue'])
    st.pyplot(fig)  

elif stroking == 'work type':
    fig = plt.figure(figsize=[8,6])
    plt.bar([80,10,127,35,62],[20,0,127,53,1],tick_label=['Govt_job','Never_worked','Private','Self-employed','children'], width=12  ,color=['black','pink','yellow','green','red'])
    st.pyplot(fig)  

elif stroking == 'smoking status':
    fig = plt.figure(figsize=[8,6])
    plt.bar([80,10,127,35],[29,57,84,39],tick_label=['Unknown','formerly smoked','never smoked','smokes'], width=12  ,color=['black','pink','yellow','green','red'])
    st.pyplot(fig)  
             
else:
    fig = plt.figure(figsize=[8,6])
    plt.bar([80,50],[100,109],tick_label=['rural','urban'], width=12  ,color=['black','pink','yellow','green','red'])
    st.pyplot(fig) 

# showing the results of predictions
st.subheader('Prediction')
st.write('we prediction our data with seven model and our target is stroke')

from PIL import Image
image = Image.open(r'C:\Users\User\Desktop\bar1.png')
image1 = Image.open(r'C:\Users\User\Desktop\bar2.png')
image2 = Image.open(r'C:\Users\User\Desktop\gain.png')

if st.checkbox('Resuits'):
   st.write('our result are:')
   st.image(image , caption= 'Accuracy')
   st.image(image1 , caption= 'Accuracy in prediction in class 1 (had stroke)')
   st.image(image2 , caption= 'Gain chart')
