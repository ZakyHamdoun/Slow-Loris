# Slow Loris

L'attaque de type Slow Loris est une attaque DoS (deni de service) s'attaquant à une adresse IP précisée.
Pour faire simple, imaginez 100 grand-mères en train de discuter avec une caissière en même temps dans un supermarché, tous 
les autres clients resteront bloqués. Et bien c'est pareil mais avec un site internet au lieu d'une caissière et des requêtes
au lieu des grand-mères.

## Installation

Téléchargez le fichier. Il faut au préalable avoir les modules :
socket - random - time - sys. (Déjà présents sur Python de base).

## Usage

Après l'installation, commencez d'abord par trouver l'adresse IP de la cible (Target) recherchée.
Pour cela, utilisez l'invité de commande et exécutez la commande suivante :

```bash
ping example.com
```

Il faut ensuite lancer le programme avec l'adresse IP correspondante.
Pour cela, utilisez de nouveau l'invité de commande et exécutez la commande suivante :

```bash
python slow_loris.py 192.168.2.1
python path_to_slow_loris.py 192.168.1.1
```

Il faut bien entendu remplacer l'adresse IP par l'adresse IP de la cible.

L'attaque commencera.

## Contribution

Si vous souhaitez modifier le programme. Faites une requête pull ou une issue.
Ce sera un plaisir.

## Crédits.

Twitter : @ZakousseMC

Merci à https://github.com/adrianchifor/pyslowloris pour l'implémentation Python du slow_loris.
Vidéo très conseillée sur le principe de fonctionnement : https://www.youtube.com/watch?v=XiFkyR35v2Y.
