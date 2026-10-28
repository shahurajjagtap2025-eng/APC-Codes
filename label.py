import numpy as np

a = np.array([10, 20, 30, 40])
labels = np.array(['A', 'B', 'C', 'D'])

print("Array:", a)
print("Labels:", labels)

for label, value in zip(labels, a):
    print(label, "=", value)=