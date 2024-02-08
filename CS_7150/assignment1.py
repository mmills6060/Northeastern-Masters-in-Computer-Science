import numpy
import pandas
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()


print(cancer.keys())

data = numpy.c_[cancer.data, cancer.target]

def answer_one():
    """converts the sklearn 'cancer' bunch

    Returns:
     pandas.DataFrame: cancer data
    """
    data = numpy.c_[cancer.data, cancer.target]
    columns = numpy.append(cancer.feature_names, ["target"])
    return pandas.DataFrame(data, columns=columns)



frame = answer_one()
assert frame.shape == (len(cancer.target), 31)


def answer_two():
    """calculates number of malignent and benign

    Returns:
     pandas.Series: counts of each
    """
    cancerdf = answer_one()
    counts = cancerdf.target.value_counts(ascending=True)
    counts.index = "malignant benign".split()
    return counts

output = answer_two()
assert output.malignant == 212
assert output.benign == 357

def answer_three():
    """splits the data into data and labels

    Returns:
     (pandas.DataFrame, pandas.Series): data, labels
    """
    cancerdf = answer_one()
    X = cancerdf[cancerdf.columns[:-1]]
    y = cancerdf.target
    return X, y

x, y = answer_three()
assert x.shape == (569, 30)
assert y.shape == (569,)




# Split the dataset into training and testing sets using scikit-learn. 

def answer_four():
    """splits data into training and testing sets

    Returns:
     tuple(pandas.DataFrame): x_train, y_train, x_test, y_test
    """
    X, y = answer_three()
    return train_test_split(X, y, train_size=426, test_size=143, random_state=0)


x_train, x_test, y_train, y_test = answer_four()
assert x_train.shape == (426, 30)
assert x_test.shape == (143, 30)
assert y_train.shape == (426,)
assert y_test.shape == (143,)




# Standardize the features to have zero mean and unit variance.

# Encode the labels (Malignant: 1, Benign: 0)


# Split the dataset into training and testing sets using a reasonable split ratio
# 80% training, 20% testing


# Create a shallow neural netowkr model using tensorflow and keras. 

# Use a simple architecture with one hidden layer and an appropriate activation
# function


# compile the model with binary cross-entropy loss and the adam optimizer


# train the model on the training set for the sufficient number of epochs

from sklearn.neighbors import KNeighborsClassifier

def answer_five():
    """Fits a KNN-1 model to the data

    Returns:
     sklearn.neighbors.KNeighborsClassifier: trained data
    """
    X_train, X_test, y_train, y_test = answer_four()
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(X_train, y_train)
    return model

knn = answer_five()
assert type(knn) == KNeighborsClassifier
assert knn.n_neighbors == 1






# monitor training and consider using validation data to prevent over-fitting

# Evaluate the model on the test set. Calculate and print metrics:
# Accuracy precision  recall visualize confusion matrix

# visualize the confusion matrix to gain insights into the models performance

# use a heatmap for better clarity



