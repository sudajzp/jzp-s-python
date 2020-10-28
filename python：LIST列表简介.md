# python：LIST列表介绍
## 1 简介
### 1.1 LIST的构成
在python中，字符串、列表和元组数据都属于序列类型，它们中的每一个元素都是按照位置编号来顺序存储的。不同于numpy以及其他语言中的数组，列表和元组可以存储不同类型的元素。这种具有特色的数据类型使得批量数据的组织和处理更加灵活方便。

`List = [factor1, factor2,...]`

其中factor可以是字符串类型、整数类型、浮点类型、布尔类型 。

#### 索引

在python中，列表中每一个元素都会根据其位置编号分配给它一个有序的值称为索引（index）。不同于现实中的位置编号，列表索引是从0开始。比如：

```
#列表索引
x = [1, '列表', 1.1, 'list']
print(x[1])
```

输出的结果为x列表中的index为1，位置为2的元素:

![图1.1](https://github.com/sudajzp/photos/blob/master/list1.png?raw=true)

### 1.2 LIST修改

如果想要修改列表中某个元素，可以通过索引定位到你要修改的元素，通过赋值语句进行修改。比如：

```
#列表修改
x[1] = 'LIST'
print(x[1])
```
输出结果为：

![图1.2](https://github.com/sudajzp/photos/blob/master/list2.png?raw=true)

#### 插入
在列表中间插入其他元素可以使用`insert()`方法。该方法需要输入两个参数：索引（index）、想要插入的元素。格式如下：

`list.insert(index, factor)`

例子见下图：

![图1.3](https://github.com/sudajzp/photos/blob/master/list16.png?raw=true)

如果想要扩展列表，在列表尾部插入元素，可以使用`append()`方法。该方法只需要一个输入参数：你想要追加的元素。格式如下：

`list.append(factor)`

比如我想在图1.3中的列表末尾依次插入1到4的数字，那么我们就可以使用for循环和`append()`的组合。

![图片1.4](https://github.com/sudajzp/photos/blob/master/list17.png?raw=true)

#### 删除

`pop()`:返回列表指定位置的元素，并且从列表重删除这个元素。pop()可以传入一个参数，表示需要删除的元素的索引，如果不传入参数，那么默认参数为最后一个元素的索引。用法为：

`del list[index]`可以按索引在列表中查找元素并且删除元素。

`list.remove(factor)`可以删除列表中的特定元素，并不需要知道元素的索引值。

注意：`pop()`是有返回值的，而其余方法并没有返回值。

![图片1.5](https://github.com/sudajzp/photos/blob/master/list18.png?raw=true)

## 2、分片
列表的分片功能可以满足用户获取某个范围内的全部元素。格式为 `list[i : j]`其中i是起始索引，j为结束索引。分片中起始索引位置的值包含在获取的元素中，而结束索引不包含在获取的元素中。获取的元素个数等于结束索引的值减去起始索引的值。

### 2.1 从头开始的索引
当我们要获取的范围是从第一个元素开始时，起始索引可以略写。比如：

`print(x[:2])`

![图2.1](https://github.com/sudajzp/photos/blob/master/list3.png?raw=true)

同样，结束索引也可以略写，因为获取范围是不包括结束索引的元素的，所以在获取范围覆盖到列表最末时，一般采用略写结束索引的方法。

`print(x[2:])`

![图2.2](https://github.com/sudajzp/photos/blob/master/list4.png?raw=true)

### 2.2 从尾开始的索引
负索引：在读取列表数据时，如果列表内元素个数较大，而我们想要获取的索引位置比较偏后，那么用负索引比用正索引更加方便。负索引从‘-1’开始.

```
print(x[-3:-2])
print(x[-2:])
```
![图2.3](https://github.com/sudajzp/photos/blob/master/list5.png?raw=true)

### 2.3 按步长获取元素list[i:j:step]
`print(x[::2])`
i,j表示获取范围，2表示获取列表内元素使用的步长。

![图2.4](https://github.com/sudajzp/photos/blob/master/list6.png?raw=true)

## 3 列表常用方法（只作简单介绍）

`list.count(factor)`:统计factor在列表中出现的次数

`list.sort()`：正向排序，没有返回值

`list.reverse`:反向排序，没有返回值

`list.copy`：复制列表

`list.clear`：清空列表

`list * n`:将原列表中元素重复n次


####  高维列表

列表内元素也可以是另一个列表，高维列表就可以看做是列表的嵌套。

`list[i][j][k]`

对高维列表的单次索引可以获得对应索引的元素，该元素为一个列表。对获得的列表继续索引，则可以继续获得新列表中的元素，以此类推。

## 4、列表与矩阵的区别
使用python列表存储一维数组，通过列表的嵌套可以实现多维数组。numpy模块中的ndarry也可以出列多维数组，存储效率和输入输出性能远优于列表的嵌套。

列表内的元素是任意的，而矩阵中的所有元素的类型都要求是相同的。因此在存储的灵活性方面，矩阵不如列表。而在计算方面矩阵支持科学计算。

矩阵的加法：对应位置元素相加（图2.5）；列表加法：拼接两个矩阵（图2.6）。

矩阵的乘法：可以相乘（图2.7）；列表不支持乘法（图2.8）。

![图4.1](https://github.com/sudajzp/photos/blob/master/list8.png?raw=true)

![图4.2](https://github.com/sudajzp/photos/blob/master/list10.png?raw=true)

![图4.3](https://github.com/sudajzp/photos/blob/master/list7.png?raw=true)

![图4.4](https://github.com/sudajzp/photos/blob/master/list9.png?raw=true)

## 附录：列表使用进阶(部分)

#### 列表生成式：
`x = [f(x) for x in range(i,j,step) if g(x)]`

f(x)是任意对x的有效操作，x可以是任意列表能够存储的类型。`if g(x)`是对x的一个条件判断。

通过列表生成式，我们可以很快速地生成一个10以内奇数的平方的列表：

`y = [x * x for x in range(10) if x % 2 == 1]`

结果为：

![附录1](https://github.com/sudajzp/photos/blob/master/list12.png?raw=true)

使用列表生成式还可以初始化一个二维列表：

![附录2](https://github.com/sudajzp/photos/blob/master/list11.png?raw=true)

#### copy()操作的意义
由于列表的特殊性，将同一个列表赋值给不同的变量名，该变量名对应的列表指向同一个存储地址。如果我们改变了其中一个，那么其他指向该列表的值也会被更改，原因是改动操作的执行对象是存储地址中的列表。实例见附录3。

![附录3](https://github.com/sudajzp/photos/blob/master/list13.png?raw=true)

我更改了y中的一个元素，z中的元素也同步更改了。

所以如果想要将该列表复制一份并保留原列表不动，就需要copy()函数。

#### zip()、enumerate()

zip():两个列表从第一个元素开始，对应位置的元素合并成一个元组，多余部分删除，返回一个组合好的打包对象。zip()需要我们有list()函数转换回列表。

![附录4](https://github.com/sudajzp/photos/blob/master/list14.png?raw=true)

enumerate():将列表内元素按顺序编写序号，起始序号可以自定义。序号与元素组成一个元组，最终返回一个枚举对象，同样需要用list()函数转换回列表。

![附录5](https://github.com/sudajzp/photos/blob/master/list15.png?raw=true)
