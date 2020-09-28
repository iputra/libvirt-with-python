### Install package
```
sudo apt -y install python3 python3-pip libvirt-dev libvirt-bin
pip3 install libvirt-python
```

### Run Program
```
python domain/create.py
python domain/list.py
. . .
python domain/shutdown.py domain_name
```

### Setup NoVNC
```
mkdir display; cd display

git clone https://github.com/novnc/websockify websockify
git clone https://github.com/novnc/novnc websockify/novnc

cd websockify

./run --web novnc localhost:6080 127.0.0.1:5901
```
