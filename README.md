Paranuara API developed using Python 3, Flask and MongoDB

### Installation

1. Create a new Python virtual environment
1. Run `pip install -r requirements.txt` to install all dependencies
1. Populate the database:

```
mongoimport --db test_db --collection people data/people.json --jsonArray
mongoimport --db test_db --collection companies data/companies.json --jsonArray
```

### Running the app

```
python main.py
```

### API Examples

1. Get all the employees working in company with ID `1`:

```
curl -i http://localhost:5000/api/company/1/employees
```

1. Get information about two people, ID `1` and `2` and list their common friends:

```
curl -i http://localhost:5000/api/people/1/2
```


1. Get person details

```
curl -i http://localhost:5000/api/person/1
```
