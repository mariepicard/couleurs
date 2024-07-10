# Couleurs
## Modélisation des couleurs en informatique
### Description
Travail expérimental tant d'un point de vue physique qu'informatique sur la modélisation des couleurs en informatique. D'un point de vue physique, il s'agissait de déterminer comment représenter certaines lumières monochromatiques, obtenues grâce à un réseau et une lampe spectrale, à partir de composantes RGB, d'une façon inspirée par l'expérience de J. Guild. Cela a été effectué grâce aux raies d'une lampe mercure-cadmium. D'un point de vue informatique, il s'agissait de représenter l'expérience des trous d'Young en lumière polychromatique, avec les valeurs trouvées, et avec les valeurs théoriques, pour différents spectres (lampes spectrales et lumière blanche). Un travail de recherche théoriques sur les différents modes de représentation des couleurs a de plus été effectué.

La partie de code a majoritairement été effectuée par ma binôme Alexane BOLDO, en python. La manipulation physique a été un travail commun. La modélisation mathématique et formalisation de l'espace CIE provenait majoritairement de moi, ainsi que la recherhce autour de l'expérience de Guild et de ses résultats.

### Utilisation
L'exécution du fichier python charge les fichiers "Valeur theoriques.txt" et "ValeursExperimentales.txt". Il est donc nécessaires que ces fichiers soient chargés et déposé dans le même répertoire que le code (ou modifier le chemin si besoin). Il affiche ensuite le résultats de l'expérience des trous d'Young pour la lampe mercure-cadmium avec les valeurs expérimentales puis théoriques) puis en lumière blanche (distrcibution uniforme puis loi de Planck).
