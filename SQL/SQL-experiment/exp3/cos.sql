/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2018/8/27 20:15:04                           */
/*==============================================================*/


drop table if exists Patron;

drop table if exists deliever;

drop table if exists food;

drop table if exists menu;

drop table if exists message;

drop table if exists orderlist;

/*==============================================================*/
/* Table: Patron                                                */
/*==============================================================*/
create table Patron
(
   id                   varchar(10) not null,
   name                 varchar(20),
   password             varchar(20),
   location             varchar(50),
   email                varchar(20),
   primary key (id)
);

alter table Patron comment '用户表';

/*==============================================================*/
/* Table: deliever                                              */
/*==============================================================*/
create table deliever
(
   deliever_id          varchar(10) not null,
   deliever_name        varchar(10),
   primary key (deliever_id)
);

/*==============================================================*/
/* Table: food                                                  */
/*==============================================================*/
create table food
(
   food_id              varchar(10) not null,
   message_id           varchar(10),
   menu_id              varchar(10),
   mes_message_id       varchar(10),
   food_name            varchar(30),
   food_cnt             int,
   menu___id            varchar(10),
   primary key (food_id)
);

alter table food comment '食材表';

/*==============================================================*/
/* Table: menu                                                  */
/*==============================================================*/
create table menu
(
   menu_id              varchar(10) not null,
   message_id           varchar(10),
   mes_message_id       varchar(10),
   order_id             varchar(10),
   menu_cnt             int,
   menu_date            date,
   menu_name            varchar(50),
   primary key (menu_id)
);

alter table menu comment '用户可以定的套餐';

/*==============================================================*/
/* Table: message                                               */
/*==============================================================*/
create table message
(
   message_id           varchar(10) not null,
   message_name         varchar(20),
   password             varchar(10),
   primary key (message_id)
);

alter table message comment '修改menu的管理员';

/*==============================================================*/
/* Table: orderlist                                             */
/*==============================================================*/
create table orderlist
(
   order_id             varchar(10) not null,
   id                   varchar(10),
   del_deliever_id      varchar(10),
   patron_id            varchar(10),
   type                 varchar(20),
   order_time           date,
   menu___id            varchar(10),
   deliever_id          varchar(10),
   primary key (order_id)
);

alter table food add constraint FK_food_menu_r foreign key (menu_id)
      references menu (menu_id) on delete restrict on update restrict;

alter table food add constraint FK_messager_food_r foreign key (message_id)
      references message (message_id) on delete restrict on update restrict;

alter table food add constraint FK_messager_food_re foreign key (mes_message_id)
      references message (message_id) on delete restrict on update restrict;

alter table menu add constraint FK_messager_menu_r foreign key (mes_message_id)
      references message (message_id) on delete restrict on update restrict;

alter table menu add constraint FK_messager_menu_re foreign key (message_id)
      references message (message_id) on delete restrict on update restrict;

alter table menu add constraint FK_order_menu_r foreign key (order_id)
      references orderlist (order_id) on delete restrict on update restrict;

alter table orderlist add constraint FK_deliever_order_r foreign key (del_deliever_id)
      references deliever (deliever_id) on delete restrict on update restrict;

alter table orderlist add constraint FK_patron_order_r foreign key (id)
      references Patron (id) on delete restrict on update restrict;

