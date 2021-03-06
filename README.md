# ModBusTCP_Client_Python
Basic ModBusTCP Client build in Python

# Installation
Le script Python utilise PyQt5 et pymodbus, installez les avec la commande suivante : 
```shell
pip install PyQt5 pymodbus
```

Puis importez le script Python.
```shell
wget https://raw.githubusercontent.com/AlexTheGeek/ModBusTCP_Client_Python/main/projet.py
```

# Exécution
Démarrer un serveur ModBusTCP, tel que celui-ci : https://sourceforge.net/projects/modrssim2/ sur une machine Windows 10 ou 11.
Ensuite lancez le script Python avec la commande suivante :
```shell
python3 projet.py ip port
```
* ip correspond à l'ip de la machine sur laquel tourne le serveur ModBus.
* port correspond au port du serveur ModBus.

Voici une petite vidéo de ce que vous pouvez faire et voir avec ce client, disponible sur [YouTube](https://youtu.be/KyKGT7kPINM).


# Capture d'écran du Client et explication
Client sans lumière rouge :  
![pas rouge](https://github.com/AlexTheGeek/ModBusTCP_Client_Python/blob/main/Screenshots/client_modbus_without_light.png)

Client avec lumière rouge :  
![rouge](https://github.com/AlexTheGeek/ModBusTCP_Client_Python/blob/main/Screenshots/client_modbus_with_light.png)

La jauge bleu correspond à la valeur dans la case 40001 sur 32767.
La lumière rouge apparait dès lors que la valeur dans la case 40001 est exactement à 10000.

# Crédit 
Damien Briquet   
Alexis Brunet  
INSA CVL - 4A MRI-SA
