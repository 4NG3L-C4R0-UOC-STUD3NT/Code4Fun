# https://www.pythonlikeyoumeanit.com/Module4_OOP/Special_Methods.html
# https://stackoverflow.com/questions/1436703/difference-between-str-and-repr
# https://www.geeksforgeeks.org/str-vs-repr-in-python/

def __add__(self, other):
    """ Add the unpurchased and purchased items from another shopping
        list to the present one.

        Parameters
        ----------
        other : ShoppingList
            The shopping list whose items we will add to the present one.
        Returns
        -------
        ShoppingList
            The present shopping list, with items added to it."""
    
    print(type(self))
    print(type(other))
    result = None
    if isinstance(self, ShoppingList):
        new_list = ShoppingList([])
        # populate new_list with items from `self` and `other`
        for l in [self, other]:
            new_list.add_new_items(l._needed)

            # add purchased items to list, then mark as purchased
            new_list.add_new_items(l._purchased)
            new_list.mark_purchased_items(l._purchased)
        result = new_list
    
    return result

def strike(text):
    """ Renders string with strike-through characters through it.

        `strike('hello world')` -> '̶h̶e̶l̶l̶o̶ ̶w̶o̶r̶l̶d'

        Notes
        -----
        \u0336 is a special strike-through unicode character; it
        is not unique to Python."""
    return ''.join('\u0336{}'.format(c) for c in text)

class SillyClass:
    def __getitem__(self, key):
        """ Determines behavior of `self[key]` """
        return [True, False, True, False]

    def __pow__(self, other):
        """ Determines behavior of `self ** other` """
        return "Python Like You Mean It"


class ShoppingList:
    
    def __init__(self, items):
        self._needed = set(items)
        self._purchased = set()

    def __repr__(self):
        """ Returns formatted shopping list as a string with
            purchased items being crossed out.

            Returns
            -------
            str"""
        if self._needed or self._purchased:
            remaining_items = [str(i) for i in self._needed]
            purchased_items = [strike(str(i)) for i in self._purchased]
            # You wont find the • character on your keyboard. I simply
            # googled "unicode bullet point" and copied/pasted it here.
            return "• " + "\n• ".join(remaining_items + purchased_items)

    def add_new_items(self, items):
        self._needed.update(items)

    def mark_purchased_items(self, items):
        self._purchased.update(set(items) & self._needed)
        self._needed.difference_update(self._purchased)

setattr(ShoppingList, "__add__", __add__)


silly = SillyClass()
print(silly[None])
print(silly ** 2)

food = ShoppingList(["grapes", "beets", "apples", "milk", "melon", "coffee", "flour", "salt", "eggs"])
food.mark_purchased_items(["grapes", "beets", "milk"])
print(food)
food.mark_purchased_items(["flour", "salt"])
print(food)

office_supplies = ShoppingList(["staples", "pens", "pencils"])
office_supplies.mark_purchased_items(["pencils"])

clothes = ShoppingList(["t-shirts", "socks"])

print(food + office_supplies + clothes)


