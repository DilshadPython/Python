# Update your machine

## sudo apt update

https://linuxways.net/mint/how-to-install-postgresql-on-linux-mint-20/

# Install postgres package and postgres contrib, whcih extended feature that extend the
# functionality of PostgreSql
## sudo apt install postgresql postgresql-contrib

# To check Postgresql is installed and running run:
## sudo systemctl status postgresql

# Login to postgresql instance:
## sudo -i -u postgres
postgres@MINIPC-E1:~$ psql
psql (12.9 (Ubuntu 12.9-0ubuntu0.20.04.1))
Type "help" for help.

postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 |
 template0 | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_GB.UTF-8 | en_GB.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(3 rows)

postgres=#

# Exit from tables run \q
postgres=# \q
postgres@MINIPC-E1:~$

## Logout from postgres run

postgres@MINIPC-E1:~$ exit
logout


