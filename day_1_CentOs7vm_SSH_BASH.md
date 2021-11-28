-0-

Установил вторую vm с одним сетевым адаптером Internal Network intnet
ip link show показал enp0s17
Сделал конфигурацию /etc/sysconfig/network-scripts/ifcfg-eth0
  DEVICE=enp0s17
  ONBOOT=yes
  IPADDR=192.168.2.10
  NETMASK=255.255.255.0
  GATEWAY=192.168.2.1
  
Для первой машины добавил второй адаптер Internal Network intnet
ip link show показал новый enp0s8
Сделал конфигурацию /etc/sysconfig/network-scripts/ifcfg-eth0
  DEVICE=enp0s8
  ONBOOT=yes
  IPADDR=192.168.2.9
  NETMASK=255.255.255.0
  GATEWAY=192.168.2.1

Подключился по ssh ко второй машине из первой ssh user@192.168.1.10
Так же осталась возможность подключения с хоста к первой машине

-1-

cd /usr/share/man
ls -la man* | grep 'config'
ls -la man{1,7} | grep 'system'
-la подробный список всех файлов в тч ссылок

-2-

cd /usr/share/man
find . -name "*help*"
find . -name "conf*"
можно добавить -type f для поиска regular files

find . -name "*help*" -delete
удалить все файлы в текущей папке, содержащие help в названии

find . -name "*help*" -fprint files
сохранить имена найденых файлов в файл files

-3-

tail -n 2 /etc/fstab
head -n 7 /etc/yum.conf

cat <(tail -n 2 /etc/fstab) <(head -n 7 /etc/yum.conf)
последние 2 строки файла fstab и первые 7 строк файла yum.conf вместе

если задать больше строк, чем есть в файле, получим все строки, что есть в файле

-4-

touch file_name{1..3}.md
mv file_name1.md file_name1.textdoc
mv file_name2.md file_name2
mv file_name3.md file_name3.md.latest
mv file_name1.textdoc file_name1.txt

-5-

cd
cd ~
cd $HOME
cd /home/$USER
cd ../home/$USER
cd /tmp/../home/$USER
cd /./././../home/$USER
можно продолжать до бесконечности

-6-

mkdir -p new in-process/tread{0..2} processed
touch new/data{00..99}
cp -t in-process/tread0 new/data{00..33}
cp -t in-process/tread1 new/data{34..66}
cp -t in-process/tread2 new/data{67..99}
ls -R in-process
mv in-process/tread*/* processed
ls -R in-process processed
if [ `ls new | wc -l` == `ls processed | wc -l` ]; then rm new/*; fi

-7-

a=1
b=3
eval echo file{$a..$b}
Сначала выполняется brace expansion, потом var expension. В целях безопастности bash не рассчитывает переменные, но можно сделать принудительно с помощью eval
На форумах пишет, что eval - зло. Можно сделать с помощью цикла и seq, но это уже не brace expansion. Или использовать zsh


