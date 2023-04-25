#!/usr/bin/env python

from Concatenate import cat, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort
from WordCount import wc
from Usage import usage

import sys


if len(sys.argv) < 2:
    usage()
    sys.exit(1)
else:
    # remove tt.py from arg list
    sys.argv.pop(0)
    # standardize input
    sys.argv[0] = sys.argv[0].lower()
    # determine which tool has been invoked
    # call on that tool, forwarding any remaining arguments to it
    if sys.argv[0] == 'cat':
        # remove superfluous arguments
        sys.argv.pop(0)
        # pass arguments through
        cat(sys.argv)
    elif sys.argv[0] == 'tac':
        # remove superfluous arguments
        sys.argv.pop(0)
        # pass arguments through
        tac(sys.argv)
    elif sys.argv[0] == 'wc':
        # remove superfluous arguments
        sys.argv.pop(0)
        # pass arguments through
        wc(sys.argv)
    elif sys.argv[0] == 'grep':
        # remove superfluous arguments
        sys.argv.pop(0)
        # pass arguments through
        grep(sys.argv)
    elif sys.argv[0] == 'head':
        # remove superfluous arguments
        sys.argv.pop(0)
        # pass arguments through
        head(sys.argv)
    elif sys.argv[0] == 'tail':
        # remove superfluous arguments
        sys.argv.pop(0)
        # pass arguments through
        tail(sys.argv)
    elif sys.argv[0] == 'cut':
        # remove superfluous arguments
        sys.argv.pop(0)
        # pass arguments through
        cut(sys.argv)
    elif sys.argv[0] == 'paste':
        # remove superfluous arguments
        sys.argv.pop(0)
        # pass arguments through
        paste(sys.argv)
    elif sys.argv[0] == 'sort':
        # remove superfluous arguments
        sys.argv.pop(0)
        # pass arguments through
        sort(sys.argv)
    else:
        print("Invalid tool name")
