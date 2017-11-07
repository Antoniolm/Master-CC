## Provisionamiento con Chef-solo

El provisionamiento de chef-solo se ha realizado sobre una máquina virtual de amazon web service. Dicha máquina
utiliza la versión 16.04 de ubuntu. Además, se ha eliminado el paquete de python3  de la máquina virtual
para realizar un despligue mas completo. Lo primero que realizamos es nuestra receta default.rb :

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

Creamos el directorio que contendra nuestra receta
```
  mkdir -p chef/cookbooks/project/recipes
```
Creamos el fichero node.json en el directorio chef:
```
  {
    "run_list":["recipe[project]"]
  }
```
Por ultimo creamos el fichero de configuración solo.rb
```
  file_cache_path "/home/ubuntu/chef"
  cookbook_path "/home/ubuntu/chef/cookbooks"
  json_attribs "/home/ubuntu/chef/node.json"
```
Por último lo ejecutamos
```
  sudo chef-solo -c chef/solo.rb
```
Como podemos ver en la imagen hemos podido provisionar correctamente la máquina virtual de amazon

![provisionchefsolo](https://user-images.githubusercontent.com/11316534/32512107-3013b158-c3f6-11e7-9559-e8460b74277f.png)
