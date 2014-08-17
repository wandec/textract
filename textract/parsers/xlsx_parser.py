import xlrd


def extract(filename, **kwargs):
    """Extract text from Excel files(.xls/xlsx).
    """

    workbook = xlrd.open_workbook(filename)
    sheets_name = workbook.sheet_names()
    output = "\n"
    for names in sheets_name:
        worksheet = workbook.sheet_by_name(names)
        num_rows = worksheet.nrows
        num_cells = worksheet.ncols

        for curr_row in range(num_rows):
            row = worksheet.row(curr_row)
            new_output = []
            for index_col in xrange(num_cells):
                value = worksheet.cell_value(curr_row, index_col)
                if value:
                    if isinstance(value, (int, float)):
                        value = unicode(value)
                    new_output.append(value)
            if new_output:
                output += u' '.join(new_output) + u'\n'
    return output.encode('utf-8')
