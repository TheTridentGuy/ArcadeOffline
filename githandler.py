import shutil
import git
import os


user = git.Actor("aidenbohlander", "aiden.bohlander@gmail.com")


def push_commit(path, commit_id, message):
    shutil.copytree(path, "tmp/")
    repo = git.Repo("tmp/")
    os.system("cd ./tmp")
    os.system(f"git reset --hard {commit_id}")
    index = repo.index
    index.commit(message)
    os.system("git add -A")
    os.system("git push --set-upstream origin master")
    shutil.rmtree("tmp/")
