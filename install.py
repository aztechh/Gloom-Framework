import sys
import os
import pip
import time

if not os.geteuid() == 0:
	sys.exit('You must Run this Script as ROOT!')

try:
	os.system('apt-get install python-pip')
	os.system('easy_install pip')
	os.system('apt-get install nmap')
	os.system('apt-get install curl')
	os.system('curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall')
	install = os.system("apt-get update && apt-get install -y build-essential git")
    	install2 = os.system("cp -R gloom/ /opt/ && cp gloom.py /opt/gloom && cp run.sh /opt/gloom && cp run.sh /usr/bin/gloom && chmod +x /usr/bin/gloom")

	pip.main(['install', 'scapy', 'termcolor', 'urllib2', 'pythonwhois', 'requests'])
	cprint("[!] Finished Installing! Run 'sudo python gloom.py' to use program.", 'green')
	sys.exit()

except KeyboardInterrupt:
	sys.exit(0)

except:
	pass
