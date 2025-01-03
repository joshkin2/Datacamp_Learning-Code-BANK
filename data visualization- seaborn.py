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

















