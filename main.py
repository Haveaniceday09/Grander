from PIL import Image, ImageDraw, ImageFont
import codecs

namestxt = codecs.open('sources/names.txt', encoding="utf8")
wordstxt = codecs.open('sources/words.txt', encoding="utf8")
font = ImageFont.truetype('sources/Montserrat-Black.ttf', size=32)

names = []
words = []

for i in namestxt:
	names.append(i.strip())

for i in wordstxt:
	words.append(i.strip())

for pers in names:
	template = Image.open('template/temp.jpg')
	draw_text = ImageDraw.Draw(template)
	draw_text.text((218,450), f'{pers}', font=font, fill=(0,0,0))
	template.save(pers + '.jpg')
	for i in words:
		current = Image.open(pers + '.jpg')
		new = ImageDraw.Draw(current)
		new.text((200,500), f'{i}', font=font, fill=(0,0,0))
		current.save(pers + ' ' + i + '.jpg')
