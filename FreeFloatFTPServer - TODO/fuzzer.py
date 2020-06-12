#!/usr/bin/env python
# Designed for use with boofuzz v0.0.9
from boofuzz import *


def main():
    session = Session(
        target=Target(
            connection=SocketConnection("192.168.5.128", 21, proto='tcp')
        ),
    )

    s_initialize(name="Request")
    s_string("USER ", fuzzable=False)
    s_string("FUZZ")
    s_delim("\n")
    s_string("PASS ", fuzzable=False)
    s_string("FUZZ")
    s_delim("\n")


    session.connect(s_get("Request"))

    session.fuzz()


if __name__ == "__main__":
    main()