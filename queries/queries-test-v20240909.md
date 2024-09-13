# Question-Query List

# Meeting: 12-09-2024

## Question1
Provide me all the development trait measurements, their specifications and the scientific names, and the names reported of the individuals belonging to the genus "Aphidius" 

## Query1
Select measurement.trait_type, measurement.trait_value, measurement.trait_unit, individual.individual_pk, trait.life_stage_general_initial, trait.life_stage_general_final, population.species_reported, ref_taxonomy.scientific_name
FROM measurement
LEFT JOIN individual ON individual.individual_pk = measurement.individual_pk
LEFT JOIN contains ON contains.individual_pk = individual.individual_pk
LEFT JOIN population ON population.population_pk = contains.population_pk
LEFT JOIN taxonomic_label ON taxonomic_label.population_pk = population.population_pk
LEFT JOIN ref_taxonomy ON ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk
LEFT JOIN trait ON trait.trait_pk = measurement.trait_pk
WHERE measurement.trait_type = "development" AND ref_taxonomy.genus_name = "Aphidius"

## Question2
How many development traits measurements exist in sharetrait for each group of species?

## Query2
Select ref_taxonomy.genus_name, count(measurement.trait_value) AS TRAIT_MEASURE
FROM measurement
LEFT JOIN individual ON individual.individual_pk = measurement.individual_pk
LEFT JOIN contains ON contains.individual_pk = individual.individual_pk
LEFT JOIN population ON population.population_pk = contains.population_pk
LEFT JOIN taxonomic_label ON taxonomic_label.population_pk = population.population_pk
LEFT JOIN ref_taxonomy ON ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk
LEFT JOIN trait ON trait.trait_pk = measurement.trait_pk
WHERE measurement.trait_type = "development" AND measurement.trait_value NOT NULL 
GROUP by ref_taxonomy.genus_name
ORDER by TRAIT_MEASURE DESC;


## Question3

Which are the datasets describing fecundity traits and what are the DOIS, and in which repository can be found and are there any published manuscripts related to them?


## Query3

Select distinct dataset.dataset_pk, dataset.doi_dataset, dataset.dataset_publisher, manuscript.doi_manuscript
FROM measurement
LEFT JOIN individual ON individual.individual_pk = measurement.individual_pk
LEFT JOIN contains ON contains.individual_pk = individual.individual_pk
LEFT JOIN population ON population.population_pk = contains.population_pk
LEFT JOIN taxonomic_label ON taxonomic_label.population_pk = population.population_pk
LEFT JOIN ref_taxonomy ON ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk
LEFT JOIN describe ON population.population_pk = describe.population_pk
LEFT JOIN dataset ON describe.dataset_pk = dataset.dataset_pk
LEFT JOIN publication ON dataset.dataset_pk = publication.dataset_pk
LEFT JOIN manuscript ON publication.manuscript_pk = manuscript.manuscript_pk
LEFT JOIN trait ON trait.trait_pk = measurement.trait_pk
WHERE measurement.trait_type = "fecundity";

*TRADAT014,https://doi.org/10.5281/zenodo.7774767,zenodo,"https://doi.org/10.1127/entomologia/2021/1186 "
TRADAT015,https://doi.org/10.5281/zenodo.7313889,zenodo,https://doi.org/10.1017/S0025315407055282
TRADAT016,https://doi.org/10.48338/VU01-0OCUNQ,yoda,https://doi.org/10.1016/j.anbehav.2012.06.002
TRADAT017,https://doi.org/10.5281/zenodo.7763964,zenodo,https://doi.org/10.3390/insects12100852
TRADAT018,https://doi.org/10.5281/zenodo.4721086,zenodo,https://doi.org/10.1016/j.jtherbio.2021.103140
TRADAT019,"","",https://doi.org/10.1111/een.12422
TRADAT020,https://doi.org/10.6084/m9.figshare.13187642.v1,figshare,https://doi.org/10.14411/eje.2021.028
TRADAT021,https://doi.org/10.5281/zenodo.7775047,zenodo,https://doi.org/10.1007/s00442-013-2810-9
TRADAT022,https://doi.org/10.5061/dryad.2v6wwpzsg,dryad,https://doi.org/10.1093/evolut/qpac033
TRADAT023,https://doi.org/10.1016/j.fishres.2020.105803,"mendeley data",https://doi.org/10.1016/j.fishres.2022.106522
TRADAT024,https://doi.org/10.5281/zenodo.7764457,zenodo,https://doi.org/10.1111/1744-7917.12794
TRADAT025,https://doi.org/10.5281/zenodo.5342664,zenodo,https://doi.org/10.3390/insects12100855
TRADAT026,https://doi.org/10.5061/dryad.72g06,dryad,https://doi.org/10.1111/jeb.12888
TRADAT027,https://doi.org/10.17026/dans-zsa-f3y9,dans,https://doi.org/10.3389/fevo.2021.659363*

