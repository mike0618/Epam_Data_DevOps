Task 1:

# As a result of each point, you should provide a corresponding command.

localhost - your CentOS VM running in VirtualBox
remotehost - 18.221.144.175 (public IP)
webserver - 172.31.45.237 (private IP)

1.1. SSH to remotehost using username and password provided to you in Slack. Log
out from remotehost.
```
[mike@localhost ~]$ ssh Mikhail_Zubko@18.221.144.175
Mikhail_Zubko@18.221.144.175's password: 
Last login: Mon Dec 20 19:38:17 2021 from 87.248.246.133

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
No packages needed for security; 4 packages available
Run "sudo yum update" to apply all updates.
```

1.2. Generate new SSH key-pair on your localhost with name "hw-5" (keys should be
created in ~/.ssh folder).
```
[mike@localhost ~]$ ssh-keygen -f .ssh/hw-5
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in .ssh/hw-5.
Your public key has been saved in .ssh/hw-5.pub.
The key fingerprint is:
SHA256:uHvv4hWBL9aPf4ucWk0wXwGpoOQiqKz1oVmLNM2v4hI mike@localhost.localdomain
The key's randomart image is:
+---[RSA 2048]----+
|             .o. |
|       . o   .  .|
|  .   o o o +   .|
| . . . + o o + . |
|o  o. o S +   o  |
|E.+ =  o . + o   |
|.+ B +.   o o .  |
|o = o ..o. + o.  |
| o.....o.++.=... |
+----[SHA256]-----+

```

1.3. Set up key-based authentication, so that you can SSH to  remotehost  without
password.
```
[mike@localhost ~]$ ssh-copy-id -i .ssh/hw-5.pub Mikhail_Zubko@18.221.144.175
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: ".ssh/hw-5.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
Mikhail_Zubko@18.221.144.175's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'Mikhail_Zubko@18.221.144.175'"
and check to make sure that only the key(s) you wanted were added.

```

1.4. SSH to remotehost without password. Log out from remotehost.
```
[mike@localhost ~]$ ssh -i .ssh/hw-5 Mikhail_Zubko@18.221.144.175
Enter passphrase for key '.ssh/hw-5': 
Last login: Tue Dec 21 14:20:18 2021 from 87.248.246.133

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
No packages needed for security; 4 packages available
Run "sudo yum update" to apply all updates.
[Mikhail_Zubko@ip-172-31-33-155 ~]$ exit
logout
Connection to 18.221.144.175 closed.

```

1.5. Create SSH config file, so that you can SSH to remotehost simply running `ssh
remotehost` command. As a result, provide output of command `cat ~/.ssh/config`.
```
[mike@localhost ~]$ cat ~/.ssh/config
Host remotehost
	User Mikhail_Zubko
	HostName 18.221.144.175
	IdentityFile ~/.ssh/hw-5
	GatewayPorts yes

```

1.6. Using command line utility (curl or telnet) verify that there are some webserver
running on port 80 of webserver.  Notice that webserver has a private network IP, so
you can access it only from the same network (when you are on remotehost that runs
in the same private network). Log out from remotehost.
```
[Mikhail_Zubko@ip-172-31-33-155 ~]$ curl 172.31.45.237:80 > /dev/null
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1856  100  1856    0     0   368k      0 --:--:-- --:--:-- --:--:--  453k

```

1.7. Using SSH setup port forwarding, so that you can reach  webserver from your
localhost (choose any free local port you like).
```
[mike@localhost ~]$ ssh remotehost -L 8080:172.31.45.237:80
```

1.8 Like in 1.6, but on localhost using command line utility verify that localhost and
port you have specified act like webserver, returning same result as in 1.6.
```
[mike@localhost ~]$ curl localhost:8080 > /dev/null 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1856  100  1856    0     0   7493      0 --:--:-- --:--:-- --:--:--  7544
```

1.9 (*) Open webserver webpage in browser of your Host machine of VirtualBox
(Windows, or Mac, or whatever else you use). You may need to setup port forwarding
in settings of VirtualBox.
```
# The solution without setting up port forwarding in VBox
# "GatewayPorts yes" is already present in .ssh/config

# First Connect to virtual machine
ssh mike@127.0.0.1 -p 2222 -L 8088:localhost:8080

# Then Connect to remotehost from vm
[mike@localhost ~]$ ssh remotehost -L 8080:172.31.45.237:80

# Finally in my Host machine browser:
http://localhost:8088/

# Never Gonna Give You Up!
```

Task 2:

# Following tasks should be executed on your localhost as you will need root privileges

2.1. Imagine your localhost has been relocated to Havana. Change the time zone on
the localhost to Havana and verify the time zone has been changed properly (may be
multiple commands).

2.2. Find all systemd journal messages on localhost, that were recorded in the last 50
minutes and originate from a system service started with user id 81 (single command).

2.3. Configure  rsyslogd  by adding  a  rule  to  the  newly created  configuration   file
/etc/rsyslog.d/auth-errors.conf to log all security and authentication messages with the
priority alert and higher to the  /var/log/auth-errors file. Test the newly added log
directive with the logger command (multiple commands).
