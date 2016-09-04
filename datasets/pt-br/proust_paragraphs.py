#@lgmoneda
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv

paragraphs = []
volumes = []
chapters = []
for volume in range(1,8):
	folder = str(volume)
	onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
	onlyfiles = sorted(onlyfiles)
	#print onlyfiles
	for file_ in onlyfiles:
		soup = BeautifulSoup(open(folder + "/" + file_), "lxml")
		#print soup
		all_p=soup.find_all('p')

		for p in all_p[:-2]:
			paragraph = p.text.encode('utf-8')
			if paragraph != "": 
				paragraphs.append(paragraph)
				volumes.append(volume)
				chapters.append(file_[file_.find("chapter") + len("chapter")])



data = pd.DataFrame()
data["paragraph"] = paragraphs
data["volume"] = volumes
data["chapter"] = chapters

print data.head(12)
data.to_csv(path_or_buf="proust_dataset_ptbr.csv", sep="@")
data.to_csv(path_or_buf='proust_dataset_ptbr.txt', index=False, header=None, quoting=csv.QUOTE_NONE, na_rep=" ", sep='\t', columns=["paragraph"], quotechar='', escapechar='|', mode='w')
 