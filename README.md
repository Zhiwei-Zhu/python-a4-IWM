# python-a4-IWM
rendu pour cours de python

stressfulgame => jeu pygame
django :
  - projet => socket
  - projet_test => CRUD

lancer le jeu :
   - cd stressfulgame
   - python game.py ou python3 game.py
 
lancer le CRUD:
   - cd projet_test
   - python manage.py runserver

lancer le socket:
   - cd projet_test
   - docker run -p 6379:6379 -d redis:5
   - python manage.py runserver
