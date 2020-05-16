#!/bin/bash

SENDER=$1
RECIPIENT=$2

curl --url 'smtps://smtp.gmail.com:465' --ssl-reqd \
  --mail-from '$SENDER' \
  --mail-rcpt '$RECIPIENT' \
  --user '$SENDER:$SND_PASSWD' \
  -T <(echo -e 'From: $SENDER\nTo: $RECIPIENT\nSubject: Curl Test\n\nHello')
