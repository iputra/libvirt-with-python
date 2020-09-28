import libvirt

domainTemplateXML = '''
<domain type='kvm'>
    <name>%s</name>
    <memory>%s</memory>
    <currentMemory>%s</currentMemory>
    <vcpu>%s</vcpu>
    <os>
        <type arch='x86_64' machine='pc-i440fx-bionic'>hvm</type>
        <boot dev='hd'/>
    </os>
    <devices>
        <disk type='file' device='disk'>
            <driver name='qemu' type='qcow2'/>
            <source file='/home/iputra/f1les/nolsatu/reuni/images/%s'/>
            <target dev='vda' bus='virtio'/>
        </disk>
        <interface type='network'>
            <source network='%s'/>
        </interface>
        <graphics type='vnc' port='%s'/>
    </devices>
</domain>
'''

domainName = "vm-ikhsan"
domainMemory = str(2 * 1024 * 1000)
domainCurrentMemory = domainMemory
domainVcpu = "2"
domainDisk = "ik-node01.img"
domainNetwork = "default"
domainVncPort = "5901"

domainXML = domainTemplateXML % (domainName,
domainMemory,
domainCurrentMemory,
domainVcpu,
domainDisk,
domainNetwork,
domainVncPort
    )

conn = libvirt.open("qemu:///system")
domain = conn.defineXML(domainXML)