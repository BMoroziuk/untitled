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
supersum = 0
for co in cot:
    URL = f"https://my.liteforex.com/ru/chart/history?symbol={co}&resolution=1D&from={time.time()-1000*86400}&to={time.time()-0*86400}"
    r = requests.get(url=URL)
    data = r.json()
    csvdata = []
    for i in range(8, len(data['c'])-1):
        csvdata.append([data['l'][i-7], data['o'][i-7], data['c'][i-7], data['h'][i-7],data['l'][i-6], data['o'][i-6], data['c'][i-6], data['h'][i-6],data['l'][i-5], data['o'][i-5], data['c'][i-5], data['h'][i-5],data['l'][i-4], data['o'][i-4], data['c'][i-4], data['h'][i-4],data['l'][i-3], data['o'][i-3], data['c'][i-3], data['h'][i-3], data['l'][i-2], data['o'][i-2], data['c'][i-2], data['h'][i-2], data['l'][i-1], data['o'][i-1], data['c'][i-1], data['h'][i-1], data['l'][i], data['o'][i], data['c'][i], data['h'][i]])
        if (data['c'][i]-data['c'][i-1] > 0.001 and 'JPY' not in co) or (data['c'][i]-data['c'][i-1] > 0.1 and 'JPY' in co):
            if co != 'AUDUSD' and co != 'EURUSD':
                csvdata[len(csvdata) - 1].append('Down')
            else:
                csvdata[len(csvdata) - 1].append('Up')
        elif (data['c'][i]-data['c'][i-1]< -0.1 and 'JPY' not in co) or (data['c'][i]-data['c'][i-1]< -0.1 and 'JPY' in co):
            if co != 'AUDUSD' and co != 'EURUSD':
                csvdata[len(csvdata) - 1].append('Up')
            else:
                csvdata[len(csvdata) - 1].append('Down')
        else:
            csvdata[len(csvdata) - 1].append('Rovno')


    with open('test.csv', 'w', newline='\n') as myfile:
        wr = csv.writer(myfile)
        for mylist in csvdata:
            wr.writerow(mylist)



    # Load dataset
    url = "test.csv"
    names = ['l-3', 'o-3', 'c-3', 'h-3','l-2', 'o-2', 'c-2', 'h-2','l-1', 'o-1', 'c-1', 'h-1','l', 'o', 'c', 'h','l0', 'o0', 'c0', 'h0','l1', 'o1', 'c1', 'h1', 'l2', 'o2', 'c2', 'h2', 'l3', 'o3', 'c3', 'h3', 'class']
    dataset = read_csv(url, names=names)
    # Split-out validation dataset
    array = dataset.values
    X = array[:,0:32]

    y = array[:,32]
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
    summ = 0
    print(co)
    i = 0
    print(LDA.predict([[data['l'][len(data['c']) - 9 + i], data['o'][len(data['c']) - 9 + i],
                          data['c'][len(data['c']) - 9 + i], data['h'][len(data['c']) - 9 + i],data['l'][len(data['c']) - 8 + i], data['o'][len(data['c']) - 8 + i],
                          data['c'][len(data['c']) - 8 + i], data['h'][len(data['c']) - 8 + i],data['l'][len(data['c']) - 7 + i], data['o'][len(data['c']) - 7 + i],
                          data['c'][len(data['c']) - 7 + i], data['h'][len(data['c']) - 7 + i],data['l'][len(data['c']) - 6 + i], data['o'][len(data['c']) - 6 + i],
                          data['c'][len(data['c']) - 6 + i], data['h'][len(data['c']) - 6 + i],data['l'][len(data['c']) - 5 + i], data['o'][len(data['c']) - 5 + i],
                          data['c'][len(data['c']) - 5 + i], data['h'][len(data['c']) - 5 + i],
                          data['l'][len(data['c']) - 4 + i], data['o'][len(data['c']) - 4 + i],
                          data['c'][len(data['c']) - 4 + i], data['h'][len(data['c']) - 4 + i],
                          data['l'][len(data['c']) - 3 + i], data['o'][len(data['c']) - 3 + i],
                          data['c'][len(data['c']) - 3 + i], data['h'][len(data['c']) - 3 + i],
                          data['l'][len(data['c']) - 2 + i], data['o'][len(data['c']) - 2 + i],
                          data['c'][len(data['c']) - 2 + i], data['h'][len(data['c']) - 2 + i]]])[0])
    print()
