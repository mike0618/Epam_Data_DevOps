Команды для запуска:

docker run -it --name namenode -p 9870:9870 -p 8088:8088 -v /tmp/namenode-dir1:/opt/mount1/namenode-dir -v /tmp/namenode-dir2:/opt/mount2/namenode-dir headnode:1.0.7

docker run -it --name worker -v /tmp/datanode-dir1:/opt/mount1/datanode-dir -v /tmp/datanode-dir2:/opt/mount2/datanode-dir -v /tmp/nodemanager-local-dir1:/opt/mount1/nodemanager-local-dir -v /tmp/nodemanager-local-dir2:/opt/mount2/nodemanager-local-dir -v /tmp/nodemanager-log-dir1:/opt/mount1/nodemanager-log-dir -v /tmp/nodemanager-log-dir2:/opt/mount2/nodemanager-log-dir worker:1.0.3