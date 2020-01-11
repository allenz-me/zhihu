如何进入MySQL命令行模式？
打开命令行，输入

```cmd
>>>mysql -uroot -pmypassword
```

把 mypassword 换成自己设定的密码

**Tips：在SQL中，语句不区分大小写，对关键词使用大写，能使代码更易阅读和调试**

本部分包含基本的MySQL操作

## 3. 使用MySQL
- 使用数据库
```mysql
USE crashcourse;
// output: Database changed
```
- 显示所有数据库
```mysql
SHOW DATABASES;
// 返回可用数据库的一个列表
```
- 显示数据库中所有表
```mysql
SHOW TABLES;
```
- 显示表列
```mysql
SHOW COLUMNS FROM customers;
// 等价于
DESCRIBE customers;
```

-   删除整个表

```mysql
DROP TABLE customers;
```

-   重命名表

```mysql
RENAME TABLE customers TO newcustomers;
```

## 4. 检索数据

- 检索单个列
```mysql
SELECT prod_name FROM products;
```
数据没有过滤，也没有排序。
- 检索多个列，列名之间用逗号隔开
```mysql
SELECT prod_id, prod_name 
FROM products;
```
- 检索所有列，使用 * 作为通配符
```mysql
SELECT * FROM products;
```
- 检索不同的行，使用 DISTINCT 关键词
```mysql
SELECT DISTINCT vend_id 
FROM products;
```
- 限制结果
```mysql
SELECT prod_name 
FROM products LIMIT 5;
```
```mysql
SELECT prod_name 
FROM products LIMIT 5, 4;  // 返回从5行开始的4行
```
```mysql
SELECT prod_name 
FROM products LIMIT 4 OFFSET 5;  // 与上一行相同作用
```
- 完全限定的列名和完全限定的表名
```mysql
SELECT products.prod_name 
FROM crashcourse.products;
```
有一些情形需要完全限定名

## 5. 排序检索数据
单纯的`SELECT`并不能保证检索出的数据是有顺序的

**可以加入`ORDER BY`子句来输出顺序**，默认的排序是升序

- 按某一列对检索结果进行排序
```mysql
SELECT prod_name 
FROM products 
ORDER BY prod_name;
```
- 按多个列排序
```mysql
SELECT prod_id, prod_price, prod_name 
FROM products 
ORDER BY prod_price, prod_name;
// 先按prod_price排序，再对prod_price相同的行按prod_name排序
```

- 降序排序
指定`DESC`关键字，只应用到前一个列。
```mysql
SELECT prod_id, prod_name, prod_name 
FROM products 
ORDER BY prod_price DESC, prod_name;
// 先按prod_price降序，再按prod_name升序；注意`
```
如果要对所有的列进行降序排序，必须对每个列指定`DESC`关键字

利用`ORDER BY`与`LIMIT`的组合，能够找出一个列中最高或最低的值
```mysql
SELECT prod_price 
FROM products 
ORDER BY prod_price DESC 
LIMIT 1;
// 注意 LIMIT 必须位于 ORDER BY 之后
// 使用子句的次序不对将产生错误消息
```
## 6. 过滤数据
**在`SELECT`语句中，数据根据`WHERE`子句中指定的搜索条件进行过滤。**

*注意：应该让`ORDER BY`位于`WHERE`子句之后*
### `where` 子句操作符

|  操作符   |        说明        |
| :-------: | :----------------: |
|     =     |        等于        |
|    <>     |       不等于       |
|    !=     |       不等于       |
|     <     |        小于        |
|    <=     |      小于等于      |
|     >     |        大于        |
|    >=     |      大于等于      |
| `BETWEEN` | 在指定的两个值之间 |



例:

```sql
SELECT prod_name, prod_price
FROM products
WHERE prod_price = 2.5;
```

```sql
SELECT prod_name, prod_price
FROM products
WHERE prod_name = 'fuses';
// MySQL 执行匹配时默认不区分大小写；单引号用来限定字符串
```
```sql
SELECT vend_id, prod_name
FROM products
WHERE vend_id <> 1003;
```
- 范围值检查
```sql
SELECT prod_name, prod_price
FROM products
WHERE prod_price BETWEEN 5 AND 10;
```
- 空值检查
```sql
SELECT prod_name
FROM products
WHERE prod_price IS NULL;
```

**在通过过滤选择出不具有特定值的行时，不会返回具有`NULL`值的行**

## 7. 高级数据过滤

- MySQL允许给出多个`WHERE`子句，需要用`AND`或者`OR`连接
```sql
SELECT prod_id, prod_price, prod_name
FROM products
WHERE vend_id = 1003 AND prod_price <= 10;
```
```sql
SELECT prod_name, prod_price
FROM products
WHERE vend_id = 1002 OR vend_id = 1003 AND prod_price >= 10;
// 同大多数语言一样，先处理 AND，再处理 OR
// 建议使用括号明确操作符的相应顺序
```

- `IN`操作符
```sql
SELECT * FROM Persons
WHERE LastName IN ('Adams','Carter')
```
- `NOT`操作符
```mysql
SELECT prod_name, prod_price
FROM products
WHERE vend_id NOT IN (1002, 1003)
ORDER BY prod_name;
// 否定 NOT 之后的所跟的任何条件
```

**MySQL支持使用`NOT`对`IN`, `BETWEEN`和`EXISTS`等子句取反**

## 8. 使用通配符进行过滤

**通配符是用来匹配值的一部分的特殊字符**

- 百分号（`%`），匹配任意字符出现任意次数
```mysql
SELECT prod_name
FROM products
WHERE prod_name LIKE 's%e';
```
- 下划线通配符（`_`），匹配任意单个字符
- 使用`NOT`对`LIKE`子句取反
```mysql
SELECT first_name, last_name
FROM employees
WHERE first_name NOT LIKE 'M%'
ORDER BY first_name;
```

*注意：尾空格可能影响通配符匹配；`%`不能匹配`NULL`*

## 9. 用正则表达式进行匹配
**MySQL 仅支持多数正则表达式实现的一个很小的子集**

*注意：`LIKE`匹配整个列，而`REGEXP`在列值内进行匹配，如果匹配的文本在列值中出现（如: `price 1000`中包含了数字`1000`），`REGEXP`会找到它，相应的行会返回。这是二者的差别*

```mysql
...
WHERE prod_name REGEXP BINARY 'JetPack .000';
// . 匹配任意一个字符
// MySQL 正则表达式匹配不支持大小写
// 为区分大小写，可以使用 BINARY 关键词
```
**MySQL 的转义字符包含两个反斜杠`\\`**

```mysql
SELECT vend_name
FROM vendors
WHERE vend_name REGEXP '\\.'
ORDER BY vend_name;
//  \\. 匹配 .
```

## 10. 创建计算字段

- 使用函数和别名
```mysql
SELECT Concat(Trim(vend_name), '(', Trim(vend_country), ')') AS vend_title
FROM vendors
ORDER BY vend_name;
// 使用了 Concat 函数和 Trim 函数
// AS 给列取别名
```
- 执行算术计算
```mysql
SELECT prod_id,
    quantity,
    item_price,
    quantity * item_price AS expanded_price
