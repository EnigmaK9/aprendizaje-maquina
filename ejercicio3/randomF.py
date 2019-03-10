import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn import preprocessing

info = ({'Ejemplares': ['<=4', '>4', '>4', '<=4', '>4', '>4', '<=4', '<=4', '>4', '<=4', '<=4', '>4', '<=4', '>4', '>4'],
	 'Ventas': ['Buenas', 'Buenas', 'Buenas', 'Buenas', 'Buenas', 'Bajas', 'Bajas', 'Bajas', 'Bajas', 'Bajas', 'Promedio', 'Promedio', 'Promedio', 'Promedio', 'Promedio'],
	 'Precio': ['<=150', '>150', '<=150', '>150', '>150', '>150', '>150', '>150', '<=150', '<=150', '<=150', '<=150', '>150', '>150', '<=150'],
	 'Etiquieta': ['si', 'si', 'si', 'si', 'si', 'si', 'no', 'si', 'si', 'no', 'no', 'no', 'si', 'si', 'no']})
data = pd.DataFrame(info)
print(data)
for column in data.columns:
    if data[column].dtype == type(object):
        le = preprocessing.LabelEncoder()
        data[column] = le.fit_transform(data[column])

X = data[['Ejemplares', 'Ventas', 'Precio']]
y = data['Etiquieta']
tamanio_test = 0.1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = tamanio_test)
print ('Tamanio de conjunto test:',tamanio_test)

rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train,y_train)
y_pred = rf.predict(X_test)

print("Precision:",metrics.accuracy_score(y_test, y_pred))
