import re

# test !!!!!!!!!
IP_ADDRESS = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

URL = re.compile(r"^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\."
                          r"[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$")

DOMAIN_NAME = re.compile(r"^[a-zA-Z0-9][-a-zA-Z0-9\\.]*$")
