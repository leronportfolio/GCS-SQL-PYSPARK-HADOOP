# GCS-SQL-PYSPARK-HADOOP
Final Project for Google Cloud Platform
Date: 3-14-23

## Analyzing the Impact of Compliments on Yelp User Engagement

### Problem Statement

The problem at hand is to understand user behavior on Yelp and the impact of various compliments given to them by other users. Without a clear understanding of user behavior and preferences, improving the platform experience for both businesses and customers becomes challenging. This lack of knowledge about the impact of compliments on users can result in ineffective marketing strategies and missed opportunities for better customer engagement. The stakeholders affected by this problem include Yelp, business partners, and users. Analyzing user data is a crucial step towards addressing the questions that arise.

### OSEMN Process

The OSEMN process (Obtain, Scrub, Explore, Model, Interpret) is followed to analyze the Yelp user data and gain insights into the impact of compliments on user engagement.

#### Obtain

The Yelp dataset is obtained from a .tar file. A Python script called "pythonscriptjsoncsv.py" is utilized to extract the dataset into .json files and a .csv file. The extracted data is then uploaded to a Google Cloud Storage (GCS) bucket named "cs512_group2".

#### Scrub

The data is scrubbed to remove any missing values (NA) and other values that may affect the analysis. Additionally, the dataset is partitioned into 160MB size partitions to ensure successful processing in the data preparation step.

#### Explore

Dataprep is employed to create a recipe that addresses a specific question of interest. In this case, the question revolves around finding the ratio of "compliment_hot" to "review_count" for Yelp users and sorting them in descending order. Additionally, BigQuery is used to partition the dataset to answer the second question. The third question is tackled using R Studio to create a visualization.

#### Model

A BigQuery dataset and table are created to calculate the correlation between "compliment_funny" and "compliment_plain". A query is executed to count the number of rows and calculate the correlation coefficient, providing insights into the relationship between these variables.

#### Interpret

R Studio is leveraged to visualize the average number of "compliment_cute" received by users who joined Yelp before 2010 compared to those who joined after. The data is filtered based on the date of joining, and the mean function is applied while excluding any NA values. The resulting bar chart illustrates that users who joined Yelp before 2010 received significantly more "compliment_cute" compared to those who joined after.

Please refer to the documentation and code files for detailed implementation and analysis steps.
