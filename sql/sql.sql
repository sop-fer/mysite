drop table auth_group;
drop table auth_group_permissions;
drop table auth_permission;
drop table auth_user;
drop table auth_user_groups;
drop table auth_user_user_permissions;
drop table django_admin_log;
drop table django_content_type;
drop table django_migrations;
drop table django_session;
drop table myapp_student;
drop table myapp_grade;

select * from myapp_student limit 10;

insert into myapp_student(sname,sage,sgender,scontent) values
('s2',3,0,'i am s2, i am 3, i am a boy'),
('s2',3,0,'i am s2, i am 3, i am a boy'),
('s2',3,0,'i am s2, i am 3, i am a boy'),
('s2',3,0,'i am s2, i am 3, i am a boy'),
('s2',3,0,'i am s2, i am 3, i am a boy')