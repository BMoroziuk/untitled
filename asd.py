# Import the libraries
from random import randint
import requests
import time
from sklearn.linear_model import LinearRegression
cot = ['AUDUSD', 'NZDUSD',




    ]
# Create a range limit for random numbers in the training set, and a count of the number of rows in the training set


# api-endpoint

for co in cot:
    URL = f"https://my.liteforex.com/ru/chart/history?symbol={co}&resolution=5&from={time.time()-1*86400}&to={time.time()-0*86400}"

    # location given here
    # location = "delhi technological university"
    #
    # # defining a params dict for the parameters to be sent to the API
    # PARAMS = {'address': location}

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    data = r.json()


    one = data['l']


    two = data['o']


    three = data['h']


    close = data['c']




    res =[]
    rez = 0
    good = 0
    bad = 0





    # Create an empty list of the input training set 'X' and create an empty list of the output for each training set 'Y'
    TRAIN_INPUT = list()
    TRAIN_OUTPUT = list()

    # Create and append a randomly generated data set to the input and output
    for i, part in enumerate(close):
        # a = randint(0, TRAIN_SET_LIMIT)
        # b = randint(0, TRAIN_SET_LIMIT)
        # c = randint(0, TRAIN_SET_LIMIT)
        # # Create a linear function for the output dataset 'Y'
        # op = (10 * a) + (2 * b) + (3 * c)
        if i > 2:
            TRAIN_INPUT.append([one[i - 1], two[i - 1], three[i - 1], close[i - 1],one[i - 2], two[i - 2], three[i - 2], close[i - 2], one[i - 3], two[i - 3], three[i - 3], close[i - 3]])
            TRAIN_OUTPUT.append(part)

    predictor = LinearRegression(
        )  # Create a linear regression object NOTE n_jobs = the number of jobs to use for computation, -1 means use all processors
    predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)  # fit the linear model (approximate a target function)

    X_TEST = [[one[len(close) - 1], two[len(close) - 1], three[len(close) - 1], close[len(close) - 1], one[len(close) - 2], two[len(close) - 2], three[len(close) - 2], close[len(close) - 2], one[len(close) - 3], two[len(close) - 3], three[len(close) - 3], close[len(close) - 3]]]  # Create our testing data set, the ouput should be 10*10 + 2*20 + 3*30 = 230
    outcome = predictor.predict(X=X_TEST)  # Predict the ouput of the test data using the linear model

    coefficients = predictor.coef_  # The estimated coefficients for the linear regression problem.
    # print(start[a])
    # print(outcome[0])

    #res.append(outcome[0] - start[a])

    # if outcome[0] - close[len(close) - 1] > 0:
    #     rez += (close[a]-close[len(close) - 1])
    #     if (close[a]-close[len(close) - 1]) > 0:
    #         good += 1
    #     else:
    #         bad += 1
    # else:
    #     rez += (close[len(close) - 1] - close[a])
    #     if (close[len(close) - 1] - close[a]) > 0:
    #         good += 1
    #     else:
    #         bad += 1

    #print(res)
    print(co)
    # print(rez)
    # print(good)
    # print(bad)
    if outcome[0] - close[len(close)-1] < 0:
        print('SELL')
        if outcome[0] - close[len(close)-1] <-0.0003:
            print('STRONG!!!')
    elif outcome[0] - close[len(close)-1] > 0:
        print('BUY')
        if outcome[0] - close[len(close)-1] >0.0003:
            print('STRONG!!!')

    print()