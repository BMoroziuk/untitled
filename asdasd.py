# compare algorithms
from pandas import read_csv
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

import csv
import requests
import time
cot = ['EURUSD', 'USDCHF', 'GBPUSD', 'USDJPY', 'EURJPY', 'AUDUSD', 'NZDUSD',


    'EURGBP', 'USDCAD',   'EURCHF',  'EURAUD',

     'USDSGD'];

for co in cot:
    URL = f"https://my.liteforex.com/ru/chart/history?symbol={co}&resolution=60&from={time.time()-365*86400}&to={time.time()-0*86400}"
    r = requests.get(url=URL)
    data = r.json()
    csvdata = []
    for i in range(4, len(data['c'])-1):
        csvdata.append([data['l'][i-3], data['o'][i-3], data['c'][i-3], data['h'][i-3], data['l'][i-2], data['o'][i-2], data['c'][i-2], data['h'][i-2], data['l'][i-1], data['o'][i-1], data['c'][i-1], data['h'][i-1], data['l'][i], data['o'][i], data['c'][i], data['h'][i]])
        if data['c'][i]>data['c'][i-1]:

            csvdata[len(csvdata) - 1].append('Up')
        elif data['c'][i]<data['c'][i-1]:

            csvdata[len(csvdata) - 1].append('Down')
        else:
            csvdata[len(csvdata) - 1].append('Rovno')


    with open('test.csv', 'w', newline='\n') as myfile:
        wr = csv.writer(myfile)
        for mylist in csvdata:
            wr.writerow(mylist)



    # Load dataset
    url = "test.csv"
    names = ['l0', 'o0', 'c0', 'h0','l1', 'o1', 'c1', 'h1', 'l2', 'o2', 'c2', 'h2', 'l3', 'o3', 'c3', 'h3', 'class']
    dataset = read_csv(url, names=names)
    # Split-out validation dataset
    array = dataset.values
    X = array[:,0:16]

    y = array[:,16]
    X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

    # Spot Check Algorithms
    models = []

    models.append(('LDA', LinearDiscriminantAnalysis()))
    # models.append(('KNN', KNeighborsClassifier()))
    # models.append(('CART', DecisionTreeClassifier()))



    # evaluate each model in turn
    results = []
    names = []
    for name, model in models:

        kfold = StratifiedKFold(n_splits=10, random_state=1)

        cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')

        results.append(cv_results)
        names.append(name)

        print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

    # Compare Algorithms
    # pyplot.boxplot(results, labels=names)
    # pyplot.title('Algorithm Comparison')
    # pyplot.show()

    # print([data['o'][len(data['c'])-2], data['l'][len(data['c'])-2], data['h'][len(data['c'])-2], data['c'][len(data['c'])-2]])
    #
    LDA = LinearDiscriminantAnalysis()
    LDA.fit(X, y)
    print(co)
    print(LDA.predict([[data['l'][len(data['c'])-5], data['o'][len(data['c'])-5], data['c'][len(data['c'])-5], data['h'][len(data['c'])-5], data['l'][len(data['c'])-4], data['o'][len(data['c'])-4], data['c'][len(data['c'])-4], data['h'][len(data['c'])-4], data['l'][len(data['c'])-3], data['o'][len(data['c'])-3], data['c'][len(data['c'])-3], data['h'][len(data['c'])-3],data['l'][len(data['c'])-2], data['o'][len(data['c'])-2], data['c'][len(data['c'])-2], data['h'][len(data['c'])-2]]])[0])
    print()
    # KNN = KNeighborsClassifier()
    # KNN.fit(X, y)
    # print('KNN', KNN.predict([[data['o'][len(data['c'])-2], data['l'][len(data['c'])-2], data['h'][len(data['c'])-2], data['c'][len(data['c'])-2]]])[0])



