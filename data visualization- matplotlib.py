#INTRODUCING PYPLOT INTERFACE
import matplotlib.pyplot as plt
fig, ax= plt.subplots()
# adding data to axes
ax.plot(seattle_we['MONTH'], seattle_we['MLY-TAVG-NORMA']) #Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(austin_we['MONTH'], austin_we['MLY-TAVG-NORMA']) # Plot MLY-PRCP-NORMAL from austin_weather against MONTH
plt.show()
#CUSTOMIZING DATA APPEARANCE
# CIRCLE MARKERS - o, v
ax.plot(seattle_we['MONTH'], seattle_we['MLY-TAVG-NORMA'], marker='o')
# SETTING LINESTYLE- '--', 'None'
ax.plot(seattle_we['MONTH'], seattle_we['MLY-TAVG-NORMA'], marker='v', linestyle='--')
# CHOOSING COLOR
ax.plot(seattle_we['MONTH'], seattle_we['MLY-TAVG-NORMA'], marker='v', linestyle='--', color='r')
# CUSTOMIZE AXES LABELS
ax.set_xlabel('Time (months)')
# ADDING TITLE
ax.set_title('Weather in Seattle')
#SUBPLOTS
# SMALL MULTIPLES TO SIMPLIFY VISULAIZATION OF MULTIPLE VALUES
fig, ax= plt.subplots()
fig, ax= plt.subplots(3,2) --# creates 3 ros of subplots and 2 columns
# ADDING DATA TO SUBPLOTS
ax[0,0].plot(seattle_weather['month'], seattle_weather['mly-prcp-norm'], color='b')
plt.show()
# subplots with 2 rows, 1 column
fig, ax= plt.subplots(2,1)
ax[0].plot(sea_we['month'], sea_wea['mly-p_norm'], color='b')
ax[0].plot(sea_we['month'],sea_wea['mly-p_25per'], linestyle='--', color='b')
ax[0].plot(sea_wea['month'],sea_wea['mly_p_75oer'], linestyle='--', color='b')
ax[1].plot(aus-wea['month'],aus-wea['mly_p_norm'],color='r')
ax[1].plot(aus-wea['month'],aus-wea['mly_p_25per'],linestyle='--',color='r')
ax[1].plot(aus-wea['month'],aus-wea['mly_p_75per'],linestyle='--',color='r')
ax[0].set_ylabel('Precipitation (inches)')
ax[1].set_ylabel('Precipitation (inches)')
ax[1].set_xlabel('Time (months)')
plt.show()
# SHaring y-axis range values between multiple charts
fig, ax= plt.subplots(2,1, sharey=True)
# 4 GRAPHS SUBPLOTS
# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)
# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-NORMAL'],color='b')
# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'])
# In the bottom left (1, 0) plot month and Austin precipitations
ax[1,0].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'])
# In the bottom right (1, 1) plot month and Austin temperatures
ax[1,1].plot(austin_weather['MONTH'], austin_weather['MLY-TAVG-NORMAL'])
plt.show()
# PLOTTING TIME-SERIES DATA
import matplotlib.pyplot as plt
fig, ax=plt.subplots()
ax.plot(climate_change.index, climate_change['co2'])
ax.set_xlabel('Time')
ax.set_ylabel('Co2 (ppm)')
plt.show()
# Zooming in on a decade
sixties= climate_change['1960-01-01':'1968-12-31']
fig, ax=plt.subplots()
ax.plot(sixties.index, sixties['co2'])
ax.set_xlabel('Time')
ax.set_ylabel('Co2 (ppm)')
plt.show()
#Read CSV,parse the "date" column as dates,set the "date" column as the index
climate_change= pd.read_csv('climate_change.csv', parse_dates=['date'],index_col='date')
# PLOTTING TIME SEREIS IN SAME SUBPLOT - twin axes
fig, ax= plt.subplots()
ax.plot(climate_change.index, climate_change['co2'], color='blue')
ax.tick_params('y', colors='blue')  # to color y tick
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)', color= 'blue')
ax2= ax.twinx()
ax2.plot(climate_change.index, climate_change['relative_temp'], color='red')
ax2.set_ylabel('Relative temperature (Celsius)', color='red')
ax2.tick_params('y', colors='red')  # to color y tick
plt.show()
# function that plots time-series
def plot_timeseries(axes,x,y, color, xlabel,ylabel):
  axes.plot(x,y,color=color)
  axes.set_xlabel(xlabel)
  axes.set_ylabel(ylabel, color=color)
  axes.tick_params('y', colors=color)
# using function above
fig, ax= plt.subplots()
plot_timeseries(ax,climate_change.index, climate_change['co2'],'b', 'Time','CO2 (ppm)')
ax2= ax.twinx()
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'],'r', 'Time',
                'Relative temperature (Celsius)')
plt.show()

# ANNOTATING TIME-SERIES DATA
fig, ax= plt.subplots()
plot_timeseries(ax,climate_change.index, climate_change['co2'],'b', 'Time','CO2 (ppm)')
ax2= ax.twinx()
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'],'r', 'Time',
                'Relative temperature (Celsius)')
ax2.annotate('>1 degree', xy=(pd.Timestamp('2015-10-06'), 1))  #annotation
plt.show()
# POSITIONING ANNOTATION TEXT
ax2.annotate('>1 degree', 
             xy=(pd.Timestamp("2015-10-06"), 1),
            xytext=(pd.Timestamp("2008-10-06"), -0.2))
# ADDING ARROWS TO ANNOTATION
ax2.annotate('>1 degree', 
             xy=(pd.Timestamp("2015-10-06"), 1),
            xytext=(pd.Timestamp("2008-10-06"), -0.2),
            arrowprops={})
# CUSTOMIZING ARROW PROPERTIES
ax2.annotate('>1 degree', 
             xy=(pd.Timestamp("2015-10-06"), 1),    # xy IS POINTING AT xytext
            xytext=(pd.Timestamp("2008-10-06"), -0.2),
            arrowprops={'arrowstyle':'->', 'color':'gray'})

# QUANTITATIVE COMPARISONS: BAR-CHARTS











































