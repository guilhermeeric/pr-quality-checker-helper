import os
import requests
from sys import exit
from github import Github
from github import Auth
from dotenv import load_dotenv

load_dotenv()

auth = Auth.Token(os.getenv('TOKEN'))
g = Github(auth=auth)

repo = g.get_repo('ResultadosDigitais/pr-quality-checker')
pr = repo.get_pull(1)
pr_description = pr.body

g.close()

print('Repo, ' + os.getenv('CIRCLE_PROJECT_REPONAME'))
print('Pull number, ' + os.getenv('CIRCLE_PULL_REQUEST'))
print('Example var, ' + os.getenv('EXAMPLE_VAR'))

if (len(pr_description) < 5):
	print('Você não escreveu a descrição do seu PR.')
	exit(1)

print('Parabéns! Você descreveu seu PR corretamente')
exit(0)
