from threading import Timer


def hello():
    print('Timer Thread')


t = Timer(5.0, hello)
t.start()

print('Main Thread')