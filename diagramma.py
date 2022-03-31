import matplotlib 
import matplotlib.pyplot as plt #importē grafiku bibliotēku

dalas=[50,20,10,60]



uzraksti=['Liepāja','Jelgava','Valmiera','Rīga']
krasas =['purple','mediumpurple','pink','plum']
izcelums=[0,0.1,0.15,0.1]

plt.title('Iedzīvotāji Latvijas pilsētās')

plt.pie(dalas,labels=uzraksti,colors=krasas,explode=izcelums,autopct='%1.1f%%')
plt.legend()
plt.show()