from crontab import CronTab
import subprocess

cron = CronTab(user='username')
job = (cron.new(command=(subprocess.run('python dashboard.py'),shell=True))
job.minute.every(1)

cron.write()