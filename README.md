# Table of Contents

-  [Introduction](#introduction)

-  [Setting up python environment](#python_setup)

-  [Setting up Mysql DB for reference](#mysql_setup)

-  [Running task one](#task_one)

-  [Running task two](#task_two)

- [Running test case](#test_case)

-  [Extra Information about files](#extra_info)

  

#### INTRODUCTION <a id='introduction'></a>

This repository contains codes for the solution to the assignment. There are two main files **task_one.py** and **task_two.py** which corresponds to task one and task two. Below are the sections for pre requisites to run the programs and DB setup.

> I have used docker for setting up database which proved very handy for bootstrapping DB within seconds.

  

____

  

#### PYTHON SETUP <a id='python_setup'></a>

  

<p  style='font-size:5px;'> I have included requirements.txt file which contains list of the dependencies which are required to run these programs. I haven't used any fancy libraries for the development. </p>

  

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

> make sure the containers are up and running, run the below command

>  ```sh

>  docker-compose ps

>  ```

  

This contains two containers, one for *MySql* and other for the *Adminer* which provides PHP based hosted UI for the MySql.

**MySql** would now be up and available on the below configurations:

  

> HOST: **localhost**

>

> USER: **root**

>

> PASSWORD: **example**

>

> PORT: **3306**

  

**Adminer** would be available on *http://localhost:8080* which can be accessed to interface with MySql container.

  

I have attached a script in the repository [setup_db.py](https://github.com/satyamsoni2211/redhat_assignment/blob/master/setup_db.py  "setup_db.py") which needs to be run for the initial DB and tables creation. To initiate the setup, kindly run the below command:

```sh

python setup_db.py

```

  

This will output names of some tables on successful completion of the script and will setup database named as **redhat** and tables **hero**,**films** and **map** which would be required in the programs.

  

____

  

#### RUNNING TASK ONE <a id='task_one'></a>

  

Task one can be simply executed by running the below command:

  

```sh

python task_one.py

```

  

[Task_one.py](https://github.com/satyamsoni2211/redhat_assignment/blob/master/task_one.py) file would generate 15 random numbers and call SWAPI to fetch their data. Once the data is available, it would transform the data, store it into MySql tables and output on the console expected JSON with Films as keys and expected characters as subkeys.

  

___

  

#### RUNNING TASK TWO<a id='task_two'></a>

  

Task two can be simply executed by running the below command:

  

```sh

python task_two.py

```

  

[Task_two.py](https://github.com/satyamsoni2211/redhat_assignment/blob/master/task_two.py) would query SWAPI for particular film id and them transform the cross links present in the body sections for **characters**, **planets**, **vehicles**, **species** and **starships**. It also removes any cross links present in the sub objects which it has transformed and saves the transformed object to [task_two.json](https://github.com/satyamsoni2211/redhat_assignment/blob/master/task_two.json) file which can further be checked for the output.

  

___

#### RUNNING TEST CASE<a id='test_case'></a>

  

Test case can be simply executed by running the below command:

  

```sh

python test.py

```

  

[Test.py](https://github.com/satyamsoni2211/redhat_assignment/blob/master/test.py) tests all the available function in util.py file. This uses unittest library to create test suite and run them.

___

  

#### EXTRA INFORMATION ABOUT FILES <a id='extra_info'></a>

  

There are aditional files along with the program files. Kindly look for the description below:

  

-  [db_wrapper.py](https://github.com/satyamsoni2211/redhat_assignment/blob/master/db_wrapper.py)

-- This contains DB class responsible for creating and closing the DB connection, creating cursor and commiting the changes.

  

-  [util.py](https://github.com/satyamsoni2211/redhat_assignment/blob/master/util.py)

-- This file includes utility function used in task_one.py and task_two.py for fetching and transformations and also some required config variables which are referenced throughout the script.

-- This also contains caching logic and sppeeds up the overall execution by avoiding redundant calls to the API.

```py

# black for caching the data

  

if os.path.exists(CACHE_FILE):

obj = pickle.load(open(CACHE_FILE,  'rb'))

else:

obj =  dict(

cache_characters=defaultdict(dict),

cache_planets=defaultdict(dict),

cache_starships=defaultdict(dict),

cache_vehicles=defaultdict(dict),

cache_species=defaultdict(dict),

cache_film=defaultdict(dict),

hero_info=defaultdict(dict),

film_info=defaultdict(dict)

)

```

-- I have used pickling for serializing and storing cache object to a pickle file [cache.pkl](https://github.com/satyamsoni2211/redhat_assignment/blob/master/cache.pkl) which is unpickled and loaded in the memory while running the programs and interfaces caching. Once the program finishes, cache object is again serialized and written to this file.

  

___

  

### Thank You

  

>Fork me on Github [satyamsoni2211](https://github.com/satyamsoni2211)

>

> Follow me on Twitter [satyamsoni1306](https://twitter.com/satyam_soni1306)

>

> Check my Repo in Docker [satyamsoni2211](https://hub.docker.com/u/satyamsoni2211)
