1. add secondary ip address to you second network interface enp0s8. Each point must be presented with commands and showing that new address was applied to the interface. To repeat adding address for points 2 and 3 address must be deleted (please add deleting address to you homework log) Methods:
   1. using ip utility (stateless)
```
   [mike@localhost ~]$ ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
       valid_lft 64449sec preferred_lft 64449sec
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.2.9/24 brd 192.168.2.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever

[mike@localhost ~]$ sudo ip a add 192.168.2.99/24 dev enp0s8

[mike@localhost ~]$ ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
       valid_lft 64380sec preferred_lft 64380sec
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.2.9/24 brd 192.168.2.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet 192.168.2.99/24 scope global secondary enp0s8
       valid_lft forever preferred_lft forever

[mike@localhost ~]$ ping 192.168.2.99
PING 192.168.2.99 (192.168.2.99) 56(84) bytes of data.
64 bytes from 192.168.2.99: icmp_seq=1 ttl=64 time=0.183 ms
64 bytes from 192.168.2.99: icmp_seq=2 ttl=64 time=0.110 ms
64 bytes from 192.168.2.99: icmp_seq=3 ttl=64 time=0.111 ms
64 bytes from 192.168.2.99: icmp_seq=4 ttl=64 time=0.127 ms
64 bytes from 192.168.2.99: icmp_seq=5 ttl=64 time=0.131 ms
^C
--- 192.168.2.99 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 3997ms
rtt min/avg/max/mdev = 0.110/0.132/0.183/0.028 ms

[mike@10 ~]$ sudo ip a del 192.168.2.99/24 dev enp0s8

[mike@10 ~]$ ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
       valid_lft 64047sec preferred_lft 64047sec
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.2.9/24 brd 192.168.2.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever


```
   2. using centos network configuration file (statefull)
```
# set up config file (I don't know why it's not "ifcfg-enp0s8", but... It works!):
[mike@10 ~]$ sudo vi /etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=enp0s8
ONBOOT=yes
IPADDR0=192.168.2.9
IPADDR1=192.168.2.99
NETMASK=255.255.255.0
GATEWAY=192.168.2.1

[mike@10 ~]$ sudo ifdown enp0s8
Device 'enp0s8' successfully disconnected.
[mike@10 ~]$ sudo ifup enp0s8
Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/5)

[mike@10 ~]$ ip -4 a show enp0s8
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.2.9/24 brd 192.168.2.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet 192.168.2.99/24 brd 192.168.2.255 scope global secondary noprefixroute enp0s8
       valid_lft forever preferred_lft forever

# set up config file:
DEVICE=enp0s8
ONBOOT=yes
IPADDR=192.168.2.9
NETMASK=255.255.255.0
GATEWAY=192.168.2.1

[mike@10 ~]$ sudo ifdown enp0s8
Device 'enp0s8' successfully disconnected.
[mike@10 ~]$ sudo ifup enp0s8
Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/5)

[mike@10 ~]$ ip -4 a show enp0s8
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.2.9/24 brd 192.168.2.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever


```
   3. using nmcli utility (statefull)
