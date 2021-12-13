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
Or like this, with some user-agent validation
```bash
[mike@localhost ~]$ awk -f awk_task_1 access.log

Mozilla/4.0 363613
```
And awk_task_1 contents:
```bash
match($0, /" ".*" ".*"$/) {agent = substr($0, RSTART + 3, RLENGTH)}
{if (agent ~ /^\w+\/[A-Za-z0-9_.]+[ "]/)
sub(/".*/, "", agent)
gsub(/ \([^)]*\)/, "", agent)
if (count[agent]++ >= max) max = count[agent]}
END {for (b in count) if(max == count[b]) print b, count[b]}

```
But do we need the most frequent browser just in file entries or by unique ip addresses?

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

[mike@localhost ~]$ awk -F ' |/' -v ip=216.244.66.230 '{if ($1 == ip) count[$5 " " substr($6, 1, 4)]++} END {for (b in count) print b, count[b]}' access.log

Jul 2021 23
Feb 2021 14
Dec 2020 1
Dec 2021 5
Oct 2021 23
Aug 2021 108
Nov 2021 106
Apr 2021 34
Jan 2021 43
Sep 2021 7
Mar 2021 2
Jun 2021 3
May 2021 27

```
3. Show total amount of data which server has provided for each unique ip (i.e. 100500 bytes for 1.2.3.4; 9001 bytes for 5.4.3.2 and so on)
```bash
[mike@localhost ~]$ awk '{count[$1] += $10} END {for (ip in count) print count[ip], "bytes for", ip}' access.log | sort -rn

36837061299 bytes for 51.210.183.78
33999609146 bytes for 88.136.178.175
32275895107 bytes for 90.39.134.147
19422743215 bytes for 84.50.127.217
18333376651 bytes for 35.231.163.195
7513922252 bytes for 83.199.121.123
7405409791 bytes for 62.39.220.35
...
0 bytes for 104.47.9.254
0 bytes for 104.47.8.254
0 bytes for 104.47.10.254
0 bytes for 

```

### Sed
1. Change all browsers to "lynx"
```bash
[mike@localhost ~]$ sed -i 's/\(.*\)Mozilla/\1lynx/' access.log

```
or
```bash
[mike@localhost ~]$ sed -i 's/\(".*"\).*\(" ".*"\)$/\1lynx\2/' access.log

```
2. Masquerade all ip addresses. Rewrite file.
```bash
[mike@localhost ~]$ sed -ri 's/(\b[0-9]{1,3}\.){3}[0-9]{1,3}\b/xxx.xxx.xxx.xxx/' access.log
```
or
```bash
[mike@localhost ~]$ sed -ri 's/^[^ ]+/xxx.xxx.xxx.xxx/' access.log
```

### Extra (*)
Show list of unique ips, who made more then 50 requests to the same url within 10 minutes (for example too many requests to "/")
```bash
awk -f awk_extra access.log
```
awk_extra contents:
```bash
BEGIN {FS = "[[ :]"}
match($0, /"[^"]+"/) {
  query = substr($0, RSTART + 1, RLENGTH - 2)
  time = $6 * 3600 + $7 * 60 + $8
  num = requests[$1][query]["num"]
  if (time - requests[$1][query][num]["start"] >= 600) {
    requests[$1][query]["num"]++
    num++
    requests[$1][query][num]["start"] = time
    requests[$1][query][num]["startdate"] = $5 " " $6 ":" $7 ":" $8
  }
  requests[$1][query][num]["date"] = $5
  requests[$1][query][num]["count"]++
}
END {
  for (ip in requests) {
    for (query in requests[ip]) {
      for (num = 1; num <= requests[ip][query]["num"]; num++) {
        if (requests[ip][query][num]["count"] > 50) {
          printf "%''15s at %s executed %''6s times query %s\n", ip, requests[ip][query][num]["startdate"], requests[ip][query][num]["count"], query
        }
      }
    }
  }
}
```

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
