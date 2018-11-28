import subprocess
import argparse
p = argparse.ArgumentParser()
p.add_argument("stg", help = "specs for stage")
p.add_argument("commit_message", help = "CommitMessage <message should be in triple dual-quotes.>")
a = p.parse_args()
what = a.stg
CommitMessage = a.commit_message
subprocess.call("git status", shell = True)
input()
subprocess.call("git add " + what + " && git commit -m "  + CommitMessage + " && git push origin master", shell = True)
