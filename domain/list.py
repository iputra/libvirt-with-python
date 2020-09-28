import libvirt

def checkStatus(state, reason):
    status = ""
    if state == libvirt.VIR_DOMAIN_NOSTATE:
        status = "No State"
    elif state == libvirt.VIR_DOMAIN_RUNNING:
        status = "Started"
    elif state == libvirt.VIR_DOMAIN_BLOCKED:
        status = "Blocked"
    elif state == libvirt.VIR_DOMAIN_PAUSED:
        status = "Paused"
    elif state == libvirt.VIR_DOMAIN_SHUTDOWN:
        status = "Shutdown"
    elif state == libvirt.VIR_DOMAIN_SHUTOFF:
        status = "Shutoff"
    elif state == libvirt.VIR_DOMAIN_CRASHED:
        status = "Crashed"
    elif state == libvirt.VIR_DOMAIN_PMSUSPENDED:
        status = "Suspended"
    else:
        status = "State Unknown"
    return status

conn = libvirt.open("qemu:///system")
listDomain = conn.listAllDomains(0)

print("{:40}{:32}{:15}".format("UUID", "NAME", "STATUS"))

for domain in listDomain:
    domainName = domain.name()
    domainUUID = domain.UUIDString()
    state, reason = domain.state()
    domainStatus = checkStatus(state, reason)
    print("{:40}{:32}{:15}".format(domainUUID, domainName, domainStatus))
