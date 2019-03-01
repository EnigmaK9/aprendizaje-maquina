
from sklearn.datasets import load_iris
from sklearn.metrics import precision_recall_fscore_support
from id3 import Id3Estimator, export_graphviz
import numpy as numpy
import graphviz
import csv

data = load_iris()

tamano = int(data.data.shape[0]*0.2)

data_t = numpy.c_[data.data, data.target]


x_prueba = data.data[:tamano, :]
x_entrenamiento = data.data[tamano:, :]
y_test = data.target[:tamano]
y_train = data.target[tamano:]

id3 = Id3Estimator()
id3.fit(x_entrenamiento, y_train)

# Evaluacion
y_prediccion = id3.predict(x_prueba)

# Precision, Recall, F-Measure and support (the number of occurrences of each class in y_true).
# For each class.  precision, recall, fbeta_score, support
print(precision_recall_fscore_support(y_test, y_prediccion))


export_graphviz(id3.tree_, 'tree_p2.dot', data.feature_names)
with open("tree_p2.dot") as f:
    dot_graph = f.read()
g = graphviz.Source(dot_graph)
g.render()
g.view()
