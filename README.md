# Projet Linguistique 2020

This is a project concerning search engines. To get more information about the method, take a look at the project report.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install wikipedia API and sklearn

```bash
pip3 install wikipedia_api
```

```bash
pip3 install sklearn
```

### Usage

#### Adding documents to DataBase

```bash
./wiki_copy.py "name_of_wikipedia_page" ["name2"] [...]
```

The script manages ambiguous names and should retrieve the one corresponding to a book if existing.

##### Example

```bash
./wiki_copy.py "qslkfj" "Citadelle" "L'âge de raison"
```

Answer :
```
qslkfj Wikipedia page does not exist.
The file Citadelle was correctly written.
The file Vol de nuit was correctly written.
```
You can see that the file citadelle refers to the book by Antoine de Saint-Exupery, and not the construction.

#### Searching into DataBase

```bash
./research.py "keywork1" ["keyword2"] [...]
```
or to use second method :

```bash
./v2_research.py "keywork1" ["keyword2"] [...]
```

##### Example

```bash
./research.py victor hugo
```

Answer :
```
The documents corresponding to your research are :
L'étranger : 0.9948775137905812
Les Fleurs Du Mal : 0.9948775137905812
Notre Dame De Paris : 0.9948775137905812
Les Misérables : 0.9943538524494836
Hernani : 0.9707624692005832
```

## Authors

* **Blanche Miret**
* **Thach Linh Tran**
