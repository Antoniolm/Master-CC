# Descripción general del proyecto

## Criterios de elección
 El problema en cuestión esta relacionado con los motores gráficos. En muchas ocasiones cada vez
 que iniciamos el motor gráfico debemos cargar todos los modelos 3D que vayan a ser utilizados lo cual
 produce un tiempo de espera que en algunos casos puede ser excesivo.

## Descripción de la aplicación
 La aplicación nos permitirá la conversión de modelos 3D en estructuras de datos que serán almacenadas en formato json dentro de un gestor de ficheros. El motor gráfico podrá acceder a los modelos cargados a traves de dicha aplicación optimizando asi el tiempo
 de carga de los modelos 3D.

 De esta forma podremos utilizar esta aplicación de forma externa al motor gráfico para que el
 realice la estructura del modelo 3D que después utilizará el motor gráfico.

## Arquitectura y planificación

### Arquitectura utilizada
 La arquitectura que será utilizada sera una arquitectura de microservicios la cual ofrecera un unico servicio.

#### Microservicio
 El microservicio que proporcionara nuestra aplicación es:
* Gestor de modelos 3D procesados.

#### Componentes
El proyecto constara de 3 componentes:
* Api Rest pública la cual utilizara nuestro usuario para acceder a nuestro microservicio.
* El microservicio en cuestión que procesara los modelos cargados.
* Gestor de ficheros de Amazon web service.

![esquema](https://user-images.githubusercontent.com/11316534/32897740-aeeb4d96-cae6-11e7-9a81-a0696e63f1b6.png)

### Planificación

Cada hito del proyecto correspondera con los hitos de la asignatura. Los hitos son:
* Hito 2 : Provisionamiento de máquinas virtuales.
* Hito 3 : Automatización de la creación máquinas virtuales.
* Hito 4 : Uso de contenedores.
* Hito 5 : Combinación de infraestructuras virtuales para desplegar una aplicación completa.

### Provisionamiento
El provisionamiento se ha realizado utilizando máquinas virtuales de Amazon web service con la versión 16.04 de Ubuntu. Se han utilizado este tipo de máquinas porque son parte de la versión gratuita (temporal) del servició de Amazon Web Service
Se han realizado dos provisiones cada uno con una aplicación diferente. Uno utilizando ansible como provisionador y otro utilizando chef-solo.

#### Ansible
Ansible ha sido mi primera opción para provisionar la máquina virtual debido a
que no tenemos que realizar el provisonamiento desde dentro de la máquina como ocurre con chef-solo, por ello veo una mejor opción ansible para realizar un provisionamiento a multiples máquinas a la vez. Para mas información -> [Readme](https://github.com/Antoniolm/Master-CC/blob/master/provision/ansible/README.md)

#### Chef-solo
Chef-solo se ha utiizado por su rapida instalacción y su facilidad de uso. Ya que nos permite provisionar de una forma sencilla una maquina virtual. Aunque tiene el problema de que se debe provisionar ella misma como ya se menciono anteriormente.
Para mas información -> [Readme](https://github.com/Antoniolm/Master-CC/blob/master/provision/chef-solo/README.md)

### Automatización
La automatización se ha realizado utilizando el cliente de azure. He seleccionado este cliente ya que quería probar otro tipo de servicios de virtualización de los disponibles.
La imagen utilizada ha sido Debian 8 para comprobar que nuestro provisionamiento funciona correctamente en diferentes sistemas.
Para mas información -> [Readme](https://github.com/Antoniolm/Master-CC/blob/master/automatizacion/README.md)

Despliegue:52.166.220.63

## Licencia

  Este proyecto será liberado bajo la licencia [GNU GLP V3](https://github.com/Antoniolm/Master-CC/blob/master/LICENSE)
