import os

def getFile():
	if "channels.md" not in os.listdir():
		os.system("curl https://raw.githubusercontent.com/fastfire/deepdarkCTI/refs/heads/main/telegram_threat_actors.md -o channels.md")
	else:
		os.remove("channels.md")
		os.system("curl https://raw.githubusercontent.com/fastfire/deepdarkCTI/refs/heads/main/telegram_threat_actors.md -o channels.md")
		
def beautify():
	with open('channels.md', 'rb') as fd:
		data = fd.readlines()
	links_with_copy = []
	keys = ["Data Leaks", "Data Leak", "Combo List", "Cracking", "spamming", "carding"]
	types = ["ONLINE", "VALID"]
	with open("links.txt", "a") as fd:
		fd.write("https://t.me/hsdumps\nhttps://t.me/NinjaByte\nhttps://t.me/FALLAGA1\n")
		for items in data:
			tmp = str(items)
			for t in types:
				if t in tmp:
					for k in keys:
						if k in tmp:
							links_with_copy.append(tmp.split("|")[1])

		list_no_copy = set(links_with_copy)

		for links in list_no_copy:
			fd.write(links + "\n")
			
def scrape():
	getFile()
	beautify()
	os.remove('channels.md')
	print('Finished scraping links')
			
if __name__ == '__main__':
	scrape()