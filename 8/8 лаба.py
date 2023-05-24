from PIL import Image, ImageDraw, ImageFont


def z1():
    a = Image.open('собачка.jpg')
    a.show()
    b = a.crop((150, 350, 450, 650))
    b.show()
    b.save('варенье вишневое.jpg')


def z2():
    a = {'23 февраля': '23.jpg', 'Новый год': 'с нг.jpg', '8 марта': '8.jpg'}
    print("У нас есть открытки к таким праздникам: 23 февраля, Новый год, 8 марта")
    b = input("Открытка к какому празднику вас интерисует? ")

    if b in a:
        x = Image.open(a[b])
        x.show()
    else:
        print("У нас нет подходящей картинки :(")


def z3():
    x = Image.open('собачка.jpg')
    a = input("Напишите, кого вы хотите поздравить с днем рождения в именительном падеже: ")

    font = ImageFont.truetype("calibri.ttf", 35)
    drawer = ImageDraw.Draw(x)
    drawer.text((15, 15), a + ", поздравляю с Днем рождения!", font=font, fill='black')

    x.show()
    x.save('др.png')

z2()
z3()
z1()