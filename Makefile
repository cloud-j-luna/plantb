setup:
	chmod u+x boot.sh
	cp boot.sh ~
	/bin/bash ~/boot.sh

clean:
	rm ~/boot.sh