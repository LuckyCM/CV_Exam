import math
import numpy as np

# theta_list = [0,30,60,90,120,150]
theta_list = [0,45,90,135]
point_list = [[0,0],[1,1],[2,2],[3,0]]
r_list = np.array([0.0000000]*len(theta_list))
for j in range(len(theta_list)):
    r_list[j] = math.radians(theta_list[j])

# 长 3, 宽 2（黑白方格）roundup
a = 3
b = 2
length = math.ceil(math.sqrt(a **2 + b **2))
print("length:", length)

ans_list = np.array([[0] * len(theta_list)] * (length*2+1))

for i in range(len(point_list)):
    for j in range(len(theta_list)):

        ans = point_list[i][1] * math.cos(r_list[j]) - point_list[i][0] * math.sin(r_list[j])
        if theta_list[j] == 150 or theta_list[j] == 30:
            ans = point_list[i][1] * math.cos(r_list[j]) - point_list[i][0] * 0.5
        p = round(ans)
        ans_list[abs(4-p)][j] += 1
print(ans_list)