## Question4

Give me all the datasets and possible DOIs and their article publications of all the populations belonging to Danio and what type of trait information they provide - 
This helps you check if you are measurement a specific trait for a specific organism.


## QUery4 

Select distinct dataset.dataset_pk, dataset.title_dataset, dataset.dataset_publisher, dataset.doi_dataset, dataset.year_publication, population.species_reported, measurement.trait_type
from dataset, describe, population, taxonomic_label, ref_taxonomy, contains, individual, measurement
where ref_taxonomy.genus_name = "Danio" AND ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk AND taxonomic_label.population_pk = population.population_pk AND population.population_pk = describe.population_pk AND describe.dataset_pk = dataset.dataset_pk
AND population.population_pk = contains.population_pk AND contains.individual_pk = individual.individual_pk AND individual.individual_pk = measurement.individual_pk 

*TRADAT028,"dbarneche/zebrafishCostOfGrowth: Published version of paper data and code: Warming increases the cost of growth in a model vertebrate",zenodo,https://doi.org/10.5281/zenodo.2634100,2019,Danio_rerio,metabolic_rate
TRADAT033,"Data from: Are acute and acclimated thermal effects on metabolic rate modulated by cell size? A comparison between diploid and triploid zebrafish larvae",dryad,https://doi.org/10.5061/dryad.2280gb5qw,2020,Danio_rerio,metabolic_rate
TRADAT040,"The dataset is not published","","","",Danio_rerio,metabolic_rate
TRADAT044,"Endocrine disruption from plastic pollution and warming interact to increase the energetic cost of growth in a fish",dryad,https://doi.org/10.5061/dryad.v6wwpzgxm,2022,Danio_rerio,metabolic_rate*

## Question5

I am really curious to know how many measurements values you have for each of these selections and the type of units they use to measure the metabolic_rate

## Query5

Select dataset.dataset_pk, population.species_reported, measurement.trait_type, count (measurement.trait_value), measurement.trait_unit
from dataset, describe, population, taxonomic_label, ref_taxonomy, contains, individual, measurement
where ref_taxonomy.genus_name = "Danio" AND ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk AND taxonomic_label.population_pk = population.population_pk AND population.population_pk = describe.population_pk AND describe.dataset_pk = dataset.dataset_pk
AND population.population_pk = contains.population_pk AND contains.individual_pk = individual.individual_pk AND individual.individual_pk = measurement.individual_pk 
Group by dataset.dataset_pk

*TRADAT028,Danio_rerio,metabolic_rate,621,mLO2/h/ind
TRADAT033,Danio_rerio,metabolic_rate,422,nmolO2/h/ind
TRADAT040,Danio_rerio,metabolic_rate,658,umolO2/h/ind
TRADAT044,Danio_rerio,metabolic_rate,777,umolO2/min/ind*

## Question6

Provide me the published datasets that describe fecundity traits and how many populations and to which species were described

## Query6

Select dataset.dataset_pk, count(population.population_pk), group_concat(population.species_reported), ref_taxonomy.scientific_name, dataset.doi_dataset, dataset.dataset_trait 
from dataset, describe, population, taxonomic_label, ref_taxonomy where dataset.dataset_trait = "fecundity" AND dataset.dataset_pk = describe.dataset_pk AND describe.population_pk = population.population_pk AND population.population_pk = taxonomic_label.population_pk AND taxonomic_label.taxonomy_pk = ref_taxonomy.taxonomy_pk
Group by dataset.title_dataset;

