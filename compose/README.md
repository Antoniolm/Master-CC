## Composición de servicios

### Introducción

La imagen utilizada ha sido una imagen alpine([link](https://hub.docker.com/r/frolvlad/alpine-python3/)) con python3 y pip3 instalados. He utilizado esta imagen por dos motivos. El primer motivo es su peso de 61mb aproximadamente lo cual me permite una mayor flexibilidad.El segundo motivo es que tenga preinstalado los paquetes de python3 y pip3 los cuales son utilizados en mi proyecto.

Para esta composición de servicios se iba a realizar con el gestor de ficheros S3 de amazon, pero debido a no tener el presupusto suficiente para ello se ha decidido utilizar la segunda opción que se barajo en el comienzo de este proyecto. Dicha segunda opción era utilizar mongoDB para el almacenamiento de los objetos 3D. Se ha utilizado este enfoque en esta práctica ya que tras profundizar en las caracteristicas de mongoDB ([link](https://www.mongodb.com/blog/post/storing-large-objects-and-files-in-mongodb)) he podido llegar a la conclusión de que es una opción tan valida como la del uso de un gestor de ficheros como el ya mencionado S3 de amazon. Además, de esta forma puedo realizar una composición del servicio principal del proyecto y del servicio de mongoDB.

Se ha utilizado la plataforma azure ya que me ha permitido utilizar mi composición de servicios de una manera rápida y sin ninguna dificultad.


### Instalaciones requeridas

Se ha realizado la instalación de docker compose en su versión 1.1.8. Para ello se ha realizado el siguiente comando:

```
sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### Descripción del hito

#### Creación de la composición de servicios
Para crear la composición de servicios es tan secillo como una vez creado tanto los dockerfiles correspondientes como el docker-compose debemos utilizar
la siguient instrucción
```
sudo docker-compose up
```

#### Despliegue en azure de la composición de servicios



Realizamos la instalación de git y clonamos el repositorio
```
git clone 
```
