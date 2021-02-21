# pyqt5-excel
本项目是使用PyQt5制作的工具，并将其打包成exe文件，可以在任意windows上运行

## 展示效果
![image](https://github.com/makalo/pyqt5-excel/blob/windows/show/show.mp4.gif)

## 项目功能
1. 支持根据关键词拆分excel成多个excel

## 组件功能
1. 支持文件浏览选取
2. 支持多线程实时显示日志
3. 支持多线程进度条

## 安装运行

### 准备工具
1. [Qt Designer Setup.exe](https://pan.baidu.com/s/1rpjv6gXCFKcRTKXZU3RqLA) 用于可视化设计界面(提取码:3cm6)
2. [Setup Factory](https://pan.baidu.com/s/1cbqwL1M3MxDjO2UQJ6HpXA) 用于生成exe安装文件(提取码:v543)

### 安装环境
```
conda create -n pyqt5 python=3.6
conda activate pyqt5
pip install -r requirements.txt
```
### 运行
```
python run.py
```
### 设计自己的界面
1. 安装 Qt Designer Setup.exe
2. 可以重新设计也可以加载之前设计好的文件 [UI_lan.ui](./UI_lan.ui)
3. 保存成.ui文件，运行 pyuic5 -o UI_lan.py UI_lan.ui 生成python文件

### 打包成exe
```
pyinstaller -F -w run.py
```
1. 此时在dist目录下面就是生成的exe
2. 将exe拷贝到上一级目录下（因为依赖文件在上一级目录下，避免运行exe的时候找不到依赖文件；也可以将exe和依赖文件单独放在一个新的文件夹里面）

### 将exe打包成安装包
1. [安装Setup Factory并制作exe](https://blog.csdn.net/u010188178/article/details/82500833)
2. 会生成setup.exe 双击就可以安装了














