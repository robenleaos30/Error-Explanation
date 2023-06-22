IndexError
fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)

KeyError
facebook_posts = [
    {'like': 21, 'comment': 2},
    {'like': 21, 'comment': 2},
    {'share': 21, 'comment': 2},
    {'share': 21, 'comment': 2},
    {'like': 21, 'comment': 2}
]
like_posts = 0
for post in facebook_posts:
    try:
        like_posts += post['like']
    except KeyError:
        pass
        # like_posts += 0
print(like_posts)


