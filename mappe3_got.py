from bs4 import BeautifulSoup, Comment
import codecs

file = open("got.html", mode="r", encoding="utf-8")

readfile = file.read()

file.close()

html = BeautifulSoup(readfile, 'html.parser')

# print(html.doctype)

comment = html.findAll(string=lambda text:isinstance(text,Comment))

unicorn = comment[0]

h1 = html.title.string

meta = html.find_all('meta',{'name':'keywords'})

keyword_content_text = meta[0]['content']

body_text = html.find(id="article-body")

p_in_body = body_text.findAll('p')

body_text = "<ul>"
for things in p_in_body[:-1]:
    # print(things.get_text())
    body_text += f"<li>{things.get_text()}</li>"
body_text += "</ul>"

 
# body p:nth-child(2){}

css = """

    h1 {
        text-decoration:underline;
    }
    #keywords{
        color:red;
        font-style:italic;
    }

    

"""

final_html = (f"""
<!DOCTYPE html>
    <!--
    {unicorn}
    -->
    <html lang="en">
        <head>
        <meta charset="utf-8">
        <style>
            {css}
        </style>
        </head>
        <body>
            <h1>{h1}</h1>
                <p>Keywords: </p><p id="keywords">{keyword_content_text}</p>
                {body_text}
        </body>
    </html>
""")

with open("got_clean.html", "w+", encoding="utf-8") as file:
    file.write(str(final_html))

