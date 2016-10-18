## 13F Scraper Readme

13F Scrapper is a command line application that inputs a company's CIK or ticker and creates a tab delineated text file of the company's most recent 13 F report on Edgar.

#### Installation/ Dependancies

The application requires Python 3.0 or later and the bs4 module. Dependancies can be installed by running

```
 pip install --upgrade -r requirements.txt
```

from the project's root directory.

#### Running Application
From the project's root directory, run (for example)

```
python main.py 0001166559
```
with any ticker or CIK number. If it is run with no argument, i,e,
```
python main.py
```
a random ticker will be chosen from a static list. The new file will be created in the project's "outputs" directory.

The program's unit tests can be running by running

```
python tests.py Tests
```

#### Design

The core behavior of the program runs functionally/declaratively in main.py, which exucutes each command and stops the program if and when an error emerges. The functions are stored in two modules, crawl_funcs and scrape_funcs, which contain the behavior for crawling Edgar's site to find the appropriate xml file, and scraping the xml to create a new file, respectively.

This structure was beneficial for several reasons. For one, the program several very different functionalities (web scraping, file writing, core python), so separating the concerns modularly allows each component to be easily tested in isolation and completely altered if the need arises.

The possibility of different formats of 13F xml files is unlikely to be problematic, since the file writing procedure should, in theory, be able to recursively search through any xml tree. If, however, a file's xml structure proves to be an issue, the file writing functions can be altered without affecting any of the other behaviors of the application. For example, if an old xml format lists the information linearly instead of having each investment nested without its own infoTable element (for some reason), the file writer would be altered to detect this upfront and conditionally run a different file writing routine.



 Company's with available 13F filings can be found here:
https://www.sec.gov/cgi-bin/browse-edgar?company=&CIK=&type=13F&owner=include&count=40&action=getcurrent