*TRADAT023,16,"Lithodes_santolla,Lithodes_santolla,Lithodes_santolla,Lithodes_santolla,Lithodes_santolla,Lithodes_santolla,Lithodes_santolla,Lithodes_santolla,Lithodes_santolla,Lithodes_santolla,Lithodes_santolla,Lithodes_santolla,Lithodes_santolla,Lithodes_santolla,Lithodes_santolla,Lithodes_santolla","Lithodes santolla (Molina, 1782)",https://doi.org/10.1016/j.fishres.2020.105803,fecundity
TRADAT027,1,Gryllus_campestris,"Gryllus (Gryllus) campestris Linnaeus, 1758",https://doi.org/10.17026/dans-zsa-f3y9,fecundity
TRADAT026,1,Gryllus_bimaculatus,"Gryllus (Gryllus) bimaculatus De Geer, 1773",https://doi.org/10.5061/dryad.72g06,fecundity
TRADAT018,1,Aphidius_colemani,"Aphidius colemani Viereck, 1912",https://doi.org/10.5281/zenodo.4721086,fecundity
TRADAT025,1,Dysaphis_plantaginea,"Dysaphis (Pomaphis) plantaginea (Passerini, 1860)",https://doi.org/10.5281/zenodo.5342664,fecundity
TRADAT017,1,Aphidius_colemani,"Aphidius colemani Viereck, 1912",https://doi.org/10.5281/zenodo.7763964,fecundity
TRADAT022,1,Drosophila_subobscura,"Drosophila (Sophophora) subobscura Collin, 1936",https://doi.org/10.5061/dryad.2v6wwpzsg,fecundity
TRADAT015,1,Petrolisthes_laevigatus,"Petrolisthes laevigatus (Guerin, 1835)",https://doi.org/10.5281/zenodo.7313889,fecundity
TRADAT020,1,Trechnites_insidiosus,"Trechnites insidiosus (Crawford, 1910)",https://doi.org/10.6084/m9.figshare.13187642.v1,fecundity
TRADAT016,1,Lymnaea_stagnalis,"Lymnaea stagnalis (Linnaeus, 1758)",https://doi.org/10.48338/VU01-0OCUNQ,fecundity
TRADAT014,5,"Aphidius_platensis,Aphidius_platensis,Aphidius_platensis,Aphidius_platensis,Aphidius_platensis","Aphidius platensis Brethes, 1913",https://doi.org/10.5281/zenodo.7774767,fecundity
TRADAT021,4,"Asobara_tabida,Leptopilina_heterotoma,Spalangia_erythromera,Trichopria_drosophilae","Asobara tabida (Nees, 1834)",https://doi.org/10.5281/zenodo.7775047,fecundity
TRADAT019,1,Copidosoma_koehleri,"Copidosoma koehleri Blanchard, 1940","",fecundity
TRADAT024,1,Aphidius_ervi,"Aphidius ervi Haliday, 1834",https://doi.org/10.5281/zenodo.7764457,fecundity*

## Question7

Provide me with all the species available in sharetrait for the development trait


## Query7

select distinct ref_taxonomy.scientific_name, ref_taxonomy.genus_name, measurement.trait_type
From ref_taxonomy, taxonomic_label, population, contains, individual, measurement
Where ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk and taxonomic_label.population_pk = population.population_pk and population.population_pk = contains.population_pk and contains.individual_pk = individual.individual_pk and individual.individual_pk = measurement.individual_pk and measurement.trait_type = "development"

*"Aphidius platensis Brethes, 1913",Aphidius,development
"Rana arvalis Nilsson, 1842",Rana,development
"Rana temporaria Linnaeus, 1758",Rana,development
"Drosophila (Sophophora) melanogaster Meigen, 1830",Drosophila,development
"Pelophylax kl. esculentus (Linnaeus, 1758)",Pelophylax,development
"Aphidius colemani Viereck, 1912",Aphidius,development
"Chalcolestes viridis",Chalcolestes,development
"Trichopria drosophilae uncertain",Drosophila,development
"Asobara tabida (Nees, 1834)",Asobara,development
"Leptopilina heterotoma",Leptopilina,development
"Spalangia erythromera",Spalangia,development
"Aphidius ervi Haliday, 1834",Aphidius,development
"Lycaena phlaeas (Linnaeus, 1761)",Lycaena,development
"Brachymeria nosatoi Habu, 1966",Brachymeria,development
"Opisina arenosella Walker, 1864",Opisina,development
"Aphidius matricariae Haliday, 1834",Aphidius,development
"Dysaphis (Pomaphis) plantaginea (Passerini, 1860)",Dysaphis,development
"Operophtera brumata (Linnaeus, 1758)",Operophtera,development*


## Question8

Provide me the max measurement value for each population of Rana genus for all the existing dataset describing development trait


## Query8

select dataset.dataset_pk, dataset.title_dataset, dataset.doi_dataset, dataset.sharetrait_datasetid, population.population_pk, ref_taxonomy.scientific_name, ref_taxonomy.genus_name, measurement.trait_type, max(measurement.trait_value), measurement.trait_unit
From ref_taxonomy, taxonomic_label, population, contains, individual, measurement, describe, dataset
Where ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk and taxonomic_label.population_pk = population.population_pk and population.population_pk = contains.population_pk and contains.individual_pk = individual.individual_pk and individual.individual_pk = measurement.individual_pk and measurement.trait_type = "development" AND ref_taxonomy.genus_name =  "Rana" AND population.population_pk = describe.population_pk and describe.dataset_pk = dataset.dataset_pk
Group by population.population_pk

