## Provisionamiento con Chef-solo

### Introducción
El provisionamiento de chef-solo se ha realizado sobre una máquina virtual de amazon web service. Dicha máquina
utiliza la versión 16.04 de ubuntu. Además, se ha eliminado el paquete de python3  de la máquina virtual para realizar una provisión desde una máquina con menos paquetes instalados.

### Instalaciones requeridas
Antes de comenzar a realizar el provisionamiento debemos instalar en la máquina a provisionar la aplicación chef-solo, para ello debemos introducir el siguiente comando:

```
curl -L https://www.opscode.com/chef/install.sh | bash
```

### Descripción del provisionamiento

En este provisionamiento se han instalado diversos paquetes para el correcto despliegue de nuestro microservicio. Los paquetes instalados han sido:
* **Django y Django rest framenwork** : para crear la API de nuestro sistema.
* **Python3** : Lenguaje en el que se desarrollara el proyecto.
* **Pip3** : Administrador de paquetes de python.
* **Git** : Para la gestión del proyecto.
* **Pytest** : Como framework para realizar pruebas unitarias.
* **Boto3** : SDK de Amazon Web Service(AWS) para poder utilizar el gestor de ficheros de AWS

#### Pasos realizados

Lo primero que hemos realizado para llevar a cabo el provisionamiento es la creación de la estructura de carpetas que chef-solo utiliza. Para ello hemos realizado la siguiente comando:

```
  mkdir -p chef/cookbooks/project/recipes
```

Una vez tenemos realizada dicha estructura comenzamos creando los ficheros requeridos para realizar correctamente el provisionamiento.

Primero creamos el fichero node.json en el directorio de chef. El contenido de este fichero es:
```
  {
    "run_list":["recipe[project]"]
  }
```
A continuación creamos el fichero de configuración solo.rb en el directorio de chef. El contenido de este fichero es:
```
  file_cache_path "/home/ubuntu/chef"
  cookbook_path "/home/ubuntu/chef/cookbooks"
  json_attribs "/home/ubuntu/chef/node.json"
```

Por último, creamos la receta default.rb que nos indicará que se hará en el provisionamiento. Este fichero estará ubicado en el directorio ./chef/cookbooks/projects/recipes :

```
execute "apt-get update" do
  command "apt-get update"
end

package 'python3' #will install python
package 'python3-pip' #will install pip3
package 'git'

execute "export LC_ALL=C" do
  command "export LC_ALL=C"
end

execute 'pip3 install django djangorestframework pytest boto3' do
  command "pip3 install django djangorestframework pytest boto3"
end
```

Una vez creados todos estos ficheros podemos pasar a ejecutar la provisión de la máquina virtual. Para ello realizar el siguiente comando:

```
  sudo chef-solo -c chef/solo.rb
```
Como podemos ver en la imagen hemos podido provisionar correctamente la máquina virtual de amazon

![provisionchefsolo](https://user-images.githubusercontent.com/11316534/32512107-3013b158-c3f6-11e7-9559-e8460b74277f.png)
