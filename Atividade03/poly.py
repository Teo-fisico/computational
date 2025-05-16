import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2,5,100)

# coeffs=np.random.uniform(0,1,4)
# print('coeffs')

coeffs=np.poly([-1,2,4])
print(coeffs)

coeffs_der=np.polyder(coeffs)
print(coeffs_der)

poly=np.polyval(coeffs,x)
deri=np.polyval(coeffs_der,x)

plt.plot(x,poly)
