# """
#     读取excel的工具:不要试图去理解它，没用。能用就行了
# """
# import xlrd

# def read_excel(excel_path, sheet_name, skip_first=True):
#     """
#         读取excel的方法
#     """

#     results = []
#     datas = xlrd.open_workbook(excel_path)  # 打开excle，并返回excel的对象
#     table = datas.sheet_by_name(sheet_name) # 在excel中读取sheet_name的页面
#     if skip_first is True:
#         start_row = 1
#     else:
#         start_row = 0

#     # 循环读取每一行的信息
#     for row in range(start_row, table.nrows):
#         results.append(table.row_values(row))

#     return results

# if __name__ == "__main__":
#     res = read_excel("E:\\PYPro\\ZYpython\\TEST\\cases\\lux项目接口测试用例1.xlsx", "注册模块")
#     print(res)



#          第二次复习

"""
    读取excel的工具:不要试图去理解它，没用。能用就行了
"""
import xlrd

def read_excel(excel_path, sheet_name, skip_first=True):
    """
        读取excel的方法
    """

    results = []
    datas = xlrd.open_workbook(excel_path)  # 打开excle，并返回excel的对象
    table = datas.sheet_by_name(sheet_name) # 在excel中读取sheet_name的页面
    if skip_first is True:
        start_row = 1
    else:
        start_row = 0

    # 循环读取每一行的信息
    for row in range(start_row, table.nrows):
        results.append(table.row_values(row))

    return results

if __name__ == "__main__":
    res = read_excel("E:\\PYPro\\ZYpython\\TEST\\cases\\lux项目接口测试用例1.xlsx", "注册模块")
    print(res)

