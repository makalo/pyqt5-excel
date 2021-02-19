from openpyxl import Workbook, load_workbook,styles
import os
import copy
import math
from openpyxl.utils import get_column_letter, column_index_from_string
def get_key(wb,idx):
    sheet_names = wb.sheetnames
    dict_idx = {}
    keys = []
    for name_s in sheet_names:
        ws = wb[name_s]
        x,y = idx
        num_row = ws.max_row #最大行数
        num_column = ws.max_column #最大列数
        for i in range(x+1,num_row+1):
            k = ws.cell(row=i, column=y).value
            if k is None:
                k = keys[-1]
            keys.append(k)
            if not k in dict_idx.keys():
                dict_idx[k] = {name_s:[i]}
            elif not name_s in dict_idx[k].keys():
                dict_idx[k][name_s] = [i]
            else:
                l = dict_idx[k][name_s]
                l.append(i)
                dict_idx[k][name_s] = l
    return dict_idx

def get_merge_cell_list(merge_idx):
    merge_idx = list(merge_idx)
    merge_list = []
    for i in range(len(merge_idx)):
        merge = merge_idx[i]
        row_min, row_max, col_min, col_max = merge.min_row, merge.max_row, merge.min_col, merge.max_col
        merge_list.append([row_min, row_max, col_min, col_max])
    return merge_list
def get_merge_map(merge_idx,idx):
    row_min, row_max, col_min, col_max = merge_idx
    col_min = get_column_letter(col_min)
    col_max = get_column_letter(col_max)
    try:
        x1 = idx.index(row_min) + 1
        x2 = idx.index(row_max) + 1
        s = '{}{}:{}{}'.format(col_min,x1,col_max,x2)
        return s
    except:
        return None

def set_style(ws):
    align = styles.Alignment(horizontal='center',vertical='center')
    font_18 = styles.Font(size=18)

    num_row = ws.max_row #最大行数
    num_column = ws.max_column #最大列数
    for i in range(1,num_row+1):
        for j in range(1,num_column+1):
            cell = ws.cell(row=i, column=j)
            cell.alignment = align
            cell.font = font_18
def assign_value(target_cell,source_cell):
    target_cell.value = source_cell.value
    target_cell.fill = copy.copy(source_cell.fill)
    if source_cell.has_style:
        target_cell._style = copy.copy(source_cell._style)
        target_cell.font = copy.copy(source_cell.font)
        target_cell.border = copy.copy(source_cell.border)
        target_cell.fill = copy.copy(source_cell.fill)
        target_cell.number_format = copy.copy(source_cell.number_format)
        target_cell.protection = copy.copy(source_cell.protection)
        target_cell.alignment = copy.copy(source_cell.alignment)





