import os
from git import Repo


class RepoManager:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def scan_local_repos(self):
        repos = []
        for root, dirs, files in os.walk(self.base_dir):
            if ".git" in dirs:
                try:
                    repo = Repo(root)
                    repos.append(repo)
                except Exception:
                    continue
        return repos

    def get_repo_status(self, repo):
        return {
            "path": repo.working_dir,
            "active_branch": repo.active_branch.name,
            "is_dirty": repo.is_dirty(),
        }

    def get_latest_commit_sha(self, repo):
        return repo.head.commit.hexsha

    def fetch_remote(self, repo):
        for remote in repo.remotes:
            remote.fetch()

    def pull_latest(self, repo):
        repo.git.pull()
