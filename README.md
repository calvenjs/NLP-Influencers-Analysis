# NLP-Influencers-Analysis
![image1](https://github.com/calvenjs/NLP-Influencers-Analysis/blob/main/images/Instagram-Influencer-marketing-tutorial.jpg)

## Introduction
Affiliate and influencer marketers has seen tremendous growth over the years with the prominence of social media sites like Youtube, Twitter, Instagram and TikTok. According to Digital Marketing Institute, influencer marketing was worth just $1.7 billion in 2016, and is set to reach $13.8 billion by 2022 as the industry witnesses more growth and becomes a more effective marketplace.<br><br>
This repository focuses on performing text analysis and text mining on ***instagram's influencers*** predominantly in the micro-influencers (e.g. 5k-20k followers) domain and discovering if a certain post is sponsored based on the caption itself as well as identifying the sponsor.

It contains 2 scripts:
1. Notebook for scraping influencers posts in Instagram.
2. Main Program - Data Preprocessing, Feature Extraction, Sponsor Tagging, Natural Language Processing techniques and Data Visualization on these posts.

## Disclaimer
All content scraped were done in a responsible and considerate fashion with adequate time stop that mimics human behavior to prevent any request overload on the server.
Additionally, this project is done purely for educational purposes with no profit or monetization were involved else it will be at the direct benefit to Meta, or the organization or the user.

## Overview
The overall workflow of this project:
### Data Collection
1.  We’ll start by configuring the Chromedriver and setting up the login credentials. Following that, we will login to Instagram and go to the user Instagram page. Next, we will get the JSON information on that page. Once we retrieve the JSON page, we’ll store all of the relevant information for the post such as name, follower, postdate, likes, comments and caption on a list and append it to our data frame. The “time sleep” in the code prevents Instagram from identifying the scraper as a BOT. Lastly, we will export the data to a CSV file
### Exploratory Data Analysis
1. We will drop duplicates and drop all posts that have an empty caption as a post with no caption will serve us no purpose. We will also replace missing values in the industry column with “General”
2. First, we will quantify the engagement rate of a post by adding up the number of comments and likes and dividing the sum by the number of followers. Next, we’ll create a new column to store hyperlinks from the post. This feature will be used in conjunction with NLP to identify sponsored posts.
### Tagging
1. We will Load the NLP model and retrieve and list of stop_words
2. Preprocess the text by cleaning caption by changing all words to lowercase and removing and character that is not alphanumeric. Tokenize each word for entities tagging and
3. Remove Emoji and duplicates. Tag the possible sponsor based on the spaCy Named Entity Recognition package, links and hashtag.
### Natural Language Processing
1. Custom NER using spaCy - Train a custom NER model on top of the base model to include new entity labels sponsors, promo codes, products
2. Topic Modeling - Preprocess and perform LDA to identify and classify key topics of captions. Achieving a 0.515 Coherence score and 8 topics ranging from giveaway, fitness, love to promotions.
### Data Visualization
1. Most occurring words in Instagram post captions
![common](https://user-images.githubusercontent.com/23024496/147430270-4659b1f8-6139-40a8-a1df-2b6059e361d1.PNG)
2. Factors that attributes to a post having high engagement rate? 
![image](https://user-images.githubusercontent.com/32923591/147747182-0bd328af-95eb-4a74-8525-0138f33b0eac.png)

3. Frequency of Sponsorship by Brand
![ff](https://user-images.githubusercontent.com/23024496/147717242-be8fa1cd-0ded-40b5-9f27-3f3087105241.png)
4. Country and Industry with the most sponsorship
![image](https://user-images.githubusercontent.com/23024496/147430376-1bd37c34-23b7-4ee5-8719-d6da7d7552a4.png)




