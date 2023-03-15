import os

class GitController():
    def __init__(self, github_id="", token=""):
        self.id = github_id
        self.token = token


    def init(self):
        os.system("git init")

    def add(self, args):
        os.system(f"git add {args}")

    def commit(self, msg, args=""):
        os.system(f"git commit -m \"{msg}\" {args}")

    def push(self, args=""):

        with open("./streams/in.txt", "w", encoding="utf8") as f:
            f.write(f"{self.id}\n")
            f.write(f"{self.token}")

        os.system(f"git push {args} < \"./streams/in.txt\"")

    def pull(self, args=""):

        with open("./streams/in.txt", "w", encoding="utf8") as f:
            f.write(f"{self.id}\n")
            f.write(f"{self.token}")

        os.system(f"git pull {args} < \"./streams/in.txt\"")

    def log(self, args=""):
        with open("./streams/out.txt", "w+", encoding="utf8") as fp:
            os.system(f"git log {args} > \"./streams/out.txt\"")
            return fp.read().rstrip()

if __name__ == "__main__":
    git = GitController()
    print(git.log("--graph --oneline"))
    # print(git.log())
