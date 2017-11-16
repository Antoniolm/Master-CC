# Master-CloudComputing Proyecto

## Descripción general del proyecto

### Criterios de elección
El problema en cuestión esta relacionado con los motores gráficos. En muchas ocasiones cada vez
que iniciamos el motor gráfico debemos cargar todos los modelos 3D que vayan a ser utilizados lo cual
produce un tiempo de espera que en algunos casos puede ser excesivo.

## Descripción de la aplicación
La aplicación nos permitirá la conversión de modelos 3D en estructuras de datos que serán almacenadas en formato json dentro de un gestor de ficheros. El motor gráfico podrá acceder a los modelos cargados a traves de dicha aplicación optimizando asi el tiempo de carga de los modelos 3D.

De esta forma podremos utilizar esta aplicación de forma externa al motor gráfico para que el realice la estructura del modelo 3D que después utilizará el motor gráfico.

Sitio web del proyecto en cuestión -> https://antoniolm.github.io/Master-CC/

## Arquitectura y planificación

### Arquitectura utilizada
La arquitectura que será utilizada sera una arquitectura de microservicios la cual ofrecera un unico servicio. El cual se encargara de gestionar los modelos 3D procesador.

#### Componentes
El proyecto constara de 3 componentes:
* Api Rest pública la cual utilizara nuestro usuario para acceder a nuestro microservicio.
* El microservicio en cuestión que procesara los modelos cargados.
* Gestor de ficheros de Amazon web service.

### Provisionamiento
El provisionamiento se ha realizado utilizando máquinas virtuales de Amazon web service con la versión 16.04 de Ubuntu. Se han utilizado este tipo de máquinas porque son parte de la versión gratuita (temporal) del servició de Amazon Web Service
Se han realizado dos provisiones cada uno con una aplicación diferente. Uno utilizando ansible como provisionador y otro utilizando chef-solo.

#### Ansible
Ansible ha sido mi primera opción para provisionar la máquina virtual debido a
que no tenemos que realizar el provisonamiento desde dentro de la máquina como ocurre con chef-solo, por ello veo una mejor opción ansible para realizar un provisionamiento a multiples máquinas a la vez.
Para mas información -> [Readme](https://github.com/Antoniolm/Master-CC/blob/master/provision/ansible/README.md)

#### Chef-solo
Chef-solo se ha utilizado por su rapida instalacción y su facilidad de uso. Ya que nos permite provisionar de una forma sencilla una maquina virtual. Aunque tiene el problema de que se debe provisionar ella misma como ya se menciono anteriormente.
Para mas información -> [Readme](https://github.com/Antoniolm/Master-CC/tree/master/provision/chef-solo)

## Licencia

Este proyecto será liberado bajo la licencia [GNU GLP V3](https://github.com/Antoniolm/Master-CC/blob/master/LICENSE)
