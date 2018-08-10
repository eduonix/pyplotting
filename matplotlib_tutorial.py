import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1000) # this ensures you get the same results as me
y = np.random.standard_normal(20) # creates a list of 20 random variables

x = range(len(y)) # creates a list of length 20
plt.plot(x, y) # plots the x and y data
plt.show() # we have to call this if our script is being run in the terminal - otherwise use jupyter notebook

'''
======================================
'''

# we could do the same with just:

plt.plot(y)
plt.show()

'''
======================================
'''

# we can also call methods on our data thanks to numpy

plt.plot(y.cumsum())
plt.show()

'''
======================================
'''

# we can specify parameters on our plt. The order doesn't matter

plt.plot(y.cumsum())
plt.grid(True)
plt.xlim(7, 15)
plt.ylim(-1,1)
plt.show()

'''
======================================
'''

# we can also style our figure size and the display of our plot

plt.figure(figsize=(10, 5))
plt.plot(y.cumsum(), 'b', lw=3)
plt.plot(y.cumsum(), 'ro')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('A simple plot')
plt.show()

'''
======================================
'''

# lastly we can also use subplots to split our plot into many plots. 
# This is quite handy as each plot is called as if it were it's own
# Note that the parameters specified after calling subplot refer to that subplot only

plt.figure(figsize=(7,5))
plt.subplot(211)
plt.plot(y.cumsum(), lw=1.5, label='This is the first plot')
plt.plot(y.cumsum(), 'ro')

plt.subplot(212)
plt.plot(y.cumsum(), label='This is the second plot')
plt.plot(y.cumsum(), 'g')
plt.show()