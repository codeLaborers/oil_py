import PyPDF2
import pdfplumber
import os


# def analyze_pdf():
#     #解析pdf
#     # 打开 PDF 文件
#     file_path = 'N:/OilWellTableExtraction/gcsj_154408_1.pdf'
#     pdf_file = open(file_path, 'rb')
#
#     # 创建 PDF 阅读器对象
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#
#     #获取 PDF 页数
#     num_pages = len(pdf_reader.pages)
#
#     # 遍历每一页
#     for page_num in range(num_pages):
#         # 获取页面对象
#         page = pdf_reader.pages[page_num]
#
#         # 提取页面文本
#         page_text = page.extract_text()
#
#
#         print(f'Page {page_num + 1}:\n{page_text}\n')
#
#     # 关闭 PDF 文件
#     pdf_file.close()
#
#
# def analyze_pdf_pdfplumber():
#     # 解析pdf table
#     file_path = 'N:/OilWellTableExtraction/gcsj_154408_1.pdf'
#
#     with pdfplumber.open(file_path) as pdf:
#         num_pages_sum = len(pdf.pages)
#
#         for page_num in range(num_pages_sum):
#             page = pdf.pages[page_num]
#
#             # 提取页面文本
#             page_text = page.extract_text()
#             print(f'Page {page_num + 1}:\n{page_text}\n')
#
#             # 提取页面表格
#             tables = page.extract_tables()
#             for table in tables:
#                 print(f'Table on Page {page_num + 1}:')
#                 for row in table:
#                     print(row)
#                 print('\n')

def optimize_table(table):
    #优化表中字符串的结构， 去掉空格
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == None: continue
            table[i][j] = table[i][j].replace(' ', '')


def is_unwanted_table(table):
    #判断表是否是需要的表， 如果不是返回true
    key_name_list = ['井号', '井别', '井型', '地理位置', '构造位置', '完钻原则', '完钻层位']
    total_len = 0#表的总长
    match_len = 0#匹配成功的串个数
    for row in table:
        for str in row:
            if str == None: continue
            total_len += 1
            if str in key_name_list:
                match_len += 1

    if match_len > 4:#此判断条件需要优化
        return False
    else:
        return True

def output_list(dict):
    for key, value in dict.items():
        print(key)
        print(value)
        print('\n')

def store_key_value(all_tables_in_one_pdf):
    #存储24个值， 每个list负责存一个值， list的大小在17w， 24个表每个相同索引必须来自同一个表。
    well_id = []
    well_category = []
    well_type = []
    construction_name = []
    geo_description = []
    well_x = []
    well_y = []
    ground_elevation = []
    repair_distance = []
    target_stratum = []
    horizontal_length = []
    target_front_displacement = []
    offset_distance = []
    design_orientation = []
    magnetic_declination = []
    oblique_point = []
    effective_target_lead = []
    design_window_well_depth = []
    design_window_vertical_depth = []
    complete_well_depth = []
    complete_vertical_depth = []
    drill_purpose = []
    drill_principle = []
    completion_method = []

    key_list = {
        '井号': well_id,
        '井别': well_category,
        '井型': well_type,
        '构造位置': construction_name,
        '地理位置': geo_description,
        'X（m）': well_x,  # 有问题
        'Y（m）': well_y,  # 有问题
        '地面海拔（m）': ground_elevation,
        '补心海拔（m）': repair_distance,
        '目的层': target_stratum,
        '水平段长度': horizontal_length,
        '靶前距': target_front_displacement,
        '偏移距': offset_distance,
        '设计方位': design_orientation,
        '磁偏角': magnetic_declination,
        '倾斜点': oblique_point,#？
        '有效目标': effective_target_lead,#？
        '设计窗口井深': design_window_well_depth,#？
        '设计窗口垂深': design_window_vertical_depth,#？
        '完钻井深': complete_well_depth,
        '完钻垂深': complete_vertical_depth,
        '钻井目的': drill_purpose,
        '完钻原则': drill_principle,
        '完井方法': completion_method,
    }



    #调用已经解析出表的函数， 此处应该是循环调用， 目前先调用一个
    #important： 以传参的方式传入all_tables_in_one_pdf
    # all_tables_in_one_pdf = analyze_pdf_integral()

    for table in all_tables_in_one_pdf:
        #遍历all_tables_in_one_pdf, 其中的一个表

        #存储有效表
        valid_table = []

        # 优化表的结构
        optimize_table(table)

        #判断此表是否可用, 如果不可用， 返回true
        if is_unwanted_table(table): continue

        #如果是有效表， 存入valid_table
        valid_table.append(table)

        return valid_table

        #如果此表中用了这个值， bool改为true
        well_id_exist = False
        well_category_exist = False
        well_type_exist = False
        construction_name_exist = False
        geo_description_exist = False
        well_x_exist = False
        well_y_exist = False
        ground_elevation_exist = False
        repair_distance_exist = False
        target_stratum_exist = False
        horizontal_length_exist = False
        target_front_displacement_exist = False
        offset_distance_exist = False
        design_orientation_exist = False
        magnetic_declination_exist = False
        oblique_point_exist = False
        effective_target_lead_exist = False
        design_window_well_depth_exist = False
        design_window_vertical_depth_exist = False
        complete_well_depth_exist = False
        complete_vertical_depth_exist = False
        drill_purpose_exist = False
        drill_principle_exist = False
        completion_method_exist = False

        key_bool_list = {
            '井号': well_id_exist,
            '井别': well_category_exist,
            '井型': well_type_exist,
            '构造位置': construction_name_exist,
            '地理位置': geo_description_exist,
            'X（m）': well_x_exist,  # 有问题
            'Y（m）': well_y_exist,  # 有问题
            '地面海拔（m）': ground_elevation_exist,
            '补心海拔（m）': repair_distance_exist,
            '目的层': target_stratum_exist,
            '设计井深（m）': horizontal_length_exist,
            'a0': target_front_displacement_exist,
            'a1': offset_distance_exist,
            'a2': design_orientation_exist,
            'a3': magnetic_declination_exist,
            'a4': oblique_point_exist,
            'a5': effective_target_lead_exist,
            'a6': design_window_well_depth_exist,
            'a7': design_window_vertical_depth_exist,
            'a8': complete_well_depth_exist,
            'a9': complete_vertical_depth_exist,
            'a10': drill_purpose_exist,
            '完钻原则': drill_principle_exist,
            '完井方法': completion_method_exist,
        }


        # for row in table:
        #     i = 0
        #     while i < len(row):
        #         #如果名称在key_list中， key_list中的value是list名，将对应的值存入list中
        #         if row[i] == None:
        #             i += 1
        #             continue
        #         # 注意while index的控制
        #         if row[i] not in key_list:
        #             i += 1
        #             continue
        #         if row[i] in key_list:
        #             #j is next index
        #             j = i + 1
        #             if j >= len(row):
        #                 break
        #             key_list[row[i]].append(row[j])
        #             #判断是否使用过的bool值变成true, 因为bool值是不可变类型， 所以在此修改了字典中的bool值
        #             key_bool_list[row[i]] = True
        #             i = j + 1



        #     print(row)
        # print('\n')

        # 将没有修改过的值append None
        # for key, value in key_bool_list.items():
        #     if value == False:
        #         key_list[key].append(None)

    # #输出24个list
    # output_list(key_list)



