
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd
from sklearn import preprocessing
# define example
data = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot', 'warm', 'cold', 'warm', 'hot']
values = array(data)
print("values:",values)

#http://www.ritchieng.com/machinelearning-one-hot-encoding/
xls="paths.xlsx"
# load dataset
X = pd.read_excel(xls,sheetname=0)
#X.head(3)

# limit to categorical data using df.select_dtypes()
#X = X.select_dtypes(include=[object])
print(X)

# TODO: create a LabelEncoder object and fit it to each feature in X


# 1. INSTANTIATE
# encode labels with value between 0 and n_classes-1.
le = preprocessing.LabelEncoder()


# 2/3. FIT AND TRANSFORM
# use df.apply() to apply le.fit_transform to all columns
X_2 = X.apply(le.fit_transform)
print("head:",X_2.head())
print("shape of X2 after transform:",X_2)
print("classes",le.classes_)
# TODO: create a OneHotEncoder object, and fit it to all of X

# 1. INSTANTIATE
enc = preprocessing.OneHotEncoder()

# 2. FIT
enc.fit(X_2)

print("shape fitttttt:",enc.fit(X_2))
# 3. Transform
onehotlabels = enc.transform(X_2).toarray()
print("shape:",onehotlabels.shape)


print(onehotlabels)
# as you can see, you've the same number of rows 891
# but now you've so many more columns due to how we changed all the categorical data into numerical data
def getLabelEncoder(values1):
 # integer encode
 label_encoder = LabelEncoder()
 integer_encoded = label_encoder.fit_transform(values1)
 print(integer_encoded)
 return integer_encoded

def getBinaryEncoder(values1):
 # binary encode
 onehot_encoder = OneHotEncoder(sparse=False)
 int_encoded=getLabelEncoder(values1)
 integer_encoded = int_encoded.reshape(len(int_encoded), 1)
 onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
 print(onehot_encoded)
 return onehot_encoded

def getEncodedPathFunction(paths):
    enc = OneHotEncoder()
    enc.fit(paths)
    #OneHotEncoder(categorical_features='all', dtype= < 'numpy.float64' >,handle_unknown = 'error', n_values = 'auto', sparse = True)
    enc.n_values_
    enc.feature_indices_
    enc.transform([[0, 1, 1]]).toarray()


# invert first example
#inverted = label_encoder.inverse_transform([argmax(onehot_encoded[0, :])])
#print("inverted",inverted)