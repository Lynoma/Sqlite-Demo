from SqlHelper import SqlHelper
from Objects.Meal import Meal


def run():
    # Initialise db
    db = SqlHelper()

    meal = Meal('Thon Mayo', 'Pomme', 14)
    db.add_item(meal)

    arr = [meal, Meal('Jambon', 'Banane', 2)]
    db.add_items(arr)

    # close db
    del db
    #done

if __name__ == '__main__':
    run()
