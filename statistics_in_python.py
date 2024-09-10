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
























