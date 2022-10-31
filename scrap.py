print(row3)
print(row3.tag)
row3col1 = root.xpath("./body/tbody/tr[position()=3]/td[position()=1]/a")[0]
print(row3col1)
print(row3col1.tag)
print(row3col1.text)

row3col2 = root.xpath("./body/tbody/tr[position()=3]/td[position()=2]/b")[0]
print(row3col2)
print(row3col2.tag)
print(row3col2.text)

row3col3 = root.xpath("./body/tbody/tr[position()=3]/td[position()=3]/i")[0]
print(row3col3)
print(row3col3.tag)
print(row3col3.text)

def get_root(filename = "/home/jamie/Documents/source/alabamaTable/data.html"):
    data = open(filename, 'r').read()
    root = etree.HTML(data)
    return root

def print_data_file(filename = "/home/jamie/Documents/source/alabamaTable/data.html"):
    # Use a breakpoint in the code line below to debug your script.
    with open(filename,"r",encoding="utf-8") as f:
        data = f.read()
    f.close()

    print(data)


    for row in row_lst:
        #make a new blank row
        row_obj = data_classes.row()
        row_obj.set_row_e(row)
        row_objects.append(row_obj)

    print(len(row_objects))
    t = data_classes.table()

    for row in row_objects:
        t.add_row(row)

    print(t)
    print(t.write_sql())