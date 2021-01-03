# sudo python2 setup.py build
# sudo python2 setup.py install

# python2 iwlist.py wlp59s0 channel
# python3 iwlist.py wlp59s0 channel

# pip2 install python-wifi --ignore-installed
import pythonwifi.flags
from pythonwifi.iwlibs import Wireless, Iwscan

wifi = Wireless('wlp59s0')
print(wifi.getEssid())
print(wifi.getMode())

keys = wifi.getKeys()

print(wifi.getPowermanagement())
print(wifi.getQualityAvg())
print(wifi.getWirelessName())
print(wifi.getAPaddr())
print(wifi.getBitrate())
print(wifi.getChannelInfo())
print(wifi.getEncryption())
print(wifi.getFragmentation())
print(wifi.getFrequency())
print(wifi.getQualityMax())
print(wifi.getRetrylimit())
print(wifi.getRTS())
#print(wifi.getSensitivity())
print(wifi.getStatistics())
print(wifi.getTXPower())
print(wifi.getWirelessName())


for key in keys:
    print(key)

scan = wifi.scan()

a = 4
(num_channels, frequencies) = wifi.getChannelInfo()
index = 1
for ap in scan.aplist:
    print("          Cell %02d - Address: %s" % (index, ap.bssid))
    print("                    ESSID:\"%s\"" % (ap.essid, ))
    print("                    Mode:%s" % (ap.mode, ))
    print("                    Frequency:%s (Channel %d)" % \
        (wifi._formatFrequency(ap.frequency.getFrequency()),
        frequencies.index(wifi._formatFrequency(
            ap.frequency.getFrequency())) + 1))
    if (ap.quality.updated & \
                pythonwifi.flags.IW_QUAL_QUAL_UPDATED):
        quality_updated = "="
    else:
        quality_updated = ":"
    if (ap.quality.updated & \
                pythonwifi.flags.IW_QUAL_LEVEL_UPDATED):
        signal_updated = "="
    else:
        signal_updated = ":"
    if (ap.quality.updated & \
                pythonwifi.flags.IW_QUAL_NOISE_UPDATED):
        noise_updated = "="
    else:
        noise_updated = ":"
    print("                    " + \
        "Quality%c%s/%s  Signal level%c%s/%s  Noise level%c%s/%s" % \
        (quality_updated,
        ap.quality.quality,
        wifi.getQualityMax().quality,
        signal_updated,
        ap.quality.getSignallevel(),
        "100",
        noise_updated,
        ap.quality.getNoiselevel(),
        "100"))
    # This code on encryption keys is very fragile
    key_status = ""
    if (ap.encode.flags & pythonwifi.flags.IW_ENCODE_DISABLED):
        key_status = "off"
    else:
        if (ap.encode.flags & pythonwifi.flags.IW_ENCODE_NOKEY):
            if (ap.encode.length <= 0):
                key_status = "on"
    print("                    Encryption key:%s" % (key_status, ))
    if len(ap.rate) > 0:
        for rate_list in ap.rate:
            # calc how many full lines of bitrates
            rate_lines = len(rate_list) // 5
            # calc how many bitrates on last line
            rate_remainder = len(rate_list) % 5
            line = 0
            # first line should start with a label
            rate_line = "                    Bit Rates:"
            while line < rate_lines:
                # print full lines
                if line > 0:
                    # non-first lines should start *very* indented
                    rate_line = "                              "
                rate_line = rate_line + "%s; %s; %s; %s; %s" % \
                    tuple(wifi._formatBitrate(x) for x in
                        rate_list[line * 5:(line * 5) + 5])
                line = line + 1
                print(rate_line)
            if line > 0:
                # non-first lines should start *very* indented
                rate_line = "                              "
            # print non-full line
            print(rate_line + "%s; "*(rate_remainder - 1) % \
                tuple(wifi._formatBitrate(x) for x in
                    rate_list[line * 5:line * 5 + rate_remainder - 1]) + \
                "%s" % (wifi._formatBitrate(
                        rate_list[line * 5 + rate_remainder - 1])))
    index = index + 1