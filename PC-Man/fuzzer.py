#!/usr/bin/env python
# Designed for use with boofuzz v0.0.9
from boofuzz import *


def main():
    session = Session(
        target=Target(
            connection=SocketConnection("192.168.5.128", 21, proto='tcp')
        ),
    )

    s_initialize("PCMAN")

    s_string("USER ", fuzzable=False)
    s_delim(" ")
    s_string("FUZZ")
    s_string("PASS ")
    s_delim(" ")
    s_string("FUZZ")

    session.connect(s_get("PCMAN"))

    session.fuzz()


if __name__ == "__main__":
    main()