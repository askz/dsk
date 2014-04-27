from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas

## reading & cleaning data
data = pandas.read_csv("data/accidents.csv",sep=',')
data = pandas.DataFrame(data=data, columns=['lum', 'agg', 'int', 'atm', 'col', 'catr', 'infra', 'situ', 'circ', 'nbv', 'plan', 'prof', 'ttue', 'tbg', 'tbl', 'tindm'])
data.columns = ['LUMIERE', 'AGGLOMERATION', 'INTERSECTION', 'CONDITION_ATMOSPHERIQUES', 'TYPE_COLLISION', 'CATEGORIE_DE_ROUTE', 'INFRASTRUCTURE', 'SITUATION', 'CIRCULATION', 'NB_VOIES', 'PLAN', 'PROFIL', 'NB_TUE', 'NB_BLESSE_GRAV', 'NB_BLESSE_LEG', 'NB_INDEMN']
data['COUNT'] = 1
data = data.dropna()

# assign human refs
data.LUMIERE[data.LUMIERE == 1] = 'Plein jour'
data.LUMIERE[data.LUMIERE == 2] = 'Crepuscule ou aube'
data.LUMIERE[data.LUMIERE == 3] = 'Nuit sans eclairage'
data.LUMIERE[data.LUMIERE == 4] = 'Nuit avec eclairage non allume'
data.LUMIERE[data.LUMIERE == 5] = 'Nuit avec eclairage'

data.AGGLOMERATION[data.AGGLOMERATION == 1] = 'Hors agglomeration'
data.AGGLOMERATION[data.AGGLOMERATION == 2] = 'Agglo de moins de 2 000 hab'
data.AGGLOMERATION[data.AGGLOMERATION == 3] = 'Agglo entre 2 000 et 5 000 hab'
data.AGGLOMERATION[data.AGGLOMERATION == 4] = 'Agglo entre 5 000 et 10 000 hab'
data.AGGLOMERATION[data.AGGLOMERATION == 5] = 'Agglo entre 10 000 et 20 000 hab'
data.AGGLOMERATION[data.AGGLOMERATION == 6] = 'Agglo entre 20 000 et 50 000 hab'
data.AGGLOMERATION[data.AGGLOMERATION == 7] = 'Agglo entre 50 000 et 100 000 hab'
data.AGGLOMERATION[data.AGGLOMERATION == 8] = 'Agglo entre 100 000 et 300 000 hab'
data.AGGLOMERATION[data.AGGLOMERATION == 9] = 'Agglo de plus de 300 000 hab'

data.INTERSECTION[data.INTERSECTION == 1] = 'Hors intersection'
data.INTERSECTION[data.INTERSECTION == 2] = 'Intersection en X'
data.INTERSECTION[data.INTERSECTION == 3] = 'Intersection en T'
data.INTERSECTION[data.INTERSECTION == 4] = 'Intersection en Y'
data.INTERSECTION[data.INTERSECTION == 5] = 'Intersection a plus de 4 branches'
data.INTERSECTION[data.INTERSECTION == 6] = 'Giratoire'
data.INTERSECTION[data.INTERSECTION == 7] = 'Place'
data.INTERSECTION[data.INTERSECTION == 8] = 'Passage a niveau'
data.INTERSECTION[data.INTERSECTION == 9] = 'Autre intersection'

data.CONDITION_ATMOSPHERIQUES[data.CONDITION_ATMOSPHERIQUES == 1] = 'Normale'
data.CONDITION_ATMOSPHERIQUES[data.CONDITION_ATMOSPHERIQUES == 2] = 'Pluie legere'
data.CONDITION_ATMOSPHERIQUES[data.CONDITION_ATMOSPHERIQUES == 3] = 'Pluie forte'
data.CONDITION_ATMOSPHERIQUES[data.CONDITION_ATMOSPHERIQUES == 4] = 'Neige - grele'
data.CONDITION_ATMOSPHERIQUES[data.CONDITION_ATMOSPHERIQUES == 5] = 'Brouillard - fumee'
data.CONDITION_ATMOSPHERIQUES[data.CONDITION_ATMOSPHERIQUES == 6] = 'Vent fort - tempete'
data.CONDITION_ATMOSPHERIQUES[data.CONDITION_ATMOSPHERIQUES == 7] = 'Temps eblouissant'
data.CONDITION_ATMOSPHERIQUES[data.CONDITION_ATMOSPHERIQUES == 8] = 'Temps couvert'
data.CONDITION_ATMOSPHERIQUES[data.CONDITION_ATMOSPHERIQUES == 9] = 'Autre'

