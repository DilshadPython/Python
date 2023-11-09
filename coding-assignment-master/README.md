# Coding assignment

This coding exercise allows us to evaluate your basic knowledge and thought
process.

Please complete as much of the assignment as you can. If you are unable or do
not have the time to complete the whole assignment, please just send us as much
as you have managed to complete.

For all of the tasks below, we'd like to see an answer in Python. However if
you would rather provide a similar solution in another language that better
shows your programming facility, we will be happy to review it instead.

# Tasks

Launchpad uses "Teams" to group people.  People may be members of teams, and
teams may also be members of teams.  Because teams can be used in most ways
that People can, Teams and People are both represented through the Person
class.

The Person class (available in `person.py`) has these attributes:

- `id` (a unique integer)
- `displayname` (a string)
- `is_team` (a boolean)
- `members` (a list for teams, None for non-team persons)


## Task one

Write a function that accepts a person and a list of all
people/teams and returns a list of all the teams of which that
person is a member. You can import the "people" list from
`data1.py` to use as example data when writing your function.

This code (where your function is named `exercise1`)...

``` python
>>> import data1
>>> print [t.displayname for t in exercise1(data1.alice, data1.people)]
```

...should result in this being printed:

``` python
['The A-Team', 'The C-Team']
```

## Task two

Does your function produce the same results as expected in
question 1 when you pass it the "people" list from `data2.py`
and alice (also from `data2.py`)?  If not, modify your function
so that it works correctly given that data.

## Task three

Write a function that gets all the people (not teams) who are
direct and indirect members of a team.  Using `data2.py`, this code
(where your function is named `get_people`)...

``` python
>>> import data2
>>> print sorted(p.displayname for p in get_members(data2.c_team))
```

...should result in this being printed:

``` python
['Alice', 'Bob', 'Carlos', 'Charlie', 'Eve']
```

Now look at `data3.py`.  Figure out what the correct answer should be for
`get_members(data3.c_team)`, and make sure your function performs as you
expect.

### Returning the assignment

Please create a git repository from your work and return this repository in a
zipped tar archive.

