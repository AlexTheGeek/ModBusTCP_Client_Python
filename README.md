# ModBusTCP_Client_Python
Basic ModBusTCP Client made in Python

# Installation
Le script Python utilise PyQt5 et pymodbus, installez les avec la commande suivante : 
```shell
pip install PyQt5 pymodbus
```

Puis importer le script Python.

# Exécution
Démarrer un serveur ModBusTCP, tel que celui-ci : https://sourceforge.net/projects/modrssim2/.
Ensuite lancé le script python avec la commande suivante :
```shell
python3 projet.py ip port
```
* ip correspond à l'ip de la machine sur laquel tourne le serveur ModBus.
* port correspond au port du serveur ModBus.

Voici une petite vidéo de ce que vous pouvez faire et voir avec ce client disponible sur [YouTube](https://youtu.be/KyKGT7kPINM).



# Capture d'écran du Client et explication
Client sans lumière rouge :

Client avec lumière rouge :

La jauge bleu correspond à la valeur dans la case 40001 sur 32767.
La lumière rouge apparait dès lors que la valeur dans la case 4000 est exactement à 10000.

Pour plus d'explication voici une petite vidéo (bientôt disponible).
