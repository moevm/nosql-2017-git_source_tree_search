# Git Source Tree Search

**TODO:** some description.

## Installation

### Project dependencies

* Python 3.*
* Virtualenv
* Neo4j database 3.3.* (at least, community edition)
* Neo4j python driver 1.5.* (neo4j-driver)
* Pygit2 library 0.16.* (pygit2)

### Example Windows 10 installation:

1. Download and install Python 3.*
2. Download Neo4j 3.3.* (zip) from [official site](https://neo4j.com/download/other-releases/#releases)
3. Unzip archive to some directory (I recommend you to use ASCII-only path 
    without spaces). For example it would be `C:\Neo4j`
4. Run PowerShell as Administrator
5. Change execution policy: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`
    to import PowerShell module
6. Import PowerShell module: 
    `Import-Module C:\Neo4j\bin\Neo4j-Management.psd1`
7. Install Neo4j service, if you want: `Invoke-Neo4j install-service -Verbose`
8. Run Neo4j server: `Invoke-Neo4j start`
9. Check Neo4j server status: `Invoke-Neo4j status`
10. Now you can go to `localhost:7474`, sign up and change default Neo4j 
    password (user: `neo4j`, password: `neo4j`)
11. Run your preffered command line and install virtualenv: 
    `pip install virtualenv`
12. Go to project dir and create new virtualenv: `virtualenv venv`
13. Activate your virtualenv: `.\venv\Scripts\activate`
14. Install project dependencies: `pip install -r .\requirements.txt`
15. Set up neo4j credentials to the environment variables: 
    `$env:NEO4J_USERNAME = "neo4j"` and `$env:NEO4J_PASSWORD = "SomeNeoPass"`
16. Run application: `python nosql-2017-git_source_tree_search.py`
17. Remove environment variables: `Remove-Item Env:\NEO4J_USERNAME` and 
    `Remove-Item Env:\NEO4J_PASSWORD`
18. Of course, you can just use your preffred IDE and run project from here, 
    for example:
    ![Screenshot](/resources/runconfigurations.png)

### Example Debian 9 installation:

**TODO:** some text. :(
