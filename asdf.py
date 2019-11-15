# visualize the data
import csv
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
import requests
import time
# Load dataset
URL = f"https://my.liteforex.com/ru/chart/history?symbol=AUDUSD&resolution=5&from={time.time()-1*86400}&to={time.time()-0*86400}"
r = requests.get(url=URL)
data = r.json()['c']
csvdata = []
for i in range(4, len(data)):
    csvdata.append([j for j in data[i-4:i+1]])

with open('test.csv', 'w') as myfile:
    wr = csv.writer(myfile)
    for mylist in csvdata:
        wr.writerow(mylist)






url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
print('sdfsdfsdfsdf',dataset,'asdasdasdasdasd')
# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()
# histograms
dataset.hist()
pyplot.show()
# scatter plot matrix
scatter_matrix(dataset)
pyplot.show()