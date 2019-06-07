# This script is used for generate visualization plots.
# It has to be run in a ipython console to avoid unfounded module
# Once run, it will automatcially generate three holoview interactive 
# plots and save as html file, and one bar plot saved as png file.
# The script reads data from get_data.py, so make sure that all the files
# are in the same directory.
import numpy as np
import pandas as pd
import holoviews as hv
import matplotlib.pylab as plt
import get_data
hv.extension('bokeh')

power_i,power,pollution_i,pollution = get_data.power_pollution()
population = get_data.population()

assert isinstance(power_i,pd.core.frame.DataFrame)
assert isinstance(power,pd.core.frame.DataFrame)
assert isinstance(pollution_i,pd.core.frame.DataFrame)
assert isinstance(pollution,pd.core.frame.DataFrame)
assert isinstance(population,pd.core.frame.DataFrame)

def plot_power():
  '''
  Input:
        This function take no input, it reads the power generation data from get_data.py
  Output:
        The function does not return anything, it will save the US power generation plot 
        as PowerGeneration.html
  '''
  edata = hv.Dataset(data=power,kdims=['YEAR','STATE','GENERATION (Megawatthours)'])
  plot1 = edata.to(hv.Bars,'STATE','GENERATION (Megawatthours)',groupby='YEAR').opts(width=800,height=400,xrotation=50)
  renderer = hv.renderer('bokeh')
  renderer.save(plot1, 'PowerGeneration')

def plot_pollution():
  '''
  Input:
        This function take no input, it reads the power generation data from get_data.py
  Output:
        The function does not return anything, it will save the US Annual average ambient 
        concentrations of PM 2.5 plot as Pollution.html
  '''
  edata_PM = hv.Dataset(data=pollution,kdims=['ReportYear','StateName','Annual average ambient concentrations of PM 2.5'])
  plot2 = edata_PM.to(hv.Bars,'StateName','Annual average ambient concentrations of PM 2.5',groupby='ReportYear').opts(width=800,height=400,xrotation=50)
  renderer = hv.renderer('bokeh')
  renderer.save(plot2, 'Pollution')

def plot_population():
  '''
  Input:
        This function take no input, it reads the power generation data from get_data.py
  Output:
        The function does not return anything, it will save the US power generation plot 
        as PowerGeneration.html
  '''
  edata_pop = hv.Dataset(data=population,kdims=['Year','States','Population'])
  plot3 = edata_pop.to(hv.Bars,'States','Population',groupby='Year').opts(width=800,height=400,xrotation=50)
  renderer = hv.renderer('bokeh')
  renderer.save(plot3, 'Population')

def plot_correlation():
  '''
  Input:
        This function take no input, it reads the power generation data from get_data.py
  Output:
        The function does not return anything, it will save the Correlation among Power, 
        Pollution and Population plot as Correlation.png
  '''
  state_s = power_i.groupby(['YEAR','STATE'])['GENERATION (Megawatthours)'].sum().to_frame()
  PM_s = pollution_i.groupby(['ReportYear','StateName'])['Value'].sum().to_frame()
  pop_s = population.groupby(['Year','States'])['Population'].sum().to_frame()
  corr = np.zeros((3,11))
  for i in range(2001,2012):
    x = (state_s['GENERATION (Megawatthours)'][i]/state_s['GENERATION (Megawatthours)'][i].sum()).tolist()
    y = (PM_s['Value'][i]/PM_s['Value'][i].sum()).tolist()
    z = (pop_s['Population'][i]/pop_s['Population'][i].sum()).tolist()
    corr[0,i-2001] = np.corrcoef(x, y)[0,1]
    corr[1,i-2001] = np.corrcoef(x, z)[0,1]
    corr[2,i-2001] = np.corrcoef(y, z)[0,1]
      
  correlation = np.mean(corr,axis = 1)
  xx = np.arange(3)
  plt.bar(xx,height = correlation,color = 'Blue')
  plt.xticks(xx, ('Power&Polution', 'Power&Population', 'Population&Pollution'),fontsize = 10)
  plt.ylabel('Average Correlation Value',fontsize = 15)
  plt.title('Correlation among Power, Pollution and Population',fontsize = 15)

  for x,y in zip(xx,correlation):
    label = "{:.2f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,-50), # distance from text to points (x,y)
                 ha='center',
                 color = 'w',
                 fontsize=40) 
  plt.savefig('Correlation.png', format='png', dpi=1000)

if __name__ == '__main__':
  plot_power()
  plot_pollution()
  plot_population()
  plot_correlation()