*TRADAT045,Burraco_etal_Oikos2021,https://doi.org/10.6084/m9.figshare.13089020.v1,Burraco_et_al_2021,TRAPOP006,"Rana arvalis Nilsson, 1842",Rana,development,150,Days
TRADAT002,"Dataset of Burraco, Valdes & Orizaola in Journal of Animal Ecology.",https://doi.org/10.6084/m9.figshare.9992201.v1,Burraco_et_al_2020,TRAPOP007,"Rana temporaria Linnaeus, 1758",Rana,development,39,Days*



##Question9


Provide me all the temperature values used during the experimental test for all the development traits measured for the Rana genus


## Query9

Select ref_taxonomy.genus_name, measurement.trait_type, group_concat(measurement.trait_value), measurement.trait_unit, condition.temperature, experiment_setup.condition_label
From ref_taxonomy, taxonomic_label, population, contains, individual, measurement, experiment_setup, condition
Where ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk and taxonomic_label.population_pk = population.population_pk and population.population_pk = contains.population_pk and contains.individual_pk = individual.individual_pk and individual.individual_pk = measurement.individual_pk and measurement.trait_type = "development" and ref_taxonomy.genus_name =  "Rana" and measurement.measurement_pk = experiment_setup.measurement_pk AND experiment_setup.condition_label = "test" AND experiment_setup.condition_pk = condition.condition_pk
Group by condition.temperature

*Rana,development,"53,53,52,53,53,50,55,54,55,67,54,58,52,61,52,52,55,62,58,60,55,53,57,63,58,57,55,75,58,56,58,59,88,93,61,58,56,55,56,51,56,56,61,60,62,57,55,57,52,57,57,54,52,51,57,56,60,51,64,117,111,102,117,112,111,110,121,108,97,88,107,118,127,97,101,116,122,119,97,125,134,132,111,82,121,130,136,100,81,104,102,126,109,131,88,90,131,109,102,103,103,106,131,97,60,65,67,61,65,60,67,65,76,65,61,58,61,64,58,63,59,56,63,64,60,60,58,59,65,65,68,63,67,62,69,70,83,72,67,66,73,62,73,88,70,68,75,66,66,58,74,63,65,66,67,72,63,62,60,55,60,63,65,59,59,67,62,82,80,100,100,99,85,95,78,97,109,113,82,72,82,87,84,81,76,84,88,86,82,79,86,94,96,85,87,107,96,77,112,101,97,93,109,150,135,115,79,85,88,85,88,99,78,101,84,83,80,83,84,84,82,87,80,88,91,86,72,60,57,60,55,56,55,56,58,58,52,55,54,62,64,63,59,61,60,55,54,63,53,53,52,62,62,61,61,60,60,66,63,62,60,58,67,65,62,61,69,61,65,66,59,54,59,58,68,66,64,60,62,58,65,62,62,54,57,59,64,65,63,62,61,57,87,88,88,101,107,108,81,84,111,93,97,89,79,76,84,84,72,76,69,83,80,81,84,83,90,93,93,92,85,102,115,113,107,107,126,81,81,92,84,88,88,93,92,107,77,81,82,95,80,82,108,87,97,103,92",Days,15,test
Rana,development,"35,34,33,33,37,34,34,32,38,35,34,37,35,35,34,36,36,33,35,34,34,35,33,36,35,36,34,39,35,39,38,37,34,34,32,35,35,34,37,37,37,39,31,34,35,32,33,33,33,35,33,32,30,32,33,30,33,30,32,30,31,31,33,32,32,34,31,30,31,31,34,31,33,31,32,30,30,30,31,31,32,33,32,30,31,34,30,31,32,30,30,30,33,32,29,29,32,31,32,30,32,32,34",Days,18,test
Rana,development,"32,37,35,37,33,35,35,36,36,36,36,35,35,36,33,34,38,41,35,37,38,33,38,39,34,35,39,38,37,46,37,40,43,40,42,42,32,36,33,35,35,35,37,40,39,40,34,38,42,35,34,36,39,38,38,39,36,38,79,81,81,85,79,71,67,67,70,79,63,65,78,68,67,78,61,78,60,64,76,67,70,85,86,79,79,81,81,87,71,69,65,86,94,77,66,69,62,66,59,85,77,75,76,62,73,78,76,85,76,72,43,46,48,45,47,51,45,45,46,46,48,45,41,45,42,42,44,40,42,43,42,46,47,47,51,47,46,50,54,41,47,48,45,44,47,48,44,50,50,53,47,49,42,40,41,46,45,46,49,46,41,46,49,41,44,47,44,46,45,45,44,47,47,50,45,80,81,80,81,95,86,78,83,78,87,79,62,69,61,63,69,69,74,63,84,80,80,80,81,80,87,79,73,78,78,80,70,70,74,85,71,63,81,70,73,76,72,76,78,85,75,69,68,70,79,75,68,73,78,77,41,43,39,40,41,40,42,40,40,41,39,37,39,39,38,43,43,36,39,38,39,40,39,40,45,39,42,43,41,41,40,44,49,39,40,41,42,50,45,40,36,38,39,39,38,41,40,39,38,42,40,37,41,41,42,39,40,38,41,42,40,41,62,75,84,79,65,62,68,68,67,65,69,54,59,60,80,54,52,61,66,69,68,62,63,67,70,64,65,66,64,64,69,67,79,67,81,70,59,60,66,59,53,74,76,68,59,79,59,73,61,60,69,67,62,56,63,65,80",Days,19,test*




