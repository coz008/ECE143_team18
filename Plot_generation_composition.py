import pandas as pd
import matplotlib.pyplot as plt
import os

def generation_composition(x, year):
    '''
    Ploting the pie charts to see the generation composition of two different years.
    Input: x is the processed data that includes the generation from 2007 to 2017;
           y is a list with two years.
    Output: two pie charts representing the generation composition of two different years.
    
    by Cong Zhao
    '''
    assert isinstance(x, pd.DataFrame)
    assert isinstance(year, list) 
    assert len(year) == 2
    for i in year:
        assert 2007 <= i <= 2017

    #2007 data
    x_1 = x.loc[x['YEAR']==year[0]]
    x_1 = x_1[x_1['ENERGY SOURCE']!='Total']
    x_1 = x_1[x_1['STATE']!='US-TOTAL']
    x_1 = x_1.groupby(['ENERGY SOURCE']).sum()
    x_1 = x_1.loc[x_1['GENERATION (Megawatthours)']>0]
    x_1.drop('YEAR',axis=1)
    source_1 = x_1.index.tolist()
    gen_1 = x_1['GENERATION (Megawatthours)'].tolist()
    colors=['yellowgreen', 'brown', 'lightskyblue', 'yellow','red', 
          'lightcoral','blue','pink', 'darkgreen', 
          'gold','grey','violet','magenta','cyan']
    plt.figure()
    title = plt.title('Electricity Generation Composition in 2007')
    title.set_ha("left")
    plt.gca().axis("equal")
    pie = plt.pie(gen_1, startangle=90,colors=colors)
    labels=source_1
    plt.legend(pie[0],labels, bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, 
           bbox_transform=plt.gcf().transFigure)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)

    #2017 data
    x_2 = x.loc[x['YEAR']==year[1]]
    x_2 = x_2[x_2['ENERGY SOURCE']!='Total']
    x_2 = x_2[x_2['STATE']!='US-TOTAL']
    x_2 = x_2.groupby(['ENERGY SOURCE']).sum()
    x_2 = x_2.loc[x_2['GENERATION (Megawatthours)']>0]
    x_2.drop('YEAR',axis=1)
    source_2 = x_2.index.tolist()
    gen_2 = x_2['GENERATION (Megawatthours)'].tolist()
    plt.figure()
    title = plt.title('Electricity Generation Composition in 2017')
    title.set_ha("left")
    plt.gca().axis("equal")
    pie = plt.pie(gen_2, startangle=120,colors=colors)
    labels=source_2
    plt.legend(pie[0],labels, bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, 
           bbox_transform=plt.gcf().transFigure)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)
    
x = pd.read_excel(os.path.join('dataset','annual_generation_state.xls'))
x = x.loc[x['YEAR']>2006]
#compare the generation composition of 2007 and 2017
generation_composition(x, [2007, 2017])
