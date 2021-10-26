#!/bin/bash
echo -e "\e[1;32mSETING UP HIVE SCANNER"
yum install cpan wget curl glibc.i686 -y
cpan force install Parallel::ForkManager
cpan force install IO::Socket
cpan force install IO::Select
echo -e "\e[1;32mFORCING SETUP..."
sleep 3
echo -e "\e[1;32mSETUP FORCED..."
yum install gcc php-devel php-pear libssh2 libssh2-devel libpcap -y
pecl install -f ssh2
touch /etc/php.d/ssh2.ini
echo extension=ssh2.so > /etc/php.d/ssh2.ini
cpan force install Net::SSH2
echo -e "\e[1;36mYOUR HIVE SCANNER IS NOW READY"
its gonna show loke this
```bash
cat << EOF
o-o    o-o  o   o o--o"
|  \  o   o |\  | |"
|   O |   | | \ | O-o"
|  /  o   o |  \| |"
o-o    o-o  o   o o--o" 
<< EOF
```
