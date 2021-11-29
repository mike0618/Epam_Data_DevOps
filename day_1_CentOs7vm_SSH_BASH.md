-0-
Установить вторую ВМ, настроить на ней только внутренний сетевой интерфейс и подключиться с первой машины.
Все команды выполняются от имени созданного во время инсталляции пользователя (не root).
---

Установил вторую vm с одним сетевым адаптером Internal Network intnet
```
ip link show показал enp0s17
```
Сделал конфигурацию 
/etc/sysconfig/network-scripts/ifcfg-eth0
```
  DEVICE=enp0s17
  ONBOOT=yes
  IPADDR=192.168.2.10
  NETMASK=255.255.255.0
  GATEWAY=192.168.2.1
```
  
Для первой машины добавил второй адаптер Internal Network intnet
```
ip link show показал новый enp0s8
```
Сделал конфигурацию 
/etc/sysconfig/network-scripts/ifcfg-eth0
```
  DEVICE=enp0s8
  ONBOOT=yes
  IPADDR=192.168.2.9
  NETMASK=255.255.255.0
  GATEWAY=192.168.2.1
```

Подключился по ssh ко второй машине из первой ssh user@192.168.1.10
Так же осталась возможность подключения с хоста к первой машине

-1-
Внутри директории /usr/share/man (хранилище встроенной документации) находятся каталоги, разбитые по секциям разделов помощи (man1, man2, man3) и по языкам (es, fr, ru).
Используя команду ls, необходимо вывести на экран все файлы, которые расположены в секционных директориях /usr/share/man/manX и содержат слово "config" в имени. Одним вызовом ls найти все файлы, содержащие слово "system" в каталогах /usr/share/man/man1 и /usr/share/man/man7
---

```bash
cd /usr/share/man
ls man?/*config*

man1/pkg-config.1.gz      man5/x509v3_config.5ssl.gz  man8/lvm-config.8.gz
man5/config.5ssl.gz       man8/authconfig.8.gz        man8/lvmconfig.8.gz
man5/config-util.5.gz     man8/authconfig-tui.8.gz    man8/lvm-dumpconfig.8.gz
man5/selinux_config.5.gz  man8/chkconfig.8.gz         man8/sys-unconfig.8.gz
man5/ssh_config.5.gz      man8/grub2-mkconfig.8.gz
man5/sshd_config.5.gz     man8/iprconfig.8.gz

ls man{1,7}/*system*

man1/systemctl.1.gz                  man1/systemd-machine-id-commit.1.gz
man1/systemd.1.gz                    man1/systemd-machine-id-setup.1.gz
man1/systemd-analyze.1.gz            man1/systemd-notify.1.gz
man1/systemd-ask-password.1.gz       man1/systemd-nspawn.1.gz
man1/systemd-bootchart.1.gz          man1/systemd-path.1.gz
man1/systemd-cat.1.gz                man1/systemd-run.1.gz
man1/systemd-cgls.1.gz               man1/systemd-tty-ask-password-agent.1.gz
man1/systemd-cgtop.1.gz              man7/lvmsystemid.7.gz
man1/systemd-delta.1.gz              man7/systemd.directives.7.gz
man1/systemd-detect-virt.1.gz        man7/systemd.generator.7.gz
man1/systemd-escape.1.gz             man7/systemd.index.7.gz
man1/systemd-firstboot.1.gz          man7/systemd.journal-fields.7.gz
man1/systemd-firstboot.service.1.gz  man7/systemd.special.7.gz
man1/systemd-inhibit.1.gz            man7/systemd.time.7.gz

```
-l вывод в виде подробного списка
-a вывод файлов начитающихся с точки (скрытых)
Я со ссылками что-то напутал

-2-
Самостоятельно изучить команду find, предназначенную для поиска файлов/папок по заданным условиям (man find, find --help).
Найти в директории /usr/share/man все файлы, которые содержат слово "help" в имени, найти там же все файлы, имя которых начинается на "conf".
Какие действия мы можем выполнить с файлами, найденными командой find (не запуская других команд)? Приведите любой пример с комментарием.
---

```bash
cd /usr/share/man
find . -name "*help*"

./man1/help.1.gz
./man5/firewalld.helper.5.gz
./man8/mkhomedir_helper.8.gz
./man8/pwhistory_helper.8.gz
./man8/ssh-pkcs11-helper.8.gz

find . -name "conf*"

./man5/config.5ssl.gz
./man5/config-util.5.gz

```
можно добавить -type f для поиска regular files

```bash
find . -name "*help*" -delete
```
удалить все файлы в текущей папке, содержащие help в названии

```bash
find . -name "*help*" -fprint files
```
сохранить имена найденых файлов в файл files

-3-
При помощи команд head и tail, выведите последние 2 строки файла /etc/fstab и первые 7 строк файла /etc/yum.conf
Что произойдёт, если мы запросим больше строк, чем есть в файле? Попробуйте выполнить это на примере, используя команду wc (word cound) для подсчёта количества строк в файле.
---

