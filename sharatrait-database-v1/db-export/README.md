# sharetrait database sql version 1.0.0

## options for using ShareTrait db

ShareTrait (ST) database is a SQLite 3 version and in this document we provide ways for you to use the database names ST_all.db version 1.0. 
The first option is by importing the current version in a [SQLiteStudio](https://sqlitestudio.pl/about/), a friendly desktop application for browsing and editing SQLite database files. Another option, whch can be also be used simuntaneosly with SQLite, but also on its own, is to use SQLite locally on a terminal, without the use of a management tool. 

# How to access and use the db 
1. [SQLiteStudio](#sqlitestudio)
2. [SQLite](#sqlite)

## sqlitestudio

1. Download
   - Go to the folder [db-export](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-export/) and download the ShareTrait (ST) database version 1.0 **ST_all.db**. The download icon is found on the top left corner of the raw data window, labelled as *Download raw file*. This option will download your databse (.db) file in the local Download folder. Please store this file in a home folder. Keep track of the path of that folder.
   - Download SQLiteStudio via the [download page](https://sqlitestudio.pl). This page contains the versions and applications that run on Windows, Linux and Mac operating systems. The SQLiteStudio is made easy and friendly and it only needs to click and run, without the need of configuring and installing it
     
2. Adding the database
   - Open SQLiteStudio application desktop and from the top right browser menu **Database** select **Add a database**. This option will open a window in which you are able to provide the path of where the database or the database version (with .db extension) is located. You have also the possibility to search the folder directory *Select new or existing file on local computer*. Make sure that the *Database type* is kept with the type default setting to **SQLite 3**
   - More information on how the display window to add a database is clearly explained here: [Adding new database](https://github.com/pawelsalawa/sqlitestudio/wiki/User_Manual#creating-new-database) 
  
3. Use database version 1.0 

   - Once you have imported the database in Studio, it can be viewed on the left window section containing the database Name List. Click on the name you recognise once. This will then allow to display the complete list of tables populated and ready to be used. This list of tables correspond to the complete table list in csv format provided in [db-tables](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharatrait-database-v1/db-tables) folder.
   - You can click on each of the table to explore **Structure** of the table, **Data**, the values contained in the table, **Constraints**, **Indexes** and **Triggers** for technical set of rules in relation to the database and **DDL**, the data definition language commands used by SQL for creating and using commands with database objects.
     Please take a look at the well documented available manual on github for [SQLiteStudio User Manual](https://github.com/pawelsalawa/sqlitestudio/wiki/User_Manual).
     Very useful is the **Tool** **SQL Editor**, in which you can write and execute your own queries and display the outputs directly on the Data display. More information on how to select the SQL editor can be found here: [executing sql queries](https://github.com/pawelsalawa/sqlitestudio/wiki/User_Manual#executing-sql-queries)


//flip the two put sqlite first even if SQLITE studio is easier for users to use db
   
## sqlite

1. Download
   - Please go to the folder [db-export](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-export/) and download the ShareTrait (ST) database version 1.0 **ST_all.db**. The download icon is found on the top left corner of the raw data window, labelled as *Download raw file*. This option will download your databse (.db) file in the local Download folder. Please store this file in a home folder. Keep track of the path of that folder. You can also connect and clone the [path](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharatrait-database-v1) to obtain and use directly the db version.
   - Download [SQLite](https://www.sqlite.org/download.html). Make sure you download the version for your operating system. You can also follow these commands for installing SQLite on Windows, MacOS and Ubuntu [How to Install SQLite on Your Machine (Windows, Linux, and Mac) — Simple Version](https://medium.com/@techwithjulles/part-5-how-to-install-sqlite-on-your-machine-windows-linux-and-mac-simple-version-f05b7963b6cd), version 2023-03-02.
   - There is a great documentation for [Command Line Shell For SQLite](https://www.sqlite.org/cli.html) with a full overview of the commands and formats with examples for you to test and follow. 

     *Please note that you do not have to have SQLite pre-installed in order to use SQLiteStudio. However you can also use both simultaneously.*

2. Connect to the database
   - Here we provide the commands for connecting to an existing database. In order to use sharetrait database **ST_all.db** you first move to the local directory where the database is lcoated by using cd path. Once you use the path, you can use these options
  
     For MacOS and Linux the **sqlite3** command is used 

   ```
   $ sqlite3 ST_all.db
   SQLite version 3.43.2 2023-10-10 13:08:14
   Enter ".help" for usage hints.
   sqlite> 
   ```

   Please note that launching sqlite3 is used for creating a new database. This following example shows that it will create a new database named *[my_first_database.db]* If the file *[my_first_database.db]* already exists, SQLite will open a connection to it; if it does not exist, SQLite will create it. Do not use the semi-colon (i.e. ;) after the database name, else it will be part of the database
   
   
   ```
   $ sqlite3 my_first_database.db
   SQLite version 3.43.2 2023-10-10 13:08:14
   Enter ".help" for usage hints.
   sqlite> 
   ```

    For Windows users, the command line programme is with sqlite3.exe. However, because double-clicking starts the sqlite3.exe without command-line arguments, no database file will have been specified, so SQLite will use a temporary database that is deleted when the session exits. To use a persistent disk file as the database, enter the ".open" command immediately after the terminal window starts up [1], [2].
   Thus from the command prompt SQLite3 shell program

   ```
   SQLite version 3.36.0 2021-06-18 18:36:39
   Enter ".help" for usage hints.
   Connected to a transient in-memory database.
   Use ".open FILENAME" to reopen on a persistent database.
   sqlite> .open ST_all.db
   sqlite>
   ```
   
3. Query and access data in sharetrait database

   - Using the *select* command to view.
     Once you have connected to the database you can use Select to Access and view tables of the Database. The easiest way to view the content of a table is by using select. For example, the following command will allow you to view the Table Dataset of ShareTrait version 1.0.
     Select is a command that needs a semi-colon (;) in order to be executed

   ```
   sqlite> select * from dataset;
   TRADAT001,"Overwintering strategies and life-history traits of different populations of Aphidius platensis along a latitudinal gradient in Chile",https://doi.org/10.5281/zenodo.7774767,Alfaro_Tapia_et_al_2022,primary,dataset,zenodo,"","","","",2022,2023-03-27,development,"5 populations of the same species aphid parasitoid Aphidius platensis.",""
   TRADAT002,"Dataset of Burraco, Valdes & Orizaola in Journal of Animal Ecology.",https://doi.org/10.6084/m9.figshare.9992201.v1,Burraco_et_al_2020,primary,dataset,figshare,"","","","",2022,2022-11-29,development,"seems that there are 2 populations rana temporaria and rana arvalis",""
   TRADAT003,"Phenotypic and Genetic Effects of Contrasting Ethanol Environments on Physiological and Developmental Traits in Drosophila melanogaster",https://doi.org/10.6084/m9.figshare.22561378.v1,Castaneda_and_Nespolo_2013,primary,dataset,figshare,"","","","",2023,2023-03-30,development,"2 populations Drosophila melanogaster",""
   ```

   - you can use Select * [table-name] to view the content for any of the tables in ShareTrait. The table list is provided under the attribute **table name** in [ShareTrait-database-tables-overview.csv](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-documentation/ShareTrait-database-tables-overview.csv) or using the same names as provided in the [table list](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharatrait-database-v1/db-tables)
   - You can use LIMIT 1 where 1 is the number of records to display at the end of the select command option in order to limit your number of records views. FOr example, the example above will select only the first 5 records from table
     
     
   ```
     sqlite> select * from population limit 5;
     TRAPOP001,dat001pop001,ind_measure,"",Aphidius_platensis,"","",""
     TRAPOP002,dat001pop002,ind_measure,"",Aphidius_platensis,"","",""
     TRAPOP003,dat001pop003,ind_measure,"",Aphidius_platensis,"","",""
     TRAPOP004,dat001pop004,ind_measure,"",Aphidius_platensis,"","",""
     TRAPOP005,dat001pop005,ind_measure,"",Aphidius_platensis,"","",""
   ```
     
4. Use the query templates to access the data

   - We have provided a list of existing [queries](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharatrait-database-v1/db-queries) for you to try. You can either paste the query in your sqlite command-line, or paste the query in the SQL Editor as described in Section 3. Use database version 1.0 of SQLiteStudio.
   - Please note that the db provided for version 1.0, [ST_all.db](https://github.com/ShareTraitProject/ShareTraitDatabase/blob/main/sharatrait-database-v1/db-export/ST_all.db) contains already Views integrated for you to view as templates and results. All documentation of results can be found in the query subfolder [queries](https://github.com/ShareTraitProject/ShareTraitDatabase/tree/main/sharatrait-database-v1/db-queries)

     Here we provide an example of query based on the question:
     **"Give me all the datasets that provide data regarding the group having the genus name *Danio*. Please also include DOIs if the dataset is published and the repository where the data is found"**

     ```
     Select distinct dataset.dataset_pk, dataset.title_dataset, dataset.dataset_publisher, dataset.doi_dataset, dataset.year_publication, population.species_reported, measurement.trait_type
      from dataset, describe, population, taxonomic_label, ref_taxonomy, contains, individual, measurement
      where ref_taxonomy.genus_name = "Danio" AND ref_taxonomy.taxonomy_pk = taxonomic_label.taxonomy_pk AND taxonomic_label.population_pk = population.population_pk AND population.population_pk = describe.population_pk AND describe.dataset_pk = dataset.dataset_pk
      AND population.population_pk = contains.population_pk AND contains.individual_pk = individual.individual_pk AND individual.individual_pk = measurement.individual_pk
     ```

   The output provides this result

   ```
   TRADAT028,"dbarneche/zebrafishCostOfGrowth: Published version of paper data and code: Warming increases the cost of growth in a model vertebrate",zenodo,https://doi.org/10.5281/zenodo.2634100,2019,Danio_rerio,metabolic_rate
   TRADAT033,"Data from: Are acute and acclimated thermal effects on metabolic rate modulated by cell size? A comparison between diploid and triploid zebrafish larvae",dryad,https://doi.org/10.5061/dryad.2280gb5qw,2020,Danio_rerio,metabolic_rate
   TRADAT040,"The dataset is not published","","","",Danio_rerio,metabolic_rate
   TRADAT044,"Endocrine disruption from plastic pollution and warming interact to increase the energetic cost of growth in a fish",dryad,https://doi.org/10.5061/dryad.v6wwpzgxm,2022,Danio_rerio,metabolic_rate
   ```

   In which shows only 4 datasets of sharetrait provide information regarding Danio and only 3 of them are published datasets. Two in Zenodo and one in Dryad repository. 
     

   
## Futher useful reads

- [Getting Started with SQLite](https://medium.com/@techwithjulles/list/getting-started-with-sqlite-dbc1bf2c4a04)
- [SQLite Documentation Quick Start](https://www.sqlite.org/quickstart.html)
- [Tutorial SQLite Commands](https://www.tutorialspoint.com/sqlite/sqlite_commands.htm)

Futher editions will provide different methods to connect and use the database. For any questions on how to use sharetrait-database-version1, please contact Irene

### Reference

[1] Command Line Shell For SQLite: https://www.sqlite.org/cli.html

[2] Data carpentry, The SQLite command line: https://datacarpentry.github.io/sql-socialsci/instructor/08-sqlite-command-line.html#:~:text=Open%20a%20command%20prompt%20(cmd,screen%20similar%20to%20that%20below.


