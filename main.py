from lxml import etree
import data_classes
import interface

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    table = interface.get_tbody("ca")
    row_lst = table.findall("./tr")
    print(len(row_lst))
    myrow = data_classes.row()
    myrow.set_row_state("ca")

    myrow.set_row_e(row_lst[2])
    myrow.parse_row_e()

    print("Trump votes")
    print(myrow.trump_votes)



