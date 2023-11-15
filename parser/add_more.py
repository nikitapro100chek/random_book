import xlsxwriter

from book003 import array


def writer(parametr):
    book = xlsxwriter.Workbook(r"\Users\a1\Desktop\Програмы\Книги\roman_data107.xlsx")
    page = book.add_worksheet("книга")

    row = 0
    column = 0

    page.set_column("A:A", 70)
    page.set_column("B:B", 100)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)
    page.set_column("E:E", 50)
    page.set_column("F:F", 50)
    page.set_column("G:G", 50)
    #page.set_column("H:H", 300)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        page.write(row, column+5, item[5])
        page.write(row, column+6, item[6])
        #page.write(row, column+7, item[7])
        row +=1

    book.close()

writer(array)