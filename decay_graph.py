import numpy as np
import matplotlib.pyplot as plt


eps = 1.0
eps_end = 0.01
eps_decay = 0.9995
e = []
for i in range(10_000):
    eps = max(eps_end, eps_decay*eps)
    # if eps == eps_end:
    #print(i, eps)
    e.append(eps)

plt.plot(np.arange(len(e)), e)
plt.savefig('decay_graph.png')
plt.show()
