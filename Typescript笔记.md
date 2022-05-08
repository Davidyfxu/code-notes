# Typescript要点记录

## 初始化

```bash
npm init -y # npm初始化项目, 并全选yes（创建package.json）

tsc --init # ts初始化，创建tsconfig.json

# 项目中新建src目录，在src中创建index.ts文件
```

## 字面量

**类型字面量**：仅仅表示一个值的类型。

**对象字面量**：TS推导对象的结构，或者直接在{}内明确描述。

## 问号？

表示可选的意思

对象类型声明中键的？---初始化可选是否使用该键

函数中的参数？--- 可选参数

## 并集类型与交集类型

## 枚举

按约定，枚举名称位大写的单数形式，枚举中的键也为大写

## 生成器

惰性生成需要的值

```typescript
function* createFibGen() {
  let a = 0;
  let b = 1;
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}

const gen = createFibGen();
console.log(gen.next());
```

## 迭代器

生成器是生成一系列值的方式，迭代器是使用这些值的方式

```typescript
let numbers = {
  *[Symbol.iterator]() {
    for (let n = 1; n <= 10; n++) {
      yield n;
    }
  },
};

for (const a of numbers) {
  console.log(a);
}
```

## 调用签名

规定函数的输入参数类型和返回类型

## 泛型

### 泛型函数

```typescript
type Filter = <T>(array: T[], f: (item: T) => boolean) => T[];
let filter:Filter = ...;


type Filter2<T> = (array: T[], f: (item: T) => boolean) => T[];
let filter2:Filter2<string> = ...;

// 多个泛型
function map<T, U>(array: T[], f: (item: T) => U): U[] {
  let res = [];
  for (let i = 0; i < array.length; i++) {
    res[i] = f(array[i]);
  }
  return res;
}
```

### 泛型别名

在类型别名中使用泛型

```typescript
type MyEvent<T> = {
  target: T;
  type: string;
};
```

