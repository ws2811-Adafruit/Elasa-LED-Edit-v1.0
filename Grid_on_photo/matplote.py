import matplotlib.pyplot as plt

fig=plt.figure()
ax = fig.add_subplot(111)

ax.plot([1,2,3],[2,3,4],'ro')

for xmaj in ax.xaxis.get_majorticklocs():
  ax.axvline(x=xmaj,ls='-')
for xmin in ax.xaxis.get_minorticklocs():
  ax.axvline(x=xmin,ls='--')

for ymaj in ax.yaxis.get_majorticklocs():
  ax.axhline(y=ymaj,ls='-')
for ymin in ax.yaxis.get_minorticklocs():
  ax.axhline(y=ymin,ls='--')
plt.show()