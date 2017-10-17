# Descripción general del proyecto

## Criterios de elección
 El problema en cuestión esta relacionado con los motores gráficos. En muchas ocasiones cada vez
 que iniciamos el motor gráfico debemos cargar todos los modelos 3D que vayan a ser utilizados lo cual
 produce un tiempo de espera que en algunos casos puede ser excesivo.

## Descripción de la aplicación
 La aplicación nos permitirá la conversión de modelos 3D en estructuras de datos que serán almacenadas en una
 base de datos. El motor gráfico podrá acceder a los modelos cargados a traves de dicha aplicación optimizando asi el tiempo
 de carga de los modelos 3D.

 De esta forma podremos utilizar esta aplicación de forma externa al motor gráfico para que el
 realice la estructura del modelo 3D que después utilizara el motor gráfico.

## Arquitectura y planificación

### Arquitectura utilizada
 La arquitectura que sera utilizada sera una arquitectura de microservicios la cual ofrecera un servicio.

#### Microservicio
 El microservicio que proporcionara nuestra aplicación es:
* Gestor de modelos 3D procesados.

La aplicación constara de 3 componentes:
* Api Rest pública donde el usuario accedera a nuestro microservicio.
* El microservicio en cuestión que procesara los modelos cargados.
* Base de datos NoSql que almacenara los modelos cargados.

![esquema](https://user-images.githubusercontent.com/11316534/31681832-a5a7cf32-b378-11e7-84e4-d19c71dfaea1.png)

### Planificación

Cada hito del proyecto correspondera con los hitos de la asignatura. Los hitos son:
* Hito 2 : Provisionamiento de máquinas virtuales.
* Hito 3 : Orquestación de máquinas virtuales.
* Hito 4 : Uso de contenedores.
* Hito 5 : Combinación de infraestructuras virtuales para desplegar una aplicación completa.

## Licencia

  Este proyecto será liberado bajo la licencia [GNU GLP V3](https://github.com/Antoniolm/Master-CC/blob/master/LICENSE)
