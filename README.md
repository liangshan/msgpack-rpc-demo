Msgpack-RPC demo
================
Simple demo with PHP as client and Python as server. Additional to official demo, MySQL R/W is also in the box.

## Dependence
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
This is ApacheBench, Version 2.3 <$Revision: 655654 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        
Server Hostname:        localhost
Server Port:            8000

Document Path:          /
Document Length:        41 bytes

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
### Start the client with nginx(Non-block Client)

TODO

