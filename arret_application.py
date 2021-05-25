#coding:utf-8
import os
def arreter_programme(mot):
	if not mot.endswith(".exe"):
		mot= mot+".exe"
	ligne=str()
	appli_trouve=0
	os.system("tasklist /FO CSV > file1.txt")
	fichier=open("file1.txt","r")
	while fichier.readline():
		ligne=fichier.readline()
		nbre=ligne.upper().find(mot.upper())
		if nbre!=-1:
			j=nbre
			while j<nbre+len(mot):
				j+=1
			i=1
			pid=str()
			while ligne[i]!='"' and i<j:
				pid+=ligne[i]
				i+=1
			print(pid)
			os.system("taskkill /F /IM {}".format(pid))
			appli_trouve=1
			break
	if appli_trouve==0:
		print("Application non trouvé")
	fichier.close()
appli=input("Enter le nom de l'application à arrêter:")
arreter_programme(appli)