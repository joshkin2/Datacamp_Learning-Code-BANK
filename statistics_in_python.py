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
# QUANTILES USING NP.LINESPACE() - start at 0, stop at 1, split into 5 intervals
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



























