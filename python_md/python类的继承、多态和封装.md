# python类的继承、多态性与封装
## 继承
继承是一种机制，它允许我们在现有的类的基础上添加新的属性和方法来创建一个新的类。新创建的类称为子类，它基于一个现有的类-父类。

当程序员需要创建一个与已用的类非常相似的类的时候，继承能够省下很大功夫。我们所需要的做的就是为它们在一个类中公有的东西编写代码--父类，然后为另一个类中具体编写-子类。这样就可以减少工作，避免大量重复代码。

假设我们正在创建一个处理各种形状的程序。每个形状都有一些共同的属性。例如，形状的颜色，它是否被填充等等。除此之外，还有一些属性因形状而异。例如，区域和周边。矩形的面积是length * width,而圆的面积是πr^2 。首先可以很容易得为不同形状创建类。

```
class Rectangle:
    def __init__(self, color, filled, width, length):
        self.__color = color
        self.__filled = filled
        self.__width = width
        self.__length = length

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled

    def get_area(self):
        return self.__width * self.__length

class Circle:
    def __init__(self, color, filled, radius):
        self.__color = color
        self.__filled = filled
        self.__radius = radius      

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled

    def get_area(self):
        return math.pi * self.__radius ** 2
```
注意到，代码中有很多重复部分。两个类共享相同的__color和__filled属性以及他们的getter和setter方法。如果我们想要更新这些方法，那么必须逐一访问每一个类来进行修改。

通过使用继承，我们就可以将公共属性定义为shape类（父类），创建子类继承父类所有的属性和方法，也可以添加子集自己的属性和方法。

要基于父类创建子类，可以使用一下语法：
```
class ParentClass:
    # body of ParentClass
    # method1 
    # method2

class ChildClass(ParentClass):
    # body of ChildClass
    # method 1
    # method 2
```
使用面向对象的术语，当一个类A2继承自A1，我们说类A2扩展类A1，或者类A2是从A1中衍生出来的。

下面的程序演示了实际的继承。它创建了一个名为shape的父类，包含所有形状共有的属性和方法。随后创建两个子类：Rectangle和Triangle。它们只包含特定于它们的属性和方法。
```
import math

class Shape:

    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled


class Rectangle(Shape):

    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_breadth(self):
        return self.__breadth

    def set_breadth(self, breadth):
        self.__breadth = breadth

    def get_area(self):
        return self.__length * self.__breadth

    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius


r1 = Rectangle(10.5, 2.5)

print("r1的面积:", r1.get_area())
print("r1的周长:", r1.get_perimeter())
print("r1的颜色:", r1.get_color())
print("r1是否被填充? ", r1.get_filled())
r1.set_filled(True)
print("r1是否被填充? ", r1.get_filled())
r1.set_color("orange")
print("r1的颜色:", r1.get_color())

c1 = Circle(12)

print(f"c1的面积:{c1.get_area()}") 
print(f"c1的周长:{c1.get_perimeter()}")
print("c1的颜色:", c1.get_color())
print("c1是否填充? ", c1.get_filled())
c1.set_filled(True)
print("c1是否填充? ", c1.get_filled())
c1.set_color("blue")
print("c1的颜色:", c1.get_color())
```

结果如下：
```
r1的面积: 26.25
r1的周长: 26.0
r1的颜色: black
r1是否被填充?  False
r1是否被填充?  True
r1的颜色: orange
c1的面积:452.3893421169302
c1的周长:75.39822368615503
c1的颜色: black
c1是否填充?  False
c1是否填充?  True
c1的颜色: blue
```
起先，我们定义了一个父类shape，只包含所有形状共有的属性和方法。这个类定义了两个私有属性__color和__filled ，然后为这些属性提供了getter和setter方法。

其后，我们定义了Rectangle继承自shape类。我们使用的语法为`class Rectangle(Shape):`
这段语法将shape类继承给Rectangle或者Rectangle是shape类的扩展。因此Rectangle继承了shape类的属性和方法，并且添加了两个特有属性和方法来计算矩形的面积和周长。

`super().__init()`在python中，使用`super()`函数调用父类中的方法。上面代码调用了shape中的`__init__`方法。这是设置父类中属性值所必须的。否则，当场试访问父类中定义的属性值时，将会出错。

## 多重继承

python允许我们同时从多个类中派生一个类，就是所谓的多重继承。一般格式是：
```
Class ParentClass_1:
    # body of ParentClass_1

Class ParentClass_2:
    # body of ParentClass_2

Class ParentClass_3:
    # body of ParentClass_1

Class ChildClass(ParentClass_1, ParentClass_2, ParentClass_3):
    # body of ChildClass
```
childClass从三个类ParentClass_1,ParentClass_2.ParentClass_3中派生，因此它将继承这三个类的属性和方法。

