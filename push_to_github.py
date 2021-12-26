from git import Repo

PATH_OF_GIT_REPO = '/home/pi/Documents/siot/'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

repo = Repo(PATH_OF_GIT_REPO)
repo.git.add(all=True)
repo.index.commit(COMMIT_MESSAGE)
origin = repo.remote(name='origin')
origin.push()