# End-To-End Machine Learning Project

### First I created a "setup.py" file to keep all of my work inside it.

## setup.py
- Responsible for creating my ML application as a package. 
- With the help of setup.py, i will be able to create my entire ML app as a package, from there anybody can install it and use it.

### Also created requirements.txt file to install all of the required libraries for this project


## Components

- Components are like all the module that we are going to create like initally we create process called data ingestion.
- Components can be created as package and it can also exported like it can be imported to some other file location.

## Data Ingestion
- It simply means reading a data set from a database or it can be from some other file location. 
- I will divide the entire dataset into train and test. And also perform cross validation.

### After injecting the data I will transform, for that i will create data_transform file.
- We will perform here task like converting categorical features into numerical features, handle one_hot_coding, handle label_encoding etc.

### After transformation I cile create model_trainer file to train my model.
- I will use different types of algorithm in here.



## Life cycle of Machine learining project
 - Understanding the problem statement
 - Data Collection
 - Data checks to perform
 - Exploratory data analysis
 - Data pre-processing
 - Data modeling
 - Choose the model

### 1) Problem Statement
- This projects usderstand how the student's perfromance (test score) is affected by other variables such as gender, Ethinicity, Parental level of education, lunch and test preparation course.


### 2) Data Collection
- Dataset Source - https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977
- The data consists of 8 column and 1000 rows.

### 2.1 Import Data and Required Packages
####  Importing Pandas, Numpy, Matplotlib, Seaborn and Warings Library.


### 2.2 Dataset Information
- gender : sex of students  -> (Male/female)
- race/ethnicity : ethnicity of students -> (Group A, B,C, D,E)
- parental level of education : parents' final education ->(bachelor's degree,some college,master's degree,associate's degree,high school)
- lunch : having lunch before test (standard or free/reduced) 
- test preparation course : complete or not complete before test
- math score
- reading score
- writing score

### 3. Data Checks to perform
    
- Check Missing values
- Check Duplicates
- Check data type
- Check the number of unique values of each column
- Check statistics of data set
- Check various categories present in the different categorical column


### 4. Exploring Data ( Visualization )

#### 4.1 Visualize average score distribution to make some conclusion. 
- Histogram
- Kernel Distribution Function (KDE)

![image](https://github.com/Jagannath29/ene-to-end-ml-project/assets/110445662/057092f5-01db-4368-882b-afc19b859ff9)
#####  Insights
- Female students tend to perform well then male students.

![image](https://github.com/Jagannath29/ene-to-end-ml-project/assets/110445662/f9f33ba6-a4a7-40a7-8405-cbb25d7b44c9)
#####  Insights
- Standard lunch helps perform well in exams
- Standard lunch helps perform well in exams be it a male or a female




