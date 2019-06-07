# ECE143_team18
Electricity generation and composition in United States

## Team Members
- Shihua Sun
- Fernando Lopez Garcia (@Fernasonlumia)ndo-LopezGarcia)
- Daoyu Li (@Nwoodle)
- Ambareesh Sreekumaran Nair Jayakumari (@ambareeshsrja16)

## Problem
Analysing course offerings in engineering departments of top universities in the United States related to industry demands.

## Summary
Technology has been evolving ever so rapidly for the past two decades. 
Both students and Departments concerned with technical learning need to keep up with the demanding changes. 
The Course Catalog of a department gives a brief, yet exhaustive description of all subjects covered. 
Analysis on a new dataset created from course catalogs provided an interesting challenge to understand how the universities have changed over time. 

## Methodology

- Catalog descriptions were scrapped to analyze the occurrence of every word and pair of words (2006-2019)
- The unigrams, and bigrams along with their occurrence frequency were stored in a database (managed through SQLite)
- Pairs of words (or Bigrams) were of relatively higher relevance ("Signal Processing", "Machine Learning", "Fuzzy Logic", "Integrated Circuits")
- To shorten the features of interest and derive more meaning, lemmatization was used (NLTK python library)
- Words with minimal frequency and common words ("credits", "pre-requisites", "classes") were discarded, to make the final processed dataset.
- Job descriptions from companies were collected and they underwent the above processing as well.


## Dataset

```
Universities (UCSD, UCB, UCLA, UCSB)
|
+--- ECE ---+   + Catalog of 2006 - 2007
|           |   |           .
+--- CSE ---+---|           .
|           |   |           .
+--- MAE ---+   + Catalog of 2018 - 2019
```
*Primary:*
- Course catalogs from 2002 to 2019 from 4 UC's. We will be scrapping for ECE, CSE and MAE Departments. 

*Secondary:*
-  Current industry job requirements from 10 leading companies in various domains, such as Qualcomm, Amazon, Google, Apple and so on.

## Applications
1. Identifying the most common skills that have been promoted by departments from different universities, which will serve as the basis of our project.
2. Analyzing how the course offerings of a department at UCSD have changed over time and observing the degree of change.
3. Ascertaining if changes in course curriculum of departments reflect the state of the industries that they are concerned with. We can discuss the relation between departments and the corresponding industries.
4. Analyzing how the offerings have changed for the same department across different universities.
5. Observing the extent of overlap between two departments of a university in terms of skills for domains (for e.g. Machine Learning)
6. Identifying how the present job requirements from different companies map to the course offerings.

## File Structure

```
Root
|
+----raw_data
|
+----industry_data
|
+----processed_data
|
+----scripts
|       |   create_processed_data.py
|       |   word_freq.py
|       |   SQLite.py
|       |   common_words.txt
|       |   Industry_words.txt
|
|    main.py
|    analyse_data.py
|    analyse_data_department_only.py
|    Plot_Extent_of_overlap.py
|    Plot_radar_chart.py
|    Plot_ucsd_cse.py
|    Plot_ucsd_ece.py
|    Plot_department.py
|    merge_industry.py
|    Notebook_for_overview.ipynb
```

## Instructions on running the code

* Python version: Python 3.6.6 64-bit
### Required packages

