# PLOTTING A SCATTER PLOT
import seaborn as sns
import matplotlib.pyplot as plt
height= [62,64,69,75,66,68,65,71,76,73]
weight= [120,136,148,175,137,165,154,172,200,187]
sns.scatterplot(x=height,y=weight)
plt.show()
# COUNT PLOT
import seaborn as sns
import matplotlib.pyplot as plt
gender= ['Female', 'Female','Male','Male','Female']
sns.countplot(x=gender)
plt.show()
# WORKING WITH DF's
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df= pd.read_csv(masculinity)
df.head()
sns.countplot(x='how_masculine',data=df)
plt.show()
#NOTE: seaborn will not work well with untidy data
# ADDING 3RD VARIABLE WITH HUE
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
tips= sns.load_dataset('tips')
tips.head()
sns.scatterplot(x='total_bill',y='tip',data=tips,hue='smoker',hue_order=['Yes','No'])
sns.relplot(x="G1", y="G3",data=student_data,kind="scatter", col="schoolsup",col_order=["yes", "no"])
plt.show()
# SPECIFYING HUE COLORS
hue_colors={'Yes':'black','No':'red'}
sns.scatterplot(x='total_bill',y='tip',data=tips,hue='smoker',hue_order=['Yes','No'])
plt.show()
# Create a count plot of school with location subgroups
sns.countplot(x="school",data=student_data,hue="location",palette=palette_colors)
# RELATIONAL PLOTS= RELATIONSHIP BTW 2 QUANTITATIVE VARIABLES
# USING RELPLOT()
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='total_bill',y='tip',data=tips,kind='scatter') #to arrange vertically add= row='smoker'
# to use both add= col='smoker',row='time'.
plt.show()
# wrapping columns, add= col_wrap=2
#ordering columns, add= col_order=['Thur','Fri','Sat','Sun']

#CUSTOMIZING SCATTER PLOTS
#subgroups with point size and hue
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='total_bill',y='tip',data=tips,kind='scatter',size='size',hue='size')
plt.show()
#subgroups with point style
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='total_bill',y='tip',data=tips,kind='scatter',style='smoker',hue='smoker')
plt.show()
# changing point transparency
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='total_bill',y='tip',data=tips,kind='scatter',alpha=0.4)
plt.show()
# LINE PLOTS
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='hour',y='NO_2_mean',data=air_df_mean,kind='line')
plt.show()
# subgroups by location
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='hour',y='NO_2_mean',data=air_df_loc_mean,kind='line',style='location',hue='location')
plt.show()
# Adding markers
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='hour',y='NO_2_mean',data=air_df_loc_mean,kind='line',style='location',hue='location',markers=True)
plt.show()
# Turning off line style
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='hour',y='NO_2_mean',data=air_df_loc_mean,kind='line',style='location',hue='location',markers=True,dashes=False)
plt.show()
# Multiple observations per x-value - shaded region is confidence interval
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='hour',y='NO_2',data=air_df,kind='line')
plt.show()
# replace confidence interval with standard deviation- show spread of distribution
import seaborn as sns
import matplotlib.pyplot as plt
sns.relplot(x='hour',y='NO_2',data=air_df,kind='line',ci='sd') # set ci to none to turn off
plt.show()

# COUNT PLOT
import seaborn as sns
import matplotlib.pyplot as plt
sns.catplot(x='how_masculine',data=masculinity,kind='count')
plt.show()
# changing order
import seaborn as sns
import matplotlib.pyplot as plt
category_order= ['No answer','Not at all','Not very','Somewhat','Very']
sns.catplot(x='how_masculine',data=masculinity,kind='count',order=category_order)
plt.show()
# BAR PLOT
import seaborn as sns
import matplotlib.pyplot as plt
sns.catplot(x='day',y='total_bill',data=tips,kind='bar')
plt.show()
# off confidence intervals
import seaborn as sns
import matplotlib.pyplot as plt
sns.catplot(x='day',y='total_bill',data=tips,kind='bar',ci=None)
plt.show()
# change orientation of bars
import seaborn as sns
import matplotlib.pyplot as plt
sns.catplot(x='total_bill',y='day',data=tips,kind='bar')
plt.show()

# BOX PLOT - comparison between groups
import seaborn as sns
import matplotlib.pyplot as plt
g= sns.catplot(x='time',y='total_bill',data=tips,kind='box',order=['Dinner','Lunch'])
plt.show()


































