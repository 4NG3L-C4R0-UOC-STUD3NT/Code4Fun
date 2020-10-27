import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if level == -1: level = 0
    elif level > maxdepth: maxdepth = level
    for node in elem:
        depth(node, level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)