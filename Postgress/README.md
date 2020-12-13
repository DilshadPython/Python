# Install Postgresql

## sudo apt-get install wget ca-certificates
## wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
## sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'

## sudo apt-get update
## sudo apt-get install postgresql-12 pgadmin4 postgresql-server-dev-12 libpq-dev postgresql-12 postgresql-client-12

## :~$ service postgresql status
## :~$ service postgresql start
## :~$ service postgresql stop
## service postgresql 
Usage: /etc/init.d/postgresql {start|stop|restart|reload|force-reload|status} [version ..]



## Connect postgresql
## sudo su - postgres
## psql
### raffi@raffi-VB:~$ sudo su - postgres
	postgres@raffi-VB:~$ psql
	psql (12.2 (Ubuntu 12.2-2.pgdg18.04+1))
	Type "help" for help.

	postgres=# 

## How to change the database password default (postgres)
## postgres=# ALTER USER postgres WITH PASSWORD 'raffi1973';
	ALTER ROLE
	postgres=# 

## Find how many users are created in the database
postgres-# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 dilmac    | Create DB                                                  | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

## Make the created user (dilmac) as superuser 

postgres=# ALTER USER dilmac WITH SUPERUSER;
ALTER ROLE
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 dilmac    | Superuser, Create DB                                       | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

postgres=# 

## CREATE more users and delete user:
postgres=# CREATE USER user_one WITH PASSWORD 'raffi1973';
CREATE ROLE
postgres=# CREATE USER user_two WITH PASSWORD 'raffi1973';
CREATE ROLE
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 dilmac    | Superuser, Create DB                                       | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 user_one  |                                                            | {}
 user_two  |                                                            | {}

postgres=# DROP USER user_two;
DROP ROLE
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 dilmac    | Superuser, Create DB                                       | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 user_one  |                                                            | {}




## To get some commands how to use in postgres
## psql --help 


## For scripy you have to install:
### sudo apt-get build-dep python-psycopg2
### pip install psycopg2-binary

## to initial the models first
### pip3 install config 

## Create Databases
## CREATE DATABASE dildatab;

## connect database outside postgresql shell

## MacBook Pro
## psql -h localhost -p 5432 -U raffi mydatab

## CREATE ROLE your_username WITH LOGIN CREATEDB ENCRYPTED PASSWORD 'your_password';

## postgres=# CREATE ROLE dilmac WITH LOGIN CREATEDB ENCRYPTED PASSWORD 'myadmin';
CREATE ROLE

## postgres@raffi-VB:~$ su - dilmac
No passwd entry for user 'dilmac'
postgres@raffi-VB:~$ createdb testme;
postgres@raffi-VB:~$ \l
-su: l: command not found
postgres@raffi-VB:~$ psql
psql (12.2 (Ubuntu 12.2-2.pgdg18.04+1))
Type "help" for help.

postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 mydatab   | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | 
 postgres  | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | 
 template0 | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 testme    | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | 
(5 rows)

##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##