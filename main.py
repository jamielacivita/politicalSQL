from lxml import etree
import data_classes
import interface

def make_ar():
    #make the table object.
    ar_table_obj = data_classes.Table()
    t_body = interface.get_tbody("ar")
    row_lst = t_body.findall("./tr")
    row_lst_count = len(row_lst)
    for i in range(2,row_lst_count):
        row = row_lst[i]
        ar_row_obj = data_classes.Row()
        ar_row_obj.set_row_state("ar")
        ar_row_obj.set_row_e(row)
        ar_table_obj.add_row(ar_row_obj)
    for row in ar_table_obj.row_object_lst:
        row.parse_row_e()

    print(ar_table_obj)

if __name__ == '__main__':
    make_ar()







