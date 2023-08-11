#!/usr/bin/env python

import os

print(os.environ["PATH"])
print(os.environ.get("HEY", "La variable no existe"))
