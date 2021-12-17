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
2. Make the second depended on the first one (should start only after the first)
3. Write a timer for the second one and configure it to run on 01.01.2019 at 00:00
4. Start all daemons and timer, check their statuses, timer list and /tmp/homework
5. Stop all daemons and timer


cron/anacron
1. Create an anacron job which executes a script with echo Hello > /opt/hello and runs 
every 2 days
2. Create a cron job which executes the same command (will be better to create a script for 
this) and runs it in 1 minute after system boot.
3. Restart your virtual machine and check previous job proper execution
-----


lsof
1. Run a sleep command, redirect stdout and stderr into two different files (both of them will 
be empty).
2. Find with the lsof command which files this process uses, also find from which file it gain 
stdin.
3. List all ESTABLISHED TCP connections ONLY with lsof
