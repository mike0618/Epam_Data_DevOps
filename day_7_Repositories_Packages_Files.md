## Repositories and Packages
​
- Use rpm for the following tasks:
1. Download sysstat package.
```
[mike@localhost ~]$ sudo yum install --downloadonly --downloaddir=/home/mike sysstat
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror.axelname.ru
 * extras: mirror.reconn.ru
 * updates: mirror.corbina.net
Resolving Dependencies
--> Running transaction check
---> Package sysstat.x86_64 0:10.1.5-19.el7 will be installed
--> Processing Dependency: libsensors.so.4()(64bit) for package: sysstat-10.1.5-19.el7.x86_64
--> Running transaction check
---> Package lm_sensors-libs.x86_64 0:3.4.0-8.20160601gitf9185e5.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================================================================================================================================================
 Package                                             Arch                                       Version                                                             Repository                                Size
===================================================================================================================================================================================================================
Installing:
 sysstat                                             x86_64                                     10.1.5-19.el7                                                       base                                     315 k
Installing for dependencies:
 lm_sensors-libs                                     x86_64                                     3.4.0-8.20160601gitf9185e5.el7                                      base                                      42 k

Transaction Summary
===================================================================================================================================================================================================================
Install  1 Package (+1 Dependent package)

Total size: 357 k
Installed size: 1.2 M
Background downloading packages, then exiting:
exiting because "Download Only" specified

```
2. Get information from downloaded sysstat package file.
```
[mike@localhost ~]$ rpm -qip sysstat-10.1.5-19.el7.x86_64.rpm 
Name        : sysstat
Version     : 10.1.5
Release     : 19.el7
Architecture: x86_64
Install Date: (not installed)
Group       : Applications/System
Size        : 1172488
License     : GPLv2+
Signature   : RSA/SHA256, Fri 03 Apr 2020 05:08:48 PM CDT, Key ID 24c6a8a7f4a80eb5
Source RPM  : sysstat-10.1.5-19.el7.src.rpm
Build Date  : Wed 01 Apr 2020 12:36:37 AM CDT
Build Host  : x86-01.bsys.centos.org
Relocations : (not relocatable)
Packager    : CentOS BuildSystem <http://bugs.centos.org>
Vendor      : CentOS
URL         : http://sebastien.godard.pagesperso-orange.fr/
Summary     : Collection of performance monitoring tools for Linux
Description :
The sysstat package contains sar, sadf, mpstat, iostat, pidstat, nfsiostat-sysstat,
tapestat, cifsiostat and sa tools for Linux.
The sar command collects and reports system activity information. This
information can be saved in a file in a binary format for future inspection. The
statistics reported by sar concern I/O transfer rates, paging activity,
process-related activities, interrupts, network activity, memory and swap space
utilization, CPU utilization, kernel activities and TTY statistics, among
others. Both UP and SMP machines are fully supported.
The sadf command may be used to display data collected by sar in various formats
(CSV, XML, etc.).
The iostat command reports CPU utilization and I/O statistics for disks.
The tapestat command reports statistics for tapes connected to the system.
The mpstat command reports global and per-processor statistics.
The pidstat command reports statistics for Linux tasks (processes).
The nfsiostat-sysstat command reports I/O statistics for network file systems.
The cifsiostat command reports I/O statistics for CIFS file systems.

```
3. Install sysstat package and get information about files installed by this package.
```
[mike@localhost ~]$ sudo rpm -i lm_sensors-libs-3.4.0-8.20160601gitf9185e5.el7.x86_64.rpm sysstat-10.1.5-19.el7.x86_64.rpm

[mike@localhost ~]$ rpm -ql sysstat
/etc/cron.d/sysstat
/etc/sysconfig/sysstat
/etc/sysconfig/sysstat.ioconf
/usr/bin/cifsiostat
/usr/bin/iostat
/usr/bin/mpstat
/usr/bin/nfsiostat-sysstat
/usr/bin/pidstat
/usr/bin/sadf
/usr/bin/sar
/usr/bin/tapestat
/usr/lib/systemd/system/sysstat.service
/usr/lib64/sa
/usr/lib64/sa/sa1
/usr/lib64/sa/sa2
/usr/lib64/sa/sadc
/usr/share/doc/sysstat-10.1.5
/usr/share/doc/sysstat-10.1.5/CHANGES
/usr/share/doc/sysstat-10.1.5/COPYING
/usr/share/doc/sysstat-10.1.5/CREDITS
/usr/share/doc/sysstat-10.1.5/FAQ
/usr/share/doc/sysstat-10.1.5/README
/usr/share/doc/sysstat-10.1.5/sysstat-10.1.5.lsm
/usr/share/locale/af/LC_MESSAGES/sysstat.mo
/usr/share/locale/cs/LC_MESSAGES/sysstat.mo
/usr/share/locale/da/LC_MESSAGES/sysstat.mo
/usr/share/locale/de/LC_MESSAGES/sysstat.mo
/usr/share/locale/eo/LC_MESSAGES/sysstat.mo
/usr/share/locale/es/LC_MESSAGES/sysstat.mo
/usr/share/locale/eu/LC_MESSAGES/sysstat.mo
/usr/share/locale/fi/LC_MESSAGES/sysstat.mo
/usr/share/locale/fr/LC_MESSAGES/sysstat.mo
/usr/share/locale/hr/LC_MESSAGES/sysstat.mo
/usr/share/locale/id/LC_MESSAGES/sysstat.mo
/usr/share/locale/it/LC_MESSAGES/sysstat.mo
/usr/share/locale/ja/LC_MESSAGES/sysstat.mo
/usr/share/locale/ky/LC_MESSAGES/sysstat.mo
/usr/share/locale/lv/LC_MESSAGES/sysstat.mo
/usr/share/locale/mt/LC_MESSAGES/sysstat.mo
/usr/share/locale/nb/LC_MESSAGES/sysstat.mo
/usr/share/locale/nl/LC_MESSAGES/sysstat.mo
/usr/share/locale/nn/LC_MESSAGES/sysstat.mo
/usr/share/locale/pl/LC_MESSAGES/sysstat.mo
/usr/share/locale/pt/LC_MESSAGES/sysstat.mo
/usr/share/locale/pt_BR/LC_MESSAGES/sysstat.mo
/usr/share/locale/ro/LC_MESSAGES/sysstat.mo
/usr/share/locale/ru/LC_MESSAGES/sysstat.mo
/usr/share/locale/sk/LC_MESSAGES/sysstat.mo
/usr/share/locale/sr/LC_MESSAGES/sysstat.mo
/usr/share/locale/sv/LC_MESSAGES/sysstat.mo
/usr/share/locale/uk/LC_MESSAGES/sysstat.mo
/usr/share/locale/vi/LC_MESSAGES/sysstat.mo
/usr/share/locale/zh_CN/LC_MESSAGES/sysstat.mo
/usr/share/locale/zh_TW/LC_MESSAGES/sysstat.mo
/usr/share/man/man1/cifsiostat.1.gz
/usr/share/man/man1/iostat.1.gz
/usr/share/man/man1/mpstat.1.gz
/usr/share/man/man1/nfsiostat-sysstat.1.gz
/usr/share/man/man1/pidstat.1.gz
/usr/share/man/man1/sadf.1.gz
/usr/share/man/man1/sar.1.gz
/usr/share/man/man1/tapestat.1.gz
/usr/share/man/man5/sysstat.5.gz
/usr/share/man/man8/sa1.8.gz
/usr/share/man/man8/sa2.8.gz
/usr/share/man/man8/sadc.8.gz
/var/log/sa

```
​
- Add NGINX repository (need to find repository config on https://www.nginx.com/) and complete the following tasks using yum:
```
[mike@localhost ~]$ sudo vi /etc/yum.repos.d/nginx.repo

[nginx]
name=nginx repo
baseurl=https://nginx.org/packages/centos/7/x86-64/
gpgcheck=0
enabled=1


```
1. Check if NGINX repository enabled or not.
```
[mike@localhost ~]$ yum repolist enabled nginx
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror.sale-dedic.com
 * extras: mirror.reconn.ru
 * updates: mirror.corbina.net
repo id                                                                                                repo name                                                                                             status
nginx/x86_64                                                                                           nginx repo                                                                                            256
repolist: 256

```
2. Install NGINX.
```
[mike@localhost ~]$ sudo yum install nginx
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.datahouse.ru
 * extras: mirror.axelname.ru
 * updates: mirror.axelname.ru
Resolving Dependencies
--> Running transaction check
---> Package nginx.x86_64 1:1.20.2-1.el7.ngx will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================================================================================================================================================
 Package                                        Arch                                            Version                                                       Repository                                      Size
===================================================================================================================================================================================================================
Installing:
 nginx                                          x86_64                                          1:1.20.2-1.el7.ngx                                            nginx                                          790 k

Transaction Summary
===================================================================================================================================================================================================================
Install  1 Package

Total download size: 790 k
Installed size: 2.8 M
Is this ok [y/d/N]: y
Downloading packages:
nginx-1.20.2-1.el7.ngx.x86_64.rpm                                                                                                                                                           | 790 kB  00:00:08     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
Warning: RPMDB altered outside of yum.
  Installing : 1:nginx-1.20.2-1.el7.ngx.x86_64                                                                                                                                                                 1/1 
----------------------------------------------------------------------

Thanks for using nginx!

Please find the official documentation for nginx here:
* https://nginx.org/en/docs/

Please subscribe to nginx-announce mailing list to get
the most important news about nginx:
* https://nginx.org/en/support.html

Commercial subscriptions for nginx are available on:
* https://nginx.com/products/

----------------------------------------------------------------------
  Verifying  : 1:nginx-1.20.2-1.el7.ngx.x86_64                                                                                                                                                                 1/1 

Installed:
  nginx.x86_64 1:1.20.2-1.el7.ngx                                                                                                                                                                                  

Complete!

```
3. Check yum history and undo NGINX installation.
```
[mike@localhost ~]$ sudo yum history
Loaded plugins: fastestmirror
ID     | Login user               | Date and time    | Action(s)      | Altered
-------------------------------------------------------------------------------
    11 | mike <mike>              | 2021-12-25 05:53 | Install        |    1 E<
    10 | mike <mike>              | 2021-12-15 12:40 | Erase          |    1 > 
     9 | mike <mike>              | 2021-12-15 12:22 | Update         |    1   
     8 | mike <mike>              | 2021-12-15 12:20 | Install        |    5   
     7 | mike <mike>              | 2021-12-15 12:05 | Install        |    1   
     6 | mike <mike>              | 2021-12-11 13:35 | Install        |    2   
     5 | mike <mike>              | 2021-12-06 22:52 | Update         |    2   
     4 | mike <mike>              | 2021-12-03 15:24 | Install        |    2   
     3 | mike <mike>              | 2021-12-02 10:41 | Install        |    1   
     2 | mike <mike>              | 2021-11-30 01:14 | Install        |   29   
     1 | System <unset>           | 2021-11-25 11:06 | Install        |  299   
history list

[mike@localhost ~]$ sudo yum history undo 11
Loaded plugins: fastestmirror
Undoing transaction 11, from Sat Dec 25 05:53:54 2021
    Install nginx-1:1.20.2-1.el7.ngx.x86_64 @nginx
Resolving Dependencies
--> Running transaction check
---> Package nginx.x86_64 1:1.20.2-1.el7.ngx will be erased
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================================================================================================================================================
 Package                                        Arch                                            Version                                                      Repository                                       Size
===================================================================================================================================================================================================================
Removing:
 nginx                                          x86_64                                          1:1.20.2-1.el7.ngx                                           @nginx                                          2.8 M

Transaction Summary
===================================================================================================================================================================================================================
Remove  1 Package

Installed size: 2.8 M
Is this ok [y/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Erasing    : 1:nginx-1.20.2-1.el7.ngx.x86_64                                                                                                                                                                 1/1 
  Verifying  : 1:nginx-1.20.2-1.el7.ngx.x86_64                                                                                                                                                                 1/1 

Removed:
  nginx.x86_64 1:1.20.2-1.el7.ngx                                                                                                                                                                                  

Complete!


```
4. Disable NGINX repository.
```
[mike@localhost ~]$ sudo sed -i 's/enabled=1/enabled=0/' /etc/yum.repos.d/nginx.repo

```
5. Remove sysstat package installed in the first task.
```
[mike@localhost ~]$ sudo rpm -e sysstat
# or
[mike@localhost ~]$ sudo yum erase sysstat

```
6. Install EPEL repository and get information about it.
```
[mike@localhost ~]$ sudo yum install epel-release
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.datahouse.ru
 * extras: mirror.axelname.ru
 * updates: mirror.axelname.ru
Resolving Dependencies
--> Running transaction check
---> Package epel-release.noarch 0:7-11 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================================================================================================================================================
 Package                                                 Arch                                              Version                                         Repository                                         Size
===================================================================================================================================================================================================================
Installing:
 epel-release                                            noarch                                            7-11                                            extras                                             15 k

Transaction Summary
===================================================================================================================================================================================================================
Install  1 Package

Total download size: 15 k
Installed size: 24 k
Is this ok [y/d/N]: y
Downloading packages:
epel-release-7-11.noarch.rpm                                                                                                                                                                |  15 kB  00:00:01     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : epel-release-7-11.noarch                                                                                                                                                                        1/1 
  Verifying  : epel-release-7-11.noarch                                                                                                                                                                        1/1 

Installed:
  epel-release.noarch 0:7-11                                                                                                                                                                                       

Complete!

[mike@localhost ~]$ sudo yum repolist
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
epel/x86_64/metalink                                                                                                                                                                        |  28 kB  00:00:00     
 * base: mirrors.datahouse.ru
 * epel: mirror.vpsnet.com
 * extras: mirror.axelname.ru
 * updates: mirror.axelname.ru
epel                                                                                                                                                                                        | 4.7 kB  00:00:00     
(1/3): epel/x86_64/group_gz                                                                                                                                                                 |  96 kB  00:00:02     
(2/3): epel/x86_64/updateinfo                                                                                                                                                               | 1.0 MB  00:00:17     
(3/3): epel/x86_64/primary_db                                                                                                                                                               | 7.0 MB  00:02:57     
repo id                                                                                repo name                                                                                                             status
base/7/x86_64                                                                          CentOS-7 - Base                                                                                                       10 072
epel/x86_64                                                                            Extra Packages for Enterprise Linux 7 - x86_64                                                                        13 703
extras/7/x86_64                                                                        CentOS-7 - Extras                                                                                                        500
updates/7/x86_64                                                                       CentOS-7 - Updates                                                                                                     3 242
repolist: 27 517

[mike@localhost ~]$ sudo yum repoinfo epel
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.datahouse.ru
 * epel: mirror.nsc.liu.se
 * extras: mirror.surf
 * updates: mirror.axelname.ru
Repo-id      : epel/x86_64
Repo-name    : Extra Packages for Enterprise Linux 7 - x86_64
Repo-status  : enabled
Repo-revision: 1640393346
Repo-updated : Fri Dec 24 19:56:38 2021
Repo-pkgs    : 13 703
Repo-size    : 16 G
Repo-metalink: https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=x86_64
  Updated    : Fri Dec 24 19:56:38 2021
Repo-baseurl : http://mirror.nsc.liu.se/fedora-epel/7/x86_64/ (84 more)
Repo-expire  : 21 600 second(s) (last: Sat Dec 25 06:20:20 2021)
  Filter     : read-only:present
Repo-filename: /etc/yum.repos.d/epel.repo

repolist: 13 703


```
7. Find how much packages provided exactly by EPEL repository.
```
[mike@localhost ~]$ sudo sudo yum repolist -v epel
Loading "fastestmirror" plugin
Config time: 0.008
Yum version: 3.4.3
Loading mirror speeds from cached hostfile
 * base: mirrors.datahouse.ru
 * epel: ftp.lysator.liu.se
 * extras: mirror.surf
 * updates: mirror.axelname.ru
Setting up Package Sacks
pkgsack time: 0.012
Repo-id      : epel/x86_64
Repo-name    : Extra Packages for Enterprise Linux 7 - x86_64
Repo-status  : enabled
Repo-revision: 1640393346
Repo-updated : Fri Dec 24 19:56:38 2021
Repo-pkgs    : 13 703
Repo-size    : 16 G
Repo-metalink: https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=x86_64
  Updated    : Fri Dec 24 19:56:38 2021
Repo-baseurl : https://ftp.lysator.liu.se/pub/epel/7/x86_64/ (84 more)
Repo-expire  : 21 600 second(s) (last: Sat Dec 25 06:20:20 2021)
  Filter     : read-only:present
Repo-filename: /etc/yum.repos.d/epel.repo

repolist: 13 703


```
8. Install ncdu package from EPEL repo.
```
[mike@localhost ~]$ sudo yum install ncdu
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirrors.datahouse.ru
 * epel: mirror.nsc.liu.se
 * extras: mirror.surf
 * updates: mirror.axelname.ru
Resolving Dependencies
--> Running transaction check
---> Package ncdu.x86_64 0:1.16-1.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================================================================================================================================================
 Package                                          Arch                                               Version                                                Repository                                        Size
===================================================================================================================================================================================================================
Installing:
 ncdu                                             x86_64                                             1.16-1.el7                                             epel                                              53 k

Transaction Summary
===================================================================================================================================================================================================================
Install  1 Package

Total download size: 53 k
Installed size: 89 k
Is this ok [y/d/N]: y
Downloading packages:
warning: /var/cache/yum/x86_64/7/epel/packages/ncdu-1.16-1.el7.x86_64.rpm: Header V4 RSA/SHA256 Signature, key ID 352c64e5: NOKEY                                                ]  0.0 B/s |  16 kB  --:--:-- ETA 
Public key for ncdu-1.16-1.el7.x86_64.rpm is not installed
ncdu-1.16-1.el7.x86_64.rpm                                                                                                                                                                  |  53 kB  00:00:00     
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
Importing GPG key 0x352C64E5:
 Userid     : "Fedora EPEL (7) <epel@fedoraproject.org>"
 Fingerprint: 91e9 7d7c 4a5e 96f1 7f3e 888f 6a2f aea2 352c 64e5
 Package    : epel-release-7-11.noarch (@extras)
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
Is this ok [y/N]: y
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : ncdu-1.16-1.el7.x86_64                                                                                                                                                                          1/1 
  Verifying  : ncdu-1.16-1.el7.x86_64                                                                                                                                                                          1/1 

Installed:
  ncdu.x86_64 0:1.16-1.el7                                                                                                                                                                                         

Complete!


```
​
*Extra task:
    Need to create an rpm package consists of a shell script and a text file. The script should output words count stored in file.
```
[mike@localhost ~]$ sudo yum install rpm-build rpmdevtools
[mike@localhost ~]$ rpmdev-setuptree
[mike@localhost ~]$ ll rpmbuild/
total 0
drwxrwx---+ 2 mike mike 6 Dec 25 07:27 BUILD
drwxrwx---+ 2 mike mike 6 Dec 25 07:27 RPMS
drwxrwx---+ 2 mike mike 6 Dec 25 07:27 SOURCES
drwxrwx---+ 2 mike mike 6 Dec 25 07:27 SPECS
drwxrwx---+ 2 mike mike 6 Dec 25 07:27 SRPMS

[mike@localhost ~]$ vi .rpmmacros
%packager MikeZ

%_topdir %(echo $HOME)/rpmbuild

%_smp_mflags %( \
    [ -z "$RPM_BUILD_NCPUS" ] \\\
        && RPM_BUILD_NCPUS="`/usr/bin/nproc 2>/dev/null || \\\
                             /usr/bin/getconf _NPROCESSORS_ONLN`"; \\\
    if [ "$RPM_BUILD_NCPUS" -gt 16 ]; then \\\
        echo "-j16"; \\\
    elif [ "$RPM_BUILD_NCPUS" -gt 3 ]; then \\\
        echo "-j$RPM_BUILD_NCPUS"; \\\
    else \\\
        echo "-j3"; \\\
    fi )

%__arch_install_post \
    [ "%{buildarch}" = "noarch" ] || QA_CHECK_RPATHS=1 ; \
    case "${QA_CHECK_RPATHS:-}" in [1yY]*) /usr/lib/rpm/check-rpaths ;; esac \
    /usr/lib/rpm/check-buildroot


[mike@localhost ~]$ echo 'some text here' > rpmbuild/SOURCES/my1package-1/text_file
[mike@localhost ~]$ echo '#!/bin/bash
> cat text_file | wc -w' > rpmbuild/SOURCES/my1package-1/shell_script.sh


[mike@localhost ~]$ vi rpmbuild/SPECS/my1package.spec
Name:           my1package
Version:        1
Release:        0
Summary:        shell_script.sh counts words in text_file

Group:          EPAM_Training
BuildArch:      noarch
License:        GPL
URL:            https://github.com/mike0618/Epam_Data_DevOps/blob/day7/day_7_Repositories_Packages_Files.md
Source0:        my1package.tar.gz

%description
This is My Very First Package

%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/etc/my1package
install -m 0600 text_file $RPM_BUILD_ROOT/etc/my1package/text_file
install -m 0755 shell_script.sh $RPM_BUILD_ROOT/etc/my1package/shell_script.sh

%files
/etc/my1package
/etc/my1package/text_file
/etc/my1package/shell_script.sh

%changelog
* Sat Dec 25 2021 Mike Zubko  1.0.0
  - Initial rpm release


[mike@localhost ~]$ cd ~/rpmbuild
[mike@localhost rpmbuild]$ rpmbuild -ba SPECS/my1package.spec
Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.aiFODg
+ umask 022
+ cd /home/mike/rpmbuild/BUILD
+ cd /home/mike/rpmbuild/BUILD
+ rm -rf my1package-1
+ /usr/bin/tar -xf -
+ /usr/bin/gzip -dc /home/mike/rpmbuild/SOURCES/my1package.tar.gz
+ STATUS=0
+ '[' 0 -ne 0 ']'
+ cd my1package-1
+ /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
+ exit 0
Executing(%build): /bin/sh -e /var/tmp/rpm-tmp.82gWAK
+ umask 022
+ cd /home/mike/rpmbuild/BUILD
+ cd my1package-1
+ exit 0
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.UHzxze
+ umask 022
+ cd /home/mike/rpmbuild/BUILD
+ '[' /home/mike/rpmbuild/BUILDROOT/my1package-1-0.x86_64 '!=' / ']'
+ rm -rf /home/mike/rpmbuild/BUILDROOT/my1package-1-0.x86_64
++ dirname /home/mike/rpmbuild/BUILDROOT/my1package-1-0.x86_64
+ mkdir -p /home/mike/rpmbuild/BUILDROOT
+ mkdir /home/mike/rpmbuild/BUILDROOT/my1package-1-0.x86_64
+ cd my1package-1
+ install -m 0755 -d /home/mike/rpmbuild/BUILDROOT/my1package-1-0.x86_64/etc/my1package
+ install -m 0600 text_file /home/mike/rpmbuild/BUILDROOT/my1package-1-0.x86_64/etc/my1package/text_file
+ install -m 0755 shell_script.sh /home/mike/rpmbuild/BUILDROOT/my1package-1-0.x86_64/etc/my1package/shell_script.sh
+ /usr/lib/rpm/find-debuginfo.sh --strict-build-id -m --run-dwz --dwz-low-mem-die-limit 10000000 --dwz-max-die-limit 110000000 /home/mike/rpmbuild/BUILD/my1package-1
/usr/lib/rpm/sepdebugcrcfix: Updated 0 CRC32s, 0 CRC32s did match.
+ '[' noarch = noarch ']'
+ case "${QA_CHECK_RPATHS:-}" in
+ /usr/lib/rpm/check-buildroot
+ /usr/lib/rpm/redhat/brp-compress
+ /usr/lib/rpm/redhat/brp-strip-static-archive /usr/bin/strip
+ /usr/lib/rpm/brp-python-bytecompile /usr/bin/python 1
+ /usr/lib/rpm/redhat/brp-python-hardlink
+ /usr/lib/rpm/redhat/brp-java-repack-jars
Processing files: my1package-1-0.noarch
warning: File listed twice: /etc/my1package/shell_script.sh
warning: File listed twice: /etc/my1package/text_file
Provides: my1package = 1-0
Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires: /bin/bash
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/mike/rpmbuild/BUILDROOT/my1package-1-0.x86_64
Wrote: /home/mike/rpmbuild/SRPMS/my1package-1-0.src.rpm
Wrote: /home/mike/rpmbuild/RPMS/noarch/my1package-1-0.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.ep1B5I
+ umask 022
+ cd /home/mike/rpmbuild/BUILD
+ cd my1package-1
+ /usr/bin/rm -rf /home/mike/rpmbuild/BUILDROOT/my1package-1-0.x86_64
+ exit 0


[mike@localhost rpmbuild]$ sudo rpm -ivh RPMS/noarch/my1package-1-0.noarch.rpm
Preparing...                          ################################# [100%]
Updating / installing...
   1:my1package-1-0                   ################################# [100%]


[mike@localhost rpmbuild]$ sudo cat /etc/my1package/text_file 
some text here
[mike@localhost rpmbuild]$ sudo bash /etc/my1package/shell_script.sh
3


```
​
## Work with files
​
1. Find all regular files below 100 bytes inside your home directory.
2. Find an inode number and a hard links count for the root directory. The hard link count should be about 17. Why?
3. Check what inode numbers have "/" and "/boot" directory. Why?
4. Check the root directory space usage by du command. Compare it with an information from df. If you find differences, try to find out why it happens.
5. Check disk space usage of /var/log directory using ncdu
