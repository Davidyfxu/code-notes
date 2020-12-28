# edis初学笔记

## 前言

最近假期在写django项目，用了几个新的非关系型数据库，当时写项目的时候用Redis只求实现功能，而没有好好系统了解一下Redis，因此今天想认认真真入门学一遍Redis。



## 简介

Redis 是一个高性能的 key-value 数据库。



## 优势

- 性能高 —— 读写快
- 数据类型丰富
- 原子性 —— 所有操作要么成功执行，要么失败完全不执行
- 特性丰富 —— 支持publish/subscribe，通知，key过期等特性



## 安装

[Redis安装连接]: https://www.runoob.com/redis/redis-install.html	"Redis安装连接"



## 基本数据类型

String、hash、list、set、zset (有序集合)



## Redis 键(Key)

### 用法

```bash
COMMAND KEY_NAME
```

### 实例

```bash
DEL runoobkey
```

**DEL** 是一个命令， **runoobkey** 是一个键。 如果键被删除成功，命令执行后输出 **(integer) 1**，否则将输出 **(integer) 0**。



## Redis 字符串(String)

### 实例

```bash
SET runoobkey Redis
GET runoobkey
```



## Redis 哈希(Hash)

### 实例

```bash
HMSET runoobkey name "Redis" description "Redis basic commands for caching"
HGETALL runoobkey
```



## Redis 列表(List)

### 实例

```bash
LPUSH runoobkey Redis
LPUSH runoobkey mongodb
LPUSH runoobkey mysql
LRANGE runoobkey 0 10
```



## Redis 集合(Set)

### 实例

```bash
SADD runoobkey Redis
SADD runoobkey mongodb
SADD runoobkey mongodb
SMEMBERS runoobkey
```



## Redis 有序集合(Sorted Set)

与集合不同的是，有序集合每一个成员会关联一个double类型的分数，Redis通过这个分数来为集合中的成员进行从小到大的排序。

有序集合的成员是唯一的，但分数却可以重复。

### 实例

```bash
ZADD runoobkey 1 Redis
ZADD runoobkey 2 mongodb
ZADD runoobkey 3 mysql
ZRANGE runoobkey 0 10 WITHSCORES
```



## Redis HyperLogLog

Redis HyperLogLog 是用来做基数统计的算法。优点是在输入元素的数量或者体积非常大时，计算基数所需的空间总是固定的、很小的。因为 HyperLogLog 只会根据输入元素来计算基数，而不会储存输入元素本身，所以 HyperLogLog 不能像集合那样，返回输入的各个元素。

### 基数

比如数据集 {1, 3, 5, 7, 5, 7, 8}， 那么这个数据集的基数集为 {1, 3, 5 ,7, 8}，基数(不重复元素)为5。基数估计就是在误差可接受的范围内，快速计算基数。

```bash
PFADD runoobkey "Redis"
PFADD runoobkey "mongodb"
PFADD runoobkey "mysql"
PFCOUNT runoobkey
```



## Redis 发布订阅

Redis 发布订阅（pub/sub）是一种消息通信模式：发送者（pub）发送消息，订阅者（sub）接受消息。

Redis的这个模式，和youtube的pub/subscribe模式一致。

### 实例

激活两个Redis-cli客户端，第一个客户端为订阅runoobChat这个频道，第二个客户端为发布新消息给所有订阅者。

![image-20201225175820554](C:\Users\xyf\AppData\Roaming\Typora\typora-user-images\image-20201225175820554.png)

![image-20201225175943819](C:\Users\xyf\AppData\Roaming\Typora\typora-user-images\image-20201225175943819.png)



## Redis 事务

Redis 事务可以一次执行多个命令， 并且带有以下三个重要的保证：

- 批量操作在发送 EXEC 命令前被放入队列缓存。
- 收到 EXEC 命令后进入事务执行，事务中任意命令执行失败，其余的命令依然被执行。
- 在事务执行过程，其他客户端提交的命令请求不会插入到事务执行命令序列中。

一个事务从开始到执行会经历以下三个阶段：

- 开始事务。
- 命令入队。
- 执行事务。

### 实例

先以 **MULTI** 开始一个事务， 然后将多个命令入队到事务中， 最后由 **EXEC** 命令触发事务， 一并执行事务中的所有命令。

![image-20201225182326822](C:\Users\xyf\AppData\Roaming\Typora\typora-user-images\image-20201225182326822.png)

单个 Redis 命令的执行是原子性的，但 Redis 没有在事务上增加任何维持原子性的机制，所以 Redis 事务的执行并不是原子性的。事务可以理解为一个打包的批量执行脚本，但批量指令并非原子化的操作，中间某条指令的失败不会导致前面已做指令的回滚，也不会造成后续的指令不做。



## Redis 脚本

```bash
EVAL script numkeys key [key ...] arg [arg ...]
```



## Redis 连接

Redis 连接命令主要是用于连接 Redis 服务。



## Redis 数据备份与恢复

Redis **SAVE** 命令用于创建当前数据库的备份。

### 恢复数据

如果需要恢复数据，只需将备份文件 (dump.rdb) 移动到 Redis 安装目录并启动服务即可。获取 Redis 目录可以使用 **CONFIG** 命令。

```bash
CONFIG GET dir
```



## 总结

总体来说，Redis的语法和命令相对简单，有python的基础学起来上手挺快。Redis虽然是一种数据库，但也被称为Redis缓存，用缓存一次表达了Redis取数速度更快，实际上Redis主要用来存储一些热数据，量也不大，但是操作很频繁。在写Django项目的时候，有记录点赞数和访问次数的时候，就用上了Redis来记录博客系统的对应数据。