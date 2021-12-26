from git import Repo

PATH_OF_GIT_REPO = '/home/pi/Documents/siot/'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(['temp_graph.png'])
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

#git_push()

repo = Repo(PATH_OF_GIT_REPO)
repo.git.add(all=True)
repo.index.commit(COMMIT_MESSAGE)
origin = repo.remote(name='origin')
origin.push()