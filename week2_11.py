import numpy as np

# #  3D space has coordinates [10,10,500] mm relative to the camera reference frame.
# x = 10
# y = 10
# z = 500
# # image principal point is at coordinates [244,180] pixels
# ox = 244
# oy = 180
# # magnification factors in the x and y directions are 925 and 740
# a = 925
# b = 740

#  3D space has coordinates [10,10,500] mm relative to the camera reference frame.
x = 40
y = -40
z = 400
# image principal point is at coordinates [244,180] pixels
ox = 244
oy = 180
# magnification factors in the x and y directions are 925 and 740
a = 925
b = 740
uv1 = 1/z * np.dot(np.dot(np.array([[a, 0, ox], [0, b, oy], [0, 0, 1]]), np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])), np.array([[x],[y],[z],[1]]))
print(uv1)