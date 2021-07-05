# Vaccine Appointment Automation with Python, Selenium and Telegram Bot

The goal of this project is to get notified about the available vaccine time by running Python script once an hour. The project is based on Python, Selenium WebDriver and Telegram Bot.

# Description

The code is checking the availability of vaccine appointment for a certain location which is Siilainen, Joensuu. 

### Getting started

* Create a Telegram Bot and store the received token as TELEGRAM_BOT_ID. 
* Create a chat and add the created Bot as admin in order to give an access to messages. 
* Store the chat ID as TELEGRAM_SUPERGROUP_ID with the minus sign. 

### Executing program

* Cron is used in order to schedule the time of running the script. In this case, I used

```bash
#Borrowed from anacron
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
#End borrowed from anacron

05 * * * *  /opt/anaconda3/bin/python  /Users/usr/Automation/Corona_Vaccine.py >> /Users/usr/Automation/log.txt
```

to schedule the script to run at every hour at 5 minutes (12:05, 13:05 and etc). The log results are stored in the log.txt file. 

## Authors

Iana Ladygina