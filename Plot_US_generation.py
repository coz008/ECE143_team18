import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def US_generation(x):
    '''
    Ploting the graph to see the electricity generation in the last ten years.
    Input: x is the processed data that includes the generation from 2007 to 2017;
    Output: histogrm showing the electricity generation.
    
    by Cong Zhao
    '''
    assert isinstance(x, pd.DataFrame)
    
    tot_gen = x.loc[x['STATE']=='US-TOTAL']
    tot_gen = tot_gen.loc[tot_gen['ENERGY SOURCE']=='Total']
    tot_gen = tot_gen.groupby('YEAR').sum()
    years = tot_gen.index.tolist()
    gen_e = tot_gen['GENERATION (Megawatthours)'].tolist()
    gen_e=np.array(gen_e)
    gen_e = gen_e/2
    plt.figure(figsize=(9,6))
    plt.bar(years,gen_e, align='center', alpha=0.5,color = 'green')

    plt.ylabel('GENERATION (Megawatthours)')
    plt.title('US Electricity Generation')
    plt.plot( years, gen_e, marker='.', markerfacecolor='blue', markersize=10, color='pink', linewidth=3)
    plt.ylim([0,6*(10**9)])
    plt.show()

x = pd.read_excel(os.path.join('dataset','annual_generation_state.xls'))
x = x.loc[x['YEAR']>2006]
US_generation(x)