DoH Analysis
============

# Docker

## Build

```
$ docker build -t dohtest .
```

## Run container with volume

```
$ docker run --rm -it --entrypoint /bin/bash -v $PWD:/app dohtest
```

## Run test

```
root@acf5adbc5d2e:/app# ./run_headless.sh
```
