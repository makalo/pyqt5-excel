
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ToolsUnit import split_excel
import os

class splitThread(QThread):
    split_signal = pyqtSignal(int)                        #创建信号
    split_signal_lcd = pyqtSignal(int)                        #创建信号

    def __init__(self, idx, files):
        super(splitThread, self).__init__()
        self.idx = idx
        self.files = files
    def run(self):
        for i,f in enumerate(self.files):
            print('正在处理:{}'.format(f))
            base_name = os.path.split(f)[-1]
            try:
                wbs_split,names_split = split_excel(f,idx = self.idx,signal = self.split_signal)
                root = os.path.splitext(f)[0]
                if not os.path.exists(root):
                    os.makedirs(root)
                for wb,name in zip(wbs_split,names_split):
                    path = os.path.join(root,name+'_'+base_name)
                    wb.save(path)
                print('保存路径 {}'.format(root))
                print('处理完成 {}'.format(base_name))

                self.split_signal_lcd.emit(i+1)
            except:
                print('拆分{}出现错误'.format(base_name))
                self.exit(0)




