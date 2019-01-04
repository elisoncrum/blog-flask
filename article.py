import re
import os
from datetime import datetime

class Blog:
	title = "Elisons Backpacking Blog"
	staticPath = 'static/'
	articlePath = 'static/articles/'

	def __init__(self):
		# FontAwesome
		
		self.footerIconSize = 'fa-3x'
		self.footerIcons = [{
				'class': 'fab fa-github', 
				'href': 'https://github.com/elisoncrum', 
				'id': 'social-git'}, {

				'class': 'fab fa-instagram', 
				'href': 'https://www.instagram.com/elison.hike/',
				'id': 'social-insta'}, {

				'class': 'far fa-envelope', 
				'href': 'mailto:#elisoncrum@gmail.com',
				'id': 'social-mail'}, {

				'class': 'fas fa-cog',
				'href': '#',
				'id': 'social-cog'
				}]
	

	def openArticles(self):
		files = os.listdir(Blog.articlePath)
		self.articles = [self.convertArticles(article) for article in files]

	def sortArticles(self):
		self.articles = sorted(self.articles, key=lambda x: datetime.strptime(x['date'][0], '%m-%d-%y'), reverse = False)

	def markup(self, raw):
		reSearchLink = r'!\(([\s\S]*?)\)\[([\s\S]*?)\]'
		reLinkReplace = r'<a href="\2">\1</a>'
		reSearchText = r'{0}([\s\S]*?){0}'
		textFormat = [r'<i>\1</i>', r'<strong>\1</strong>', r'<strong><i>\1</i></strong>']

		raw = re.sub(reSearchLink, reLinkReplace, raw)
		for i in range(3, 0, -1):
			raw = re.sub(reSearchText.format('\*' * i), textFormat[i - 1], raw)
		
		return raw

	def convertArticles(self, fileName):
		articleData = {
			'title': None,
			'date': None,
			'content': [ ]
		}

		article = open(Blog.articlePath + fileName, 'r')
		reTagPattern = '```(\w*)\n([\s\S]*?)```'
		reResult = re.findall(reTagPattern, article.read(), re.MULTILINE)
		reResult = [(tag.strip(), content.replace('\n', ' ')) for tag, content in reResult]
		article.seek(0)

		index = 0
		iterResult = 0
		carouselIndex = 1
		for line in article.readlines():
			line = line.strip()

			reCommand = re.match('!\(([^\)]+)\)\[([^\)]+)\]', line)
			reElem = re.match('```(\w+)', line)
			if index == 0:
				articleData['title'] = line
			elif index == 1:
				date = datetime.strptime(line, '%m-%d-%y')
				articleData['date'] = [line, date.strftime('%B %d, %Y').replace(' 0', ' ')]
			
			elif reElem:
				content = reResult[iterResult][1]
				content = self.markup(content)
				articleData['content'].append(('elem', reElem.group(1), content))
				iterResult += 1

			elif reCommand:
				if '|' in reCommand.group(0):
					sldshwData = list(zip(reCommand.group(2).split('|'), reCommand.group(1).split('|')))
					articleData['content'].append(('sldshw', carouselIndex, sldshwData))
					carouselIndex += 1
				else:
					articleData['content'].append(('img', reCommand.group(2), reCommand.group(1)))
				
			index += 1
		return articleData