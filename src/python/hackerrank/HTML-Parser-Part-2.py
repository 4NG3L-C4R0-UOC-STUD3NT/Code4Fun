from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        #print(data)
        if '\n' not in data:
            print('>>> Single-line Comment')
            print(data)
        elif '\n' in data:
            print('>>> Multi-line Comment')
            print(data)
    def handle_data(self, data):
        #print(data)
        if data != '\n':
            print('>>> Data')
            print(data)

html = ""

html += "<!--[if IE 9]>IE9-specific content"
html += '\n'

html += "<![endif]-->"
html += '\n'

html += "<div> Welcome to HackerRank</div>"
html += '\n'

html += "<!--[if IE 9]>IE9-specific content<![endif]-->"
html += '\n'

html += "<p>Your task is to print the single-line comments,"
html += '\n'

html += "multi-line comments and the data.</p>"
html += '\n'

# html = ""
# for i in range(int(input())):
#     line = input()
#     html += line
#     html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()