Msgpack-RPC demo
================
Simple demo with PHP as client and Python as server. Additional to official demo, MySQL R/W is also in the box.

## Dependence
+ PHP 5.6.0
+ python 2.7.8
+ [msgpack-php 0.5.5](https://github.com/msgpack/msgpack-php)
+ mysql server at localhost, if you want to change the endpoint, hack the code in `server/database.py`

## Optional
Recommand phpbrew and virtualenv to install the dependences independently, but not system-wide.

## Quick start

	$ git clone https://github.com/liangshan/msgpack-rpc-demo.git

### Start the server

	$ cd /PATH/TO/msgpack-rpc-demo/server
	$ virtualenv .virtualenv
	$ .virtualenv/bin/python setup.py develop
	$ .virtualenv/bin/python example/property.py init # setup database and mock data
	$ .virtualenv/bin/python example/property.py # start the server

### Start the client with builtin web server(Block Client)
	
	$ cd /PATH/TO/msgpack-rpc-demo/client
	$ php -S localhost:8000 -t example/index.php

#### Benchmark

```
$ ab -n 2000 -c 200 "http://localhost:8000/"

Concurrency Level:      200
Time taken for tests:   5.322 seconds
Complete requests:      2000
Failed requests:        207
   (Connect: 0, Receive: 0, Length: 207, Exceptions: 0)
Write errors:           0
Total transferred:      301739 bytes
HTML transferred:       81739 bytes
Requests per second:    375.80 [#/sec] (mean)
Time per request:       532.194 [ms] (mean)
Time per request:       2.661 [ms] (mean, across all concurrent requests)
Transfer rate:          55.37 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.3      0       7
Processing:     3  334  66.8    328     521
Waiting:        3  334  66.8    328     521
Total:         10  335  66.1    329     521

Percentage of the requests served within a certain time (ms)
  50%    329
  66%    330
  75%    332
  80%    339
  90%    382
  95%    495
  98%    520
  99%    521
 100%    521 (longest request)
```

### Start the client with nginx+php-fpm
#### nginx configure

```
server {
    listen       8000;
    root         /PATH/TO/msgpack-rpc-demo/client/example/;
    index        index.php;

    location ~ \.php$ {
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_param  SCRIPT_FILENAME    $document_root$fastcgi_script_name;
        include        fastcgi_params;
        fastcgi_index  index.php;
    }
}
```

#### Benchmark

```
ab -n 2000 -c 100 "http://localhost:8000/"

Concurrency Level:      100
Time taken for tests:   2.976 seconds
Complete requests:      2000
Failed requests:        215
   (Connect: 0, Receive: 0, Length: 215, Exceptions: 0)
Write errors:           0
Total transferred:      431445 bytes
HTML transferred:       109445 bytes
Requests per second:    671.99 [#/sec] (mean)
Time per request:       148.811 [ms] (mean)
Time per request:       1.488 [ms] (mean, across all concurrent requests)
Transfer rate:          141.57 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.6      0       4
Processing:     6  145  18.7    146     178
Waiting:        6  145  18.7    146     178
Total:         11  145  18.1    146     178

Percentage of the requests served within a certain time (ms)
  50%    146
  66%    149
  75%    150
  80%    151
  90%    153
  95%    158
  98%    175
  99%    176
 100%    178 (longest request)
```


