from lxml import etree

def get_tbody(state):
    filename = {}
    path = {}

    filename["az"] = "az.html"
    path["az"] = "/html/body/div[position()=3]/div[position()=3]/div[position()=5]/div[position()=1]/table[position()=10]/tbody"

    filename["ca"] = "ca.html"
    path["ca"] = "/html/body/div[position()=3]/div[position()=3]/div[position()=5]/div[position()=1]/table[position()=15]/tbody"

    with open(filename[state], "r", encoding="utf-8") as f:
        data = f.read()
    f.close()
    root = etree.HTML(data)
    #print(path[state])
    tbody = root.xpath(path[state])[0]

    return tbody


def main():
    with open("ar.html", "r", encoding="utf-8") as f:
        data = f.read()
    f.close()

    root = etree.HTML(data)
    #print(root)

    tbody = root.xpath("/html/body/div[3]/div[3]/div[5]/div[1]/table[10]/tbody")[0]
    print(tbody)
    rows_lst = tbody.xpath("tr")
    print(len(rows_lst))




if __name__ == "__main__":
    main()