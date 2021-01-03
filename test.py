# sudo python2 setup.py build
# sudo python2 setup.py install

# python2 iwlist.py wlp59s0 channel
# python3 iwlist.py wlp59s0 channel
from pythonwifi.iwlibs import Wireless, Iwscan
wifi = Wireless('wlp59s0')
#wifi_scan = Iwscan('wlp59s0')
test = wifi.getEssid()
print(test)
print(wifi.getMode())
#wifi_scan.getScan()