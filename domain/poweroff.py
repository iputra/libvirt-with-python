# python shutdown_domain.py domain_name

import libvirt
import sys

conn = libvirt.open("qemu:///system")

domainName = sys.argv[1]

domain = conn.lookupByName(domainName)
domain.destroy()

print("%s Poweroff" % domainName)