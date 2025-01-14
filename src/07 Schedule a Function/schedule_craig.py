import time, sched

def schedule_function( event_time, function, *args ):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(event_time, 1, function, argument=args)
    s.enterabs(event_time + 2, 1, function, argument=args)

    print(f'{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}')
    s.run(blocking = True)

schedule_function( time.time() + 3 , print, "Hello")
schedule_function( time.time() + 2 , print, "Goodbye")
print ("Waiting...")
time.sleep(5)