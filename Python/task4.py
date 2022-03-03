import os
import pwd


def task4():
    pid = os.getpid()
    # username = os.getlogin()
    username = pwd.getpwuid(os.getuid())[0]
    os_name = os.uname().sysname
    os_release = os.uname().release
    print(f"This script has the following PID: {pid}. It was run by {username} to work happily on {os_name}-{os_release}")
    print("This script has the following PID: {}. It was run by {} to work happily on {}-{}".format(pid, username, os_name, os_release))
    print("This script has the following PID: " + str(pid) + ". It was run by " + username + " to work happily on " + os_name + "-" + os_release)


if __name__ == '__main__':
    task4()
