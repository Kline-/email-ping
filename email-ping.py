#!/usr/bin/python3
import datetime
import json
import pathlib
import random
import smtplib
import time


def main():
    hc = '/tmp/hc.timestamp'
    print('Starting up...', flush=True)
    cfg = read_config()

    while True:
        pathlib.Path.touch(hc)
        d = random.randint(cfg['time_min'], cfg['time_max'])
        time.sleep(d)
        t = str(datetime.datetime.now())
        m = cfg['message'].format(t, d)
        try:
            with smtplib.SMTP_SSL(host=cfg['smtp_host']) as s:
                if s.login(cfg['smtp_user'], cfg['smtp_pass']):
                    s.sendmail(cfg['smtp_user'], cfg['smtp_user'], m)
                    print('Ping successful: {}'.format(t), flush=True)
                else:
                    print('Login failed: {}'.format(t), flush=True)
        except Exception as e:
            print('Err: {}'.format(e), flush=True)


def read_config():
    cfg = dict()
    keys = ['time_min', 'time_max', 'smtp_host', 'smtp_user', 'smtp_pass', 'message']

    try:
        with open('config.json') as fd:
            cfg = json.load(fd)
    except Exception as e:
        print('Err: {}'.format(e), flush=True)

    for x in keys:
        if not x in cfg:
            raise KeyError('Key not found in config', x)

    return cfg


if __name__ == '__main__':
    main()
