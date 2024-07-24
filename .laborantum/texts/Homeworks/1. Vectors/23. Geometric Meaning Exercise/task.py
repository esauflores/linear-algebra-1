import numpy as np
import math

x_abs = 4
y_abs = 3
theta = math.pi / 6

dot_product = x_abs * y_abs * math.cos(theta)
proj_x_to_y = y_abs * math.cos(theta)

answer = {
    "dot_product": dot_product,
    "proj_x_to_y": proj_x_to_y,
}

print(answer)
