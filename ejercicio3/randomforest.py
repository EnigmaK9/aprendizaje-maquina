# Carga la biblioteca con el conjunto de datos de los Iris
from sklearn.datasets import load_iris

# Carga la biblioteca de clasificacion Random Forest de scikit-learn
from sklearn.ensemble import RandomForestClassifier

# Carga la biblioteca pandas
import pandas as pd

# Carga la biblioteca numpy
import numpy as np

# Configura una semilla aleatoria
np.random.seed(0)

# Crea un objeto llamado iris con los datos de iris
iris = load_iris()


# Crea un panel de datos con las cuatro variables caracteristicas
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Ver las 5 filas superiores
df.head()

# Agrega una nueva columna con los nombres de las especies,
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Ver las 5 filas superiores
df.head()

# Create a new column that for each row, generates a random number between 0 and 1, and
# Crea una nueva columna para cada fila, genera un numero aleatorio entre 0 y 1 y 
# si el valor es menor o mayor a 0.75, entonces configura el valor de esa celda como verdadero
# y falso en cualquier otro caso. Esto es una manera rapida y sucia de asignar algunas filas
# para ser usadas como los datos de entrenamiento y algunos para ser usados como los datos de prueba.

df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75

# Ver las 5 filas superiores
df.head()



# Crea dos nuevos paneles de datos, uno con las filas de entrenamiento, otro con las filas de prueba
train, test = df[df['is_train']==True], df[df['is_train']==False]



# Muestran los numeros de observaciones para los paneles de datos de entreneamiento y prueba
print('Numero de observaciones en los datos de entrenamiento:', len(train))
print('Numero de observaciones en los datos de prueba:',len(test))


# Crea una lista de los nombres de las columnas caracteristicas

features = df.columns[:4]

# Ve las caracteristicas
features
# Entrena ['especies'] cotnieene los nombres de las especies. Antes de poder usarlas
# Necesitamox convertir cada nombre de especies en un digito. Entocnes, en este caso hay
# tres especies, que han sido codificadas entre 0,1 o 2.
y = pd.factorize(train['species'])[0]

# Ve el atributo objetivo
y
# Create a random forest Classifier. By convention, clf means 'Classifier'
clf = RandomForestClassifier(n_jobs=2, random_state=0)

# Train the Classifier to take the training features and learn how they relate
# to the training y (the species)
clf.fit(train[features], y)

# Apply the Classifier we trained to the test data (which, remember, it has never seen before)
clf.predict(test[features])
# View the predicted probabilities of the first 10 observations
clf.predict_proba(test[features])[0:10]

# Create actual english names for the plants for each predicted plant class
preds = iris.target_names[clf.predict(test[features])]


# View the PREDICTED species for the first five observations
preds[0:5]


# View the ACTUAL species for the first five observations
test['species'].head()



# Create confusion matrix
pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames=['Predicted Species'])


# View a list of the features and their importance scores
list(zip(train[features], clf.feature_importances_))

