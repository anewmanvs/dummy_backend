# Dummy backend

Creates a localhost backend that redirects to the host you configured.
Only works with API serving hosts which accepts any method request and URL params. Not currently working sending JSON data with POST method.

Please use this for development only (workaround CORS or replicate third party APIs on localhost).

## Requirements

Please make sure you use Python 3.5 or above. Install `flask==2.1.2` and `requests==2.27.1` before using this. Or run command

```
pip install -r requirements.txt
```


## Get started

On the file `main.py` change the variable `REDIRECT_URL` to match the host you want to make requests.
Main script is configured to use port 15002. Change that for what you're expecting just make sure to use an available port. That means, if you already have a server serving the front or an app at port 80, you can use that to serve this dummy backend as well.

Use the following command to start the dummy server (PLEASE DO NOT USE THAT FOR PRODUCTION)

```
python main.py
```

Press CTRL + C to stop the dummy server.
