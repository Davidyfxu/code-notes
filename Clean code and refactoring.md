# Clean code and refactoring（整洁代码与重构）

## abstract（摘要）

本文是对codewithmosh的clean code and refactoring课程的内容整理和总结，自认为Mosh Hamedani的课程是北美最好的代码教学课程之一（由于是英文教学，虽然没有字幕，但真心听得懂至少80%以上的英文），希望本文对大家学习本课程有帮助。

整洁代码与重构这课，我个人觉得适合学完一门面向对象语言后再听，主要讲了代码规范和代码重构，后半部分有一些设计模式的内容，可以结合《代码整洁之道》和《大话设计模式》两本书，配上该课程一起使用。

## Poor Name

Mysterious Names

Meaningless Names

Names with encodings

Ambiguous Names

Noisy names

## Naming Conventions

**PascalCase**: 帕斯卡命名法是在命名的时候将首字母大写,如: 程序代码public void DisplayInfo(); string UserName; 二者都是采用了帕斯卡命名法。 在C#中,以帕斯卡命名法和骆驼命名法居多。 C#中的编码惯例中,给公共成员变量(public)、受保护的成员变量(protect)、或内部成员变量(internal)命名时,应使用帕斯卡命名法,如score、name、Status均为有效的成员变量名;私有成员变量(private)必须以骆驼命名法命名,并以一个下划线开头。 1“Pascal命名法”可视为一种命名惯例,并无绝对与强制,为的是增加识别和可读性。一旦选用或设定好命名规则,在程式编写时应保持格式的一致性。

**camelCase**: 驼峰命名法与帕斯卡命名法相似，但首字母小写。

还有匈牙利命名法、下划线命名法等，但用的没有上述两种方法多。

## Poor Method Signatures

check the return type

check the method name

check the parameters

## Long Parameters List

Limit less than 3 parameters 限制方法/函数的输入变量小于3个

## Output Parameters

Avoid them 避免函数返回值返回大量的参数

Return an object from a method instead 从方法里返回一个类而不是一个一个的变量返回

## Variable Declarations On the Top

Declare variables close to their usage 在使用前较近的位置声明该变量（最重要的变量在代码顶端位置声明）

## Magic Numbers

Use constants or enums 对于大量使用的恒定常数，可将它们封装在一个固定的类中，用具体意思的常量名称代替纯数字

## Nest Conditionals

减少大量的if...else...嵌套选择语句

```c
if(a)
    if(b)
        if(c)
        else
    else
else
```

**solutions:**

1. Ternary Operator（三目运算）

   ```c
   //冗杂的表示法
   if(a)
       c = 1;
   else
       c = 2;
   
   //三目运算
   c = (a)?1:2;
   
   //python中对于三目运算的方法
   c = 1 if a else 2
   ```

2. Avoid Ternary Operator Abuse（三目运算不要嵌套使用）

3. Simplify True/False

4. Combine

   ```c
   // complex way
   if(a)
       if(b)
       {
           statements
       }
   
   // combine
   if(a&&b)
       statements
   ```

5. Early Exit

   ```c
   if(!a||!b)
       return
   ```

6. Swap Orders

7. Everything in Moderation

## Switch Statements

**可以利用设计模式的简单工厂来改善switch语句**

**Open Close principle （开放-封闭原则）**

- Open for extension（开放扩展）
- close for modification （封闭修改）

**Replace them with polymorphic dispatch（多态性的使用）**

**Use Push Member Down refactoring（中文不知道怎么合适的翻译，类似于把成员放置底层类来重构）**

## Duplicated Code

代码重复——don't repeat your code

## Comments

**注释的使用场景：**

- Version history
- Clarify the code
- Dead code（把一段代码注释掉，程序运行时直接跳过该段代码，用于调试）

**Tips**:

- Don't write comments, re-write your code.
- Don't explain 'what'. (obvious)
- Explain 'whys' and 'hows'.

## Long Methods

Problems: hard to understand, change and re-use.

We want methods that specialize in One thing.

**Cohesion Principle:** 

- Things that are related, should be together.

- Thing that are not related, should not be together.

**Single Responsibility:**

- A class / method should do only one thing, and do it well.

**Best Practices:**

- should be short. (less than 10 lines)
- should do only one thing.



