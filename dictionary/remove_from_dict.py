"""
Demonstrates safe item removal using pop() and popitem().
"""

def demo_advanced_removal():
    post = dict(
        stid='0814747', fullname='Dilshad Abdulla',
        university='Anglia Ruskin University', location='44.2658974, -102.5586589',
        language='English'
    )

    popped_lang = post.pop('language', 'Not Found')
    # popitem() removes and returns the last key-value pair (in Py3.7+)
    last_item = post.popitem()

    print('Popped language:', popped_lang)
    print('Popped last item:', last_item)
    print('Remaining dict:', post)

    return popped_lang, last_item, post

if __name__ == '__main__':
    demo_advanced_removal()
