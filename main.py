import os
import requests
from sys import exit
from dotenv import load_dotenv

load_dotenv()

r_headers = {
	'Authorization': 'Bearer ' + str(os.getenv('GH_TOKEN')),
	'Accept': 'application/vnd.github+json',
	'X-GitHub-Api-Version': '2022-11-28'
}

r = requests.get(
	'https://api.github.com/repos/guilhermeeric/' + str(os.getenv('CIRCLE_PROJECT_REPONAME')) + '/pulls/' + os.getenv('CIRCLE_PULL_REQUEST').split('/')[-1],
	headers=r_headers
)

print('repo', str(os.getenv('CIRCLE_PROJECT_REPONAME')))
print('pr number', os.getenv('CIRCLE_PULL_REQUEST').split('/')[-1])

pr_description = r.json()['body']
print(pr_description)

if (len(pr_description) < 5):
	print('Você não escreveu a descrição do seu PR.')
	exit(1)

print('Parabéns! Você descreveu seu PR corretamente')
exit(0)
