from langchain.tools import tool
from repo_manager import RepoManager
from github_client import GitHubClient
from config import BASE_REPO_DIR

repo_manager = RepoManager(BASE_REPO_DIR)
github = GitHubClient()


@tool
def scan_local_repos():
    """Scan filesystem and return all local git repositories."""
    repos = repo_manager.scan_local_repos()
    return [r.working_dir for r in repos]


@tool
def get_repo_status(repo_path: str):
    """Get status of a local repository."""
    from git import Repo

    repo = Repo(repo_path)
    return {
        "branch": repo.active_branch.name,
        "dirty": repo.is_dirty(),
        "commit": repo.head.commit.hexsha,
    }


@tool
def get_remote_status(repo_name: str):
    """Get GitHub repo latest commit SHA."""
    repo = github.get_repo(repo_name)
    branch = repo.default_branch
    sha = github.get_branch_sha(repo, branch)
    return {"branch": branch, "commit": sha}


@tool
def sync_repo(repo_path: str):
    """Pull latest changes for a repo."""
    from git import Repo

    repo = Repo(repo_path)
    repo.git.pull()
    return "synced"


@tool
def create_repo(name: str):
    """Create a new GitHub repository."""
    repo = github.create_repo(name)
    return {"name": repo.name, "url": repo.clone_url}
