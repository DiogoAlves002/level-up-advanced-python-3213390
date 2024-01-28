
def html2markdown(html):
    '''Take in html text as input and return markdown'''
    
    # italics
    html = html.replace("<em>", "*")
    html = html.replace("</em>", "*")

    # white spaces
    html = " ".join(html.split())

    # paragraphs
    while "</p>" in html:
        end_of_p = html.find("</p>")
        if html[end_of_p + 4: end_of_p + 4 + 3] == "<p>": # consecutive paragraphs -> \n\n
            print("yo")
            html = html.replace("<p>", "", 2)
            html = html.replace("</p>", "\n\n", 1)
            html = html.replace("</p>", "", 1)
        else:
            html = html.replace("<p>", "")
            html = html.replace("</p>", "")

    # urls
    while "<a" in html:
        a_pos = html.find("<a")
        before_a = html[: a_pos]

        href_pos = html.find("\"", a_pos) + 1
        href_end = html.find("\"", href_pos + 1)
        href = html[href_pos : href_end]

        link_pos = html.find(">", href_end) + 1
        link_end = html.find("</", link_pos)
        link = html[link_pos : link_end]

        a_end = html.find(">", link_end) + 1
        after_a = html[a_end:]

        html = before_a + f'[{link}]({href})' + after_a

    return html