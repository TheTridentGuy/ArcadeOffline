import shutil
import git


user = git.Actor("aidenbohlander", "aiden.bohlander@gmail.com")


def push_commit(path, commit_id, url, message):
    shutil.copytree(path, "tmp/")
    repo = git.Repo("tmp/")
    repo.git.reset("--hard", commit_id)
    index = repo.index
    index.commit(message)
    origin = repo.create_remote("origin", url)
    origin.push()
    shutil.rmtree("tmp/")
