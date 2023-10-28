#!/usr/bin/env python3
import sys
import os
import time
import argparse
import logging
import daemon
import pidfile
from daemon import context

debug_p = False

def pretty_lights(logf):
    ### This does the "work" of the daemon

    logger = logging.getLogger('neopixel')
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler(logf)
    fh.setLevel(logging.INFO)

    formatstr = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(formatstr)

    fh.setFormatter(formatter)

    logger.addHandler(fh)

    if now >= s["sunset"]:
        print("we should start")
    else:
        print("we should wait")

#    while True:
#        logger.debug("this is a DEBUG message")
#        logger.info("this is an INFO message")
#        logger.error("this is an ERROR message")
#        time.sleep(5)


def start_daemon(pidf, logf):
    ### This launches the daemon in its context

    global debug_p

    if debug_p:
        print("neopixel: entered run()")
        print("neopixel: pidf = {}    logf = {}".format(pidf, logf))
        print("neopixel: about to start daemonization")

    ### XXX pidfile is a context
    with daemon.DaemonContext(
        working_directory='/var/lib/neopixel',
        umask=0o002,
        pidfile=pidfile.TimeoutPIDLockFile(pidf),
        ) as context:
        pretty_lights(logf)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NeoPixel daemon in Python")
    parser.add_argument('-p', '--pid-file', default='/var/run/neopixel.pid')
    parser.add_argument('-l', '--log-file', default='/var/log/neopixel.log')

    args = parser.parse_args()
    
    start_daemon(pidf=args.pid_file, logf=args.log_file)
