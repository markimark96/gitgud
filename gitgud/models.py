from subprocess import run

class GitTree():
    def __init__(self,directory):
        self.directory = directory
        self.name = directory.split("/")[-1]
        self.commits = []
        self.readCommits()


    def readCommits(self):
        commits = run('git -C ' + self.directory + ' log --all --no-decorate --date-order --reverse --pretty="format:%H,%ce,%an,%cI,%P" | grep ""', capture_output=True,shell=True,encoding="utf-8").stdout
        for commit in commits.splitlines():
            commitData = str(commit).split(",")
            hash = commitData[0]
            email = commitData[1]
            user = commitData[2]
            date = commitData[3]
            parents = commitData[4].split(" ")
            message = run('git -C ' + self.directory + ' log --pretty="format:%s" -n 1 '+hash, capture_output=True,shell=True,encoding="utf-8").stdout
            branch = run('git -C ' + self.directory + ' name-rev --name-only '+hash, capture_output=True,shell=True,encoding="utf-8").stdout.split("~")[0]
            self.commits.append(GitCommit(hash,user,email,date,parents,message,branch))



class GitCommit():
    def __init__(self,hash,author,email,date,parents,message,branch):
        self.hash = hash
        self.author = author
        self.email = email
        self.date = date
        self.message = message
        self.parents = parents
        self.branch = branch


