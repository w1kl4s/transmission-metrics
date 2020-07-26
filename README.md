## yatrex - Yet Another TRansmission Exporter

yatrex is a server/daemon made for collecting data from Transmission torrent client and exposing it in Prometheus-compatible format `--mode pull` or pushing it to Influx-compatible endpoints `--mode push` (latter is still in development). 

# Installation:
In the future, package will be avalaible on PyPI, for now you will have to clone the repo and install it manually:

```
git clone https://github.com/w1kl4s/yatrex.git
cd yatrex
pip install -e .
```

Note that this program requires at least python3.6, so you need to use python3 pip. In my case, it's just `pip`:
```
➜  ~ pip --version
pip 20.1.1 from /usr/lib/python3.8/site-packages/pip (python 3.8)
```
However, many distributions will still have `pip` as python2 pip, and `pip3` as python3 pip. Use correct `pip` for installing, else it will fail.

# Usage:

Only requiered argument is the config file which contains data of clients you want to scrape. Check out the example file `clients.json.example`. Use other options to override the defaults, like bind address, port, or interval between scrapes.

```
$ yatrex -c yatrex_config.json --p 1234 --address ::1 --interval 15
```

# WIP
This program is heavily in development. There is tons of stuff i want to add, and you can expect frequent updates.
