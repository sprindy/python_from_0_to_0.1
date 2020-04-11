from matplotlib import pyplot as plt

# plt.plot([1, 2, 3, 4], [1, 4, 2, 3])  # MATLAB plot.

plt.bar([2001, 2002, 2003, 2004], [1, 4, 2, 3])
plt.title("simple plot")
plt.xlabel("Year")
plt.ylabel("Counter")
plt.xticks(rotation=45)
plt.show()