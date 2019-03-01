from id3 import Id3Estimator, export_graphviz
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn import metrics
import graphviz

feature_names = ["No. de ejemplares","Nivel de ventas","Precio"]

x = np.array([["<=4", "Buenas", "<=150"],
	[">4", "Buenas", ">150"],
	[">4", "Buenas", "<=150"],
	["<=4", "Buenas", ">150"],
	[">4", "Buenas", ">150"],
	[">4", "Bajas", ">150"],
	["<=4", "Bajas", ">150"],
	["<=4", "Bajas", ">150"],
	[">4", "Bajas", "<=150"],
	["<=4", "Bajas", "<=150"],
	["<=4", "Promedio", "<=150"],
	[">4", "Promedio", "<=150"],
	["<=4", "Promedio", ">150"],
	[">4", "Promedio", ">150"],
	[">4", "Promedio", "<=150"]])

y = np.array(["si",
	"si",
	"si",
	"si",
	"si",
	"si",
	"no",
	"si",
	"si",
	"no",
	"no",
	"no",
	"si",
	"si",
	"no"])
tamanio_test = 0.15

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = tamanio_test)

id3 = Id3Estimator()
id3.fit(x_train, y_train)
y_pred = id3.predict(x_test)
print('Tamanio test: ',tamanio_test)
print("Precisio'n:",metrics.accuracy_score(y_test, y_pred))

export_graphviz(id3.tree_, 'librerias.dot', feature_names)
with open("librerias.dot") as f:
	dot_graph = f.read()
g = graphviz.Source(dot_graph)
g.render()
g.view()