# plot histogram, scatterplot, graph
plt.hist(x,y), plt.scatter(x,y), plt.plot(x,y)
# Create histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()
plt.show()
# Create histogram of co2_emission for food_category 'eggs'
food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist()
plt.show()
# build histogram with 5 bins. few bins= oversimplicity, too many bins= overcomplicate and hinder bigger picture
plt.hist(x or y, bins=5)
# Histogram of co2_emission for rice and show plot
rice_consumption['co2_emission'].hist()
plt.show()

# clean up plot
plt.clf()
# to add grid to plot
plt.grid(True)
#Plotting missing values
dogs.isna().sum().plot(kind='bar')
plt.show()
# add data to graph source
year = [1800 ,1850 ,1900] + year
pop = [1.0, 1.262, 1.650] + pop

# labelling graphs, adding title, starting y from zero
plt.xlabel("year")
plt.ylabel("population")
plt.title("World Population Projections")
plt.yticks([0,2,4,6,8,10])
plt.show()
#Layering plots and adding a legend and transparency(alpha)
dog_pack[dog_pack['sex']=='F']['height_cm'].hist(alpha=0.7)
dog_pack[dog_pack['sex']=='M']['height_cm'].hist(alpha=0.7)
plt.legend(['F', 'M'])
plt.show()

#Creating bar plots
avg_weight_by_breed.plot(kind="bar", title= "Mean Weight by Dog Breed")
plt.show()

#Creating line plots
sully.plot(x='date', y='weight_kg', kind= 'line')
plt.show()
#Rotating axis labels
sully.plot(x='date', y='weight_kg', kind= 'line', rot=45)

#Creating Scatter plots
dog_pack.plot(x='height_cm', y='wight_kg', kind= 'scatter')
