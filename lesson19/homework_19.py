from lxml import html
import requests

url = "https://qalight.ua/"

response = requests.get(url)
html_content = response.text

# Аналіз HTML-документу з використанням lxml
tree = html.fromstring(html_content)

# 1. Заголовок сторінки (title)
title = tree.xpath('//title/text()')
print("Заголовок сторінки:", title[0] if title else "Not found")

# 2. Абзац
heading = tree.xpath('//p[@class="heading1"]/text()')
print("Абзац:", heading[0] if heading else "Not found")

# 3. Абзац2
heading2 = tree.xpath('//p[@class="main-text"]/text()')
print("Абзац2:", heading2[0] if heading2 else "Not found")

# 4. Ссылка
src = tree.xpath('//script[contains(@src,"wmac")]/@src')
print("Ссылка:", src[0] if src else "Not found")

# 5. Контент
#<meta property="og:url" content="https://qalight.ua/kursy/automation/stvorennya-proektu-avtomatizaczii-ta-napisannya-ui-testiv/">
content = tree.xpath('//meta[@property="og:url"]/@content')
print("Контент:", content[0] if content else "Not found")

# 6. Контент
#<a lang="uk" hreflang="uk" href="https://qalight.ua/kursy/automation/stvorennya-proektu-avtomatizaczii-ta-napisannya-ui-testiv/">ua</a>
link = tree.xpath('//a[@lang="uk"]/text()')
print("Контент:", link[0] if link else "Not found")

# 7. Опис сторiнки
links = tree.xpath('//meta[@name="description"]/@content')
print("Опис сторiнки:", links[0] if links else "Not found")

# 8. email
email = tree.xpath('//a[contains(@href,"mailto")]/text()')
print("email:", email[0] if email else "Not found")

# 9. logo
# <img src="https://qalight.ua/wp-content/themes/qalight/images/logo_qalight_footer.png" width="115px" height="37px" alt="qalight">
logo = tree.xpath('//img[contains(@src,"logo")]/@src')
print("logo:", logo[0] if logo else "Not found")

# 10. links in footer
# <div class="footer clearfix">
# 				<div class="logo-block">
# 					<div class="logo-image"><a href="/"><img src="https://qalight.ua/wp-content/themes/qalight/images/logo_qalight_footer.png" width="115px" height="37px" alt="qalight"></a></div>
# 					<div class="logo-text">Центр підготовки<br>IT фахівців</div>
# 				</div>
# 				<div class="social-block">
# 					<ul class="social">
# 						<li><a href="https://qalight.ua/publicoffer/" target="_blank"><span style="font-size: 13px; color: white;">Договір оферти</span></a></li>
# 						<li><a href="https://www.facebook.com/QALight" target="_blank"><span class="icon facebook"></span></a></li>
# 						<!-- <li><a href="https://new.vk.com/qalighttrainingcentre" target="_blank"><span class="icon vkontakte"></span></a></li> -->
# 						<!-- <li><a href="https://plus.google.com/+QalightUaQalight" target="_blank"><span class="icon google"></span></a></li> -->
# 						<li><a href="https://www.linkedin.com/company/qa-light" target="_blank"><span class="icon linkedin"></span></a></li>
# 						<!-- <li><a href="https://twitter.com/QA_Light" target="_blank"><span class="icon twitter"></span></a></li> -->
# 						<li><a href="https://www.youtube.com/channel/UCYcjZ9X2WOtGHgxTsg-n5zQ" target="_blank"><span class="icon youtube"></span></a></li>
# 					</ul>
# 				</div>
# 				<div class="developer-block">
# <!-- 				<p class="developer">By <a rel="nofollow" href="http://www.greenweb.com.ua" target="_blank"><img src="https://qalight.ua/wp-content/themes/qalight/images/greenweb.png" width="33px" height="17px" alt="greenweb"></a></p> -->
# 				</div>
# 			</div>

footer = tree.xpath('//div[contains(@class,"footer")]//a/@href')
for link in footer:
    print(link)