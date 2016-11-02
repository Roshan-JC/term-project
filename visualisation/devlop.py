import matplotlib.pyplot as plt

pie2_labels = 'Developed - 72 countires','Devloping - 133 countries'
pie2_sizes = []

Devloped_Total = 2715
Devloping_Total = 1893

total = Devloping_Total+Devloped_Total

pie2_sizes.append((Devloped_Total/total)*100)
pie2_sizes.append((Devloping_Total/total)*100)




colors = ['yellow', 'red']
explode = (0.1, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')


plt.pie(pie2_sizes, explode=explode, labels=pie2_labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)


plt.axis('equal')

plt.show()