Select distinct condition.temperature, experiment_setup.condition_label
From ref_taxonomy, taxonomic_label, population, contains, individual, measurement, experiment_setup, condition
Where ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk and taxonomic_label.population_pk = population.population_pk and population.population_pk = contains.population_pk and contains.individual_pk = individual.individual_pk and individual.individual_pk = measurement.individual_pk and measurement.trait_type = "development" and ref_taxonomy.genus_name =  "Rana" and measurement.measurement_pk = experiment_setup.measurement_pk AND experiment_setup.condition_label = "test" AND experiment_setup.condition_pk = condition.condition_pk

*18,test
19,test
15,test*

## Question10

 Effect of development temperature on body size of individuals.
(this would be possible if mass is given as a trait value, rather than an attribute of individual).

## Query10

Select ref_taxonomy.genus_name, measurement.trait_type, measurement.trait_value, measurement.trait_unit, measurement.size_value_final, measurement.size_units, measurement.size_type, condition.temperature, experiment_setup.condition_label
From ref_taxonomy, taxonomic_label, population, contains, individual, measurement, experiment_setup, condition 
Where ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk and taxonomic_label.population_pk = population.population_pk and population.population_pk = contains.population_pk and contains.individual_pk = individual.individual_pk and individual.individual_pk = measurement.individual_pk and measurement.trait_type = "development" and measurement.measurement_pk = experiment_setup.measurement_pk AND experiment_setup.condition_label = "test" AND experiment_setup.condition_pk = condition.condition_pk AND measurement.size_value != " " AND ref_taxonomy.genus_name = "Chalcolestes" AND measurement.trait_value NOT NULL;

Select ref_taxonomy.genus_name, measurement.trait_type, measurement.trait_value, measurement.trait_unit, measurement.size_value_final, measurement.size_units, measurement.size_type, condition.temperature, experiment_setup.condition_label
FROM ref_taxonomy
LEFT JOIN taxonomic_label ON taxonomic_label.taxonomy_pk = ref_taxonomy.taxonomy_pk
LEFT JOIN population ON population.population_pk = taxonomic_label.population_pk
LEFT JOIN contains ON contains.population_pk = population.population_pk
LEFT JOIN individual ON individual.individual_pk = contains.individual_pk
LEFT JOIN measurement ON measurement.individual_pk = individual.individual_pk 
LEFT JOIN experiment_setup ON experiment_setup.measurement_pk = measurement.measurement_pk 
LEFT JOIN condition ON condition.condition_pk = experiment_setup.condition_pk
WHERE ref_taxonomy.genus_name = "Chalcolestes" AND measurement.trait_type = "development" AND experiment_setup.condition_label = "test" AND measurement.trait_value NOT NULL;

*Chalcolestes,development,113,Days,27.57,milligram,"fresh body mass",20,test
Chalcolestes,development,108,Days,34.24,milligram,"fresh body mass",20,test
Chalcolestes,development,112,Days,29.86,milligram,"fresh body mass",20,test
Chalcolestes,development,99,Days,"",milligram,"fresh body mass",20,test
Chalcolestes,development,91,Days,31.88,milligram,"fresh body mass",20,test
Chalcolestes,development,89,Days,33.07,milligram,"fresh body mass",20,test
Chalcolestes,development,107,Days,32.8,milligram,"fresh body mass",20,test*




