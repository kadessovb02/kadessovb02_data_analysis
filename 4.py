import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datalist import rates
tot_sum = 0
avg = []
data = rates
month = []
days = []
days = [range(0, 23), range(23, 23+21), range(44, 44 + 31-9), range(66, 88), range(88, 109), range(109, 131), range(131, 131+23), range(154, 154 + 21),range(175, 175+22), range(197, 197+22), range(219, 219+21), range(240, 261)]
for i in range(0, 12):
    tot_sum = 0
    num = 0
    for j in days[i]:
        num += 1
        tot_sum += data[j]
    avg.append(tot_sum/num) 
heights = avg

y_pos = [23, 44, 66, 88, 109, 131, 154, 175, 197, 219, 240, 261]
data1 = {"USDCNY": data}
df = pd.DataFrame(data1)
x = np.arange(261)
plt.axis([0, 261, 6, 8])
plt.plot(x,df)
plt.plot(y_pos, heights, "r")
plt.legend(data1, loc=1)
plt.show()
