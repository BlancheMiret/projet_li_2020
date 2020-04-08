# Projet Linguistique 2020

This is a project concerning search engines.



### Adding documents to DataBase

#### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install wikipedia API

```bash
pip3 install wikipedia_api
```

#### Usage

```bash
./widi_copy.py 'name_of_wikipedia_page' 'name2' ...
```

The script manages ambiguous names and retrieve the one corresponding to a book if existing.

### Exemple

```bash
./wiki_copy.py 'qslkfj' 'Citadelle' 'Vol de nuit'
```

Answer :
```
qslkfj Wikipedia page does not exist.
The file Citadelle was correctly written.
The file Vol de nuit was correctly written.
```
You can see that the file citadelle refers to the book by Antoine de Saint-Exupery, and not the construction.

## Authors

* **Blanche Miret**
* **Thach Linh Tran**
