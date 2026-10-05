import random

AUTHOR = "Tyler Guest"
APP_NAME = "Random Number"

def run():
  rint = random.randint(1, 100)
  result = rint
  return f"{APP_NAME}: {result}"