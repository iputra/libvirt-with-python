import libvirt
import sys

conn = libvirt.open("qemu:///system")

domainName = sys.argv[1]
domain = conn.lookupByName(domainName)
domain.undefine()

print("%s Deleted" % domainName)