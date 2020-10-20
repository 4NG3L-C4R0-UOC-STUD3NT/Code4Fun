from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attributes):
        print(tag)
        for attribute in attributes:
            print("-> %s > %s" % (attribute[0], attribute[1]))

    def handle_startendtag(self, tag, attributes):
        print(tag)
        for attribute in attributes:
            print("-> %s > %s" % (attribute[0], attribute[1]))


html = '<head>'
html += '<title>HTML</title>'
html += '</head>'
html += '<object type="application/x-flash" '
html += '  data="your-file.swf" '
html += '  width="0" height="0">'
html += '  <!-- <param name="movie" value="your-file.swf" /> -->'
html += '  <param name="quality" value="high"/>'
html += '</object>'

# html = ""
# for i in range(input()):
#     line = input()
#     html += line
#     html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()