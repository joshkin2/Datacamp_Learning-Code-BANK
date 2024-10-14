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
# Expected value won with 30% win rate
won_30pct = 3 * 0.3
print(won_30pct)
# Expected value won with 25% win rate
won_25pct = 3 * 0.25
print(won_25pct)
# sampling from discrete distributions
roll_10 = die.sample(10, replace=True)
# Continous distributions
# continous uniform distribution - falt line to represent same probabiity along multiple possibilities
# uniform distribution in Python, 7 = probability we're looking for, 0 = lower limit on scale, 12= upper limit on scale
from scipy.stats import uniform
uniform.cdf(7,0,12)      # P (WAIT TIME <= 7)
# Greater than probabilities
from scipy.stats import uniform
1 - uniform.cdf(7,0,12)      # P (WAIT TIME >= 7) = 1 - P (WAIT TIME<= 7)
# P (4<= WAIT TIME <= 7) = P(WAIT<=7) - P (WAIT<=4)    between 7 and 4 mins
from scipy.stats import uniform
uniform.cdf(7,0,12) - uniform.cdf(4,0,12)
# Generate rand no according to uniform distribution
from scipy.stats import uniform
uniform.rvs(0,5, size=10)         # 0 - min value, 5 - max value, 10 - no of rand values
# eg of distribution 
1. #discrete uniform - ticket no of reffle winner, with limited no of ticket. or outcome of rolling 4-sided die.
2. # continuous - wait time for geyser to erupt which is exactly every 10 mins or time of day a baby will be born.
# Simulating wait times - mini project
np.random.seed(334) - # set random seed to 334
from scipy.stats import uniform - # import uniform
wait_times = uniform.rvs(0,30,size=1000) - # generate 100 wait times between 0 and 30mins
plt.hist(wait_times) - # hist of simulated times
plt.show()
# binomial distribution- prob distri of the no of success in a sequence of independent trials
from scipy.stats import binom
binom.rvs(1, 0.5, size=8) - # flip 1 coin with 50% chance 8 times
# probability of getting 7 heads
# binom.pmf( no heads, no trials, prob of heads)
binom.pmf(7, 10, 0.5)
# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3,3,0.3)
# binom.cdf - prob of getting no of success <= first argument
binom.cdf(7,10,0.5) - # P(heads <= 7)
# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1,3,0.3)
# probability of more than 7 heads
1 - binom.cdf(7,10,0.5) - # P(heads > 7)
# Probability of closing > 1 deal out of 3 deals
prob_greater_than_1 = 1 - binom.cdf(1,3,0.3)
# expected value = n * p
10 * 0.5 = 5 # if trails are not independent then we can't use binomial distribution
# Normal Distribution
# percent of women shorter than 154cm - height = 154, mean = 161, SD = 7
from scipy.stats import norm
norm.cdf(154, 161, 7)
# percent of women taller than 154cm 
from scipy.stats import norm
1 - norm.cdf(154, 161, 7)
# percent of women between 154 - 157 cm
norm.cdf(157,161,7) - norm.cdf(154,161,7)
# height 90% of women are shorter than
norm.ppf(0.9,161,7)
# height 90% of women are taller than
norm.ppf((1-0.9), 161, 7)
# generate random heights/ numbers
norm.rvs(161,7, size=10)
# Histogram of amount with 10 bins and show plot
amir_deals['amount'].hist( bins= 10)
plt.show()
# Central limit theorem -sampling distribution of stats becomes closer to normal distribution as no of trials increases
# Rollig dice 5X
die = pd.Series([1,2,3,4,5,6])
samp_5= die.sample(5, replace=True) # then print samp_5
# get mean for rolling dice 5X 10 times with for loop
sample_means = []
for i in range(10):
  samp_5 = die.sample(5, replace=True)
  sample_means.append(np.mean(samp_5))
print (sample_means)
# Mean of means -  estimate the mean by taking several random samples of deals
# Set seed to 321
np.random.seed(321)
sample_means = []
# Loop 30 times to take 30 means
for i in range(30):
  # Take sample of size 20 from num_users col of all_deals with replacement
  cur_sample = all_deals['num_users'].sample(20, replace=True)
  # Take mean of cur_sample
  cur_mean = np.mean(cur_sample)
  # Append cur_mean to sample_means
  sample_means.append(cur_mean)
# Print mean of sample_means
print(np.mean(sample_means))
# Print mean of num_users in amir_deals - END
print(np.mean(amir_deals['num_users']))
# -poisson processes= events happen at certain rate but randonm- no of animals adopted from shelter weekly
# Poisson distribution = prob of some no of events occurring over fixed period of time described by Lambda
# Lambda(⋋) = avg no of events per time interval
#prob of single value - if avg no of adop per wk is 8, what is P(#adoptions in wk=5)?
from scipy.stats import poisson
poisson.pmf(5,8)
# prob of <= 5?
from scipy.stats import poisson
poisson.cdf(5,8)
# prob of > 5?
1 - poisson.cdf(5,8)
# sampling from poisson distribution
from scipy.stats import poisson
poisson.rvs(8,size=10)















