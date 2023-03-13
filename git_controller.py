import os

def init():
    os.system("git init")

def add(args):
    os.system(f"git add {args}")

def commit(msg, args=""):
    os.system(f"git commit -m \"{msg}\" {args}")

if __name__ == "__main__":
    init()
    add(".")
    commit("FIRST COMMIT")
