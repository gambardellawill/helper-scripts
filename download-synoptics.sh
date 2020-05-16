#!/bin/sh
# Author: William Gambardella
# Date: 2020-04-26

help() {
    echo "Cartas Sinóticas da Marinha do Brasil"
    echo "---"
    echo "Usage:"
    echo "\t- ./download-synoptics.sh -d [DATETIME]"
    echo "\t- ./download-synoptics.sh -o [FILEPATH] -d"
    echo "\t- ./download-synoptics.sh -o [FILEPATH] -d [DATETIME]"
    echo "\tDATETIME format: yymmdd00 or yymmdd12 (daily charts for 0:00 UTC or 12:00 UTC)." 
    echo "\tThis field can be left blank in order to download the latest chart."
    echo "Help:"
    echo "\t-d:\tSelects the chart for the desired date and time"
    echo "\t-o:\tDirectory in which the chart will be saved. The default directory is \$PWD"  
    echo "\t-h:\tOutputs this help section"
}

invalid_input() {
    help
    exit 1
}

[ "$#" -eq "0" ] && invalid_input

while getopts ":d:o:h:" arg; do
    case $arg in
        d) DATETIME=$OPTARG;;
        o) FILEPATH=$OPTARG;;
        h) help;;
    esac
done

DATE=$(date +"%y%m%d") 
[ $(date +"%H") -ge 12 ] && TIMEOFDAY="12" || TIMEOFDAY="00" 
[ -z "$DATETIME" ] && DATETIME="${DATE}${TIMEOFDAY}"

[ -z "$FILEPATH" ] && FILEPATH="${PWD}/${DATETIME}.jpg"

CHART_FILE="c${DATETIME}.jpg"
NAVY_URL="https://www.marinha.mil.br/chm/sites/www.marinha.mil.br.chm/files/cartas-sinoticas/${CHART_FILE}"

curl -sL $NAVY_URL -o "${FILEPATH}"
