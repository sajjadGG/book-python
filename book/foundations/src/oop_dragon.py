class Dragon:
    pass


wawelski = Dragon(name='Wawelski', pos_x=0, pos_y=0)

wawelski.move(left=10, down=20)
wawelski.move(right=15, up=5)

wawelski.hit(10)
wawelski.hit(50)
wawelski.hit(35)
wawelski.hit(20)
