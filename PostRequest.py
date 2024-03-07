import requests


# Set up your personal access token and the base URL for the GitHub API
personal_access_token = "Your personal access token"
api_base_url = "https://api.github.com"

# Create a dictionary to store the data for your new repository
data = {
    "name": "Your new repository",
    "description": "repository description",
    "private": True
}

# Send a POST request to the API endpoint to create a new repository
response = requests.post(f"{api_base_url}/user/repos", json=data, headers={
    "Authorization": f"Bearer {personal_access_token}",
    "Accept":"application/vnd.github.v3+json"
})

# Check the status code of the response
if response.status_code == 201:
    print("Successfully created repository")
else:
    print("Failed to create repository", response.text)
