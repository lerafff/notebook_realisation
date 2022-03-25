# Notebook realisation

___We had a task to make our own realisation of Notebook by classes___
```python
I have 3 classes: 
1. Note
2. Notebook
3. Menu
```


## Class Note
The class gives all info about note
Here we have such a functions:
```python
def __init__(self, mem, date, tag)
def match(self, to_find) - finds matches in all info about note
```

## Class Notebook
The class gives info about notebook and includes all needed functions
Here we have such a functions:
```python
def __init__(self)
def create_note(self, mem, date, tag) - creates new note
def show_notes(self) - returns all notes in Notebook
def search(self, filter) - search in all info some filter
def modify_memo(self, note_id, memo) - enable user to modify memo in the note
def modify_tags(self, note_id, tag) - enable user to modify tag in the note
```
## Class Menu
Class Menu includes static methods and interaction with user
Here we have such a functions:
```python
@staticmethod def try_if_okay(notebook) - checks if input of user was int and if it is less than len of notes
@staticmethod def try_if_enough(notebook) - checks if notebook have some notes or it is empty
def menu(self, notebook) - all interaction with user and cool output
```
## main()
Little function to start program
