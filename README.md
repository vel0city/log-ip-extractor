# log-ip-extractor

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9b9d0acab2ee493781885f22bad14472)](https://www.codacy.com/app/SimpleLTC/log-ip-extractor?utm_source=github.com&utm_medium=referral&utm_content=simpleltc/log-ip-extractor&utm_campaign=badger)

Quick Python script to rip all the IP addresses out of a log and give you countries and hostnames. Uses FreeGeoIP.net to get country of origin for all found IP addresses. It may take a while if there are a lot of IP addresses that don't resolve with gethostbyaddr.

# usage
python extract.py /path/to/logfile

# future update ideas
We could boost the speed of this by threading out the ```socket.gethostbyaddr()``` part of the script. That's the part that takes the longest.
