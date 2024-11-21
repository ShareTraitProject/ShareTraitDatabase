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

     Please note that you do not have to have SQLite pre-installed in order to use SQLiteStudio. However you can also use both simultaneously.

2. Connect to the database
   here we provide a few general commands to connect to the database.
   
3. Query and access data in sharetrait database

