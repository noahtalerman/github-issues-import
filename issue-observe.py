from github import Github
from pprint import pprint

g = Github('PAT-TODO')
repo = g.get_repo('REPO_TODO')
issues = repo.get_issues(state=)

for issue in issues:
  pprint(issue)