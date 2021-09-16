# WSGI example

## Run Python HTTP server (non-WSGI)

```
python serve.py
```

## Run Gunicorn (WSGI)

```
gunicorn -b 127.0.0.1 [--log-level debug] [--workers N] [--threads N] [--worker-class eventlet] wsgi_serve:my_web_app
```
