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
1. huachicoleo.cfg es el ejemplo de robo de combustible de la clase de Hugo León Estrada
### Resultados

![results](https://github.com/EnigmaK9/id3-aprendizaje/blob/master/ejercicio1/recursos/Resultados.png "Ejemplo Robo de Combustible")

## TODO
- Agregar código para clasificar los datos
- Agregar código para las reglas de poda (Modificaciones C4.5)
