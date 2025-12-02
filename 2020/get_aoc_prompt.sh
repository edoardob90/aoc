#!/bin/bash
# must supply the day index
[[ "$#" < 1 ]] && echo -e "Day number is missing!\nUSAGE: $(basename $0) <day number> [<pandoc path>]" >&2 && exit 1

# system must have Pandoc
if ! type pandoc 2>/dev/null 1>/dev/null; then
    echo "The script requires Pandoc! Install it and re-run the script" >&2
    exit 1
fi

# full path of the script's directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# just make sure the destination directory exists
DEST=${DIR}/day${1}; mkdir -p ${DEST}

# get html with pandoc and convert it to md
${2:-/usr/local/bin/pandoc} -f html -t gfm --wrap=preserve "https://adventofcode.com/2020/day/${1}" | \
awk '{
    if ($0 ~ /<div role="main">/) {
        getline
        while ($0 !~ /^To play/) {
            if ($0 ~ /^#+/) {
                title=substr($0, index($0, "Day"))
                sub(/---/, "", title)
                printf("# %s\n", title)
            } else print $0
            getline
        }
    }
}' > ${DEST}/readme.md

