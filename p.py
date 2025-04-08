import matplotlib.pyplot as plt

# define the points as lists
x = [ 0.8, 2.2, 2.8, 3.8, 5.2, 6.3, 7.3, 7.9, 9.4, 10.0 ]
y = [ 4.0, 6.0, 7.5, 12, 15, 17.5, 22, 23, 27, 30 ]

# plot as points
plt.scatter(x, y, color='black')
# add elements to the the figure
plt.xlabel('t (s)')
plt.ylabel('S (cm)')
plt.grid()
# finish the plot
plt.show()