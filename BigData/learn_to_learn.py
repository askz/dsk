import pylab as plt
import numpy as np
import pandas
import random

from scipy.stats.stats import pearsonr
from sklearn.metrics import mean_squared_error
from sklearn import svm, metrics, preprocessing
from sklearn import cross_validation
from sklearn import ensemble
from sklearn.ensemble.partial_dependence import plot_partial_dependence

# reading & cleaning data
data = pandas.read_csv("data/accidents.csv",sep=',')
data = pandas.DataFrame(data=data, columns=['long','lat','lum', 'agg', 'int', 'atm', 'col', 'catr', 'infra', 'situ', 'circ', 'nbv', 'plan', 'prof', 'ttue', 'tbg', 'tbl', 'tindm'])
data.columns = ['LONGITUDE','LATITUDE','LUMIERE', 'AGGLOMERATION', 'INTERSECTION', 'CONDITION_ATMOSPHERIQUES', 'TYPE_COLLISION', 'CATEGORIE_DE_ROUTE', 'INFRASTRUCTURE', 'SITUATION', 'CIRCULATION', 'NB_VOIES', 'PLAN', 'PROFIL', 'NB_TUE', 'NB_BLESSE_GRAV', 'NB_BLESSE_LEG', 'NB_INDEMN']

## feed logic
# select all columns 
selected_features = set(data.columns)
# unselect non-features
selected_features.difference_update(['LONGITUDE','LATITUDE','NB_TUE', 'NB_BLESSE_GRAV', 'NB_BLESSE_LEG', 'NB_INDEMN'])
# data to predict
to_predict = "NB_TUE"

data = data.dropna()

print("shufling")
data.reindex(np.random.permutation(data.index))

y = data.ix[:, to_predict].astype("float64")
x = data.ix[:, selected_features].astype("float64")

print("Normalizing")
x_norm = (x - x.mean()) / (x.max() - x.min())
#remove nan columns
x_norm = x_norm.replace([np.inf, -np.inf], np.nan)
x_norm = x_norm.dropna(axis=1, how='all')
y = y.ix[x_norm.index]

print("learning")
params = {'n_estimators': 3000, 'max_depth': 9, 'min_samples_split': 1,
          'learning_rate': 0.01, 'loss': 'ls', 'verbose': 1}
regressor = ensemble.GradientBoostingRegressor(**params)

size = 9*len(x_norm)/10
size = int(size)
regressor.fit(x_norm[:size],y[:size])
expected = y[size:]
predicted = regressor.predict(x_norm[size:])
pearson = pearsonr(expected,predicted)[0]
# measures the correlation between what was predicted and what actually happened
print("Pearson coefficient: %s" % str(pearson))
# (Mean Squared Error) is a measure of the amplitude of the error
print("MSE : %s" % np.sqrt(mean_squared_error(expected, predicted)))

### feature importance
feature_importance = regressor.feature_importances_
feature_importance = 100.0 * (feature_importance / feature_importance.max())
sorted_idx = np.argsort(feature_importance)

## relative importance
# plot relative importance
plt.barh(np.arange(len(x_norm.columns)), regressor.feature_importances_[sorted_idx])
plt.yticks(np.arange(len(x_norm.columns)) + 0.25, np.array(x_norm.columns)[sorted_idx])
_ = plt.xlabel('Importance relative')
plt.savefig("relative_importance.png", bbox_inches='tight')

# shell info
print("most important features:")
i=1
for f,w in zip(x_norm.columns[sorted_idx], feature_importance[sorted_idx]):
	print("%d) %s : %d" % (i, f, w))
	i+=1
    # plot partial dependence / feature
	features = [f]
	fig, axs = plot_partial_dependence(regressor, x_norm, features, feature_names=x_norm.columns, figsize=(8, 6))
	name = f + "_partial_dependence.png"
	plt.savefig(name, bbox_inches='tight')    