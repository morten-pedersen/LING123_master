from bs4 import BeautifulSoup, Comment

# opens the got.html file (in the same folder as this .py file)
file = open("got.html", mode="r", encoding="utf-8")
readfile = file.read()
file.close()

# uses the HTML parser from beautiful soup
html = BeautifulSoup(readfile, 'html.parser')

# finds the first comment in the document, which in this case is the unicorn
comment = html.findAll(string=lambda text:isinstance(text,Comment))
unicorn = comment[0]

# finds the <title> of the document and returns only the text inside the tags
h1 = html.title.string

# finds the content within the <meta name="keywords"> tag
meta = html.find_all('meta',{'name':'keywords'})
keyword_content_text = meta[0]['content']

# navigates to the article-body <div>, and returns all the text (stripped of tags)
# from the three <p> tags within the document. The loop also appends the <ul> and <li> 
# tags for use when saving it to the new clean HTML file
body_text = html.find(id="article-body")
p_in_body = body_text.findAll('p')
body_text = "<ul>"
for content in p_in_body[:-1]:
    body_text += f"<li>{content.get_text()}</li>"
body_text += "</ul>"

# multiline string for internal CSS
css = """
    h1 {
        text-decoration:underline;
    }
    #keywords{
        color:red;
        font-style:italic;
    }
    ul {
        list-style-type: square;
    }
"""

# variable containing a multiline string with all the content from the other variables
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

# saves a new HTML file, "got_clean.html", containing the multiline 
# string from the final_html variable
with open("got_clean.html", "w+", encoding="utf-8") as file:
    file.write(str(final_html))

