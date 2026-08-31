"""
Demonstrates iterating over dictionary keys and key-value pairs via items().
"""

def demo_read_dict():
    post = dict(
        stid='0814747', fullname='Dilshad Abdulla',
        university='Anglia Ruskin University', location='44.2658974, -102.5586589',
        language='English'
    )

    keys_list = list(post.keys())
    items_list = list(post.items())

    print('Keys:', keys_list)
    print('Items:', items_list)

    return keys_list, items_list

if __name__ == '__main__':
    demo_read_dict()
