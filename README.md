# python-timezone-schedular
Schedule a job at the same time in multiple time zones  

```python
from schedule_timezone import get_local_time_for_remote_time_alpha2, get_local_time_for_remote_time

result = get_local_time_for_remote_time("Europe/Amsterdam","Brazil/West", "12:00")
hours = result.strftime("%H:%M")
print(f"The time in Amsterdam when it will be around 13:00 in Brazil is: {hours}")
result = get_local_time_for_remote_time_alpha2("NL","US", "12:00")
hours = result.strftime("%H:%M")
print(f"The time in Netherlands when it will be around 13:00 in United states is: {hours}")
```

## Full example

Do the scheduling with the [schedule](https://schedule.readthedocs.io/en/stable/) python package. These functions give you the time in other timezones.

```python
from schedule_timezone import get_local_time_for_remote_time
import schedule, time

result = get_local_time_for_remote_time("Europe/Amsterdam","Brazil/West", "12:00")
hours = result.strftime("%H:%M")
job = lambda : print(hours)
schedule.every().day.at(hours).do(job, hours)

while True:
    schedule.run_pending()
    time.sleep(3600)
```

