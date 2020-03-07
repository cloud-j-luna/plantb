setup:
	chmod u+x boot.sh
	chmod u+x auto-update.sh
	/bin/bash auto-update.sh &
	cp boot.sh ~
	/bin/bash ~/boot.sh

dependencies:
	pip install watchdog

clean:
	rm ~/boot.sh