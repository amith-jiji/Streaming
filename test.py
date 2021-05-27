from datetime import *
s1 = '23:58:26'
s2 = '0:36:49' # for example
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
now = datetime.now()
print("Created at %s:%s" % (s1.hour, s1.minute))        
            
current_time=now.strftime("%H_%M_%S")
duration_in_s=tdelta.total_seconds()
print(duration_in_s)
minutes = divmod(duration_in_s, 3600)[0]  
print(minutes)