#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import tweepy, os, platform, psutil, time
from datetime import datetime

# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process, using the keys and tokens  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
  
# Creation of the actual interface, using authentication  
api = tweepy.API(auth)

while True:
    
    if datetime.now().minute==15:
        uptime =  datetime.now() - datetime.fromtimestamp(psutil.boot_time())
        cpu = int(round(psutil.cpu_percent(interval=0.5)))
        cpu_temp = float(os.popen('vcgencmd measure_temp').readline().replace('temp=','').replace('\'C\n',''))
        virtual_memory = int(round(psutil.virtual_memory()[2]))
        #swap_memory = int(round(psutil.swap_memory()[3]))
        processes = len(psutil.pids())

        status = 'Uptime: %s days %s hours %s minutes | CPU usage: %s%% | CPU temp: %s°C | RAM usage: %s%% | Processes: %s' % (uptime.days, uptime.seconds//3600, \
        (uptime.seconds//60)%60, cpu, cpu_temp, virtual_memory, processes)

        try:
            api.update_status(status=status)
            print status
            time.sleep(3300)
        except Exception, e:
            print 'Error', e

    else:
        time.sleep(15) # Check every 15 seconds
