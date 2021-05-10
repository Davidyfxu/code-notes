# Java代码笔记

## String

两个字符串比较，必须总是使用`equals()`方法。

要忽略大小写比较，使用`equalsIgnoreCase()`方法。

```java
String s = new String(new char[]{'1','2','3'})
```

## StringBuilder/StringBuffer

可变对象，可以预分配缓冲区，这样，往`StringBuilder`中新增字符时，不会创建新的临时对象。

## 常用

### String拼接

```java
String.join()
```

## JavaBean

getter setter

## 异常

errors 错误

exception 异常

## 反射

通过Class实例获取`class`信息的方法称为反射（Reflection）；

## 注解

1. `SOURCE`类型：编译器使用的注解。@Override、@SuppressWarnings 在编译后就被编译器扔掉了.
2. `CLASS`类型：由工具处理`.class`文件使用的注解，不会被加载进JVM.
3. `RUNTIME`类型：在程序运行期能够读取的注解,在加载后一直存在于JVM.(自己编写). @Range/@Check

## 泛型

泛型就是定义一种模板，例如`ArrayList`，然后在代码中为用到的类创建对应的`ArrayList<类型>`

注意泛型的继承关系：可以把`ArrayList`向上转型为`List`（`T`不能变！），但不能把`ArrayList`向上转型为`ArrayList`（`T`不能变成父类）。

```java
// 可以省略后面的Number，编译器可以自动推断泛型类型：
List<Number> list = new ArrayList<>();
```

**擦拭法**是指，虚拟机对泛型其实一无所知，所有的工作都是编译器做的。

通配符`<T extends Number>`的一个重要限制：方法参数签名`setFirst(? extends Number)`无法传递任何`Number`的子类型给setFirst(? extends Number)。（可读操作，不可写增删操作）

使用类似`<T extends Number>`定义泛型类时表示：

- 泛型类型限定为`Number`以及`Number`的子类。

使用类似`<? super Integer>`通配符作为方法参数时表示：（可写操作，不可读操作）

- 方法内部可以调用传入`Integer`引用的方法，例如：`obj.setFirst(Integer n);`；
- 方法内部无法调用获取`Integer`引用的方法（`Object`除外），例如：`Integer n = obj.getFirst();`。

## 集合

Collection 特点：一是实现了接口和实现类相分离，例如，有序表的接口是`List`，具体的实现类有`ArrayList`，`LinkedList`等，二是支持泛型，我们可以限制在一个集合中只能放入同一种数据类型的元素

### List

通过`Iterator`遍历`List`永远是最高效的方式。并且，由于`Iterator`遍历是如此常用，所以，Java的`for each`循环本身就可以帮我们使用`Iterator`遍历。

```java
List<String> list = List.of("apple", "pear", "banana");
        for (String s : list) {
            System.out.println(s);
        }
```

### Map

遍历`key`可以使用`for each`循环遍历`Map`实例的`keySet()`方法返回的`Set`集合，它包含不重复的`key`的集合

### Collections工具类

```java
Collections.sort(list); // 排序
Collections.shuffle(list); // 洗牌
```

## 多线程

初始Demo

```java
// 方法一：从Thread派生一个自定义类，然后覆写run()方法：
public class Main {
    public static void main(String[] args) {
        Thread t = new Thread();
        t.start(); // 启动新线程
    }
}
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("start new thread!");
    }
}
// 方法二：创建Thread实例时，传入一个Runnable实例：
public class Main {
    public static void main(String[] args) {
        Thread t = new Thread(new MyRunnable());
        t.start(); // 启动新线程
    }
}
class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("start new thread!");
    }
}
```

直接调用`Thread`实例的`run()`方法是无效的

一个线程还可以等待另一个线程直到其运行结束。例如，`main`线程在启动`t`线程后，可以通过`t.join()`等待`t`线程结束后再继续运行

### 中断线程

中断线程就是其他线程给该线程发一个信号，该线程收到信号后结束执行`run()`方法，使得自身线程能立刻结束运行。调用`interrupt()`方法

### 线程同步

保证一段代码的原子性就是通过加锁和解锁实现的。Java程序使用`synchronized`关键字对一个对象进行加锁。

```java
synchronized(Counter.lock) { // 获取锁
    ...
} // 释放锁
```

对JVM定义的单个原子操作不需要同步。

让线程自己选择锁对象往往会使得代码逻辑混乱，也不利于封装。更好的方法是把`synchronized`逻辑封装起来。例如，我们编写一个计数器如下

```java
public class Counter {
    private int count = 0;
    public void add(int n) {synchronized(this) {count += n;}}
    public void dec(int n) {synchronized(this) {count -= n;}}
    public int get() {return count;}
}
```

如果一个类被设计为允许多线程正确访问，我们就说这个类就是“**线程安全**”的（thread-safe）

### 死锁

在获取多个锁的时候，不同线程获取多个不同对象的锁可能导致死锁。

如何避免死锁呢？答案是：线程获取锁的顺序要一致。即严格按照先获取`lockA`，再获取`lockB`的顺序

**多线程协调运行**的原则就是：当条件不满足时，线程进入等待状态；当条件满足时，线程被唤醒，继续执行任务。