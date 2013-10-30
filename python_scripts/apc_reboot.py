#!/usr/bin/env python

import sys
import pexpect

if len(sys.argv) < 3:
    print "usage: ./apc_reboot.py <apc_ip> <id1> [<id2>]"
    exit(1)

apc_ip = sys.argv[1]
machine1 = sys.argv[2]
machine2 = ""
if len(sys.argv) == 4:
    machine2 = sys.argv[3]

c = pexpect.spawn('ssh heca@%s' % apc_ip)
c.expect ("password: ")
c.sendline("r3dr0p3")
c.expect("apc>")
c.sendline("olReboot %s" % machine1)
c.expect("Success")
if (machine2):
    c.sendline("olReboot %s" % machine2)
    c.expect("Success")
c.sendline("exit")

import time
time.sleep(5)

exit(0)
