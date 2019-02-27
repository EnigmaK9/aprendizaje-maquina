# ID3 PYTHON
Implementación en python del [id3 Arboles de clasificación](https://en.wikipedia.org/wiki/ID3_algorithm). El ID3 es un algoritmo de aprendizaje máquina para construir arboles de clasificación desarrollado por Ross Quinlan en 1986.

El algoritmo es recursivo, que particiona un conjunto de datos sobre el atributo que maximiza la ganancia de información. La ganancia de información del atributo A está definida como la diferencia entre la entropía de un conjunto de datos S y el tamaño medio de los pesos de la entropía para los subconjuntos S'de S cuando se dividen en el atributo A.

La implementación fue solicitadad por [Luis Hugo León]. Un texto muy citado para el algoritmo ID3 es el de Tom Mitchell (https://www.amazon.com/Machine-Learning-Tom-M-Mitchell/dp/0070428077) 
## Ejecutando el código
Se corre el código proporcionado con el intérprete de Python:

```python id3.py ./recursos/<config.cfg>```

Donde config.cfg  es un texto plano con el archivo de configuración. El formato del archivo de configuración es un arbol sintactico abstracto de python representando un dict con los siguientes campos:

``
{
   'archivo_datos' : '\\recursos\\huachicoleo.csv',
   'data_project_columns' : ['Outlook', 'Temperature', 'Humidity', 'Windy', 'PlayTennis'],
   'atributo_objetivo' : 'PlayTennis'
}
``

Tienes que especificar

 + Direccion relativa al archivo csv archivo_datos
 + Qué columnas hay que proyectar del archivo (útil cuando tienes un gran archivo de entrada, y solo te interesa un subconjunto de columnas).
 + El Atributo objetivo, el que quieres predecir.
 


### Ejemplos
1. tennis.cfg is the 'Play Tennis' example from Machine Learning, by Tom Mitchell, also used by Dr. Lutz Hamel in his lecture notes, both referenced above.
2. credithistory.cfg is the credit risk assement example from [Artificial Intelligence: Structures and Strategies for Complex Problem Solving (6th Edition), Luger](https://www.amazon.com/Artificial-Intelligence-Structures-Strategies-Complex/dp/0321545893), see Table 10.1 & Figure 10.14 (full text is available online asof 11/19/2017).  

### Results

![results](https://github.com/tofti/python-trees/blob/master/resources/results.png "Tennis & Credit Assesment Examples")

## TODO
- Add code to classify data.
- Add code to prune rules (C4.5 modifications)
