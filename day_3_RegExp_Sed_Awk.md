# Input data
You have log file 'access.log' with the following format:


remote-ip - - [date] "method query protocol" status-code object-size "referrer" "user-agent" "x-forwarded-for"


object-size - the size of the object returned to the client
referrer    - the location where the client came from
user-agent  - information about client browser


Sample can be downloaded from http://www.almhuette-raith.at/apache-log/access.log (~650 Mb)
-
Download access.log using curl:
```bash
curl -O http://www.almhuette-raith.at/apache-log/access.log
```
-
# Tasks


### Awk /ɔːk/
1. What is the most frequent browser?
```bash 
[mike@localhost ~]$ awk -F '"' '{if(count[$6]++ >= max) max = count[$6]} END {for (b in count) if(max == count[b]) print b, count[b]}' access.log

Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) 340874
```
2. Show number of requests per month for ip 216.244.66.230 (for example: Sep 2016 - 100500 reqs, Oct 2016 - 0 reqs, Nov 2016 - 2 reqs...)
```bash
[mike@localhost ~]$ awk '{if($1 == "216.244.66.230") count[substr($4, 5, 8)]++} END {for (m in count) print m, count[m]}' access.log

May/2021 27
Jul/2021 23
Feb/2021 14
Dec/2020 1
Dec/2021 5
Oct/2021 23
Aug/2021 108
Nov/2021 106
Apr/2021 34
Jan/2021 43
Sep/2021 7
Mar/2021 2
Jun/2021 3
```
3. Show total amount of data which server has provided for each unique ip (i.e. 100500 bytes for 1.2.3.4; 9001 bytes for 5.4.3.2 and so on)
```bash
[mike@localhost ~]$ awk '{count[$1] += $10} END {for (ip in count) print count[ip], "bytes for", ip}' access.log

```

### Sed
1. Change all browsers to "lynx"
2. Masquerade all ip addresses. Rewrite file.


### Extra (*)
Show list of unique ips, who made more then 50 requests to the same url within 10 minutes (for example too many requests to "/")


---


**Learn while practice**
- vimtutor (installed with vim)
- [Vimgenius](http://www.vimgenius.com/)
- [Vim movement speed challenge](https://vimvalley.com/vim-movement-speed-challenge/)


**Videos**
- [More Instantly Better Vim](https://www.youtube.com/watch?v=aHm36-na4-4)
- [Do things with just Vim](https://www.youtube.com/watch?v=XA2WjJbmmoM)
- [Learning Vim in a Week](https://www.youtube.com/watch?v=_NUO4JEtkDw)
- [How Vim Makes my Daily Life Easier](https://www.youtube.com/watch?v=NzD2UdQl5Gc)
- [Vim + tmux](https://www.youtube.com/watch?v=5r6yzFEXajQ)
