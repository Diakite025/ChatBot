# ProjetChatBot

## HOW TO RUN

1. create venv (recommended)
```bash
python3 -m venv venv
```

2. activate it
```bash
source venv/bin/activate
```

3. install dependancies
```bash
pip install -r requirements.txt
```

4. 
## re train the model
you can re train the model by simply execute the ModeleChatBot.ipynb file

## use pre trained model
you can find a model [Here](https://www.mediafire.com/file/ywbadjz9pe7zxmn/ModelChatBot.zip/file) uncompress it and replace the directory ModelChatBot by the one you have download

5. run app
```bash
streamlit run main.py
```

## Exemple de question
```
Bonjour
Donne-moi des informations détaillées sur la batterie numéro 7417940528182
Donne-moi les batteries avec une tension supérieure à 3
Donne-moi les batteries avec un poids compris entre 20.0 et 30.0
Quelles sont les batteries avec une capacité inférieure à 1000 mAh ?
Donne-moi les batteries de marque Samsung disponibles
Merci
Au revoir
```