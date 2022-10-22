from matplotlib import pyplot as plt
import numpy as np
from profile import Profile

def to_str(var):
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]

t = Profile(300, 15, 20, 50)

steps = [x for x in np.arange(0, 120, 1)]
results = []

for step in steps:
    
    t.crop(step)
    res = t.getResult()
    print("step:" + to_str(step) + " --> " + to_str(res))
    results.append(res)

plt.plot(steps, results, "o:r")
plt.show()

