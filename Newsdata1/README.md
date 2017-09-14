Project: Logs Analysis Project  - Shaista Ahmad
================================
To develop an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
Logs Analysis Project is a python program with a backend database in postgresql.
The python program queries the database using python database API.It uses psycopg2 module to connect to the database.


Required Libraries and Dependencies
-----------------------------------
To run the Logs Analysis project it is required that you install Python v2 and a linux based Virtual machine.

How to Run Project
------------------
From your terminal, inside the vagrant subdirectory, run the command "vagrant up"
Run "vagrant ssh" to log into VM.
Inside the VM, change directory to /vagrant by running the command "cd /vagrant"
Connect to news database by running the command "psql -d news"

Drop views if already exists using the following commands :
drop view if exists errors cascade;drop view if exists total cascade;drop view if exists perc cascade;

Create views :
1.create or replace view errors as(SELECT time::date,count(status) as err from log where status != '200 OK' group by time::date);
2.create or replace view total as (SELECT time::date,count(status) as tot from log group by time::date);
3.create or replace view perc as (SELECT errors.time::date,((cast(err as float) * 100) / (cast(tot as float)))as percentage from errors,total where errors.time::date = total.time::date);

Run the command "\q" to disconnect from the database
Navigate to the project's directory "cd newsdata"
Run the python program with the following command "python newsdata.py"
The logs will be generated in output.txt file in the projects directory.
