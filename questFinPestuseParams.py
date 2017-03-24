# -*- coding: utf-8 -*-
"""=============================================================================
This modules contains the variables and the parameters.
Do not change the variables.
Parameters that can be changed without any risk of damages should be changed
by clicking on the configure sub-menu at the server screen.
If you need to change some parameters below please be sure of what you do,
which means that you should ask to the developer ;-)
============================================================================="""

# variables --------------------------------------------------------------------
BASELINE = 0
TREATMENTS_NAMES = {BASELINE: "Baseline"}

# parameters -------------------------------------------------------------------
TREATMENT = BASELINE
TAUX_CONVERSION = 1
NOMBRE_PERIODES = 0
TAILLE_GROUPES = 0
GROUPES_CHAQUE_PERIODE = False
MONNAIE = u"ecu"
PERIODE_ESSAI = False

# DECISION
DECISION_MIN = 0
DECISION_MAX = 100
DECISION_STEP = 1

NATIONALITES = [u"Choisir","Afghan", u"Albanais", u"Algérien", u"Allemand", u"Américain", u"Angolais", u"Argentin", u"Arménien", \
u"Australien", u"Autrichien", u"Bangladais", u"Belge", u"Béninois", u"Bosniaque", u"Botswanais", u"Bhoutan", u"Brésilien", \
u"Britannique", u"Bulgare", u"Burkinabè", u"Cambodgien", u"Camerounais", u"Canadien", u"Chilien", u"Chinois", u"Colombien", \
u"Congolais", u"Cubain", u"Danois", u"Ecossais", u"Egyptien", u"Espagnol", u"Estonien", u"Européen", u"Finlandais", u"Français", \
u"Gabonais", u"Georgien", u"Grec", u"Guinéen", u"Haïtien", u"Hollandais", u"Hong-Kong", u"Hongrois", u"Indien", u"Indonésien", \
u"Irakien", u"Iranien", u"Irlandais", u"Islandais", u"Israélien", u"Italien", u"Ivoirien", u"Jamaïcain", u"Japonais", u"Kazakh", \
u"Kirghiz", u"Kurde", u"Letton", u"Libanais", u"Liechtenstein", u"Lituanien", u"Luxembourgeois", u"Macédonien", u"Madagascar", \
u"Malaisien", u"Malien", u"Maltais", u"Marocain", u"Mauritanien", u"Mauricien", u"Mexicain", u"Monégasque", u"Mongol", \
u"Néo-Zélandais", u"Nigérien", u"Nord Coréen", u"Norvégien", u"Pakistanais", u"Palestinien", u"Péruvien", u"Philippins", \
u"Polonais", u"Portoricain", u"Portugais", u"Roumain", u"Russe", u"Sénégalais", u"Serbe", u"Serbo-croate", u"Singapour", \
u"Slovaque", u"Soviétique", u"Sri-lankais", u"Sud-Africain", u"Sud-Coréen", u"Suédois", u"Suisse", u"Syrien", u"Tadjik", \
u"Taïwanais", u"Tchadien", u"Tchèque", u"Thaïlandais", u"Tunisien", u"Turc", u"Ukrainien", u"Uruguayen", u"Vénézuélien", \
u"Vietnamien"]

ETUDES_DISCIPLINES = [u"Choisir", u"AES", u"Archéologie", u"Biologie", u"Chimie", u"Droit", u"Ecole de commerce", u"Ecole d\'infirmière", u"Ecole d\'ingénieur", \
u"Economie", u"Géographie", u"Histoire", u"Informatique", u"IAE", u"IPAG", u"ISEM", u"Lettres", u"Mathématiques", u"Médecine", u"Musique", u"Pharmacie", \
u"Philosophie", u"Physique", u"Science politique", u"Science de l\'éducation", u"Sociologie", u"STAPS", u"SupAgro", u"Autre"]

ETUDES_ANNEES = [u"Choisir",  u"Licence 1",  u"Licence 2",  u"Licence 3",  u"Master 1",  u"Master 2",  u"Doctorat"]
