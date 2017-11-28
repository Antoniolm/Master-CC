## Provisionamiento máquina Azure

### Introducción

La automatización se ha realizado utilizando el cliente de azure. He seleccionado este cliente ya que quería probar otro tipo de servicios de virtualización de los disponibles. Además, me permitía una creación más intuitiva de las máquinas virtuales y me permitía obtener la información de una manera más sencilla que AWS.

He utilizado una imagen Debian porque tras investigar varias distribuciones de linux descubri que es una de las más ligeras y además es más segura y tiene un mejor rendimiento que otras distribuciones. Además, en el aspecto de personalización del sistema operativo supera en mucho a otras distribuciones. Todos estos aspectos me han hecho decantarme por esta distribuciones frente a otras distribuciones como centos o ubuntu.

 He utilizado la PPA de ansible ya que con el no necesito realizar instalaciones previas en la maquina a provisionar como sucede con chef-solo.

### Instalaciones requeridas
Antes de comenzar a realizar el provisionamiento debemos instalar en nuestra máquina la aplicación ansible, para ello debemos tener instalado python y su gestionador de paquetes (pip). Para instalar ansible tenemos que introducir el siguiente comando:

```
sudo pip install ansible
```
Además, tenemos que instalar el comando jq para el procesamiento de datos en formato  json, para ello:

```
sudo apt-get install jq
```

Por último, debemos realizar la instalación del cliente de azure ( si ya tienes python instalado omite ese paso)
```
sudo apt-get install python
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ wheezy main" | \
     sudo tee /etc/apt/sources.list.d/azure-cli.list

sudo apt-key adv --keyserver packages.microsoft.com --recv-keys 52E16F86FEE04B979B07E28DB02C46DF417A0893
sudo apt-get install apt-transport-https
sudo apt-get update && sudo apt-get install azure-cli
```

### Descripción del provisionamiento

#### Pasos realizados
Lo primero que debemos realizar es conectar nuestro azure client con nuestra
cuenta de azure. Para ello utilizamos el siguiente comando:
```
az login
```
Una vez introducimos el código que nos proporciona en el sitio web ya estariamos logueados.

Además, si no se ha creado un grupo en azure lo debemos crear con el siguiente comando:
```
az resource group create -l westeurope -n CCGroupEU
```
Lo siguientes es crear el script que automatizara la creación y aprovisionamiento
de una máquina virtual. El script realizado es el siguiente:

```
#!/bin/bash

echo Creando maquina virtual...
ipAddress=$(az vm create -g CCGroupEU -n TestMachine --image Debian --generate-ssh-keys | jq -r '.publicIpAddress')
echo -------------------------
echo Maquina virtual creada
echo -name : TestMachine
echo -ip : $ipAddress
echo -------------------------

echo Realizando provisionamiento...
ansible-playbook -i "$ipAddress," provision.yml -u antoniolm

```

También debemos crear la receta que utilizara nuestro script, la receta en cuestión es:
```
---
- hosts: all
  sudo: yes

  tasks:
    ##
    # Actualización del sistema
    ##
    - name: Actualización de repositorios
      apt:
          update_cache: yes
    ##
    # Instalación de paquetes necesarios.
    ##
    - name: Instalación de paquetes requeridos.
      apt: name=git state=present
      apt: name=python3 state=present
      apt: name=python3-pip state=present

    ##
    # Configuración de python3-pip
    ##
    - name: Configuración de python3-pip
      shell: export LC_ALL=C

    ##
    # Instalación de paquetes de pip
    ##
    - name: Instalación de paquetes pip
      shell: pip3 install django djangorestframework pytest boto3
```

Una vez realizado todo esto solo nos falta ejecutar el script.
```
sh acopio.sh
```

Como podemos ver en la imagen hemos podido crear y provisionar correctamente la máquina virtual de azure.

![azureshdone](https://user-images.githubusercontent.com/11316534/33094462-938c723c-cf00-11e7-9304-bad7ea15ba71.png)
