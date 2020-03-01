import requests
import bs4
import rstobj
from pathlib_mate import PathCls as Path

url = "https://wiki.d.163.com/index.php?title=Swords_(Diablo2)"

html = requests.get(url).text
soup = bs4.BeautifulSoup(html, "html.parser")

domain = "https://wiki.d.163.com"

def remove_empty_line(text):
    lines = list()
    for line in text.strip().split("\n"):
        if line.strip():
            lines.append(line.strip())
    return "\n".join(lines)

lines = list()

item_list = list()
for table in soup.find_all("table"):
    tr_lst = table.find_all("tr")
    if len(tr_lst) == 3:
        tr1, tr3 = tr_lst[0], tr_lst[2]
        img = tr3.find("img")
        img_link = domain + img.attrs["src"]

        tr1_content = tr1.get_text(separator="\n")
        tr1_content = tr1_content.replace("套装: \n", "套装: ")
        tr1_content = tr1_content.replace("暗金: \n", "暗金: ")
        tr1_content = remove_empty_line(tr1_content)

        tr1_lines = tr1_content.split("\n")
        title = "{} ({})".format(tr1_lines[0], tr1_lines[1])
        title_slug = title.replace(" ", "-")

        item_taozhuang_anjin = rstobj.BulletList(items=[
            tr1_lines[2], tr1_lines[3]
        ])
        img_href = "./images/{}.png".format(title_slug)


        tr3_content = tr3.get_text(separator="\n")

        print(title)

        h4 = rstobj.Header4(title=title, auto_label=True)
        lines.append(h4.render())

        img = rstobj.Image(uri=img_href)
        lines.append(img.render())

        # item_title = rstobj.CodeBlock(code=rstobj.Code(text=tr1_content))
        lines.append(item_taozhuang_anjin.render())

        lines.append("\n")

        item_description = rstobj.CodeBlock(code=rstobj.Code(text=tr3_content))
        lines.append(item_description.render())

        # dst = Path(__file__).parent.append_parts(title_slug + ".png")
        # try:
        #     with open(dst.abspath, "wb") as f:
        #         f.write(requests.get(img_link).content)
        # except:
        #     print("failed to download {}".format(title_slug))

        # break


with open("index.rst", "wb") as f:
    f.write("\n".join(lines).encode("utf-8"))