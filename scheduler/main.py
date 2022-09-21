from scheduler import Scheduler

job = Scheduler()

@job.repeat(10, True)
async def handler():
    print("Hello World")

while True:
    job.start()