FROM orderitems
WHERE order_num = 20005;
// 创建一个新的计算字段并取别名
```

## 11. 使用数据处理函数

|           文本处理函数            |              说明               |
| :-------------------------------: | :-----------------------------: |
|            `Length()`             |          返回串的长度           |
|       `Left(field, length)`       |  返回串最左边的长length的字符   |
|      `Right(field, length)`       |  返回串最右边的长length的字符   |
| `SubString(field, start, length)` | 返回从start开始长为length的子串 |
|        `Lower() / Upper()`        |        返回串的小写/大写        |
|        `RTrim() / LTrim()`        |      去除串右边/左边的空格      |



| 日期和时间处理函数 |            说明            |
| :----------------: | :------------------------: |
|      `Now()`       |        返回当前时间        |
|      `Date()`      |   返回日期时间的日期部分   |
|      `Year()`      |       返回日期的年份       |
|     `Month()`      |       返回日期的月份       |
|      `Day()`       |     返回日期的天数部分     |
|   `DayOfWeek()`    | 对于一个日期，返回是星期几 |
|      `Time()`      | 返回一个日期时间的时间部分 |
|      `Hour()`      |     返回时间的小时部分     |
|     `Minute()`     |     返回时间的分钟部分     |
|     `Second()`     |      返回时间的秒部分      |
|  `Date_Format()`   |  返回格式化的日期或时间串  |

例
-

```mysql
SELECT cust_id, order_name
FROM orders
WHERE Date(order_date) BETWEEN '2005-09-01' AND '2005-09-30';
```
```mysql
SELECT cust_id, order_name
FROM orders
WHERE Year(order_date) = 2005 AND Month(order_date) = 9;
```

此外，MySQL还支持数值处理函数，如`Abs(), Cos(), Mod(), Sqrt()`等（`Mod`函数可以用来判断奇偶）

其他常用函数：

|    函数名     | 说明                      |
| :-----------: | ------------------------- |
| `FIRST, LAST` | 返回该列的第一个/最后一个 |



## 12. 汇总数据

- 聚集函数
聚集函数包括`AVG, COUNT, MAX, MIN, SUM`等
```mysql
SELECT AVG(prod_price) AS avg_price
FROM products;
// AVG 函数会忽略值为 NULL 的行
```

`Count`函数有两种使用方式：
1. 使用`Count(*)`对表中的行数进行计数，不管有没有 NULL 值
2. 使用`Count(col_name)`对特定列中具有值的行进行技术，忽略 NULL 值

```mysql
// 使用 SUM 进行合计计算
SELECT SUM(item_price * quantity) AS total
FROM orderitems
WHERE order_num = 20005;
```
- 聚集不同值
使用`DISTINCT`来聚集不同值

_注意：`DISTINCT`不能用于`COUNT(*)`， 并且`DISTINCT`必须使用列名，不能使用计算或者表达式_
```mysql
SELECT AVG(DISTINCT prod_price) AS avs_price
FROM products;
// 提取 prod_price 列的所有不同值求平均
```

## 19. 插入数据

**`INSERT INTO`：用来插入行到数据库表中的**

插入可以用几种方式使用：

-   插入完整的行

-   插入行的一部分

-   插入多行

-   插入某些查询的结果



- 建议使用的插入方法
```mysql
INSERT INTO customers(cust_name,
                      cust_city,
                      cust_state,
                      cust_zip,
                      cust_country,
                      cust_contact,
                      cust_email)
