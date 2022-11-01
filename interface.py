from lxml import etree
import path_dicts

def get_tbody(state):

    with open(path_dicts.filename[state], "r", encoding="utf-8") as f:
        data = f.read()
    f.close()
    root = etree.HTML(data)
    path = path_dicts.path[state]
    tbody = root.xpath(path)[0]
    return tbody


def main():
    with open("ar.html", "r", encoding="utf-8") as f:
        data = f.read()
    f.close()

    root = etree.HTML(data)

    #print AR table




if __name__ == "__main__":
    main()