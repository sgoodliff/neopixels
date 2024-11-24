#!/usr/bin/python3

import zoneinfo
timezone = zoneinfo.ZoneInfo("Europe/London")

from astral import LocationInfo
city = LocationInfo("London", "England", "Europe/London", 51.5, -0.116)

from crontab import CronTab

from datetime import date

from astral.sun import sun

s = sun(city.observer, date.today(),tzinfo=timezone)

pi_cron  = CronTab(user=True)
# remove yesterdays start time
pi_cron.remove_all(comment='Setup NeoPixels')

job = pi_cron.new(command='sudo /home/pi/git_repos/neopixels/bin/sjg.py -l -c')
job.setall(s["sunset"].minute,s["sunset"].hour)
job.set_comment("Setup NeoPixels")
pi_cron.write() 
