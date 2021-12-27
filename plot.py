import hst
import matplotlib.pyplot as plt

# plotting-the-results
hst.returns.plot.bar(figsize=(12, 6))
plt.gcf().autofmt_xdate()
plt.title('Monthly Returns of Portfolio - 4 stock case', fontsize=20)
plt.ylabel('Return %', fontsize=15)
plt.xlabel('Dates', fontsize=15)
# plt.savefig('Portfolio Bar Returns.png')
plt.show()