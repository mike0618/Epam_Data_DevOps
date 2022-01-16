## Boot process
​
1. enable recovery options for grub, update main configuration file and find new item in grub2 config in /boot.
```
[mike@localhost ~]$ sudo sed -i 's/DISABLE_RECOVERY="true"/DISABLE_RECOVERY="false"/' /etc/default/grub
[mike@localhost ~]$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-3.10.0-1160.el7.x86_64
Found initrd image: /boot/initramfs-3.10.0-1160.el7.x86_64.img
Found linux image: /boot/vmlinuz-0-rescue-f04dae94670ace46a0c5dbabb8b3b1cf
Found initrd image: /boot/initramfs-0-rescue-f04dae94670ace46a0c5dbabb8b3b1cf.img
done

# appeared new entry in /boot/grub2/grub.cfg
menuentry 'CentOS Linux (3.10.0-1160.el7.x86_64) 7 (Core) (recovery mode)' --class centos --class gnu-linux --class gnu --class os --unrestricted $menuentry_id_option 'gnulinux-3.10.0-1160.el7.x86_64-recovery-f53f4005-0f31-4ac7-9c28-d5cb7b895b20' {
        load_video
        set gfxpayload=keep
        insmod gzio
        insmod part_msdos
        insmod xfs
        set root='hd0,msdos1'
        if [ x$feature_platform_search_hint = xy ]; then
          search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1 --hint='hd0,msdos1'  32ffc3b0-c9dc-4070-aa48-44836852b0be
        else
          search --no-floppy --fs-uuid --set=root 32ffc3b0-c9dc-4070-aa48-44836852b0be
        fi
        linux16 /vmlinuz-3.10.0-1160.el7.x86_64 root=/dev/mapper/centos-root ro single crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap rhgb quiet
        initrd16 /initramfs-3.10.0-1160.el7.x86_64.img
}


```
2. modify option vm.dirty_ratio:
   - using echo utility
```
[root@localhost mike]# cat /proc/sys/vm/dirty_ratio
30
[root@localhost mike]# echo 31 > /proc/sys/vm/dirty_ratio
[root@localhost mike]# cat /proc/sys/vm/dirty_ratio
31
```
   - using sysctl utility
```
[root@localhost mike]# sysctl vm.dirty_ratio
vm.dirty_ratio = 31
[root@localhost mike]# sysctl vm.dirty_ratio=30
vm.dirty_ratio = 30
```
   - using sysctl configuration files
```
[root@localhost mike]# vi /etc/sysctl.conf
vm.dirty_ratio = 29

[root@localhost mike]# sysctl -p
vm.dirty_ratio = 29
[root@localhost mike]# sysctl vm.dirty_ratio
vm.dirty_ratio = 29


```
​
* extra
1. Inspect initrd file contents. Find all files that are related to XFS filesystem and give a short description for every file.
2. Study dracut utility that is used for rebuilding initrd image. Give an example for adding driver/kernel module for your initrd and recreating it.
3. Explain the difference between ordinary and rescue initrd images.
​
## Selinux
​
Disable selinux using kernel cmdline
```
in grub-menu press 'e' in order to enter to edit mode, then append 'selinux=0' to the kernel parameters line, pressed ctrl+x
sestatus
SELinux status: disabled

```
​
## Firewalls
​
1. Add rule using firewall-cmd that will allow SSH access to your server *only* from network 192.168.56.0/24 and interface enp0s8 (if your network and/on interface name differs - change it accordingly).
```
set for enp0s8 in network-scripts:
DEVICE=enp0s8
ONBOOT=yes
IPADDR=192.168.56.9
NETMASK=255.255.255.0
GATEWAY=192.168.56.1

[root@localhost mike]# firewall-cmd --zone=internal --add-port=22/tcp --permanent
success
[root@localhost mike]# firewall-cmd --zone=internal --add-source=192.168.56.0/24 --permanent
success
[root@localhost mike]# firewall-cmd --zone=internal --add-interface=enp0s8 --permanent
The interface is under control of NetworkManager, setting zone to 'internal'.
success
[root@localhost mike]# firewall-cmd --reload
success
[root@localhost mike]# firewall-cmd --zone=public --remove-service=ssh
success
# test ssh
[root@localhost mike]# uname -a
Linux localhost.localdomain 3.10.0-1160.el7.x86_64 #1 SMP Mon Oct 19 16:18:59 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux

[root@localhost mike]# firewall-cmd --zone=public --remove-service=ssh --permanent
success
# test again
[root@localhost mike]# firewall-cmd --reload
success
[root@localhost mike]# firewall-cmd --zone=public --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3
  sources: 
  services: dhcpv6-client
  ports: 
  protocols: 
  masquerade: no
  forward-ports: 
  source-ports: 
  icmp-blocks: 
  rich rules: 
	
[root@localhost mike]# firewall-cmd --zone=internal --list-all
internal (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s8
  sources: 192.168.56.0/24
  services: dhcpv6-client mdns samba-client ssh
  ports: 22/tcp
  protocols: 
  masquerade: no
  forward-ports: 
  source-ports: 
  icmp-blocks: 
  rich rules: 

[root@localhost mike]# uname -a
Linux localhost.localdomain 3.10.0-1160.el7.x86_64 #1 SMP Mon Oct 19 16:18:59 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux

```
2. Shutdown firewalld and add the same rules via iptables.
```
[root@localhost mike]# systemctl stop firewalld
[root@localhost mike]# firewall-cmd --state
not running
[root@localhost mike]# systemctl disable firewalld
Removed symlink /etc/systemd/system/multi-user.target.wants/firewalld.service.
Removed symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.
# prevent the firewall from being started by other services
[root@localhost mike]# systemctl mask --now firewalld
Created symlink from /etc/systemd/system/firewalld.service to /dev/null.

[root@localhost mike]# iptables -A INPUT -i enp0s8 -s 192.168.56.0/24 -p tcp --dport 22 -j ACCEPT
[root@localhost mike]# iptables -A INPUT -p tcp --dport 22 -j DROP
[root@localhost mike]# iptables --list
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     tcp  --  192.168.56.0/24      anywhere             tcp dpt:ssh
DROP       tcp  --  anywhere             anywhere             tcp dpt:ssh

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination  
```
