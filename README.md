# RPiMonitoring
Raspberry Pi monitoring with Twitter.

Uptime, CPU usage, CPU temp, RAM usage and Processes.

## Requirements
A [Twitter app](https://apps.twitter.com/) (!).

python-dev package (needed to install psutil) for Raspbian « Wheezy » `sudo apt-get install python-dev`.

Python packages :

- psutil `sudo pip install psutil`
- tweepy `sudo pip install tweepy`

pyOpenSSL, ndg-httpsclient and pyasn1 packages `sudo pip install requests==2.5.3` to avoid warning on https requests (like staus updates).

## Demo
[https://twitter.com/itsimsrpi](https://twitter.com/itsimsrpi)

![screenshot](https://cloud.githubusercontent.com/assets/12429123/11637208/65697b02-9d20-11e5-8330-20b1b102f117.png)

## More
Check out my [blog post](http://nbyim.com/monitorer-son-raspberry-pi-avec-twitter) :)
