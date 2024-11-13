#INTRODUCING PYPLOT INTERFACE
import matplotlib.pyplot as plt
fig, ax= plt.subplots()
# adding data to axes
ax.plot(seattle_we['MONTH'], seattle_we['MLY-TAVG-NORMA']) #Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(austin_we['MONTH'], austin_we['MLY-TAVG-NORMA']) # Plot MLY-PRCP-NORMAL from austin_weather against MONTH
plt.show()
#CUSTOMIZING DATA APPEARANCE
# CIRCLE MARKERS - o, v
ax.plot(seattle_we['MONTH'], seattle_we['MLY-TAVG-NORMA'], marker='o')
# SETTING LINESTYLE- '--', 'None'
ax.plot(seattle_we['MONTH'], seattle_we['MLY-TAVG-NORMA'], marker='v', linestyle='--')
# CHOOSING COLOR
ax.plot(seattle_we['MONTH'], seattle_we['MLY-TAVG-NORMA'], marker='v', linestyle='--', color='r')
# CUSTOMIZE AXES LABELS
ax.set_xlabel('Time (months)')
# ADDING TITLE
ax.set_title('Weather in Seattle')






























