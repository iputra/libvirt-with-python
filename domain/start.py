# python start_domain.py domain_name

import libvirt
import sys

conn = libvirt.open("qemu:///system")

domainName = sys.argv[1]

domain = conn.lookupByName(domainName)
domain.create()

print("%s Started" % domainName)