def process_all_pdfs_in_folder(folder_path):
    # 遍历文件夹中的所有文件
    # 所有的表
    total_table = []
    for filename in os.listdir(folder_path):
        # 检查文件是否是 PDF 文件
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            print(f'Processing {file_path}...')
            tables = analyze_pdf_integral(file_path)
            #在这里对每个 PDF 文件的表格进行进一步处理
            valid_table = store_key_value(tables)
            for table in valid_table:
                total_table.append(table)

            print(f'Extracted {len(tables)} tables from {file_path}')
    return total_table


def analyze_pdf_integral(file_path):
    # 解析pdf
    # file_path = 'N:/OilWellTableExtraction/gcsj_154408_1.pdf'

    # 用于存储所有表格的列表
    all_tables = []

    with pdfplumber.open(file_path) as pdf:
        num_pages = len(pdf.pages)

        for page_num in range(num_pages):
            page = pdf.pages[page_num]

            # 提取页面表格
            tables = page.extract_tables()
            all_tables.extend(tables)

    # 打印所有表格
    # for table_num, table in enumerate(all_tables, 1):
    #     optimize_table(table)
    #     print(f'Table {table_num}:')
    #     for row in table:
    #         print(row)
    #     print('\n')

    return all_tables

def output_total_tables(total_tables):
    for table_num, table in enumerate(total_tables, 1):
        print(f'Table {table_num}:')
        for row in table:
            print(row)
        print('\n')

def output_total_tables_to_txt(total_tables, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for table_num, table in enumerate(total_tables, 1):
            f.write(f'Table {table_num}:\n')
            for row in table:
                f.write(f'{row}\n')
            f.write('\n')

def main():

    #主函数逻辑
    #解析pdf
    # analyze_pdf()
    #解析出表格
    # analyze_pdf_pdfplumber()
    #解析表格， 不分页
    # analyze_pdf_integral()
    #主控制函数
    # store_key_value()
    #批量处理pdf的主控制函数
    folder_path = 'N:/OilWellTableExtraction/pdf_set'
    output_file = 'N:/OilWellTableExtraction/result.txt'
    total_tables = []
    total_tables = process_all_pdfs_in_folder(folder_path)
    # output_total_tables(total_tables)
    #将结果存到文本文档里
    output_total_tables_to_txt(total_tables, output_file)

if __name__ == "__main__":
    main()

