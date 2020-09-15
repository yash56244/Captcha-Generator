from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont
from random import randint

app = Flask(__name__)
def character():
    characters = []
    az = []
    AZ = []
    num = []
    for i in range(48, 58):
        num.append(chr(i))
    characters.append(num)
    for i in range(65, 91):
        az.append(chr(i))
    characters.append((az))
    for i in range(97, 123):
        AZ.append(chr(i))
    characters.append(AZ)
    characters = characters[randint(0, 2)]
    return characters[randint(0, len(characters) - 1)]

def captcha(length):
    img = Image.new("RGB", (200, 100), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("static/Pacifico.ttf", 40)
    text = ""
    for i in range(length):
        rcharacter = character()
        text += rcharacter
        rlen = randint(0, 8)
        draw.text((25*(i+1) + rlen, 15 + 2*rlen), rcharacter, (0, 0, 0), font)
    img.save("static/captcha/" + text + ".jpg")
    return text + ".jpg"
    
@app.route('/')
def home():
    img = captcha(randint(4, 6))
    request_xhr_key = request.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key == 'XMLHttpRequest':
        return img
    return render_template("home.html", img=img)

if __name__ == "__main__":
    app.run(debug=True)