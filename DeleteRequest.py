import requests


# Set up your personal access token and the base URL for the GitHub API

personal_access_token = "Your personal access token"
api_base_url = "https://api.github.com"

# Set the owner name && name of the repository

repo = " Repository name"
owner = "Owner of the repository name"
data = {
    "owner": "owner",
    "repo": repo,
}
response = requests.delete(f"{api_base_url}/repos/{owner}/{repo}", json=data,headers={
    "Authorization": f"Bearer {personal_access_token}",
    "Accept":"application/vnd.github.v3+json"
})

if (response.status_code == 200 or response.status_code == 204 or response.status_code == 202):
    print("Successfully deleted repository")
else:
    print("Failed to deletd repository", response.text)
