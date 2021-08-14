import numpy as np
from scipy import signal

H = (np.array([[1, 0],
             [1, 1]]))

I1 = np.array([[0,0,0],
              [1,1,0],
              [0,1,0]])

print(signal.convolve2d(H, I1, 'valid'))

H = (np.array([[0,0,0],
               [0,0,1],
               [0,0,0]]))

I1 = np.array([[0.25, 1, 0.8],
              [0.75, 1, 1],
              [0, 1, 0.4]])

print(signal.convolve2d(H, I1, 'same'))

# H = (np.array([[1, 0.5, 0.1],
#                [0.5, 0.25, 0.05],
#                [0.1, 0.05, 0.01]])).T
#
# I1 = np.array([[1,1,1],
#               [1,1,1],
#               [1,1,1]])
H = (np.array([[1, 0.5, 0.1]]))

I1 = np.array([[1,1,1],
              [1,1,1],
              [1,1,1]])


I_h = signal.convolve2d(I1, H, 'same')
I_h_hT = signal.convolve2d(I_h, H.T, 'same')
print(I_h)
print(I_h_hT)
# print(signal.convolve2d(H.T, H))