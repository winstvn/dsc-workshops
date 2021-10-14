# imports and definitions
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# for random functions
seed_number = 123

# load the dataset to pandas
from sklearn import datasets
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)


test_proportion = 0.3
X_train, X_test, y_train, y_test = train_test_split(
    df[iris.feature_names],
    iris.target,
    test_size=test_proportion,
    stratify=iris.target,
    random_state=seed_number,
)

# define the model
n_trees = 100
rf = RandomForestClassifier(
    n_estimators=n_trees, oob_score=True, random_state=seed_number
)

# train the model
rf.fit(X_train, y_train)

# save the model to a pickle file
pickle_save = 'rf-model.pkl'
with open(pickle_save, 'wb') as file:
    pickle.dump(rf, file)