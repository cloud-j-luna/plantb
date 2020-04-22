setup:
	chmod u+x boot.sh
	chmod u+x auto-update.sh
	/bin/bash auto-update.sh &
	cp boot.sh /etc/init.d/
	update-rc.d boot.sh defaults
	/bin/bash /etc/init.d/boot.sh

dependencies:
	pip install watchdog
	pip install pyyaml
	pip install slackclient
	pip install RPi.GPIO

clean:
	rm /etc/init.d/boot.sh
