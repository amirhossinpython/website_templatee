
import requests
from bs4 import BeautifulSoup

# URL وب‌سایت مورد نظر
url = 'ادرس سایت مورد نظر'

# ارسال درخواست GET به URL وب‌سایت
response = requests.get(url)

# بررسی موفقیت درخواست
if response.status_code == 200:
    # پردازش محتوای HTML با استفاده از BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # استخراج قالب وب‌سایت
    website_template = soup.prettify()

    # استخراج کدهای CSS
    css_code = ''
    for style in soup.find_all('style'):
        css_code += style.get_text()

    # استخراج کدهای JavaScript
    js_code = ''
    for script in soup.find_all('script'):
        if script.get('src') is None:
            js_code += script.get_text()

    # ذخیره قالب وب‌سایت، کد CSS و کد JavaScript در فایل‌های متنی
    with open('website_hack.txt', 'w', encoding='utf-8') as file:
        file.write(website_template)

    with open('css_code.css', 'w', encoding='utf-8') as file:
        file.write(css_code)

    with open('js_code.js', 'w', encoding='utf-8') as file:
        file.write(js_code)

else:
    print('Error:', response.status_code)
    
