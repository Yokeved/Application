list de 3 question reponses pour la preparation en mode test

qest_ans= [{'question':'A journalist\'s source who wants to remain anonymous may speak "on" this, or even "on deep" this','reponse': 'background'}, 
     {'question':'Hairy Himalayans herded here', 'reponse': 'yaks'}, 
     {'question':'Born in Kentucky Feb.12, 1809, Abe Lincoln lived from age 7 to 21 in this state before the move to Illinois'},{'reponse':'Indiana'} ]

- pour afficher la 1ere question reponse tu fais
qest_ans[0]
- pour la 2 
qest_ans[1]
pour afficher juste la question 
qest_ans[0]['question']
- pour afficher que la reponse
qest_ans[0]['reponse']


# model
- ici je t'ecri les commande que tu doi mettre pour enregistree les donne dans la base de donner car elle est exterieur au site meme si elle est deja connecter il faut lui dire qu'il y a eu des changement a prendre en compte
1. python manage.py makemigrations
2. python manage.py migrate

# Python on Replit

This is a template to get you started with Python on Replit. It's ready to go so you can just hit run and start coding!

## Running the repl

1. Setup a new secret environment variable (the lock icon) where the key is `SECRET_KEY` and the value is
   a randomly generated token of 32 bits of randomnese. To generate such a token type this into the shell and hit Enter:
```
python
import secrets
secrets.token_urlsafe(32)
```
2. Hit run!

See this 1 minute video for a walkthrough: [https://www.loom.com/share/ecc4e738149f4d1db3bcff01758b3e71](https://www.loom.com/share/341b5574d12040fb9fcbbff150777f1c)

## Installing packages

To add packages to your repl, you can just import directly in the file you want to use the package in, and it will automatically be installed when you press the run button. Like below:
```python
import math
import pandas as pd
```

You could also install packages by using the Replit packager interface in the left sidebar.

## Help

If you need help you might be able to find an answer on our [docs](https://docs.replit.com) page. Feel free to report bugs and give us feedback [here](https://replit.com/support).