data.TYPE_COLLISION[data.TYPE_COLLISION == 1] = '2 vehicules - frontale'
data.TYPE_COLLISION[data.TYPE_COLLISION == 2] = '2 vehicules - arriere'
data.TYPE_COLLISION[data.TYPE_COLLISION == 3] = '2 vehicules - cote'
data.TYPE_COLLISION[data.TYPE_COLLISION == 4] = '3+ vehicules - en chaine'
data.TYPE_COLLISION[data.TYPE_COLLISION == 5] = '3+ vehicules - multiple'
data.TYPE_COLLISION[data.TYPE_COLLISION == 6] = 'Autre collision'
data.TYPE_COLLISION[data.TYPE_COLLISION == 7] = 'Sans collision'

data.CATEGORIE_DE_ROUTE[data.CATEGORIE_DE_ROUTE == 1] = 'Autoroute'
data.CATEGORIE_DE_ROUTE[data.CATEGORIE_DE_ROUTE == 2] = 'Route nationale'
data.CATEGORIE_DE_ROUTE[data.CATEGORIE_DE_ROUTE == 3] = 'Voie Departementale'
data.CATEGORIE_DE_ROUTE[data.CATEGORIE_DE_ROUTE == 4] = 'Voie communale'
data.CATEGORIE_DE_ROUTE[data.CATEGORIE_DE_ROUTE == 5] = 'Hors reseau public'
data.CATEGORIE_DE_ROUTE[data.CATEGORIE_DE_ROUTE == 6] = 'Parc de stationnement'
data.CATEGORIE_DE_ROUTE[data.CATEGORIE_DE_ROUTE == 9] = 'Autre'

data.INFRASTRUCTURE[data.INFRASTRUCTURE == 1] = 'Tunnel'
data.INFRASTRUCTURE[data.INFRASTRUCTURE == 2] = 'Pont'
data.INFRASTRUCTURE[data.INFRASTRUCTURE == 3] = 'Bretelle'
data.INFRASTRUCTURE[data.INFRASTRUCTURE == 4] = 'Voie ferre'
data.INFRASTRUCTURE[data.INFRASTRUCTURE == 5] = 'Carrefour'
data.INFRASTRUCTURE[data.INFRASTRUCTURE == 6] = 'Zone pietonne'
data.INFRASTRUCTURE[data.INFRASTRUCTURE == 7] = 'Peage'

data.SITUATION[data.SITUATION == 1] = 'Chaussee'
data.SITUATION[data.SITUATION == 2] = 'Bande d\'arret d\'urgence'
data.SITUATION[data.SITUATION == 3] = 'Accotement'
data.SITUATION[data.SITUATION == 4] = 'Trottoir'
data.SITUATION[data.SITUATION == 5] = 'Piste cyclable'

data.CIRCULATION[data.CIRCULATION == 1] = 'Sens unique'
data.CIRCULATION[data.CIRCULATION == 2] = 'Bidirectionnelle'
data.CIRCULATION[data.CIRCULATION == 3] = 'Chaussees separees'
data.CIRCULATION[data.CIRCULATION == 4] = 'Voies d\'affectation variable'

data.PLAN[data.PLAN == 1] = 'Rectiligne'
data.PLAN[data.PLAN == 2] = 'Courbe a gauche'
data.PLAN[data.PLAN == 3] = 'Courbe a droite'
data.PLAN[data.PLAN == 4] = 'En "S"'

data.PROFIL[data.PROFIL == 1] = 'Plat'
data.PROFIL[data.PROFIL == 2] = 'Pente'
data.PROFIL[data.PROFIL == 3] = 'Sommet de cote'
data.PROFIL[data.PROFIL == 4] = 'Bas de cote'

## plot histograms
for col in enumerate(data.columns):
	# geting the sub df | col[1] -> name
	c = col[1]
	fig = pandas.DataFrame({c : data[c], 'COUNT' : data['COUNT']})
	fig = fig.groupby(c).sum()
	fig.set_index('COUNT')
	fig.reset_index(level=0, inplace=True)

	# ignore some nan values
	if ( c == 'CIRCULATION'):
		fig = fig.loc[1:]
	elif ( c == 'INFRASTRUCTURE' ):
		fig = fig.loc[1:]
	elif ( c == 'INTERSECTION' ):
		fig = fig.loc[1:]
	elif ( c == 'PLAN' ):
		fig = fig.loc[1:]
	elif ( c == 'PROFIL' ):
		fig = fig.loc[1:]
	elif ( c == 'SITUATION' ):
		fig = fig.loc[1:]
	# shell print
	print(fig)
	# plotting
	fig.plot(kind='barh', x=fig[c], legend=False, stacked=True)
	name = "figs/data/" + c + "_HIST.png"
	plt.savefig(name, bbox_inches='tight')