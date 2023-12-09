from secrets import *

# The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.
# In particular, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling and simulation, not security or cryptography.
# The secrets module provides access to the most secure source of randomness that your operating system provides.


def random_choice():
    rand = choice(range(0, 10000))
    return rand


def random_below():
    rand = randbelow(10000)
    return rand


def random_bits():
    rand = randbits(8)
    return rand


def my_random():
    digits = int(input("How many digits you want maximal? "))
    uptime = get_uptime()
    sub = uptime[-digits:len(uptime)]
    base = int(uptime) * int(sub)
    base = str(base)[::-1]
    rand = int(base[0:digits])
    return rand


def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = f.readline().replace(" ", "").replace(".", "").replace("\n", "")
    return uptime_seconds


print(my_random())
