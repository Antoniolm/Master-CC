#!/bin/bash

echo Creando maquina virtual...
ipAddress=$(az vm create -g CCGroupEU -n TestMachine --image Debian --generate-ssh-keys | jq -r '.publicIpAddress')
echo -------------------------
echo Maquina virtual creada
echo -name : TestMachine
echo -ip : $ipAddress
echo -------------------------


echo Realizando provisionamiento...
#Provisionamiento de la maquina virtual
ansible-playbook -i "$ipAddress," provision.yml -u antoniolm
