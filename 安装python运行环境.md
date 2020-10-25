# 安装python运行环境
## 第一步：

从python官网上下载对应的python版本，地址是：
[https://www.python.org/downloards/](https://www.python.org/donloards/)


![python官网](https://github.com/sudajzp/photos/blob/master/python1.png?raw=true)


然后运行下载的exe安装包。


在安装时，要特别注意勾选上&emsp;Add python3.6 to PATH，然后点“install now”即可完成安装。
 
## 第二步：
 
打开命令窗口(windows + R)，输入“CMD”。敲入python后，会出现两种情况：

### 情况一
![情况一](https://github.com/sudajzp/photos/blob/master/python2.png?raw=true)
 
 
出现以上情况，说明python安装成功！
 
当看到提示符>>>时，就表示已经处于python交互界面，可以输入python代码，按下回车键就会执行相应的代码。退出python交互环境时，可以输入“exit()”并按下回车（直接关掉命令窗口，或者使用快捷键“CTRL + C”也可以）。
 
 ### 情况二
 得到一个错误：
 python不是一个内部或外部命令，也不是可运行的程序或批处理文件。
 
 ![情况二](https://github.com/sudajzp/photos/blob/master/python3.png?raw=true)
 
 这是因为Windows会根据一个PATH的环境变量设定的路径去查找python.exe,如果没有找到，就会报错。如果在python安装时漏掉之前的勾选操作
 ，就需要用户手动得将python.exe所在的路径添加到PATH中。
 
 
 如果不清楚如何添加，可以重新运行python.exe安装。