```bash
tail -n 2 /etc/fstab

UUID=32ffc3b0-c9dc-4070-aa48-44836852b0be /boot                   xfs     defaults        0 0
/dev/mapper/centos-swap swap                    swap    defaults        0 0

head -n 7 /etc/yum.conf

[main]
cachedir=/var/cache/yum/$basearch/$releasever
keepcache=0
debuglevel=2
logfile=/var/log/yum.log
exactarch=1
obsoletes=1

cat <(tail -n 2 /etc/fstab) <(head -n 7 /etc/yum.conf)

UUID=32ffc3b0-c9dc-4070-aa48-44836852b0be /boot                   xfs     defaults        0 0
/dev/mapper/centos-swap swap                    swap    defaults        0 0
[main]
cachedir=/var/cache/yum/$basearch/$releasever
keepcache=0
debuglevel=2
logfile=/var/log/yum.log
exactarch=1
obsoletes=1

```
последние 2 строки файла fstab и первые 7 строк файла yum.conf вместе

если задать больше строк, чем есть в файле, получим все строки, что есть в файле
```bash
length=`cat /etc/yum.conf | wc -l`
head=`head -n 7777 /etc/yum.conf | wc -l`
if [ $length -lt 7777 -a $length -eq $head ]; then echo 'That is true!'; fi

That is true!

```

-4-
Создайте в домашней директории файлы file_name1.md, file_name2.md и file_name3.md. Используя {}, переименуйте:
file_name1.md в file_name1.textdoc
file_name2.md в file_name2
file_name3.md в file_name3.md.latest
file_name1.textdoc в file_name1.txt
---

```bash
touch file_name{1..3}.md
mv file_name1.{md,textdoc}
mv file_name2{.md,}
mv file_name3.md{,.latest}
mv file_name1.t{extdoc,xt}
```

-5-
Перейдите в директорию /mnt. Напишите как можно больше различных вариантов команды cd, с помощью которых вы можете вернуться обратно в домашнюю директорию вашего пользователя. Различные относительные пути также считаются разными вариантами.
---

```bash
cd
cd ~
cd $HOME
cd /home/$USER
cd ../home/$USER
cd /tmp/../home/$USER
cd /./././../home/$USER
```
можно продолжать до бесконечности

-6-
Создайте одной командой в домашней директории 3 папки new, in-process, processed. При этом in-process должна содержать в себе еще 3 папки tread0, tread1, tread2.
Далее создайте 100 файлов формата data[[:digit:]][[:digit:]] в папке new
Скопируйте 34 файла в tread0 и по 33 в tread1 и tread2 соответственно. Выведете содержимое каталога in-process одной командой
После этого переместите все файлы из каталогов tread в processed одной командой. Выведете содержимое каталога in-process и processed опять же одной командой.
Сравните количество файлов в каталогах new и processed при помощи изученных ранее команд, если они равны удалите файлы из new.
** Сравнение количества и удаление сделано при помощи условия
---

```bash
mkdir -p new in-process/tread{0..2} processed
touch new/data{00..99}
cp new/data{00..33} in-process/tread0
cp new/data{34..66} in-process/tread1
cp new/data{67..99} in-process/tread2
ls -R in-process

in-process:
tread0  tread1  tread2

in-process/tread0:
data00  data03  data06  data09  data12  data15  data18  data21  data24  data27  data30  data33
data01  data04  data07  data10  data13  data16  data19  data22  data25  data28  data31
data02  data05  data08  data11  data14  data17  data20  data23  data26  data29  data32

in-process/tread1:
data34  data37  data40  data43  data46  data49  data52  data55  data58  data61  data64
data35  data38  data41  data44  data47  data50  data53  data56  data59  data62  data65
data36  data39  data42  data45  data48  data51  data54  data57  data60  data63  data66

in-process/tread2:
data67  data70  data73  data76  data79  data82  data85  data88  data91  data94  data97
data68  data71  data74  data77  data80  data83  data86  data89  data92  data95  data98
data69  data72  data75  data78  data81  data84  data87  data90  data93  data96  data99

mv in-process/tread*/* processed
ls -R in-process processed

in-process:
tread0  tread1  tread2

in-process/tread0:

in-process/tread1:

in-process/tread2:

processed:
data00  data08  data16  data24  data32  data40  data48  data56  data64  data72  data80  data88  data96
data01  data09  data17  data25  data33  data41  data49  data57  data65  data73  data81  data89  data97
data02  data10  data18  data26  data34  data42  data50  data58  data66  data74  data82  data90  data98
data03  data11  data19  data27  data35  data43  data51  data59  data67  data75  data83  data91  data99
data04  data12  data20  data28  data36  data44  data52  data60  data68  data76  data84  data92
data05  data13  data21  data29  data37  data45  data53  data61  data69  data77  data85  data93
data06  data14  data22  data30  data38  data46  data54  data62  data70  data78  data86  data94
data07  data15  data23  data31  data39  data47  data55  data63  data71  data79  data87  data95

if [ `ls new | wc -l` == `ls processed | wc -l` ]; then rm new/*; fi

```

-7-
Получить разворачивание фигурных скобок для выражения. Согласно стандартному поведению bash, стандартного для CentOS 7, скобки в приведённом ниже выражении развёрнуты не будут. Необходимо найти способ получить ожидаемый вывод.
a=1; b=3
echo file{$a..$b}
Необходимо предоставить модицицированную команду, результатом которой является следующий вывод: 
file1 file2 file3
---

```bash
a=1
b=3
eval echo file{$a..$b}

file1 file2 file3

```
Сначала выполняется brace expansion, потом var expension. В целях безопастности bash не рассчитывает переменные, но можно сделать принудительно с помощью eval
На форумах пишут, что eval - зло. Можно сделать с помощью цикла и seq, но это уже не brace expansion. Или использовать zsh
