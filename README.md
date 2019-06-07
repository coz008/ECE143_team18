# ECE143_team18
Electricity generation and composition in United States

## Team Members
- Shihua Sun
- Cong Zhao
- Zhao Zhang

## Problem
Visualizing power generation in the past 10 years throughout each state in the US and electricity source composition in each year and state. 

## Summary
Electricity is indispensable in the modern world and electricity is generated from many energy sources. In the project, we visualized overall power generation and composition in United States, studied the compositions and compare to other countries and correlated power generation with pollution and population.
 
## Methodology
- Clean the dataset: we discarded facilities(mostly storages) that generate negative electricity. 
- Extract  useful information: we extracted only useful information from the data set for different graphs.
- Plot and Analyze: We analyzed the data and graphs from the following four parts: total generation, composition ,distribution and correlation.

## Dataset
*Primary:*
- We primarily used data from U.S. Energy Information Administration  and The World Bank for electricity generation data. From the dataset, we can get the electricity generation from different energy sources from 1997 to 2007.

*Secondary:*
-  We also used data from United States Census Bureau for pollution and population.

## File Structure

```
Root
|
+----dataset
|       |   create_processed_data.py
|       |   word_freq.py
|       |   SQLite.py
|       |   common_words.txt
|       |   Industry_words.txt
|
|    Plot_US_generation.py
|    Plot_animation.py
|    Plot_comparsion_different_sources.py
|    Plot_generation_coal.py
|    Plot_generation_composition.py
|    Plot_plots.py
|    get_abbrev.py
|    get_data.py
|    Notebook_for_overview.ipynb
```

## Instructions on running the code

* Python version: Python 3.6.6 64-bit
### Required packages

1. numpy
2. pandas
3. matplotlib
4. os
5. holoviews
6. requests
7. lxml.html

### Run the code
1. Run the ```get_data.py``` and ```get_abbrev.py``` to extract the data from the dataset.
2. Run the ```Plot_US_generation.py```, ```Plot_animation.py```etc. to get the graphs.

