"""
Overview: Backpropagation artificial neural network
"""
import numpy as np
import pandas as pd
# from random import random
# import math

f = open('backpropagation_network_info.txt', 'w')
# ------------------------------------------Data pre-processing------------------------------------- #
# import data set
dataSet = pd.read_csv("GlassData.csv")
# only take useful data, ignore ID column

X = dataSet.iloc[:, 0:9].to_numpy()
temp = dataSet.iloc[:, 9].to_numpy()

num_class = 7
y = []
for i in range(len(temp)):
    y.append([temp[i]/num_class])


# normalize data to scale inputs to identical ranges
def normalize_data(data_set):
    min_max = [[min(column), max(column)] for column in zip(*data_set)]
    for row in data_set:
        for i in range(len(row) - 1):
            row[i] = (row[i] - min_max[i][0]) / (min_max[i][1] - min_max[i][0])
    return data_set


X = normalize_data(X)

# splitting data for training (70%), validation (15%), and testing (15%)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=0)
X_train, X_validate, y_train, y_validate = train_test_split(X_train, y_train, test_size=0.15, random_state=0)

# ------------------------------------------Backpropagation ANN------------------------------------- #
'''
    Algorithm Backpropagation pseudo code
    start with randomly chosen weights
    while MSE is unsatisfactory AND computational bounds are not exceeded, do
    for each input patter x_p, 1 <= p <= P
    compute hidden node inputs (net_p,j)
    compute hidden node outputs (x_p,j)
    compute inputs to the output nodes (net_p,k)
    compute the network outputs (o_p,k)
    compute the error between o_p,k and desired output d_p,k
    modify the weights between hidden and output nodes
    modify the weights between input and hidden nodes
    end for
    end while
    end function back propagation
'''


class Backpropagation(object):
    # constant learning rate to decrease computation expense and avoid being trapped in local minima
    LEARNING_RATE = 0.5
    ACCURACY_THRESHOLD = 0.03  # early stopping validation set condition
    MOMENTUM = 0
    n_epoch = 1000
    
    def __init__(self, num_input, num_output, num_hidden):
        self.num_input = num_input
        self.num_output = num_output
        self.num_hidden = num_hidden
        
        # assume a 2-layer network because a single hidden layer can provide decent performance
        # start with randomly chosen weights between -0.5 and 0.5
        self.W1 = np.random.uniform(low=-0.5, high=0.5, size=(self.num_input, self.num_hidden))
        self.W2 = np.random.uniform(low=-0.5, high=0.5, size=(self.num_hidden, self.num_output))
        
        f.write('----------- Initial weights: ------------- \n')
        f.write('Weight matrix from input to hidden layer \n')
        f.write(str(self.W1))
        f.write('\n Weight matrix from hidden to output \n')
        f.write(str(self.W2))
        
        # initialize previous weight for momentum
        self.previous_delta1 = 0
        self.previous_delta2 = 0
    
    # -----------Supporting functions ------------- #
    def mean_squared_error(self, outputs, desired):
        # MSE = 1/P (sum(sum(|o-d|^2))
        return np.mean(np.square(outputs - desired))
    
    def sigmoid(self, activation):
        # activation transfer function f(a) = 1/(1+e^-a)
        return 1 / (1 + np.exp(-activation))
    
    def sigmoid_deriv(self, sigmoid):
        # derivative of sigmoid function
        return sigmoid * (1 - sigmoid)
    
    def activation_function(self, weights, inputs):
        # activation = sum (weight * input node value)
        activation = inputs.dot(weights)
        return activation
    
    def forward(self, inputs):
        # the feed forward phase to calculate node outputs
        
        # compute hidden node inputs (net_p,j)
        sum1 = self.activation_function(self.W1, inputs)
        out1 = self.sigmoid(sum1)
        
        # compute hidden node outputs (x_p,j)
        sum2 = self.activation_function(self.W2, out1)
        out2 = self.sigmoid(sum2)
        
        return out1, out2
    
    def backward(self, inputs, desired, hidden_in, hidden_out):
        # backward propagate error through network
        
        # compute the error between o_p,k and desired output d_p,k
        predicted_error = desired - hidden_out
        predicted_delta = predicted_error * self.sigmoid_deriv(hidden_out)
        
        hidden_error = predicted_delta.dot(self.W2.T)
        hidden_delta = hidden_error * self.sigmoid_deriv(hidden_in)
        
        # modify the weights between input and hidden nodes
        self.W1 = self.W1 + self.LEARNING_RATE * (inputs.T.dot(hidden_delta)) + (self.MOMENTUM * self.previous_delta1)
        # modify the weights between hidden and output nodes
        self.W2 = self.W2 + self.LEARNING_RATE * (hidden_in.T.dot(predicted_delta)) + \
            (self.MOMENTUM * self.previous_delta2)
        
        # update previous delta value to current, ready for next weight update
        self.previous_delta1 = np.asarray(self.W1)
        self.previous_delta2 = np.asarray(self.W2)
    
    # ------Main backpropagation training function ---------#
    def train(self, training_x, training_y, validation_x, validation_y):
        for _ in range(self.n_epoch):
            out1, out2 = self.forward(training_x)
            self.backward(training_x, training_y, out1, out2)
            
            # verify increase weight provides better accuracy, not changing weights
            hidden_in, validate_output = self.forward(validation_x)
            MSE = self.mean_squared_error(validate_output, validation_y)
            if MSE < self.ACCURACY_THRESHOLD:
                print(MSE)
                break  # if the threshold validation is met, exit training to avoid over-fitting
                # if not met, retrain so network can generalize better