1. numpy
1. pandas
2. matplotlib
3. matplotlib_venn
3. [apsw](####apsw)
4. sqlite3
5. plotly
6. xlrd

For installing these packages, you can use either ```pip3``` to install packages. For example, 

```pip3 install numpy```

#### ```apsw```

In part of our code, ```apsw``` is used to create connections to our database. 

Please install it using:

```pip3 install apsw```

If the above failed or you don't have a C compiler, please go to [this link](https://rogerbinns.github.io/apsw/download.html) to download binaries for your specific machine. I would recommend using conda to install this package on macOS.

### Run the code
1. Run the ```main.py``` to generate all the data from raw txt files in ```industry_data``` and ```raw_data```  
2. Run the ```Plot_Extent_of_overlap.py```, ```Plot_radar_chart.py```, ```Plot_ucsd_ece.py``` etc. to get the graphs.# Engineering Course Analysis (Group 6)

## Team Members
- Renjie Zhu (@johnsonlumia)
- Fernando Lopez Garcia (@Fernando-LopezGarcia)
- Daoyu Li (@Nwoodle)
- Ambareesh Sreekumaran Nair Jayakumari (@ambareeshsrja16)

## Problem
Analysing course offerings in engineering departments of top universities in the United States related to industry demands.

## Summary
Technology has been evolving ever so rapidly for the past two decades. 
Both students and Departments concerned with technical learning need to keep up with the demanding changes. 
The Course Catalog of a department gives a brief, yet exhaustive description of all subjects covered. 
Analysis on a new dataset created from course catalogs provided an interesting challenge to understand how the universities have changed over time. 

## Methodology

- Catalog descriptions were scrapped to analyze the occurrence of every word and pair of words (2006-2019)
- The unigrams, and bigrams along with their occurrence frequency were stored in a database (managed through SQLite)
- Pairs of words (or Bigrams) were of relatively higher relevance ("Signal Processing", "Machine Learning", "Fuzzy Logic", "Integrated Circuits")
- To shorten the features of interest and derive more meaning, lemmatization was used (NLTK python library)
- Words with minimal frequency and common words ("credits", "pre-requisites", "classes") were discarded, to make the final processed dataset.
- Job descriptions from companies were collected and they underwent the above processing as well.


## Dataset

```
Universities (UCSD, UCB, UCLA, UCSB)
|
+--- ECE ---+   + Catalog of 2006 - 2007
|           |   |           .
+--- CSE ---+---|           .
|           |   |           .
+--- MAE ---+   + Catalog of 2018 - 2019
```
*Primary:*
- Course catalogs from 2002 to 2019 from 4 UC's. We will be scrapping for ECE, CSE and MAE Departments. 

*Secondary:*
-  Current industry job requirements from 10 leading companies in various domains, such as Qualcomm, Amazon, Google, Apple and so on.

## Applications
1. Identifying the most common skills that have been promoted by departments from different universities, which will serve as the basis of our project.
2. Analyzing how the course offerings of a department at UCSD have changed over time and observing the degree of change.
3. Ascertaining if changes in course curriculum of departments reflect the state of the industries that they are concerned with. We can discuss the relation between departments and the corresponding industries.
4. Analyzing how the offerings have changed for the same department across different universities.
5. Observing the extent of overlap between two departments of a university in terms of skills for domains (for e.g. Machine Learning)
6. Identifying how the present job requirements from different companies map to the course offerings.

## File Structure

```
Root
|
+----raw_data
|
+----industry_data
|
+----processed_data
|
+----scripts
|       |   create_processed_data.py
|       |   word_freq.py
|       |   SQLite.py
|       |   common_words.txt
|       |   Industry_words.txt
|
|    main.py
|    analyse_data.py
|    analyse_data_department_only.py
|    Plot_Extent_of_overlap.py
|    Plot_radar_chart.py
|    Plot_ucsd_cse.py
|    Plot_ucsd_ece.py
|    Plot_department.py
|    merge_industry.py
|    Notebook_for_overview.ipynb
```

## Instructions on running the code

* Python version: Python 3.6.6 64-bit
### Required packages

1. numpy
1. pandas
2. matplotlib
3. matplotlib_venn
3. [apsw](####apsw)
4. sqlite3
5. plotly
6. xlrd

For installing these packages, you can use either ```pip3``` to install packages. For example, 

```pip3 install numpy```

#### ```apsw```

In part of our code, ```apsw``` is used to create connections to our database. 

Please install it using:

```pip3 install apsw```

If the above failed or you don't have a C compiler, please go to [this link](https://rogerbinns.github.io/apsw/download.html) to download binaries for your specific machine. I would recommend using conda to install this package on macOS.

### Run the code
1. Run the ```main.py``` to generate all the data from raw txt files in ```industry_data``` and ```raw_data```  
2. Run the ```Plot_Extent_of_overlap.py```, ```Plot_radar_chart.py```, ```Plot_ucsd_ece.py``` etc. to get the graphs.
