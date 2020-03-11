setup:
	chmod u+x boot.sh
	chmod u+x auto-update.sh
	/bin/bash auto-update.sh &
	cp boot.sh /etc/init.d/
	update-rc.d boot.sh defaults
	/bin/bash /etc/init.d/boot.sh

dependencies:
	pip3 install watchdog
	pip3 install pyyaml
	pip3 install slackclient
	pip3 install RPi.GPIO

clean:
	rm /etc/init.d/boot.sh