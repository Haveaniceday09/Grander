from PIL import Image, ImageDraw, ImageFont
import codecs

persons = codecs.open('sources/names.txt', encoding="utf8")
texts = codecs.open('sources/words.txt', encoding="utf8")
font = ImageFont.truetype('sources/Montserrat-Black.ttf', size=32)
template = Image.open('template/temp.jpg')
for pers in persons:
	draw_text = ImageDraw.Draw(template)
	draw_text.text((218,450), f'{pers}', font=font, fill=(0,0,0))
	template.save(pers.strip() + '.jpg')
	for i in texts:
		current = Image.open(pers.strip() + '.jpg')
		new = ImageDraw.Draw(current)
		new.text((200,500), f'{i}', font=font, fill=(0,0,0))
		current.save(pers.strip() + ' ' + i + '.jpg')