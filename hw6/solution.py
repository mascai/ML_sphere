import numpy
import pandas
import sklearn.ensemble


train = pandas.read_csv('Train.csv')
test = pandas.read_csv('Test.csv')

train = train.replace(numpy.nan, -999)
test = test.replace(numpy.nan, -999)

COLUMNS = ['street_id', 'build_tech', 'floor', 'area', 'rooms', 'balcon', 'metro_dist', 'g_lift', 'n_photos']

y = train['price'].values
X = train[COLUMNS].values
Xt = test[COLUMNS].values

mdl = sklearn.ensemble.RandomForestRegressor()

mdl.fit(X, y)

preds = mdl.predict(Xt)

test['price'] = preds

test[['id', 'price']].to_csv('sub.csv', index=False)
