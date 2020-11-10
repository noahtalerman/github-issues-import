from github import Github
from pprint import pprint

g = Github('63f7a8622820aa8e132e860b84be3522a0caec46')
repo = g.get_repo('fleetdm-import-bot/issue-sender')
issues = repo.get_issues(state=)

for issue in issues:
  pprint(issue)