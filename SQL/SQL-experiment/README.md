# 2018/8
# 数据库实验课
# 实验1 
# 环境搭建与MySQL基本操作
    1.下载并安装MySQL,MySQL Workbench  
    2.MySQL服务启动、停止    
    3.新建cos数据库，并为该数据库新建用户cos_admin，分配权限为DBA  
    3.新建Patron表，用户名（varchar）,密码，住址。修改Patron表，加入电话号码字段  
  
# 实验二
# SQL语句练习
    1.完成patron表，menu表，food_item表的创建(主键，外键如果在此处没有考虑清楚，可以在下面的实验中逐步添加)  
    2.完成修改patron表的结构，增加一个字段patron的身份证号，然后再删除这个字段  
    3.任意新建一张表，然后删除此表  
    4.查询patron表中name字段的长度小于3的所有的人的记录  
    5.增加一种菜类型（menu），并增加这种类型的菜2~3样（food_item）  
    6.新建一个视图，包含patron表中的name,email两个字段  
    7.查询food_item表中的总记录数  
    8.查询patron表中手机尾号为’5728’的记录  
    9.将menu表按时间排序（升序）  
    10.查询出food_item表中menu_id以及对应的menu_id的菜的个数  
    11.查询出patron表中的前5条记录  
    12.查询出菜名为’土豆丝’的菜的价格，菜的描述以及它所属的菜的种类的名字  
    13.查询出food_item表中和’土豆丝’一样菜价的菜的名字，价格  
    
# 实验三
# 数据库设计&Powerdesiner使用
    1.下载并安装Powerdesigner 16.5  
    2.根据需求文档中功能需求部分的2.1和2.5，在PowerDesigner中建立相应的表概念数据模型，并将其转化为物理数据模型  
    3.根据1中完成的物理数据模型，利用PowerDesigner自动生成对应的数据库表  
      
# 实验四
# 数据库应用
    通过编写C++或Java或Python程序，来操作数据库表，对数据库中的记录进行增加，删除，查询和修改等操作  