# implementation of backpropagation with training and testing data
def neural_network(training_x, training_y, validation_x, validation_y, testing_x):
    predictions = []
    nn = Backpropagation(9, 6,5)
    
    nn.train(training_x, training_y, validation_x, validation_y)
    
    f.write('\n ----------- Final weights: ------------- \n')
    f.write('Weight matrix from input to hidden layer \n')
    f.write(str(nn.W1))
    f.write('\n Weight matrix from hidden to output \n')
    f.write(str(nn.W2))
    
    for row in testing_x:
        # only forward propagate through network once after weights trained
        hidden_in, prediction = nn.forward(row)
        prediction = list(prediction.ravel())
        predictions.append([np.mean(prediction)])
    return predictions


predictedVal = neural_network(X_train, y_train, X_validate, y_validate, X_test)
predictedVal = [round(val*num_class) for sublist in predictedVal for val in sublist]
y_test = [val*num_class for sublist in y_test for val in sublist]

print("Actual: " + str(y_test))
print("Predict:" + str(predictedVal))

f.write('\n ----------- Outputs: ------------- \n')
f.write("Actual: " + str(y_test) + '\n')
f.write("Predict:" + str(predictedVal) + '\n')

# ------------------------------------------Performance statistics --------------------------------- #
def eval_network(actual_output, predicted_values):
    num_class = 7
    true_positive = [0] * num_class
    false_positive = [0] * num_class
    false_negative = [0] * num_class
    confusionMatrix = [[0] * num_class for i in range(num_class)]
    
    correct = 0
    for j in range(len(actual_output)):
        answer = int(actual_output[j])
        predict = int(predicted_values[j])
        confusionMatrix[answer - 1][predict - 1] += 1
        if answer == predict:
            correct += 1
            true_positive[answer - 1] += 1
        else:
            false_positive[predict - 1] += 1
            false_negative[answer - 1] += 1
    
    precisions = []
    recalls = []
    
    for k in range(num_class):
        try:
            precision = true_positive[k] / (true_positive[k] + false_positive[k])
            recall = true_positive[k] / (true_positive[k] + false_negative[k])
            precisions.append(precision)
            recalls.append(recall)
        except ZeroDivisionError:
            precisions.append(0)  # Optionally append 0 to keep the lists consistent
            recalls.append(0)     # Optionally append 0 to keep the lists consistent

    print('Confusion Matrix:')
    for i in range(num_class):
        for j in range(num_class):
            print(confusionMatrix[i][j], end='\t')
        print()

    print('Overall accuracy:', str(round(correct / float(len(actual_output)), 3) * 100.0) + '%')
    print('Average Precision:', str(round(sum(precisions) / num_class * 100, 2)) + '%')
    print('Average Recall:', str(round(sum(recalls) / num_class * 100, 2)) + '%')


eval_network(y_test, predictedVal)

