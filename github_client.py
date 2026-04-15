from github import Github
from config import GITHUB_TOKEN


class GitHubClient:
    def __init__(self):
        if not GITHUB_TOKEN:
            raise ValueError("Missing GITHUB_TOKEN")
        self.client = Github(GITHUB_TOKEN)
        self.user = self.client.get_user()

    def get_repo(self, name):
        return self.client.get_repo(f"{self.user.login}/{name}")

    def create_repo(self, name):
        return self.user.create_repo(name)

    def get_branch_sha(self, repo, branch):
        return repo.get_branch(branch).commit.sha
