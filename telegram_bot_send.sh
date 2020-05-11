#!/bin/bash

TOKEN=<TOKEN>
CHAT_ID=<CHAT_ID>
MESSAGE="Hello World"
URL="https://api.telegram.org/bot$TOKEN/sendMessage"

curl -s -X POST $URL -d chat_id=$CHAT_ID -d text="$MESSAGE"