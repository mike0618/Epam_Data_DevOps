Processes
1. Run a sleep command three times at different intervals
```
[mike@localhost ~]$ sleep 1111 & sleep 2222 & sleep 3333 &
[1] 3498
[2] 3499
[3] 3500

```
2. Send a SIGSTOP signal to all of them in three different ways.
```
[mike@localhost ~]$ kill -SIGSTOP 3498 3499 3500
[mike@localhost ~]$ kill -19 {3498..3500}
[mike@localhost ~]$ kill -19 %1 %2 %3

```
3. Check their statuses with a job command
```
[mike@localhost ~]$ jobs
[1]   Stopped                 sleep 1111
[2]-  Stopped                 sleep 2222
[3]+  Stopped                 sleep 3333

```
4. Terminate one of them. (Any)
```
[mike@localhost ~]$ kill %1
[mike@localhost ~]$ jobs
[1]   Terminated              sleep 1111
[2]-  Stopped                 sleep 2222
[3]+  Stopped                 sleep 3333

```
5. To other send a SIGCONT in two different ways.
```
[mike@localhost ~]$ kill -SIGCONT 3499
[mike@localhost ~]$ kill -18 %2
[mike@localhost ~]$ jobs
[2]-  Running                 sleep 2222 &
[3]+  Stopped                 sleep 3333

```
6. Kill one by PID and the second one by job ID
```
[mike@localhost ~]$ kill %2
[mike@localhost ~]$ kill 3500
```


systemd
1. Write two daemons: one should be a simple daemon and do sleep 10 after a start and 
then do echo 1 > /tmp/homework, the second one should be oneshot and do echo 2 > 
/tmp/homework without any sleep
```
firstd

#! /bin/bash
sleep 10
echo 1 > /tmp/homework

secondd

#! /bin/bash
echo 2 > /tmp/homework
```
2. Make the second depended on the first one (should start only after the first)
```
my1.service

[Unit]
Description=My First Unit

[Service]
ExecStart=/home/mike/firstd

[Install]
WantedBy=multi-user.target

my2.service

[Unit]
Description=My Second Unit
After=my1.service
Requires=my1.service

[Service]
Type=oneshot
ExecStart=/home/mike/secondd

[Install]
WantedBy=multi-user.target
```
3. Write a timer for the second one and configure it to run on 01.01.2019 at 00:00
```
mytimer.timer

[Unit]
Description=My Timer
Requires=my2.service

[Timer]
Unit=my2.service
OnCalendar=2019-01-01 00:00:00

[Install]
WantedBy=timers.target
```
4. Start all daemons and timer, check their statuses, timer list and /tmp/homework
```
[root@localhost mike]# systemctl start my1.service
[root@localhost mike]# systemctl start my2.service
[root@localhost mike]# systemctl start mytimer.timer

[root@localhost mike]# cat /tmp/homework 
2
# After 10s:
[root@localhost mike]# cat /tmp/homework 
1

[root@localhost mike]# systemctl status my1.service
● my1.service - My First Unit
   Loaded: loaded (/etc/systemd/system/my1.service; disabled; vendor preset: disabled)
   Active: inactive (dead) since Fri 2021-12-17 12:20:09 MSK; 1min 29s ago
  Process: 4403 ExecStart=/home/mike/firstd (code=exited, status=0/SUCCESS)
 Main PID: 4403 (code=exited, status=0/SUCCESS)

Dec 17 12:19:59 localhost.localdomain systemd[1]: Started My First Unit.

[root@localhost mike]# systemctl status my2.service
● my2.service - My Second Unit
   Loaded: loaded (/etc/systemd/system/my2.service; disabled; vendor preset: disabled)
   Active: inactive (dead) since Fri 2021-12-17 12:19:59 MSK; 2min 38s ago
  Process: 4404 ExecStart=/home/mike/secondd (code=exited, status=0/SUCCESS)
 Main PID: 4404 (code=exited, status=0/SUCCESS)

Dec 17 12:19:59 localhost.localdomain systemd[1]: Starting My Second Unit...
Dec 17 12:19:59 localhost.localdomain systemd[1]: Started My Second Unit.

[root@localhost mike]# systemctl status mytimer.timer
● mytimer.timer - My Timer
   Loaded: loaded (/etc/systemd/system/mytimer.timer; disabled; vendor preset: disabled)
   Active: active (elapsed) since Fri 2021-12-17 12:14:26 MSK; 6min ago

Dec 17 12:14:26 localhost.localdomain systemd[1]: Started My Timer.

[root@localhost mike]# systemctl list-timers --all
NEXT                         LEFT     LAST                         PASSED  UNIT                         ACTIVATES
n/a                          n/a      n/a                          n/a     mytimer.timer                my2.service
Fri 2021-12-17 23:42:28 MSK  11h left Thu 2021-12-16 23:42:28 MSK  12h ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
n/a                          n/a      n/a                          n/a     systemd-readahead-done.timer systemd-readahead-done.service

3 timers listed.
```
5. Stop all daemons and timer
```
[root@localhost mike]# systemctl stop mytimer.timer
[root@localhost mike]# systemctl stop my2.service
[root@localhost mike]# systemctl stop my1.service
```