```
[mike@10 ~]$ nmcli connection show
NAME         UUID                                  TYPE      DEVICE 
enp0s3       9975c189-27e7-4e33-b20f-7460491ccc82  ethernet  enp0s3 
System eth0  5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03  ethernet  enp0s8 

[mike@10 ~]$ sudo nmcli con mod 'System eth0' +ipv4.addresses "192.168.2.99/24"

[mike@10 ~]$ sudo nmcli device disconnect enp0s8
Device 'enp0s8' successfully disconnected.
[mike@10 ~]$ sudo nmcli device connect enp0s8
Device 'enp0s8' successfully activated with '5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03'.

[mike@10 ~]$ ip -4 a show enp0s8
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.2.9/24 brd 192.168.2.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet 192.168.2.99/24 brd 192.168.2.255 scope global secondary noprefixroute enp0s8
       valid_lft forever preferred_lft forever



```
2. You should have a possibility to use ssh client to connect to your node using new address from previous step. Run tcpdump in separate tmux session or separate connection before starting ssh client and capture packets that are related to this ssh connection. Find packets that are related to TCP session establish.
```
# Set up VBox - MyCentOs7 - Settings - Network - Port Forwarding - {Protocol: TCP, Host IP: 127.0.0.1, Host Port: 2222, Guest IP: 192.168.2.99, Guest Port: 22}
# On host machine. Flags [S] - TCP session established:
sudo tcpdump -i lo port 2222 > tcpdump.log

# Connect to virtual machine in other console

20:30:45.346595 IP localhost.51314 > localhost.2222: Flags [S], seq 771513756, win 65495, options [mss 65495,sackOK,TS val 844285421 ecr 0,nop,wscale 7], length 0
20:30:45.346618 IP localhost.2222 > localhost.51314: Flags [S.], seq 2105504145, ack 771513757, win 65483, options [mss 65495,sackOK,TS val 844285421 ecr 844285421,nop,wscale 1], length 0

# and tcpdump on virtual machine (it moves continuously):
12:50:44.659187 IP 192.168.2.99.ssh > 10.0.2.2.51458: Flags [P.], seq 1872760:1873020, ack 1153, win 40880, length 260
12:50:44.659247 IP 10.0.2.2.51458 > 192.168.2.99.ssh: Flags [.], ack 1873020, win 65535, length 0
12:50:44.659359 IP 192.168.2.99.ssh > 10.0.2.2.51458: Flags [P.], seq 1873020:1873280, ack 1153, win 40880, length 260
12:50:44.659454 IP 10.0.2.2.51458 > 192.168.2.99.ssh: Flags [.], ack 1873280, win 65535, length 0
12:50:44.659553 IP 192.168.2.99.ssh > 10.0.2.2.51458: Flags [P.], seq 1873280:1873540, ack 1153, win 40880, length 260
12:50:44.659612 IP 10.0.2.2.51458 > 192.168.2.99.ssh: Flags [.], ack 1873540, win 65535, length 0
12:50:44.659712 IP 192.168.2.99.ssh > 10.0.2.2.51458: Flags [P.], seq 1873540:1873800, ack 1153, win 40880, length 260
12:50:44.659783 IP 10.0.2.2.51458 > 192.168.2.99.ssh: Flags [.], ack 1873800, win 65535, length 0
12:50:44.659881 IP 192.168.2.99.ssh > 10.0.2.2.51458: Flags [P.], seq 1873800:1874060, ack 1153, win 40880, length 260
12:50:44.659941 IP 10.0.2.2.51458 > 192.168.2.99.ssh: Flags [.], ack 1874060, win 65535, length 0

```
3. Close session. Find in tcpdump output packets that are related to TCP session closure.
```
# Flags [F.] - Finish flag, indication of termination.
20:43:38.976904 IP localhost.51434 > localhost.2222: Flags [F.], seq 3778, ack 3074, win 512, options [nop,nop,TS val 845059052 ecr 845059051], length 0
20:43:38.992049 IP localhost.2222 > localhost.51434: Flags [F.], seq 3074, ack 3779, win 32742, options [nop,nop,TS val 845059067 ecr 845059052], length 0

```
4. run tcpdump and request any http site in separate session. Find HTTP request and answer packets with ASCII data in it.  Tcpdump command must be as strict as possible to capture only needed packages for this http request.
```
[mike@10 ~]$ sudo tcpdump -A host 10.0.2.15 and testingmcafeesites.com and tcp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on enp0s3, link-type EN10MB (Ethernet), capture size 262144 bytes

# in another console:
[mike@10 ~]$ curl http://www.testingmcafeesites.com/testcat_ac.html > /dev/null
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  9509  100  9509    0     0   4916      0  0:00:01  0:00:01 --:--:--  4916

# filally, in first console got this:

06:07:01.682491 IP 10.0.2.15.60704 > 161.69.49.22.http: Flags [S], seq 4056866744, win 29200, options [mss 1460,sackOK,TS val 64796301 ecr 0,nop,wscale 7], length 0
E..<i5@.@...
....E1.. .P..........r............
............
06:07:01.882457 IP 161.69.49.22.http > 10.0.2.15.60704: Flags [S.], seq 3989832705, ack 4056866745, win 65535, options [mss 1460], length 0
E..,....@....E1.
....P. ........`.............
06:07:01.882591 IP 10.0.2.15.60704 > 161.69.49.22.http: Flags [.], ack 1, win 29200, length 0
E..(i6@.@../
....E1.. .P........P.r.....
06:07:01.883080 IP 10.0.2.15.60704 > 161.69.49.22.http: Flags [P.], seq 1:106, ack 1, win 29200, length 105: HTTP: GET /testcat_ac.html HTTP/1.1
E...i7@.@...
....E1.. .P........P.r.....GET /testcat_ac.html HTTP/1.1
User-Agent: curl/7.29.0
Host: www.testingmcafeesites.com
Accept: */*


06:07:01.883650 IP 161.69.49.22.http > 10.0.2.15.60704: Flags [.], ack 106, win 65535, length 0
E..(....@....E1.
....P. ......."P... 5........
06:07:02.105254 IP 161.69.49.22.http > 10.0.2.15.60704: Flags [P.], seq 1:1473, ack 106, win 65535, length 1472: HTTP: HTTP/1.1 200 OK
E.......@....E1.
....P. ......."P....D..HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 9509
Connection: keep-alive
Last-Modified: Tue, 31 Jan 2012 09:39:31 GMT
Accept-Ranges: bytes
ETag: "808b813bfcdfcc1:0"
Server: Microsoft-IIS/8.5
X-Powered-By: ASP.NET
SN: LV2MINIWEB01
Date: Fri, 31 Dec 2021 11:07:01 GMT

<html>
      <head>
            <title>URL for testing - Category Art/Culure</title>
      </head>

      <body>
            <code>
             http://www.testingmcafeesites.com/testcat_ac.html<br>
             <br>

                  This is an example URL which should be categorized as an art/culture website with a minimal risk reputation score.<br>
                  This page simply displays this text without any specific content on it, it is just for testing purpose.<br>
                  <br>
                  <b>If you can see this text, it was not blocked by any filter!</b><br>
                  <br>
            </code>
      </body>.
</html>....................................................................................................................................................................................................................................................................................................................................
06:07:02.105355 IP 10.0.2.15.60704 > 161.69.49.22.http: Flags [.], ack 1473, win 32120, length 0
E..(i8@.@..-
....E1.. .P...".. .P.}x....
06:07:02.105789 IP 161.69.49.22.http > 10.0.2.15.60704: Flags [.], seq 1473:5853, ack 106, win 65535, length 4380: HTTP
E..D....@....E1.
....P. ..   ...."P.................................................................................................................................................................................................................................................................................
06:07:02.105848 IP 10.0.2.15.60704 > 161.69.49.22.http: Flags [.], ack 5853, win 40880, length 0
E..(i9@.@..,
....E1.. .P..."....P.......
06:07:02.106154 IP 161.69.49.22.http > 10.0.2.15.60704: Flags [P.], seq 5853:9800, ack 106, win 65535, length 3947: HTTP
E.......@..j.E1.
....P. ......."P...................................................................................................................................................................................................................................................................................................................

06:07:02.106185 IP 10.0.2.15.60704 > 161.69.49.22.http: Flags [.], ack 9800, win 48180, length 0
E..(i:@.@..+
....E1.. .P..."..*IP..4....
06:07:02.106805 IP 10.0.2.15.60704 > 161.69.49.22.http: Flags [F.], seq 106, ack 9800, win 48180, length 0
E..(i;@.@..*
....E1.. .P..."..*IP..4....
06:07:02.107168 IP 161.69.49.22.http > 10.0.2.15.60704: Flags [.], ack 107, win 65535, length 0
E..(....@....E1.
....P. ..*I...#P.............
06:07:02.405187 IP 161.69.49.22.http > 10.0.2.15.60704: Flags [F.], seq 9800, ack 107, win 65535, length 0
E..(....@....E1.
....P. ..*I...#P.............
06:07:02.405309 IP 10.0.2.15.60704 > 161.69.49.22.http: Flags [.], ack 9801, win 48180, length 0
E..(..@.@.nn
....E1.. .P...#..*JP..4=...
^C
15 packets captured
19 packets received by filter
0 packets dropped by kernel


```
