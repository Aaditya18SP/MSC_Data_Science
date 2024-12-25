import numpy as np
marks = np.array([[[20, 30, 40], [10, 20, 30]], [[1, 2, 3], [4, 5, 6]]])
ids = np.array([0, 2, 4])
print("marks are:", marks, "dimensions are:", marks.ndim, "shape are:", marks.shape)
print(marks.itemsize)
print("ids are:", ids)
