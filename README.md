# NLP-to-predict-disaster
Project to enhance my skills in NLP, ML, DL and development web with Flask


# NLP-with-disaster-tweets
Kaggle project

Version 2.0 of this project.

Twitter has become an important communication channel in times of emergency. The ubiquitousness of smartphones enables people to announce an emergency they’re observing in real-time. Because of this, more agencies are interested in programatically monitoring Twitter (i.e. disaster relief organizations and news agencies).

In this competition, we’re challenged to build a machine learning model that predicts which Tweets are about real disasters and which one’s aren’t. We have access to a dataset of 10,000 tweets that were hand classified.

## Table of Contents
<details open>
<summary>Show/Hide</summary>
<br>

1. [ File Descriptions ](#File_Description)
2. [ Technologies Used ](#Technologies_Used)    
3. [ Structure ](#Structure)
4. [ Web development ](#Web)
5. [ Future Development ](#Executive_Summary)
</details>

## File Descriptions
<details>
<a name="File_Description"></a>
<summary>Show/Hide</summary>
<br>
  
* train.csv  - the training set
* test.csv - the test set
* sample_submission.csv - a sample submission file in the correct format

*Columns*
* id - a unique identifier for each tweet
* text - the text of the tweet
* location - the location the tweet was sent from (may be blank)
* keyword - a particular keyword from the tweet (may be blank)
* target - in train.csv only, this denotes whether a tweet is about a real disaster (1) or not (0)
</details>

## Technologies Used:
<details>
<a name="Technologies_Used"></a>
<summary>Show/Hide</summary>
<br>
    
* <strong>Python</strong>
* <strong>Pandas</strong>
* <strong>Numpy</strong>
* <strong>Matplotlib</strong>
* <strong>Seaborn</strong>
* <strong>NLTK</strong>
* <strong>CountVectorizer</strong>
* <strong>Scikit-Learn</strong>
* <strong>Keras</strong>
* <strong>Tensorflow</strong>
</details>

## Structure of Notebooks:
<details>
<a name="Structure"></a>
<summary>Show/Hide</summary>
<br>
    
1. Import packages

2. Data Exploration
   * 2.1 Number of characters in tweets
   * 2.2 Number of words in tweets
   * 2.3 Average word length in a tweet

3. Deep Learning methods
   * 3.1 Basic NLP Techniques
   * 3.2 Building model
   * 3.3 Model performances
   * 3.4 First submission to Kaggle

4. Machine Learning methods
   * 4.1 Basic NLP Techniques
   * 4.2 Building models
   * 4.3 Models performances
   * 4.4 Second Submission to Kaggle
</details>  




## Web develoment :
<details>
<a name="Web"></a>
<summary>Show/Hide</summary>
<br>
  
In order to have a concret and prompt outcome, I created a website to ensure that our model is useable by everyone.

I will share in our Github all the necessary files required fro creating it (app.py, templates, home and so on..)

There is the website where my model has been implemented : https://ml-deployment-evan.herokuapp.com/
</details>

## Future Development

<a name="Executive_Summary"></a>
    
* Masterise NLP, maybe enhance the text pre processing to enhance the result. I also would like deploying the model for actionnable use like I did for other project like "What's Cooking".

