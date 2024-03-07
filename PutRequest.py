from git import Repo
import base64
import requests


################## You can Use this #####################
api_base_url = "https://api.github.com"

# Set up your personal access token and the base URL for the GitHub API
personal_access_token = "Your personal access token"

# Set the owner name && name of the repository
owner = "owner of the repository name"
repo = "repository name"

# Set the fil_path here
file_path = "file path that you want to add to the repository"

## Reading the file first
aa = open(file_path,'r').read()
print(aa)

text= base64.b64encode(aa.encode("utf-8"))

# Set up the user data for put request && commit message && name of the committer && his email as well
data = {
  "owner": owner,
  "repo" :repo,
  "path": file_path,
  "message":  'my commit message',
  "content": text.decode("utf-8"),
  "committer": {
    "name": 'name of the committer',
    "email": 'Committer email address'
  }
}

response = requests.put(f"{api_base_url}/repos/{owner}/{repo}/contents/file.txt", json=data,headers={
    "Authorization": f"Bearer {personal_access_token}",
    "Accept":"application/vnd.github.v3+json"
})

if response.status_code == 201:
    print("file is pushed successfully")
else:
    print("file is not pushed successfully", response.text, response.status_code)

############################ OR YOU CAN USE THIS #################################

PATH_OF_GIT_REPO = r'PATH OF THE .GIT REPO'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'YOUR COMMIT MESSAGE'

def git_push():
        try:
            repo = Repo(PATH_OF_GIT_REPO)
            repo.git.add(update=True)
            repo.index.commit(COMMIT_MESSAGE)
            repo.remotes.origin.push()
        except:
                print("Erro occured while pushing your data to your repository")

git_push()
