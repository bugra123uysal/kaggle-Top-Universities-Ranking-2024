import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 

 
dta=pd.read_csv("C:\\Users\\buğra\\Desktop\\shanghai_ranking_2024.csv" )
print(dta.info())
print(dta.head())
print(dta.tail())
print(dta.describe())


print(dta.columns)
f=dta.head()
l=dta.tail()
""" fırs """
plt.plot(f.index , label="fırst", marker='o' )
plt.plot(f.index , label="fırst", marker='o' )

plt.plot(l.index , label='last' , marker='x', linestyle='--'  )
plt.plot(l.index , label='last' , marker='x', linestyle='--' )
plt.grid(True)
plt.show()
top_10=dta.nlargest(10,'PCP' )
sns.barplot(x='University_Name', y='PCP', data=top_10 )
plt.xticks(rotation=90)
plt.title("PCP large 10")
plt.show()

last_10=dta.nsmallest(10, 'PCP')
sns.barplot(x='University_Name', y='PCP', data=last_10)
plt.xticks(rotation=90)
plt.title("PCP smaller 10")
plt.show()



topaw_10=dta.nlargest(10,'Award' )
sns.barplot(x='University_Name'  , y='Award' , data=topaw_10)
plt.xticks(rotation=90)
plt.title("Award larges 10")
plt.show()
lastaw_10=dta.nsmallest(10, 'Award')
sns.barplot(x='University_Name'  , y='Award' , data=lastaw_10)
plt.xticks(rotation=90)
plt.title(" Award last 10 " )
plt.show()


tophi_10=dta.nlargest(10,'Hici' )
sns.barplot(x='University_Name'  , y='Hici' , data=tophi_10)
plt.title("Hici large 10")
plt.xticks(rotation=90)
plt.show()
lasthi_10=dta.nsmallest(10, 'Hici')

sns.barplot(x='University_Name'  , y='Hici' , data=lasthi_10)
plt.xticks(rotation=90)
plt.title(" Hici last 10 " )
plt.show()
topns_10=dta.nlargest(10,'N&S' )
sns.barplot(x='University_Name'  , y='N&S' , data=topns_10)
plt.title("N&S large 10")
plt.xticks(rotation=90)
plt.show()

lastns_10=dta.nsmallest(10, 'N&S')

sns.barplot(x='University_Name'  , y='N&S' , data=lastns_10)
plt.xticks(rotation=90)
plt.title(" HN&S last 10 " )
plt.show()
toppu_10=dta.nlargest(10,'PUB' )
sns.barplot(x='University_Name'  , y='PUB' , data=toppu_10)
plt.title("PUB large 10")
plt.xticks(rotation=90)
plt.show()
lastpu_10=dta.nsmallest(10, 'PUB')

sns.barplot(x='University_Name'  , y='PUB' , data=lastpu_10)
plt.xticks(rotation=90)
plt.title(" PUB last 10 " )
plt.show()



topal_10=dta.nlargest(10,'Alumni' )
sns.barplot(x='University_Name'  , y='Alumni' , data=topal_10)
plt.title("Alumni large 10")
plt.xticks(rotation=90)
plt.show()

lastal_10=dta.nsmallest(10, 'Alumni')
sns.barplot(x='University_Name' , y='Alumni' , data=lastal_10 )
plt.xticks(rotation=90)
plt.title("last Alumni 10")
plt.show()


"""  National/Regional Rank """


sns.scatterplot(x='University_Name'  , y='N&S', size='Award'  , data=dta)
plt.xticks(rotation=90)
plt.title(" N&S Award")
plt.show()