下面程序中演示了实际中的多重继承：
```
class person:
    def __init__(self, name = 'jzp'):
        self.name = name
        self.legs = 2
        self.eyes = 2
    
    def run(self):
        print(f'{self.name} is running')
    
    def set_name(self, name):
        self.name = name
        
class student:
    def __init__(self, school = 'scow', study = True):
        self.school = school
        self.study = study
        
    def set_study(self, study):
        self.study = study
        
class worker(person, student):
    def __init__(self, sex):
        super().__init__()
        student.__init__(self)
        self.sex = sex
    
    def work(self):
        print(f'{self.name} is typing codes')

jzp = worker('男')
print(jzp.study)
jzp.run()
jzp.work()
```
输出为：
```
True
jzp is running
jzp is typing codes
```
注意到代码中获取父类属性使用了两种方式，`super().__init__()`在子类继承多个父类时，只能够调用第一个父类的属性，其余父类的属性调用只能使用未绑定的方式调用。

## 多态和方法重写
从字面意义上讲，多态性是指具有多种形式的能力。在python中，多态性允许我们定义子类中的方法，其名称与父类中定义的名称相同。

如我们所知，子类继承父类中的所用方法。但是，有时也会遇到从父类继承的方法不完全适应子类的情况。在这种情况下，就必须在子类中重新实现方法。此过程称为方法重写。

在已经重写了子类中的方法时，将根据调用该方法的对象的类型来调用该方法的不同版本。如果使用子类对象调用重写的方法，则调用该方法的子类版本，另一方面，如果使用父类对象调用重写的方法，则调用该方法的父类版本。

下面程序演示了重写操作的方法：
```
class A:
    def explore(self):
        print("explore() method from class A")

class B(A):
    def explore(self):
        print("explore() method from class B")


b_obj = B()
a_obj = A()

b_obj.explore()
a_obj.explore()
```
结果如下：
```
explore() method from class B
explore() method from class A
```
这里b_obj是类B的对象，因此类B的版本explore()方法被调用。但是，变量a_obj是类A的对象，因此，类A的版本explore()方法被调用。

如果出于某些原因，仍然希望访问子类中父类的重写方法，则可以使用supper()职能如下：
```
class A:
    def explore(self):
        print("explore() method from class A")

class B(A):
    def explore(self):
        super().explore()  # calling the parent class explore() method
        print("explore() method from class B")


b_obj = B()
b_obj.explore()
```
结果如下：
```
explore() method from class A
explore() method from class B
````
# 封装 
将同种对象的属性和方法对外隐藏，封装到一个抽象的类中，不能从外部直接调用它们。封装有两个层面：第一层面的封装：创建类和对象时，分别创建两者的名称空间。只能通过“类名.”或者“对象名.”的方式访问里面的信息。第二层面的封装：在创建好的类中把某些属性或方法隐藏起来，只在类的内部使用，在类的外部无法直接访问。但无论是哪种层面的封装，都要对外提供好访问内部隐藏内容的接口。   

把属性或方法的名称前加上双下划线__，通过这种命名规范来实现隐藏属性。  
第一层面的封装：通过对象直接调用被封装的内容：对象.属性名。或者通过self间接调用被封装的内容：self.属性名或self.方法名( )。第二层面的封装：隐藏属性之后可以通过"_类名__属性"的方式来访问其内部的属性值。   

来看下面一个例子：
```
class worker1():
    def __init__(self, name, work):
        self.name = name
        self.work = work
    
    def working(self):
        print(f'{self.name} is typing codes')
jzp1 = worker1('jzp', 'student')
jzp1.working()
print(jzp1.name)    
```
在创建worker1类时，使用了“__init__(self)”这一方法，使得在创建类的实例时，实例都会自动调用这个方法，也是对实例属性的初始化。第一个形参self是必须要的，self指的是被创建的实例本身。这里对属性属于第一个层面的封装，因此就像是前面所说：可以通过jzp1.name，self.name，jzp1.work()去调用其属性。得到的返回信息如下：

```
jzp is typing codes.
jzp
```
使用第二种封装方法，在属性名前加上__来实现隐藏属性。
```
class worker2():
    def __init__(self, name, work):
        self.__name = name
        self.__work = work
    
    def working(self):
        print(f"{self.__name} is typing codes.")
        
jzp2 = worker2('jzp', 'student')
print(jzp2._worker2__name)
jzp2._worker2__working()
```
直接调用方法不再能够调用类的属性或方法，需要使用如上所示的特殊调用形式。
结果如下：

```
jzp
jzp is typing codes.
```