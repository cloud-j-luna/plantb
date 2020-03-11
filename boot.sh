#!/bin/bash

ENTRYPOINT="main.py"

watchmedo shell-command \
auto-restart \
--patterns="*.py" \
--command='python3 "$ENTRYPOINT"' \
.