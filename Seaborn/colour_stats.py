import matplotlib.pyplot as plt
import seaborn as sns

# loading dataset now

data = sns.load_dataset('iris')
# sns.boxenplot(x='species', y='petal_length', data=data)
# sns.barplot(x='species', y='sepal_length', data=data)
# sns.countplot(x='species', data=data)
sns.violinplot(x='species', y='sepal_width', data=data)
# now display
plt.show()
