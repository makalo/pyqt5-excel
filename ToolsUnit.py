from openpyxl import Workbook, load_workbook,styles
import os
import copy
import math
from openpyxl.utils import get_column_letter
from utils import get_key,get_merge_cell_list,get_merge_map,set_style,assign_value

def split_excel(path,idx,signal = None):
    wb = load_workbook(filename=path)
    x,y = idx
    head_idx =list(range(1,x+1))
    dict_idx = get_key(wb,idx)
    wbs_split = []
    names_split = []

    num_keys = len(list(dict_idx.keys()))
    count = 0
    for k,dict_sheet in dict_idx.items():
        print('开始拆关键词:{}'.format(k))
        wb_tmp = Workbook()
        wb_tmp.remove(wb_tmp[wb_tmp.sheetnames[0]])

        for sheet,idxes in dict_sheet.items():
            ws = wb[sheet]
            # ws_rows = list(ws.values)
            ws_tmp = wb_tmp.create_sheet(sheet)
            idxes = head_idx+idxes

            #======合并单元格=======
            merge_idx = ws.merged_cells
            merge_idx = get_merge_cell_list(merge_idx)
            for m_idx in merge_idx:
                map_idx = get_merge_map(m_idx,idxes)
                if map_idx is not None:
                    ws_tmp.merge_cells(map_idx)
            #======合并单元格=======

            num_column = ws.max_column #最大列数
            for i in range(1,len(idxes)+1):
                idx = idxes[i-1]
                # ws_tmp.append(ws_rows[idx-1])
                for j in range(1,num_column+1):
                    ws_tmp.row_dimensions[i].height = ws.row_dimensions[idx].height
                    ws_tmp.column_dimensions[get_column_letter(j)].width = ws.column_dimensions[get_column_letter(j)].width
                    
                    cell = ws.cell(row=idx, column=j)
                    cell_tmp = ws_tmp.cell(row=i, column=j,value = cell.value)
                    assign_value(cell_tmp,cell)
            # set_style(ws_tmp)
        wbs_split.append(wb_tmp)
        names_split.append(k)
        count += 1
        if signal is not None:
            proess = count / num_keys * 100
            signal.emit(int(proess))
    return wbs_split,names_split


# if __name__ == "__main__":
#     idx = [2,2]
#     wbs_split,names_split = split_excel('test.xlsx',idx)
#     root = './debug'
#     if not os.path.exists(root):
#         os.makedirs(root)
#     for wb,name in zip(wbs_split,names_split):
#         path = os.path.join(root,name+'.xlsx')
#         wb.save(path)