cron/anacron
1. Create an anacron job which executes a script with echo Hello > /opt/hello and runs 
every 2 days
```
[mike@localhost ~]$ sudo touch /opt/hello
[mike@localhost ~]$ sudo chown mike /opt/hello

hello.sh

#! /bin/bash
echo Hello > /opt/hello

[mike@localhost ~]$ chmod +x hello.sh

[root@localhost ~]# echo "2 0 hello_every2days /home/mike/hello.sh" >> /etc/anacrontab
```
2. Create a cron job which executes the same command (will be better to create a script for 
this) and runs it in 1 minute after system boot.
```
[mike@localhost ~]$ cp {,cron_}hello.sh
[mike@localhost ~]$ sed -i 's/Hello/"Hello from cron"/' cron_hello.sh

[mike@localhost ~]$ crontab -e

SHELL=/bin/bash
MAILTO=mike
@reboot sleep 60 && /home/mike/cron_hello.sh
```
3. Restart your virtual machine and check previous job proper execution
```
[mike@localhost ~]$ sudo reboot

# Right after boot:
[mike@localhost ~]$ cat /opt/hello

# A minute after boot:
[mike@localhost ~]$ cat /opt/hello
Hello from cron
```
-----


lsof
1. Run a sleep command, redirect stdout and stderr into two different files (both of them will 
be empty).
```
[mike@localhost ~]$ sleep 9999 1> out.log 2> err.log &
[1] 1417
```
2. Find with the lsof command which files this process uses, also find from which file it gain 
stdin.
```
[mike@localhost ~]$ lsof -p 1417
COMMAND  PID USER   FD   TYPE DEVICE  SIZE/OFF     NODE NAME
sleep   1417 mike  cwd    DIR  253,0      4096  4194383 /home/mike
sleep   1417 mike  rtd    DIR  253,0       274       64 /
sleep   1417 mike  txt    REG  253,0     33128 12741138 /usr/bin/sleep
sleep   1417 mike  mem    REG  253,0 106172832 12799883 /usr/lib/locale/locale-archive
sleep   1417 mike  mem    REG  253,0   2156272    15641 /usr/lib64/libc-2.17.so
sleep   1417 mike  mem    REG  253,0    163312    15634 /usr/lib64/ld-2.17.so
sleep   1417 mike    0u   CHR  136,1       0t0        4 /dev/pts/1
sleep   1417 mike    1w   REG  253,0         0  4195946 /home/mike/out.log
sleep   1417 mike    2w   REG  253,0         0  4195974 /home/mike/err.log

[mike@localhost ~]$ lsof -a -p 1417 -d 0
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
sleep   1417 mike    0u   CHR  136,1      0t0    4 /dev/pts/1

```
3. List all ESTABLISHED TCP connections ONLY with lsof
```
[mike@localhost ~]$ sudo lsof -iTCP -sTCP:ESTABLISHED
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
sshd    1284 root    3u  IPv4  18748      0t0  TCP localhost.localdomain:ssh->gateway:47494 (ESTABLISHED)
sshd    1288 mike    3u  IPv4  18748      0t0  TCP localhost.localdomain:ssh->gateway:47494 (ESTABLISHED)
sshd    1377 root    3u  IPv4  19453      0t0  TCP localhost.localdomain:ssh->gateway:47988 (ESTABLISHED)
sshd    1381 mike    3u  IPv4  19453      0t0  TCP localhost.localdomain:ssh->gateway:47988 (ESTABLISHED)
```
