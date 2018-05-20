

def get_src_dst(sheet):
    cells = []  #declare a list to store cells' values
    for i in range(1, 16): #40 is a tentative number that should be enough to cover the whole request's table
        columns = [] #a list to store all values in a column
        for j in range(10, 14):
            columns.append(sheet.cell(column=i, row=j).value)
        cells.append(columns)

    src = []
    dst = []
    for column in cells:
        # print(column[0])
        if not src:
            if "IP Address / Netmask" == column[0]:
                src.append(column)
        else:
            if "IP Address / Netmask" == column[0]:
                dst.append(column)
    src = src[0][1:]
    dst = dst[0][1:]
    return src, dst




