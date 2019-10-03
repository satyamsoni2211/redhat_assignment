
# Table of Contents
- [Introduction](#introduction)
- [Setting up python environment](#python_setup)
- [Setting up Mysql DB for reference](#mysql_setup)

####  INTRODUCTION <a id='introduction'></a>
This repository contains codes for the solution to the assignment. There are two mail files **task_one.py** and **task_two.py**  which corresponds to task one and task two. Below are the sections for pre requisites to run the programs and DB setup.
> I have used docker for setting up database which proved very handy for bootstrapping DB within seconds.

____

#### PYTHON SETUP <a id='python_setup'></a>

<p style='font-size:5px;'> I have included requirements.txt file which contains list of the dependencies which are required to run these programs. I haven't used any fancy libraries for the development. </p>

To setup python simply run the below command:
>pip install -r requirements.txt

This could be done in global **Env** or any virtual **Env** if exist.

Python Version: **3.7.0**

____

#### MYSQL SETUP <a id='mysql_setup'></a>

For Mysql setup, I have used Docker. Benefit of using Docker was that I didn't require to install MySql on my local machine and got it bootstrapped within seconds. I have included [**docker-compose.yml**](https://docs.docker.com/compose/compose-file/) file already with the repository for the setup.

For BootStrapping MySql DB, run the below commands: 
** _Considering Docker is already up and running_

```sh
docker-compose up -d
```
>  make sure the containers are up and running, run the below command
>  ```sh
>  docker-compose ps
>  ```

This contains two containers, one for *MySql* and other for the *Adminer* which provides PHP based hosted UI for the MySql.
**MySql** would now be up and available on the below configurations:

> HOST: **localhost**
> USER: **root**
> PASSWORD: **example**
> PORT: **3306**

**Adminer** would be available on *http://localhost:8080* which can be accessed to interface with MySql container.

I have attached a script in the repository [setup_db.py](https://github.com/satyamsoni2211/redhat_assignment/blob/master/setup_db.py "setup_db.py") which needs to be run for the initial DB and tables creation. To initiate the setup, kindly run the below command:
```sh
python setup_db.py
```

This will output names of some tables on successful completion of the script and will setup database named as **redhat** and tables **hero**,**films** and **map** which would be required in the programs.

____