VALUES('Pep E. LAPew',
      '100 Main Street',
      'CA',
      'Los Angeles',
      '90046',
      'USA',
      NULL,
      NULL);
```

在表名后明确给出列名。在插入行时，MySQL将用`VALUSE`列表中的相应值填入列表中的相应项。即便表的结构发生变化，此语句仍然能够执行。

_如果不提供列名，则必须给每个表列一个值，否则报错_

_如果表的定义允许，则可以在插入时省略某些列（该列定义为允许`NULL`值，或在表定义中给出默认值）_

-   同时插入多行

```mysql
INSERT INTO customers(...)
VALUES(...), (...), (...);
// 单条 INSERT 语句有多组值，每组值用一对圆括号括起来，用逗号分隔
```



Tips：可以使用 `INSERT LOW_PRIORITY INTO` 来降低`INSERT`语句的优先级，这也适用于`UPDATE`和`DELETE`语句



-   插入检索出的数据

```mysql
INSERT INTO customers(cust_id,
                     cust_contact,
                     cust_email,
                     cust_name,
                     cust_address,
                     cust_city,
                     cust_state,
                     cust_zip,
                     cust_country)
SELECT cust_id, cust_contact, cust_email,
	cust_name, cust_address, cust_city, cust_state,
	cust_zip, cust_country)
FROM custnew;
// MySQL 不关心 SELECT 返回的列名，只使用列的位置
```

这个例子将custnew表中的所有数据导入customers

`SELECT`语句也可包含`WHERE`子句以过滤插入的数据



## 20. 更新和删除数据

`UPDATE`语句用来更新表中的数据，可以更新表中的特定行，也可以更新表中的所有行。



_使用 `UPDATE` 的时候一定要注意 `WHERE` 子句，稍不注意就会更新所有行_

-   更新数据

```mysql
UPDATE customers
SET cust_email = 'elmer@fudd.com'
WHEE cust_id = 10005
```

+   删除数据，使用 `DELETE FROM` 语句

```mysql
DELETE FROM customers
WHERE cust_id = 10005;
```



### MySQL 中的数据类型



#### 串数据类型

| 数据类型 | 说明 |
| :-: | :-|
| `CHAR` |1 - 255 个字符的定长串，长度在创建时指定，CHAR(n)|
| `TEXT` |最大长度为 64KB 的变长文本|
| `VARCHAR` |长度可变但不超过255字节。创建时指定为 VARCHAR(n)，则可以存储0到n个字符|
|  ||

注意：

1.  MySQL 处理定长列比变长列要快许多
2.  `CHAR`类型的不足长度用空格补齐
3.  `VARCHAR`类型还要用1-2字节保存长度信息



#### 数值数据类型

|      数据类型      | 说明                       |
| :----------------: | -------------------------- |
|     `TINYINT`      | 支持 -128 - 127 的整数值   |
|  `INT`或`INTEGER`  | 支持 32 位整数             |
| `FLOAT` , `DOUBLE` | 分别是单精度、双精度浮点数 |
|      `BIGINT`      | 大整数                     |

注意：

1.  如果不需要存储负值，可以使用 `UNSIGNED` 关键字

2.  在创建表时`int(5)`的意思是用0补齐左边，比如 1 -> 00001

    

#### 日期和时间存储类型

|  数据类型   | 说明                                                         |
| :---------: | ------------------------------------------------------------ |
|   `DATE`    | 表示 1000-01-01 $\sim$ 9999-12-31 的日期，格式为 `YYYY-MM-DD` |
|   `TIME`    | 格式为 `HH:MM:SS`                                            |
| `DATETIME`  | 是`DATE`和`TIME`的组合                                       |
| `TIMESTAMP` | 功能和`DATETIME`相同（但范围较小）                           |
|   `YEAR`    | 用两位数字表示，范围是 70(1970年) - 69(2069年)，用四位数字表示，范围是 1901-2155年 |

