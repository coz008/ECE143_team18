# This script is in charge of retriving data from both web page and downloaded csv and xsl files
# It will be refered by other scripts multiple times so make sure it's in the same directory as
# other files. 
# Once refered by other scripts, this script will automatically convert and process the data in to 
# pandas dataframe that is suitable for plotting and analysis. 
import numpy as np
import pandas as pd
import holoviews as hv
import get_abbrev as abv
import requests
import lxml.html as lh
import os

us_state_abbrev = abv.get_abbrev()
power = pd.read_excel(os.path.join('data.xls')
pollution = pd.read_csv(os.path.join(pollution.csv')
url='https://www.infoplease.com/us/population/us-population-state-1790-2015'

assert isinstance(us_state_abbrev,dict)
assert isinstance(power,pd.core.frame.DataFrame)
assert isinstance(pollution,pd.core.frame.DataFrame)

def power_pollution():
  '''
  Input:
        This function inputs data from local downloaded csv and xsl files.
  Output:
        The output data are in pandas dataframe format and do not requires
        further process for plotting.
  '''
  state_p = power[np.logical_and(power['STATE']!= 'US-TOTAL',power['STATE']!= 'US-Total')]
  state_p = state_p[np.logical_and(power['STATE']!= 'DC',power['STATE']!= 'HI')]
  state_p = state_p[power['STATE']!= 'AK']
  state_p = state_p[state_p['ENERGY SOURCE']=='Total']
  state_p_f = state_p.groupby(['YEAR','STATE'])['GENERATION (Megawatthours)'].sum().reset_index()
  edata = hv.Dataset(data=state_p_f,kdims=['YEAR','STATE','GENERATION (Megawatthours)'])

  PM_data = pollution[pollution['MeasureName']=='Annual average ambient concentrations of PM 2.5 in micrograms per cubic meter, based on seasonal averages and daily measurement (monitor and modeled data)']
  PM_data = PM_data[PM_data['StateName']!='District of Columbia']
  PM_data = PM_data.replace({'StateName':us_state_abbrev})
  PM_data_f = PM_data.groupby(['ReportYear','StateName'])['Value'].sum().reset_index()
  PM_data_f = PM_data_f.rename(index=str, columns={'Value': 'Annual average ambient concentrations of PM 2.5'})
  edata_PM = hv.Dataset(data=PM_data_f,kdims=['ReportYear','StateName','Annual average ambient concentrations of PM 2.5'])
  return state_p,state_p_f,PM_data,PM_data_f


def get_population(web):
  '''
  Input:
        This function retrives population data from website with html tools.
  Output:
        The output data is a list of three lists, each contains the state names,
        the year 2000 and 2010 state-wise population.
  '''
  state_name = []
  p2000 = []
  p2010 = []
  url = web
  #Create a handle, page, to handle the contents of the website
  page = requests.get(url)
  #Store the contents of the website under doc
  doc = lh.fromstring(page.content)
  #Parse data that are stored between <tr>..</tr> of HTML
  for i in range(2,53):
      tr_elements = doc.xpath('//*[@id="uspopulationbystate"]/tbody/tr'+'['+str(i)+']')
      elements = tr_elements[0].text_content().strip().split()
      if len(elements)==8:
          state_name.append(elements[0])
          p2000.append(elements[3])
          p2010.append(elements[2])
      elif len(elements)==9:
          state_name.append(elements[0]+' '+elements[1])
          p2000.append(elements[4])
          p2010.append(elements[3])
  return [state_name,p2000,p2010] 

def population():
  '''
  Input:
        This function further processes the list data from get_population() function.
  Output:
        The output data is in the form of pandas dataframe and requires no further
        processes for plotting.
  '''
  pop = get_population(url)
  pop[1] = [int(s.replace(',', '')) for s in pop[1]]
  pop[2] = [int(s.replace(',', '')) for s in pop[2]]
  p2000 = np.array(pop[1])
  p2010 = np.array(pop[2])

  population = np.zeros((len(p2000),11))
  for i in range(len(p2000)):
      population[i,:] = np.arange(p2000[i]+(p2010[i]-p2000[i])/10,
                                  p2010[i]+2*(p2010[i]-p2000[i])/10,
                             (p2010[i]-p2000[i])/10).astype(int)[0:11]
      
  population = np.reshape(population,(-1),order='F').astype(int)
  states = pop[0]*11
  years = sorted([i+2000 for i in range(1,12)]*51)
  d = {'Year':years,'States':states,'Population':population}
  df_pop = pd.DataFrame(data=d)
  df_pop = df_pop.replace({'States':us_state_abbrev})
  df_pop = df_pop[np.logical_and(df_pop['States']!= 'DC',df_pop['States']!= 'HI')]
  df_pop = df_pop[df_pop['States']!= 'AK']
  return df_pop