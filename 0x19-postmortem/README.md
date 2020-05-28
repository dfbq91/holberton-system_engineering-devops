# Postmortem - Debugging wordpress

For this school project, I will write a situation presented in on of our servers. This problem was about wordpress. It is a good example that ilustres how a postmortem can be written.

![](https://github.com/dfbq91/holberton-system_engineering-devops/blob/master/0x19-postmortem/postmortem.jpg)

## Issue summary
Between 09:00 AM and 10:20 AM, requests made to the wordpress server resulted in an error 500. The result was a general disruption of web traffic, which during that time was completely reduced.

The problem was caused by a typing error in one of the wordpress configuration files.
```shell
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html
```

## Timeline

- The problem was detected at 10:05 am on 05/21/2020 when an engineer curled up to the address 127.0.0.1

- The response to the request was an error 500, i.e. a server error. (10:06 am)

- The notification was made to the Senior Engineer to debug the error. (10:07 am)

- The first reaction was to see through the history command, what could be the command that triggered the error. However, nothing unusual was observed. (10:08 am)

- The mysql log and error log were checked: `/var/log/apache2/error.log` and `/var/log/mysql.err`, respectively, but no error log was found there. (10:09 am)

- The server was restarted but still had the error. (10:11 am)

- The permissions of the apache configuration file `/etc/apache2/apache2.conf` were fixed. (10:12 am)

- The CPU load was checked through the top command. Everything was in order. (10:13 am)

- A trace was used on a php child process and in another terminal, the command curl `curl -s 127.0.0.1` was run again to see what happened to the system when the server received a request. (10:13 am)

- There it was found that something was not right, however the solution was difficult to appreciate with this approach. However, the output made it clear that the error was in a wordpress configuration file. (10:16 am)

- With the clarity that the error was coming from a wordpress configuration file, the engineering team activated the wordpress debugging by editing the `wp-config.php` file and modifying the line `define( 'WP_DEBUG',  false )` to `define( 'WP_DEBUG',  true )` (10:17 am)

- The file where the error was found was in wp settings.  (10:18 am)

- Fixed the printing error in the file path. The system was put back online at 10:20 am. The correction of the error took 18 minutes. (10:20 am)

## Root cause and resolution

The cause of the error was in an invalid line containing `/class-wp-locale.phpp` in the file `/var/www/html/wp-settings.php`.

The first clue was obtained by using strace and Curl to localhost from another terminal, which returned quite a large output, but there was one part that attracted attention:

`lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x2ggcde25dje0) = -1 ENOENT (No such file or directory)`

-1 as result allow us to see that this file class-wp-locale did not exist in that moment.

To further refine the track, wordpress debug mode was activated, which allowed to find the file where the line detected by strace was located.

The solution was to modify `/var/www/html/wp-includes/class-wp-locale.phpp` to `/var/www/html/wp-includes/class-wp-locale.php`.

## Corrective and preventive measures:

The file writing error was probably caused by mental and physical exhaustion. As a preventive measure, it is important to follow up on the exhaustion of the engineers to prevent them from falling into this type of error.

Sometimes, worker-related measures are useful. Technical measures can help, but are not the best option in all cases. For example:
![](https://github.com/dfbq91/holberton-system_engineering-devops/blob/master/0x19-postmortem/wordpress-meme.jpg)
