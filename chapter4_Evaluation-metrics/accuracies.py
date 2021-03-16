#!/usr/bin/env python
# coding: utf-8

# ## Accuracy implementation (simplest)

l1 = [0,1,1,1,0,0,0,1]    #true targets
l2 = [0,1,0,1,0,1,0,0]    #predicted targets

def accuracy(y_true, y_pred):
    """
    Function to calculate accuracy
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: accuracy score
    """
    # initialize a simple counter for correct predictions
    correct_counter = 0
    # loop over all elements of y_true
    # and y_pred "together"
    for yt, yp in zip(y_true, y_pred):
        if yt == yp:
            # if prediction is equal to truth, increase the counter
            correct_counter += 1
    # return accuracy
    # which is correct predictions over the number of samples
    return correct_counter / len(y_true)

print("Accuracy V1:", accuracy(l1, l2))      #0.625


# ## accuracy using scikit-learn

from sklearn import metrics
print("Accuracy using sklearn:", metrics.accuracy_score(l1, l2))      #0.625


# ## accuracy calculation with True positive, True negative, False positive, False negative

def true_positive(y_true, y_pred):
    """
    Function to calculate True Positives
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: number of true positives
    """
    # initialize
    tp = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 1 and yp == 1:
            tp += 1
    return tp


def true_negative(y_true, y_pred):
    """
    Function to calculate True Negatives
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: number of true negatives
    """
    # initialize
    tn = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 0 and yp == 0:
            tn += 1
    return tn


def false_positive(y_true, y_pred):
    """
    Function to calculate False Positives
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: number of false positives
    """
    # initialize
    fp = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 0 and yp == 1:
            fp += 1
    return fp

def false_negative(y_true, y_pred):
    """
    Function to calculate False Negatives
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: number of false negatives
    """
    # initialize
    fn = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == 1 and yp == 0:
            fn += 1
    return fn


print("Number of true positive:", true_positive(l1, l2))      #0.625

print("Number of false positive:", false_positive(l1, l2))      #0.625

print("Number of false negative:", false_negative(l1, l2))      #0.625

print("Number of true negative:", true_negative(l1, l2))      #0.625

# ### Accuracy Score = (TP + TN) / (TP + TN + FP + FN)

def accuracy_v2(y_true, y_pred):
    """
    Function to calculate accuracy using tp/tn/fp/fn
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: accuracy score
    """
    tp = true_positive(y_true, y_pred)
    fp = false_positive(y_true, y_pred)
    fn = false_negative(y_true, y_pred)
    tn = true_negative(y_true, y_pred)
    accuracy_score = (tp + tn) / (tp + tn + fp + fn)
    return accuracy_score


print("Accuracy V2:", accuracy_v2(l1, l2))      #0.625

print("Accuracy V1:", accuracy(l1, l2))      #0.625

print("Accuracy using sklearn:", metrics.accuracy_score(l1, l2))      #0.625

# ###Precision = TP / (TP + FP)

def precision(y_true, y_pred):
    """
    Function to calculate precision
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: precision score
    """
    tp = true_positive(y_true, y_pred)
    fp = false_positive(y_true, y_pred)
    precision = tp / (tp + fp)
    return precision
    # ## Bingo!!!

print("Precision:", precision(l1, l2))      #0.6666666666666666

# ###Recall = TP / (TP + FN)

def recall(y_true, y_pred):
    """
    Function to calculate recall
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: recall score
    """
    tp = true_positive(y_true, y_pred)
    fn = false_negative(y_true, y_pred)
    recall = tp / (tp + fn)
    return recall

print("Recall:", recall(l1, l2))      #0.5


# ###F1 = 2PR / (P + R)
# ###F1 = 2TP / (2TP + FP + FN)

def f1(y_true, y_pred):
    """
    Function to calculate f1 score
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: f1 score
    """
    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)
    score = 2 * p * r / (p + r)
    return score

print("F1 score:", f1(l1, l2))      #0.5714285714285715

from sklearn import metrics
print("F1 score through sklearn:", metrics.f1_score(l1, l2))      #0.5714285714285715

