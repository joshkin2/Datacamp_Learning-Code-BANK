# plot histogram, scatterplot, graph
plt.hist(x,y), plt.scatter(x,y), plt.plot(x,y)
# display graph- nothing goes in parenthesis
plt.show()
# build histogram with 5 bins. few bins= oversimplicity, too many bins= overcomplicate and hinder bigger picture
plt.hist(x or y, bins=5)
# clean up plot
plt.clf()
# labelling graphs, adding title, starting y from zero
plt.xlabel("year")
plt.ylabel("population")
plt.title("World Population Projections")
plt.yticks([0,2,4,6,8,10])
plt.show()
# add data to graph source
year = [1800 ,1850 ,1900] + year
pop = [1.0, 1.262, 1.650] + pop
# import decision trees scikit-learn libraries
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion matrix
