import requests

reqUrl = "https://api.github.com/octocat"

headersList = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "X-GitHub-Api-Version": "2022-11-28"
}

payload = ""

response = requests.request("GET", reqUrl, data=payload, headers=headersList)

print(response.text)