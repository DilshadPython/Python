# coding: utf8


class Item:
    # initialse methode or constracture methods

    def __init__(self, item_name, item_color, item_num):
        # instance variables
        self.item_name = item_name
        self.item_color = item_color
        self.item_num = item_color + '.' + item_num

    # create method insted of obj user self
    def item_detail(self):
        return '{} {}'.format(self.item_name, self.item_color)


# create two different instance object
obj_1 = Item('Carbon', 'Red', '081')
obj_2 = Item('Hydrogin', 'Green', '035')

print(obj_1.item_name, obj_1.item_color, obj_1.item_num)
print(obj_2.item_name, obj_2.item_color, obj_2.item_num)

print('**' * 30)
print('Item details one')

# here doesn't need to add the self in the method because it knows
# automatically
print(obj_1.item_detail())

print('###' * 30)

print('Item details two')
print(obj_2.item_detail())
print('==' * 30)

# here we call the method from the class we need to tell which object need
# to add the object
print(Item.item_detail(obj_1))
print(Item.item_detail(obj_2))
