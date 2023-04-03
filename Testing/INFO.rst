# Benchmarking with TimeIt

- Benchmarking, means comparing two code snippets to see which is executes faster. 
- Time and memory are often not a concern to use, but it is to some Python Programmers.
- Time tests should be run multiple times
- Tests should consider the context in which they will run.
- Benchmarking is something of an art.

# Unit Testing: The PyTest Module
- Python tests are Python programs that test other Python programs
- py.test looks for scripts functions/methods called test_
- After calling function or method, assert something is true
- with pytest.raises() to assert that an exception is raised
- setup_class() method to do test prep
- teardown_class() method to clean up after tests
- to run use: pytest test_apps.py