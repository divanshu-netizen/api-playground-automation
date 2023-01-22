# api-playground-automation
API automation of Best Buy API Playground APIs using Python, pytest, requests &amp; json libraries


Prerequisites:

1. Python should be installed 
2. PIP should be installed
3. IDE like PyCharm
4. Best Buy API Playground App should be running locally on your system (https://github.com/BestBuy/api-playground)

Few of the APIs under Categories were automated:

i) Retrieve categories (GET method)
ii) Create a category (POST method)
iii) Delete a category (DELETE method)
iv) Retrieve a single category, filtering Categories with single Category id ( GET method)


Setup:

1. Go to the Terminal or Command Prompt and run:

``` https://github.com/divanshu-netizen/api-playground-automation.git ```

2. Run these commands to install needed packages, libraries

``` pip install requests ```

``` pip install pytest ```

``` pip install pytest-html ```

``` pip install jsons ```

3. Go to the repo folder and run this command 

``` pytest --html=report.html ```

this will run all the Test Cases &  create a report, report.html file in the directory containing test summary which can be viewed on the browser of your choice 
