from captcha.image import ImageCaptcha

image = ImageCaptcha(width=280, height=90)

captcha_text = "J A B E D"

data = image.generate(captcha_text)

image.write(captcha_text, 'CAPTCHA.png')
