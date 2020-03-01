reate table t_user(
fid  INT  not null AUTO_INCREMENT,
fusername varchar(100)  not null comment '用户名称',
fsalt     varchar(256)  null comment '加密盐值',
fcreatetime datetime not null comment '创建时间',
fnotes    varchar(10000) not null comment '留言',
primary key (fid));

insert into t_user(fusername,fcreatetime,fnotes)
values('aaa',CURRENT_TIMESTAMP(),'python好难qwq');

select * from t_user;

insert into t_user(fusername,fcreatetime,fnotes)
values('bbb',CURRENT_TIMESTAMP(),'没错你咋这么蠢呢');

select * from t_user;