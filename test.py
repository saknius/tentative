import requests
 
owner = "saknius"
repo = "tentative"
branch = "main"
token = "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"

def update_branch_protection():
    url = f"https://api.github.com/repos/{owner}/{repo}/branches/{branch}/protection"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.luke-cage-preview+json"  # Required for branch protection API
    }
    payload = {
        "required_status_checks": None,
        "required_pull_request_reviews": {
            "dismissal_restrictions": {},
            "dismiss_stale_reviews": False,
            "require_code_owner_reviews": False,
            "required_approving_review_count": 1  # Set the required approving review count as per your needs
        },
        "restrictions": None,
        "enforce_admins": False
    }

    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Branch protection rules updated successfully!")
    else:
        print("Failed to update branch protection rules. Error:", response.text)

update_branch_protection()