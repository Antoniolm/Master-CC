## Provisionamiento con ansible
El provisionamiento de ansible se ha realizado sobre una máquina virtual de amazon web service. Dicha máquina
utiliza la versión 16.04 de ubuntu.

El primer paso que he tenido que realizar ha sido instalar python en la máquina a provisionar ya que es necesarios
para la el uso de ansible. Para ello:
```
sudo apt-get install python
```

Tras tener lista la maquina a provisionar debemos añadir nuestra máquina virtual a los hosts de ansible ( /etc/ansible/hosts ).

```
[project]

52.15.144.171 ansible_user=ubuntu
```

La receta que se ha utilizado para el provisionamiento ha sido:
```
---
- hosts: 52.15.144.171
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
Como podemos ver en la imagen hemos podido provisionar correctamente la máquina virtual de amazon

![ansibledone](https://user-images.githubusercontent.com/11316534/32512096-23c7e0fe-c3f6-11e7-81d3-b2745a3dead4.png)
