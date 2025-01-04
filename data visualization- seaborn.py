#CATEGORICAL PLOTS= COUNT,BAR,BOX,POINT- distribution of quantitative var within categories
# RELATIONAL PLOTS= scatter and line - relationship btw 2 quantitative variables
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
# Omitting Outliers
g= sns.catplot(x='time',y='total_bill',data=tips,kind='box',sym='')
plt.show()
# changing whiskers
g= sns.catplot(x='time',y='total_bill',data=tips,kind='box',whis=[0,100]) #min & max values 
g= sns.catplot(x='time',y='total_bill',data=tips,kind='box',whis=2.0) #extend to 2.0 
g= sns.catplot(x='time',y='total_bill',data=tips,kind='box',whis=[5,95]) #show 5th and 95th percentiles
plt.show()

# POINT PLOTS - shows mean of quantitative variable, vertical line= 95% confidence intervals
import seaborn as sns
import matplotlib.pyplot as plt
sns.catplot(x='age',y='masculine',data=masculine_data,kind='point')
plt.show()
# disconnecting points
sns.catplot(x='age',y='masculine',data=masculine_data,kind='point',join=False)
plt.show()
# displaying median
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import median
sns.catplot(x='age',y='masculine',data=masculine_data,kind='point',estimator=median) #median is robust to outliers
plt.show()
# customizing CI
sns.catplot(x='age',y='masculine',data=masculine_data,kind='point',capsize=0.2)
plt.show()

# CHANGING PLOT STYLE - color of baackground 
sns.set_style('variable of style preferred')
# CHANGING PALETTE - color of main elements of plot
#diverging, sequential and custom pallettes
sns.set_palette()
# CHANGING SCALE- scale of plot elements and labels
sns.set_context()

# seaborn plot creates 2 objects type: FacetGrid and AxesSubplot
type(g) #display type of scatter plot
# ADDING TITLE to FacetGrid
g= sns.catplot(x='region',y='birthrate',data=gdp_data,kind='box')
g.fig.suptitle('New Title')
plt.show()
# adjust height of title facetgrid- default is 1
g.fig.suptitle('New Title',y=1.03)

#ADDING TITLE TO AXESSUBPLOT
g= sns.boxplot(x='region',y='birthrate',data=gdp_data)
g.set_title('New Title',y=1.03)
# titles for subplots
g.set_titles('This is {col_name}')
# add axis labels
g.set(xlabel='New X label',ylabel='New Y label')
plt.show()
# rotating x-axis tick labels
plt.xticks(rotation=90)
























