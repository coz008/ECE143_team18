import pandas as pd
import matplotlib.pyplot as plt
import os

def compare_sources(x, year):
    '''
    Ploting the graph to compare the electricity generation from different sources.
    Input: x is the processed data that includes the generation from 2007 to 2017;
           year is the start year.
    Output: Graph with three curves representing coal, natural gas and nuclear.
    by Shihua Sun
    '''
    x_coal = x.loc[x['ENERGY SOURCE'] == 'Coal'] # extract the generation of coal
    x_coal_sum = x_coal.groupby(['YEAR']).sum()
    #print(x_coal_sum)
    x_gas = x.loc[x['ENERGY SOURCE'] == 'Natural Gas'] # extract the generation of natural gas
    x_gas_sum = x_gas.groupby(['YEAR']).sum()
    #print(x_gas_sum)
    x_nuclear = x.loc[x['ENERGY SOURCE'] == 'Nuclear'] # extract the generation of nuclear
    x_nuclear_sum = x_nuclear.groupby(['YEAR']).sum()
    #print(x_nuclear_sum)
    x_total = x.loc[x['ENERGY SOURCE'] == 'Total'] # extract the total generation of every state
    x_total_sum = x_total.groupby(['YEAR']).sum()
    #print(x_total_sum)
    # plot the tendency of the generation from the three main sources from 200co5 to 2017
    x_coal_sum = x_coal.loc[x['YEAR'] >= year].groupby(['YEAR']).sum()
    x_gas_sum = x_gas.loc[x['YEAR'] >= year].groupby(['YEAR']).sum()
    x_nuclear_sum = x_nuclear.loc[x['YEAR'] >= year].groupby(['YEAR']).sum()

    l1, = plt.plot(x_coal_sum.index, x_coal_sum['GENERATION (Megawatthours)'], 'r', linewidth=2, label='Coal')
    l2, = plt.plot(x_gas_sum.index, x_gas_sum['GENERATION (Megawatthours)'], 'g', linewidth=2, label='Natural Gas')
    l3, = plt.plot(x_nuclear_sum.index, x_nuclear_sum['GENERATION (Megawatthours)'], 'b', linewidth=2, label='Nuclear')
    plt.ylabel('Generation (Megawatthours)')
    plt.xlabel('Year')
    plt.legend(loc='upper right')
    plt.title('Comparison of generation from different sources')

x = pd.read_excel(os.path.join('dataset','annual_generation_state.xls'))
x = x.loc[x['YEAR']>2006]
compare_sources(x, 2007)