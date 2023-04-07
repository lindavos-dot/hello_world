# Import what we need from flask
from flask import Flask


# Create a Flask app inside `app`
app = Flask(__name__)

# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/cow')
def cow():
    return 'MOoooOo!'

    '''C:\Users\Linda Vos\Desktop\hello-world\farm-site> set FLASK_APP=main.py

C:\Users\Linda Vos\Desktop\hello-world\farm-site> flask run
 * Serving Flask app 'main.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\Linda Vos\Desktop\hello-world> ssh root@165.227.133.158
root@165.227.133.158's password:
Permission denied, please try again.
root@165.227.133.158's password:
Welcome to Ubuntu 22.10 (GNU/Linux 5.19.0-38-generic x86_64)

 * Documentation:  https://help.ubuntu.com
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\Linda Vos\Desktop\hello-world> ssh root@165.227.133.158
root@165.227.133.158's password:
Permission denied, please try again.
root@165.227.133.158's password:
Welcome to Ubuntu 22.10 (GNU/Linux 5.19.0-38-generic x86_64)
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\Linda Vos\Desktop\hello-world> ssh root@165.227.133.158
root@165.227.133.158's password:
Permission denied, please try again.
root@165.227.133.158's password:
Welcome to Ubuntu 22.10 (GNU/Linux 5.19.0-38-generic x86_64)

PS C:\Users\Linda Vos\Desktop\hello-world> ssh root@165.227.133.158
root@165.227.133.158's password:
Permission denied, please try again.
root@165.227.133.158's password:
Welcome to Ubuntu 22.10 (GNU/Linux 5.19.0-38-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
root@165.227.133.158's password:
Permission denied, please try again.
root@165.227.133.158's password:
Welcome to Ubuntu 22.10 (GNU/Linux 5.19.0-38-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Apr  4 12:33:45 UTC 2023

  System load:  0.0               Users logged in:       0
  Usage of /:   24.0% of 9.52GB   IPv4 address for eth0: 165.227.133.158
  Memory usage: 53%               IPv4 address for eth0: 10.19.0.5
  Swap usage:   0%                IPv4 address for eth1: 10.114.0.2
  Processes:    92

Welcome to Ubuntu 22.10 (GNU/Linux 5.19.0-38-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Apr  4 12:33:45 UTC 2023

  System load:  0.0               Users logged in:       0
  Usage of /:   24.0% of 9.52GB   IPv4 address for eth0: 165.227.133.158
  Memory usage: 53%               IPv4 address for eth0: 10.19.0.5
  Swap usage:   0%                IPv4 address for eth1: 10.114.0.2
  Processes:    92

0 updates can be applied immediately.

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Apr  4 12:33:45 UTC 2023

  System load:  0.0               Users logged in:       0
  Usage of /:   24.0% of 9.52GB   IPv4 address for eth0: 165.227.133.158227.133.158                                                  9.0.5
  Memory usage: 53%               IPv4 address for eth0: 10.114.0.29.0.5
  Swap usage:   0%                IPv4 address for eth1: 10.114.0.2
  Processes:    92

0 updates can be applied immediately.

                                                              main:app
Last login: Tue Apr  4 12:33:46 2023 from 85.145.213.197     0.1.0
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:~# cd /var/www/foo    //127.0.0.1:8000 (1705)
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:/var/www/foo# gunicorn main:app                                                     pid: 1706
[2023-04-04 12:41:58 +0000] [1705] [INFO] Starting gunicorn 20.1.0                                                        nch[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:41:58 +0000] [1705] [INFO] Listening at: http:nch//127.0.0.1:8000 (1705)                                      nch[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:41:58 +0000] [1705] [INFO] Using worker: sync nch
[2023-04-04 12:41:58 +0000] [1706] [INFO] Booting worker withnch pid: 1706                                                   nch
gunicorn main:app -b 0.0.0.0                                 nch[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch

  System information as of Tue Apr  4 12:33:45 UTC 2023

  System load:  0.0               Users logged in:       0
  Usage of /:   24.0% of 9.52GB   IPv4 address for eth0: 165.227.133.158
  Memory usage: 53%               IPv4 address for eth0: 10.19.0.5
  Swap usage:   0%                IPv4 address for eth1: 10.114.0.2
  Processes:    92

0 updates can be applied immediately.


Last login: Tue Apr  4 12:33:46 2023 from 85.145.213.197
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:~# cd /var/www/foo
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:/var/www/foo# gunicorn main:app main:app                                                    0.1.0
[2023-04-04 12:41:58 +0000] [1705] [INFO] Starting gunicorn 2//127.0.0.1:8000 (1705)0.1.0
[2023-04-04 12:41:58 +0000] [1705] [INFO] Listening at: http: pid: 1706//127.0.0.1:8000 (1705)
[2023-04-04 12:41:58 +0000] [1705] [INFO] Using worker: sync nch[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:41:58 +0000] [1706] [INFO] Booting worker withnch pid: 1706                                                   nch[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch
gunicorn main:app -b 0.0.0.0                                 nch
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winchnch[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal:nch winch                                                       nch[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winchnch                                                          nch[2023-04-04 12:46:06 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winchnch[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal:nch[2023-04-04 12:46:07 +0000] [1705] [INFO] Handling signal: winch winch                                                       nch
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch[2023-04-04 12:46:11 +0000] [1705] [INFO] Handling signal: winchnch                                                          nch
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch[2023-04-04 12:51:17 +0000] [1705] [INFO] Handling signal: winchnch                                                          nch
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winchnch                                                          int
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: wi: 1706)nch[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal:er winch                                                        main:app -b 0.0.0.0
[2023-04-04 12:46:06 +0000] [1705] [INFO] Handling signal: wi0.1.0nch                                                          //0.0.0.0:8000 (1709)
[2023-04-04 12:46:06 +0000] [1705] [INFO] Handling signal: winch[2023-04-04 12:46:06 +0000] [1705] [INFO] Handling signal: pid: 1710 winch

Last login: Tue Apr  4 12:33:46 2023 from 85.145.213.197
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:~# cd /var/www/foo
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:/var/www/foo# gunicorn main:app
[2023-04-04 12:41:58 +0000] [1705] [INFO] Starting gunicorn 20.1.0
[2023-04-04 12:41:58 +0000] [1705] [INFO] Listening at: http://127.0.0.1:8000 (1705)
[2023-04-04 12:41:58 +0000] [1705] [INFO] Using worker: sync
[2023-04-04 12:41:58 +0000] [1706] [INFO] Booting worker with pid: 1706
gunicorn main:app -b 0.0.0.0
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch[2023-04-04 12:46:05 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:06 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:06 +0000] [1705] [INFO] Handling signal: winch[2023-04-04 12:46:06 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:06 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:07 +0000] [1705] [INFO] Handling signal: winch[2023-04-04 12:46:07 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:07 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:11 +0000] [1705] [INFO] Handling signal: winch[2023-04-04 12:46:11 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:46:11 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:51:17 +0000] [1705] [INFO] Handling signal: winch[2023-04-04 12:51:17 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:51:17 +0000] [1705] [INFO] Handling signal: winch
[2023-04-04 12:51:17 +0000] [1705] [INFO] Handling signal: winch
^C[2023-04-04 12:51:22 +0000] [1705] [INFO] Handling signal: int
[2023-04-04 12:51:22 +0000] [1706] [INFO] Worker exiting (pid: 1706)
[2023-04-04 12:51:22 +0000] [1705] [INFO] Shutting down: Master
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:/var/www/foo# gunicorn main:app -b 0.0.0.0
[2023-04-04 12:52:32 +0000] [1709] [INFO] Starting gunicorn 20.1.0
[2023-04-04 12:52:32 +0000] [1709] [INFO] Listening at: http://0.0.0.0:8000 (1709)
[2023-04-04 12:52:32 +0000] [1709] [INFO] Using worker: sync
[2023-04-04 12:52:32 +0000] [1710] [INFO] Booting worker with pid: 1710
[2023-04-04 12:52:42 +0000] [1709] [INFO] Handling signal: winch[2023-04-04 12:52:42 +0000] [1709] [INFO] Handling signal: winch
[2023-04-04 12:52:42 +0000] [1709] [INFO] Handling signal: winch
[2023-04-04 12:52:45 +0000] [1709] [INFO] Handling signal: winch
[2023-04-04 12:53:43 +0000] [1709] [CRITICAL] WORKER TIMEOUT (pid:1710)
[2023-04-04 12:53:43 +0000] [1710] [INFO] Worker exiting (pid: 1710)
[2023-04-04 12:53:43 +0000] [1711] [INFO] Booting worker with pid: 1711
^C[2023-04-04 12:55:58 +0000] [1709] [INFO] Handling signal: int
[2023-04-04 12:55:58 +0000] [1711] [INFO] Worker exiting (pid: 1711)
[2023-04-04 12:55:58 +0000] [1709] [INFO] Shutting down: Master
root@ubuntu-s-1vcpu-512mb-10gb-fra1-01:/var/www/foo#
'''

