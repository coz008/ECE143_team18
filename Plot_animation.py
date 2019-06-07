# This script is used for create an animation that compares the relations among 
# power generation, pm 2.5 data and population. The script has to be run in a 
# ipython console, since pandas require a compiler in a plain python console.
# Once run in a console, it will import data from the get_data.py and plot a bar 
# plot animation comparison among California, Pennsylvania and Texus.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import get_data
from matplotlib import animation

power_i,state_p_f,pollution_i,PM_data_f = get_data.power_pollution()
df_pop = get_data.population()

assert isinstance(power_i,pd.core.frame.DataFrame)
assert isinstance(state_p_f,pd.core.frame.DataFrame)
assert isinstance(pollution_i,pd.core.frame.DataFrame)
assert isinstance(PM_data_f,pd.core.frame.DataFrame)
assert isinstance(df_pop,pd.core.frame.DataFrame)

def plot_animation():
  '''
  Input:
        This function takes in no input, and the data used is from 
        get_data.py. 
  Output:
        The function does not return anything but will save an animation
        in the working directory. The animation is in mp4 format. 
  '''
  power = np.zeros((11,3))
  pollu = np.zeros((11,3))
  popul = np.zeros((11,3))
  for i in range(11): 
    a=state_p_f[state_p_f['YEAR']==2001+i]
    a=a[np.logical_or(np.logical_or(a['STATE']=='TX',a['STATE']=='PA'),
                      a['STATE']=='CA')]['GENERATION (Megawatthours)'].tolist()   
    b=PM_data_f[PM_data_f['ReportYear']==2001+i]
    b=b[np.logical_or(np.logical_or(b['StateName']=='TX',b['StateName']=='PA'),
                      b['StateName']=='CA')]['Annual average ambient concentrations of PM 2.5'].tolist()   
    c=df_pop[df_pop['Year']==2001+i]
    c=c[np.logical_or(np.logical_or(c['States']=='TX',c['States']=='PA'),
                      c['States']=='CA')]['Population'].tolist()   
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    power[i,:] = a/1000000
    pollu[i,:] = b
    popul[i,:] = c/100000
  N=3
  def barlist(n): 
    '''
    Input:
          This function is used for animation update, the input n is the 
          index of frame playing.
    Output:
          It will output a list of parameters that updates the animation.
    '''
    assert isinstance(n,int)
    return [power[n,:].tolist(),pollu[n,:].tolist(),popul[n,:].tolist()]
  ind = np.arange(N)  # the x locations for the groups
  width = 0.2      # the width of the bars
  fig = plt.figure(figsize=(20, 6))
  ax = fig.add_subplot(111)
  ax.set_xticks(ind + width / 2)
  ax.set_xticklabels( ['California','Pennsylvania','Texus'],fontsize = 15 )
  plt.title('US Power Generation, PM2.5, and Population in 2001-2011',fontsize=20)
  ax.set_ylabel('Normalized Value',fontsize = 15)
  barcollection1 = ax.bar(ind, barlist(1)[0], width, color='black',label='Power')
  barcollection2 = ax.bar(ind+width, barlist(1)[1], width, color='red',label='Pollution')
  barcollection3 = ax.bar(ind+2*width, barlist(1)[2], width, color='seagreen',label='Population')
  ax.legend( fontsize = 15)

  n=10
  def animate(i):
    '''
    Input:
          This is the main update function for the animation,
          The i is the current index of frame.
    Output:
          This function does not return anything but it will 
          update the barplot heights.
    '''
    y=barlist(i+1)
    for i, b in enumerate(barcollection1):
      b.set_height(y[0][i])
    for i, b in enumerate(barcollection2):
      b.set_height(y[1][i])
    for i, b in enumerate(barcollection3):
      b.set_height(y[2][i])

  anim=animation.FuncAnimation(fig,animate,repeat=True,blit=False,frames=n,interval=1000)
  Writer = animation.writers['ffmpeg']
  writer = Writer(fps=1.0, metadata=dict(artist='Me'))
  anim.save('3_state_compare.mp4', writer=writer)

if __name__ == '__main__':
  plot_animation()