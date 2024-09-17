# MEASURES OF SPREAD
# CALCULATE VARIANCE - SUBTRACT MEAN FROM EACH DATA POINT #1
dist= msleep['sleep_total'] - np.mean(msleep['sleep_total'])
#2 SQUARE EACH DISTANCE
sq_dists = dists ** 2
# 3 SUM squared distances
sum_sq_dists = np.sum(sq_dists)
# 4 DIVIDE BY NO OF DATA POINTS -1
variance = sum_sq_dists / (83 - 1)
# OR calculate var in 1 step using : without ddof=1, population variance is cal'd instead of sample var
np.var(msleep['sleep_total'], ddof=1)
# STANDARD DEVIATION- any of both methods below
np.sqrt(np.var(mfg['sjdh_total'], ddof=1)) #1
np.std(mfg['sjdh_total'], ddof=1)          #2
# MEAN ABSOLUTE DEVIATION
dists = msleep['sleep_total'] - mean(msleep$sleep_total)
np.mean(np.abs(dists))
# QUANTILES/ PERCENTILE 50%- which is also median
np.quantile(msleep['sleep_total'], 0.5)
# multiple quantiles
np.quantile(msleep['sleept_total'], [0, 0.25,0.5,0.75,1])
# Boxplots use quartiles
plt.boxplot(msleep['sleep_total'])
plt.show()      # bottom of box is 1st quartile, top is 3rd quartile 
                # and, middle ine is 2nd quartile or median
# QUARTILES USING NP.LINESPACE() - start at 0, stop at 1, split into 5 intervals
np.quantile(msleep['sleept_total'], np.linespace(0,1,5))
# INTERQUARTILE RANGE (IQR) - DISTANCE BTW 25TH AND 75TH PERCENTILE, ALSO HEIGHT OF BOX IN BOXPLOT
np.quantile(msleep['sleep_total'], 0.75) - np.quantile(msleep['sleep_total'], 0.25)
# OR 
from scipy.stats import iqr
iqr(msleep['sleep_total'])
# OUTLIER - data point is an outlier if:
data < QI - 1.5 * IQR  # OR
data > Q3 + 1.5 * IQR
# Finding outliers
from scipy.stats import iqr
iqr = iqr(msleep['bodywt'])
low_threshold= np.quantile(msleep['bodywt'], 0.25) - 1.5 * iqr
upper_threshold= np.quantile(msleep['bodywt'], 0.75) + 1.5 * iqr
msleep[(msleep['bodywt'] < low_threshold) | (msleep['bodywt'] > upper_threshold)]
# summary statistics
msleep['bodywt'].describe()
# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))
# Create histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()
plt.show()
# Create histogram of co2_emission for food_category 'eggs'
food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist()
plt.show()
# Calculate the total co2_emission per country by grouping by country and taking the sum of co2_emission
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()
# Compute the first and third quartiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = np.quantile(emissions_by_country, 0.75) - np.quantile(emissions_by_country, 0.25)
# MEASURING CHANCE
P(event) = no of ways event can happen / total no of possible outcomes
p(heads) = 1 way to get heads in coin / 2 possible outcomes
# Sampling from a DF - choose random row
sales_counts.sample()
# Setting a random seed- seed is a no python random no generator uses as starting point
np.random.seed(10)
sales_counts.sample()
# sampling with/without replacement 5 values
sales_counts.sample(5, replace= True)
# Calculate the probability of selecting a deal for the different product types by dividing the counts by the total number of deals Amir worked on.
counts = amir_deals['product'].value_counts()    # Count the deals for each product
probs = counts/ amir_deals.shape[0]
# lAW OF LARGE NUMBERS ::
As sample size increases, sample mean will approach expected value.
# Create probability distribution by Count the number of each group_size in restaurant_groups, then divide by-
#-the number of rows in restaurant_groups to calculate the probability of randomly selecting a group of each size. 
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]
# Rename the columns of size_dist to group_size and prob
size_dist.columns = ['group_size', 'prob']
# Calculate the expected value of the size_dist, which represents the expected-
#-group size, by multiplying the group_size by the prob and taking the sum.
expected_value = np.sum(size_dist['group_size']* size_dist['prob'])
# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size'] >=4]
# Sum the probabilities of groups_4_or_more
prob_4_or_more = np.sum(groups_4_or_more['prob'])
# discrete distributions
probability distribution - # describes each possible outcome in a scenario
expected value [ev] - # mean of a probability distribution
ev = n * probability- for a dice= (1*1/6) + (2*1/6) + (3*1/6)... #and so on till (6*1/6).
# sampling from discrete distributions
roll_10 = die.sample(10, replace=True)
















