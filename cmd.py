import subprocess
import argparse
p = argparse.ArgumentParser()
p.add_argument("stg", help = "Stage What??")
p.add_argument("commit_message", help = "CommitMessage")
a = p.parse_args()
what = a.stg
CommitMessage = a.commit_message
subprocess.call("git status", shell = True)
input()
subprocess.call("git add " + what + " && git commit -m "  + CommitMessage + " && git push origin master", shell = True)
