#INTRODUCING PYPLOT INTERFACE
import matplotlib.pyplot as plt
fig, ax= plt.subplots()
# adding data to axes
ax.plot(seattle_we['MONTH'], seattle_we['MLY-TAVG-NORMA'])   # plot 1
ax.plot(austin_we['MONTH'], austin_we['MLY-TAVG-NORMA'])   # plot 2
plt.show()



































