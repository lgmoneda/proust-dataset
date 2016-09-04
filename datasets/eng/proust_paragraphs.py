#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import pandas as pd
import os
import numpy as np
import csv
paragraphs = []
volumes = []
chapters = []
for volume in range(1,8):
	folder = str(volume)
	onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
	onlyfiles = sorted(onlyfiles)
	for file_ in onlyfiles:
		soup = BeautifulSoup(open(folder + "/" + file_))
		all_p=soup.find_all('p')

		for p in all_p[:-2]:
			paragraph = p.find(text=True).encode('utf-8')
			paragraphs.append(paragraph)
			volumes.append(volume)
			chapters.append(file_[-6])


data = pd.DataFrame()
data["paragraph"] = paragraphs
data["volume"] = volumes
data["chapter"] = chapters
print data.head(10)
data.to_csv(path_or_buf="proust_dataset_ENG.csv", sep="@")
#string = data["paragraph"].to_string(buf="")
#print string.shape
#data.to_csv(path_or_buf='test.txt', index=False, header=None, quoting=csv.QUOTE_NONE, sep="|", cols=["paragraph"], quotechar='', escapechar='|')

#data["paragraph"].to_csv(r'proust_dataset_ENG.txt', header=None, index=None, sep=' ', mode='w', quoting=csv.QUOTE_MINIMAL)
#np.savetxt(r'proust_dataset_ENG.txt', string, fmt='%c')
#data["paragraph"].values


base_filename = 'Values.txt'
with open(base_filename,'w') as outfile:
	for paragraph in paragraphs[:3]:
		outfile.writelines(paragraphs)
	#outfile.write(paragraphs)
    #data.to_string(outfile)
"""
#def csv_to_txt(df):
	
"""
