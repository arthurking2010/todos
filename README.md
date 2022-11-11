# TODOs

This project is carried out to exemplify a good structure of the directory, programs and tests in their standard places and to be able to perform packaging


### Pre-requisitos 📋

1. Download the file: todos-0.1.0-py3-none-any.whl
2. Copy that file in your working directory
3. Execute this command in your terminal in the work directory

```
pip install dist/todos-0.1.0-py3-none-any.whl
```
And you'll see all the libraries needed will be installed

Next we will see the commands that can be used with this package to handle the "to-do" lists

Creating a new list

```
python -m todos create --listname <"listname">
```

Showing the existing lists

```
python -m todos list
```

Showing the tasks in a list

```
python -m todos show -ln <"listname">
```

Adding one task to a list

```
python -m todos add -ln <"listname"> -tn <"taskname"> -d <"description"> -o <"owner">
```

Updating one task in a list

```
python -m todos update -ln <"listname"> -i  <"taskid"> -f <"field"> -c <"new_value">
```

Listing all the commands
```
python -m todos --help
```


## Built with 🛠️

Python 3.10

Poetry
