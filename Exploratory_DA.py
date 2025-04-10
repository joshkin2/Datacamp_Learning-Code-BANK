# GATHER MORE INFO
books.info()
# LOOK A CAEGORICAL COLUMNS
books.value_counts('genre')
# DESCRIBE NUMERICAL COLUMNS
books.describe()
# VISUALIZING NUM DATA
import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(data=books, x='rating')
plt.show()
# ADJUSTING BIN WIDTH
sns.histplot(data=books, x='rating', binwidth=.1)






















