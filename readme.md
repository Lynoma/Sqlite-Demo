# SQLITE DEMO

---
REQUIREMENTS
---
* sqlite3
* python3
---
Ceci est une démonstration de l'utilisation de sqlite3 avec des classes
---
* Le nom de la bdd est défini par `constants.py`, puis initalisé dans la classe `SqlHelper` 
* La classe contient deux méthodes permettant d'insérer un ou plusieurs objets
* La fonction se lance depuis `run()` dans `main.py`
---
Pour personnaliser sa bdd
---

1) Changer le nom de la bdd dans `constants.py`:
    ```py
    PATH_TO_DB = 'bin/<yourname>.db'
    ```
2) Changer la table dans `SqlHelper.py`:
    ```py
    def __init__(self):
        ...
        self.c.execute('CREATE TABLE IF NOT EXISTS <YourTable>(<colonne1> <TYPE>, <colonne2> <TYPE>, <colonne3> <TYPE>)')    
   ```
3) Changer les requêtes INSERT dans `SqlHelper.py`:
    ```py
    def add_item(self, object: <Type>):
        self.c.execute('INSERT INTO <TABLE> VALUES (?,?,?)', (object.<attribut1>, object.<attribut2>, object.<attribut3>))
    ```
    ```py
    def add_items(self, objects: list[<Type>]):
        for item in objects:
            self.c.execute('INSERT INTO <TABLE> VALUES (?,?,?)', (item.<attribut1>, item.<attribut2>, item.<attribut3>))
    ```
4) Changer la classe objet:
    ```py
    class <ClassName>:
   
   
    def __init__(self, <attr1>, <attr2>, <attr3>):
        self.<attribut1> = <attr1>
        self.<attribut2> = <attr2>
        self.<attribut3> = <attr3>
    ```

5) Changer les imports dans `Main.py` et `SqlHelper.py`:

    ```py
    from Objects.<ClassFile> import <ClassName>
    ```