Msgpack-RPC demo
================
Simple demo with PHP as client and Python as server. Additional to official demo, MySQL R/W is also in the box.

## Dependence
+ [msgpack-php 0.5.5](https://github.com/msgpack/msgpack-php)

## Optional
Recommand phpbrew and virtualenv to install the dependences independently, but not system-wide.

## Quick start

	$ git clone https://github.com/liangshan/msgpack-rpc-demo.git

### Start the server

	$ cd msgpack-rpc-demo/server
	$ virtualenv .virtualenv
	$ .virtualenv/bin/python example/property.py

### Start the client with builtin web server
	
	$ cd  msgpack-rpc-demo/client
	$ php -S localhost:8000 -t example/index.php

#### Benchmark

```
$ ab -n 1000 -c 100 localhost:8000

```
### Start the client with nginx

TODO

