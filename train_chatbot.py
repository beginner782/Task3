accuracy=0.9

import os

if accuracy < 0.8:
    os.system("curl --user 'admin:admin@123' http://192.168.0.113:8080/job/task3_job4/build?token=tweak")
else:
    os.system("curl --user 'admin:admin@123' http://192.168.0.113:8080/job/task3_job5/build?token=notify")




