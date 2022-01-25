1. Imagine you was asked to add new partition to your host for backup purposes. To simulate appearance of new physical disk in your server, please create new disk in Virtual Box (5 GB) and attach it to your virtual machine.
```
VBox - Settings - Storage - add 5GB backup.vdi
```
Also imagine your system started experiencing RAM leak in one of the applications, thus while developers try to debug and fix it, you need to mitigate OutOfMemory errors; you will do it by adding some swap space.
/dev/sdc - 5GB disk, that you just attached to the VM (in your case it may appear as /dev/sdb, /dev/sdc or other, it doesn't matter)
```
[mike@localhost ~]$ ls -la /dev/sd*
brw-rw----. 1 root disk 8,  0 Dec 28 05:43 /dev/sda
brw-rw----. 1 root disk 8,  1 Dec 28 05:43 /dev/sda1
brw-rw----. 1 root disk 8,  2 Dec 28 05:43 /dev/sda2
brw-rw----. 1 root disk 8, 16 Dec 28 05:43 /dev/sdb

```
1.1. Create a 2GB   !!! GPT !!!   partition on /dev/sdc of type "Linux filesystem" (means all the following partitions created in the following steps on /dev/sdc will be GPT as well)
```
[mike@localhost ~]$ sudo gdisk /dev/sdb
GPT fdisk (gdisk) version 0.8.10

Partition table scan:
  MBR: not present
  BSD: not present
  APM: not present
  GPT: not present

Creating new GPT entries.

Command (? for help): o
This option deletes all partitions and creates a new protective MBR.
Proceed? (Y/N): Y

Command (? for help): n
Partition number (1-128, default 1): 
First sector (34-10485726, default = 2048) or {+-}size{KMGTP}: 
Last sector (2048-10485726, default = 10485726) or {+-}size{KMGTP}: +2G
Current type is 'Linux filesystem'
Hex code or GUID (L to show codes, Enter = 8300): 8300
Changed type of partition to 'Linux filesystem'


```
1.2. Create a 512MB partition on /dev/sdc of type "Linux swap"
```
Command (? for help): n
Partition number (2-128, default 2): 
First sector (34-10485726, default = 4196352) or {+-}size{KMGTP}: 
Last sector (4196352-10485726, default = 10485726) or {+-}size{KMGTP}: +512M
Current type is 'Linux filesystem'
Hex code or GUID (L to show codes, Enter = 8300): 8200
Changed type of partition to 'Linux swap'

Command (? for help): w

Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!

Do you want to proceed? (Y/N): Y
OK; writing new GUID partition table (GPT) to /dev/sdb.
The operation has completed successfully.

```
1.3. Format the 2GB partition with an XFS file system
```
[mike@localhost ~]$ sudo mkfs -t xfs /dev/sdb1
meta-data=/dev/sdb1              isize=512    agcount=4, agsize=131072 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=0, sparse=0
data     =                       bsize=4096   blocks=524288, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal log           bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0

```
1.4. Initialize 512MB partition as swap space
```
[mike@localhost ~]$ sudo mkswap -f /dev/sdb2
Setting up swapspace version 1, size = 524284 KiB
no label, UUID=8fb7f819-d962-4bc5-8a54-033885ee7dee
[mike@localhost ~]$ sudo swapon /dev/sdb2
[mike@localhost ~]$ lsblk
NAME            MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda               8:0    0    8G  0 disk 
├─sda1            8:1    0    1G  0 part /boot
└─sda2            8:2    0    7G  0 part 
  ├─centos-root 253:0    0  6,2G  0 lvm  /
  └─centos-swap 253:1    0  820M  0 lvm  [SWAP]
sdb               8:16   0    5G  0 disk 
├─sdb1            8:17   0    2G  0 part 
└─sdb2            8:18   0  512M  0 part [SWAP]
sr0              11:0    1 1024M  0 rom 

```
1.5. Configure the newly created XFS file system to persistently mount at /backup
```
[mike@localhost ~]$ sudo mkdir /backup
[root@localhost mike]# echo "/dev/sdb1          /backup     xfs       defaults          0 0" >> /etc/fstab

```
1.6. Configure the newly created swap space to be enabled at boot
```
[root@localhost mike]# echo "/dev/sdb2          swap     swap       defaults          0 0" >> /etc/fstab

```
1.7. Reboot your host and verify that /dev/sdc1 is mounted at /backup and that your swap partition  (/dev/sdc2) is enabled
```
[mike@localhost ~]$ sudo reboot

[mike@localhost ~]$ lsblk
NAME            MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda               8:0    0    8G  0 disk 
├─sda1            8:1    0    1G  0 part /boot
└─sda2            8:2    0    7G  0 part 
  ├─centos-root 253:0    0  6,2G  0 lvm  /
  └─centos-swap 253:1    0  820M  0 lvm  [SWAP]
sdb               8:16   0    5G  0 disk 
├─sdb1            8:17   0    2G  0 part /backup
└─sdb2            8:18   0  512M  0 part [SWAP]
sr0              11:0    1 1024M  0 rom  

```
2. LVM. Imagine you're running out of space on your root device. As we found out during the lesson default CentOS installation should already have LVM, means you can easily extend size of your root device. So what are you waiting for? Just do it!
2.1. Create 2GB partition on /dev/sdc of type "Linux LVM"
```
[mike@localhost ~]$ sudo gdisk /dev/sdb
GPT fdisk (gdisk) version 0.8.10

Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present

Found valid GPT with protective MBR; using GPT.

Command (? for help): n
Partition number (3-128, default 3): 
First sector (34-10485726, default = 5244928) or {+-}size{KMGTP}: 
Last sector (5244928-10485726, default = 10485726) or {+-}size{KMGTP}: +2G
Current type is 'Linux filesystem'
Hex code or GUID (L to show codes, Enter = 8300): 8e00
Changed type of partition to 'Linux LVM'

Command (? for help): w

Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!

Do you want to proceed? (Y/N): Y
OK; writing new GUID partition table (GPT) to /dev/sdb.
Warning: The kernel is still using the old partition table.
The new table will be used at the next reboot.
The operation has completed successfully.

[mike@localhost ~]$ sudo reboot
```
2.2. Initialize the partition as a physical volume (PV)
```
[mike@localhost ~]$ sudo pvcreate /dev/sdb3
  Physical volume "/dev/sdb3" successfully created.
[mike@localhost ~]$ sudo pvs
  PV         VG     Fmt  Attr PSize  PFree
  /dev/sda2  centos lvm2 a--  <7,00g    0 
  /dev/sdb3         lvm2 ---   2,00g 2,00g
[mike@localhost ~]$ sudo pvdisplay
  --- Physical volume ---
  PV Name               /dev/sda2
  VG Name               centos
  PV Size               <7,00 GiB / not usable 3,00 MiB
  Allocatable           yes (but full)
  PE Size               4,00 MiB
  Total PE              1791
  Free PE               0
  Allocated PE          1791
  PV UUID               oz1mCV-A79A-158v-Rrcl-qLA1-ewcv-Tw8VTo
   
  "/dev/sdb3" is a new physical volume of "2,00 GiB"
  --- NEW Physical volume ---
  PV Name               /dev/sdb3
  VG Name               
  PV Size               2,00 GiB
  Allocatable           NO
  PE Size               0   
  Total PE              0
  Free PE               0
  Allocated PE          0
  PV UUID               zkhGc0-Ib6w-QabO-Svqd-iwFZ-6vEV-QwfoEf
```
2.3. Extend the volume group (VG) of your root device using your newly created PV
```
[mike@localhost ~]$ sudo vgs
  VG     #PV #LV #SN Attr   VSize  VFree
  centos   1   2   0 wz--n- <7,00g    0 
[mike@localhost ~]$ sudo vgextend centos /dev/sdb3
  Volume group "centos" successfully extended
[mike@localhost ~]$ sudo vgs
  VG     #PV #LV #SN Attr   VSize VFree 
  centos   2   2   0 wz--n- 8,99g <2,00g
```
2.4. Extend your root logical volume (LV) by 1GB, leaving other 1GB unassigned
```
[mike@localhost ~]$ sudo vgdisplay
  --- Volume group ---
  VG Name               centos
  System ID             
  Format                lvm2
  Metadata Areas        2
  Metadata Sequence No  4
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                2
  Open LV               2
  Max PV                0
  Cur PV                2
  Act PV                2
  VG Size               8,99 GiB
  PE Size               4,00 MiB
  Total PE              2302
  Alloc PE / Size       1791 / <7,00 GiB
  Free  PE / Size       511 / <2,00 GiB
  VG UUID               OAOLsb-dhv0-6L5v-M2Dh-dXy3-yPGW-DSEksy
   
[mike@localhost ~]$ sudo lvdisplay
  --- Logical volume ---
  LV Path                /dev/centos/swap
  LV Name                swap
  VG Name                centos
  LV UUID                pj45z8-N78k-h9AK-aKEL-XsDs-7AsO-3J6ToR
  LV Write Access        read/write
  LV Creation host, time localhost, 2021-11-25 11:06:27 -0500
  LV Status              available
  # open                 2
  LV Size                820,00 MiB
  Current LE             205
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     8192
  Block device           253:1
   
  --- Logical volume ---
  LV Path                /dev/centos/root
  LV Name                root
  VG Name                centos
  LV UUID                vbDBwT-7lNa-ar3i-d336-VfIl-AkzN-JmfUBC
  LV Write Access        read/write
  LV Creation host, time localhost, 2021-11-25 11:06:27 -0500
  LV Status              available
  # open                 1
  LV Size                <6,20 GiB
  Current LE             1586
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     8192
  Block device           253:0

[mike@localhost ~]$ sudo lvextend -l +256 /dev/centos/root
  Size of logical volume centos/root changed from <6,20 GiB (1586 extents) to <7,20 GiB (1842 extents).
  Logical volume centos/root successfully resized.

```
2.5. Check current disk space usage of your root device
```
[mike@localhost ~]$ sudo df -h /
Filesystem               Size  Used Avail Use% Mounted on
/dev/mapper/centos-root  6,2G  2,0G  4,2G  33% /

```
2.6. Extend your root device filesystem to be able to use additional free space of root LV
```
[root@localhost mike]# sudo xfs_growfs -d /
meta-data=/dev/mapper/centos-root isize=512    agcount=4, agsize=406016 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=0 spinodes=0
data     =                       bsize=4096   blocks=1624064, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal               bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
data blocks changed from 1624064 to 1886208
[root@localhost mike]# sudo reboot

```
2.7. Verify that after reboot your root device is still 1GB bigger than at 2.5.
```
[mike@localhost ~]$ sudo df -h /
Filesystem               Size  Used Avail Use% Mounted on
/dev/mapper/centos-root  7,2G  2,0G  5,2G  28% /

```
