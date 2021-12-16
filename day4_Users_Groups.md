Task 1: Users and groups

Используйте команды: groupadd, useradd, passwd, chage и другие.
Создайте группу sales с GID 4000 и пользователей bob, alice, eve c основной группой sales. 
Измените пользователям пароли.
```
[mike@localhost ~]$ sudo passwd bob
[mike@localhost ~]$ sudo passwd alice
[mike@localhost ~]$ sudo passwd eve
```
Все новые аккаунты должны обязательно менять свои пароли каждый 30 дней.
Установил в /etc/login.defs
```
#	PASS_MAX_DAYS	Maximum number of days a password may be used.

PASS_MAX_DAYS	30
```
Новые аккаунты группы sales должны истечь по окончанию 90 дней срока, а bob должен изменять его пароль каждые 15 дней.
```
[mike@localhost ~]$ sudo groupadd -g 4000 sales
[root@localhost mike]# for user in bob alice eve; do useradd -g sales -e 90 $user; done
[mike@localhost ~]$ sudo chage -M 15 bob
```

Дополнительно:
Заставьте пользователей сменить пароль после первого логина.
```
[root@localhost mike]# for user in bob alice eve; do passwd -e $user; done
```

Предварительный шаг:
Исследуйте файл /etc/login.defs.
Исследуйте, как работает команда date и как её использовать совместно с chage.
```
[mike@localhost ~]$ sudo chage -d 0 $(date -d "-32 days" +%F) eve
# Заставит пользователя сменить пароль при первом логине, т.к. устанавливает дату последнего логина на 32 день ранее
```

Task 2: Controlling access to files with Linux file system permissions

Используйте команды: su, mkdir, chown, chmod и другие.
Создайте трёх пользователей glen, antony, lesly.
У вас должна быть директория /home/students, где эти три пользователя могут работать совместно с файлами.
Должен быть возможен только пользовательский и групповой доступ, создание и удаление файлов в /home/students. 
Файлы, созданные в этой директории, должны автоматически присваиваться группе студентов students.

```
[mike@localhost ~]$ sudo groupadd students
[mike@localhost ~]$ sudo mkdir /home/students
[root@localhost mike]# for user in glen antony lesly; do useradd -g students $user; done
[mike@localhost ~]$ sudo chmod 775 /home/students
[mike@localhost ~]$ sudo chown :students /home/students
[mike@localhost ~]$ sudo chmod g+s /home/students

```
Предварительный шаг:
Исследуйте, для чего нужны файлы .bashrc и .profile.
```
.bashrc содержит команды для оболочки bash. При запуске bash shell ищет этот файл в домашней директории и выполняет находящиеся в нем команды, если они есть. 
.profile содержит настройки вида консоли, переменные
```

Task3: ACL

Детективное агентство Бейкер Стрит создает коллекцию совместного доступа для хранения файлов дел, в которых члены группы bakerstreet будут иметь права на чтение и запись.
Ведущий детектив, Шерлок Холмс, решил, что члены группы scotlandyard также должны иметь возможность читать и писать в общую директорию. Тем не менее, Холмс считает, что инспектор Джонс является достаточно растерянным, и поэтому он должен иметь доступ только для чтения. 
Миссис Хадсон только начала осваивать Linux и смогла создать общую директорию и скопировать туда несколько файлов. Но сейчас время чаепития, и она попросила вас закончить работу.

Ваша задача - завершить настройку директории общего доступа. 
Директория и всё её содержимое должно принадлежать группе bakerstreet, при этом файлы должны обновляться для чтения и записи для владельца и группы (bakerstreet). У других пользователей не должно быть никаких разрешений. 
Вам также необходимо предоставить доступы на чтение и запись для группы scotlandyard, за исключением Jones, который может только читать документы.
Убедитесь, что ваша настройка применима к существующим и будущим файлам. После установки всех разрешений в директории проверьте от каждого пользователя все его возможные доступы.

Используйте команды: touch, mkdir, chgrp, chmod, getfacl, setfacl и другие. 
Создайте общую директорию /share/cases.
Создайте группу bakerstreet с пользователями holmes, watson.
Создайте группу scotlandyard с пользователями lestrade, gregson, jones.
Задайте всем пользователям безопасные пароли.

Предварительный шаг:
От суперпользователя создайте папку /share/cases и создайте внутри 2 файла murders.txt и moriarty.txt.