#     for i in range(0, -240, -1):
#
#         if (LDA.predict([[data['l'][len(data['c']) - 9 + i], data['o'][len(data['c']) - 9 + i],
#                           data['c'][len(data['c']) - 9 + i], data['h'][len(data['c']) - 9 + i],data['l'][len(data['c']) - 8 + i], data['o'][len(data['c']) - 8 + i],
#                           data['c'][len(data['c']) - 8 + i], data['h'][len(data['c']) - 8 + i],data['l'][len(data['c']) - 7 + i], data['o'][len(data['c']) - 7 + i],
#                           data['c'][len(data['c']) - 7 + i], data['h'][len(data['c']) - 7 + i],data['l'][len(data['c']) - 6 + i], data['o'][len(data['c']) - 6 + i],
#                           data['c'][len(data['c']) - 6 + i], data['h'][len(data['c']) - 6 + i],data['l'][len(data['c']) - 5 + i], data['o'][len(data['c']) - 5 + i],
#                           data['c'][len(data['c']) - 5 + i], data['h'][len(data['c']) - 5 + i],
#                           data['l'][len(data['c']) - 4 + i], data['o'][len(data['c']) - 4 + i],
#                           data['c'][len(data['c']) - 4 + i], data['h'][len(data['c']) - 4 + i],
#                           data['l'][len(data['c']) - 3 + i], data['o'][len(data['c']) - 3 + i],
#                           data['c'][len(data['c']) - 3 + i], data['h'][len(data['c']) - 3 + i],
#                           data['l'][len(data['c']) - 2 + i], data['o'][len(data['c']) - 2 + i],
#                           data['c'][len(data['c']) - 2 + i], data['h'][len(data['c']) - 2 + i]]])[0]) == 'Up':
#             # print(data['c'][len(data['c']) - 1 + i] - data['c'][len(data['c']) - 2 + i])
#             if 'JPY' in co:
#                 summ += (data['c'][len(data['c']) - 1 + i] - data['c'][len(data['c']) - 2 + i])/100
#             else:
#                 summ += data['c'][len(data['c']) - 1 + i] - data['c'][len(data['c']) - 2 + i]
#
#         elif (LDA.predict([[data['l'][len(data['c']) - 9 + i], data['o'][len(data['c']) - 9 + i],
#                             data['c'][len(data['c']) - 9 + i], data['h'][len(data['c']) - 9 + i],data['l'][len(data['c']) - 8 + i], data['o'][len(data['c']) - 8 + i],
#                             data['c'][len(data['c']) - 8 + i], data['h'][len(data['c']) - 8 + i],data['l'][len(data['c']) - 7 + i], data['o'][len(data['c']) - 7 + i],
#                             data['c'][len(data['c']) - 7 + i], data['h'][len(data['c']) - 7 + i],data['l'][len(data['c']) - 6 + i], data['o'][len(data['c']) - 6 + i],
#                             data['c'][len(data['c']) - 6 + i], data['h'][len(data['c']) - 6 + i],data['l'][len(data['c']) - 5 + i], data['o'][len(data['c']) - 5 + i],
#                             data['c'][len(data['c']) - 5 + i], data['h'][len(data['c']) - 5 + i],
#                             data['l'][len(data['c']) - 4 + i], data['o'][len(data['c']) - 4 + i],
#                             data['c'][len(data['c']) - 4 + i], data['h'][len(data['c']) - 4 + i],
#                             data['l'][len(data['c']) - 3 + i], data['o'][len(data['c']) - 3 + i],
#                             data['c'][len(data['c']) - 3 + i], data['h'][len(data['c']) - 3 + i],
#                             data['l'][len(data['c']) - 2 + i], data['o'][len(data['c']) - 2 + i],
#                             data['c'][len(data['c']) - 2 + i], data['h'][len(data['c']) - 2 + i]]])[0]) == 'Down':
#             # print(data['c'][len(data['c']) - 2 + i] - data['c'][len(data['c']) - 1 + i])
#             if 'JPY' in co:
#                 summ += (data['c'][len(data['c']) - 2 + i] - data['c'][len(data['c']) - 1 + i])/100
#             else:
#                 summ += data['c'][len(data['c']) - 2 + i] - data['c'][len(data['c']) - 1 + i]
#
#     print(summ)
#     supersum += summ
#     print()
# print(supersum)
    # KNN = KNeighborsClassifier()
    # KNN.fit(X, y)
    # print('KNN', KNN.predict([[data['o'][len(data['c'])-2], data['l'][len(data['c'])-2], data['h'][len(data['c'])-2], data['c'][len(data['c'])-2]]])[0])



