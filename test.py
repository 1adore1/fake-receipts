from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def create_image(name, phone, amount):
    amount = str(amount)
    numbers = phone.split()
    phone = f'+7 {numbers[0]} {numbers[1]}-{numbers[2]}-{numbers[3]}'
    img = Image.open('source_image.png')
    draw = ImageDraw.Draw(img)
    
    font_amount = ImageFont.truetype("fonts/TinkoffSans-Bold.ttf", 53)
    font_phone = ImageFont.truetype("fonts/TinkoffSans-Regular.ttf", 29)
    font_name = ImageFont.truetype("fonts/TinkoffSans-Regular.ttf", 28)
    font_time = ImageFont.truetype("fonts/SF-Pro-Display-Bold.otf", 28)

    img_width, img_height = img.size

    def centered_coords(text, font, y_coord):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x_coord = (img_width - text_width) // 2
        return x_coord, y_coord

    name_coords = centered_coords(name, font_name, 483)
    phone_coords = centered_coords(phone, font_phone, 662)
    amount_coords = centered_coords(f"–{amount} ₽", font_amount, 380)
    time_coords = (61, 22)

    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M")

    draw.text(name_coords, name, font=font_name, fill=(60, 42, 40))
    draw.text(phone_coords, phone, font=font_phone, fill=(71, 71, 71))
    draw.text(amount_coords, f"–{amount} ₽", font=font_amount, fill=(252, 252, 252))
    draw.text(time_coords, formatted_time, font=font_time, fill=(255, 255, 255))

    img.save('output_image.png')

create_image('Джамшенджон И.', '951 809 76 76', 33)
