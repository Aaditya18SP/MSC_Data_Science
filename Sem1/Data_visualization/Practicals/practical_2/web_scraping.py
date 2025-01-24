import requests
from bs4 import BeautifulSoup as bs
import builtwith as bw
url = "https://rethinkingsoftware.substack.com/p/why-scrum-is-stressing-you-out"
path = "scrum_blog.html"

web_page = requests.get(url)
res_status = web_page.status_code
if res_status == 200:
    with open(path, "w") as html_file:
        bs_web_page = bs(web_page.content, "lxml")
        print(type(bs_web_page))
        for (idx, content) in enumerate(bs_web_page):
            if idx > 10:
                break
            html_file.write(str(content))
            # print(str(content))

print(f"The website is built with using \n {bw.builtwith(url)}")
