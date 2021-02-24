
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ToolsUnit import split_excel
import os

class splitThread(QThread):
    split_signal = pyqtSignal(int)                        #创建信号
    split_signal_lcd = pyqtSignal(int)                        #创建信号

    def __init__(self, infos):
        super(splitThread, self).__init__()
        self.infos = infos
    def run(self):
        files = list(self.infos.keys())
        for i,base_name in enumerate(files):
            f = self.infos[base_name]['path']
            print('正在处理:{}'.format(f))
            # try:
            base_info = self.infos[base_name]['sheet_names']
            wbs_split,names_split = split_excel(f,base_info = base_info,signal = self.split_signal)
            root = os.path.splitext(f)[0]
            if not os.path.exists(root):
                os.makedirs(root)
            for wb,name in zip(wbs_split,names_split):
                path = os.path.join(root,name+'_'+base_name)
                wb.save(path)
            print('保存路径 {}'.format(root))
            print('处理完成 {}'.format(base_name))

            self.split_signal_lcd.emit(i+1)
            # except:
            #     print('拆分{}出现错误'.format(base_name))
            #     self.exit(0)




