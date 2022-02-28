# Simple jobmanager

Very simple concurrent job manager for Python to run functions in concurrency.

Another good use case is to safely catch exceptions in multiple function runs.

Built as a thin wrapper for `concurrent.futures`

### Installing
pip install git+https://github.com/marcelotournier/jobmanager.git

### Using
```python3
from jobmanager import JobManager

# Constructing a manager
mgr = JobManager()

# Making our function to run
def div(a,b):
    return a/b

# Submitting some jobs
mgr.submit("one",div,{"a":1, "b":2})
mgr.submit("other",div,{"a":3, "b":2})
mgr.submit("another",div,{"a":3, "b":0})

# Checking the queue
mgr.queue
"""
Out[]:

[Task(id='one', function=<function div at 0x7fbd820d50d0>, future=<Future at 0x7fbd821d0970 state=finished returned float>),
 Task(id='other', function=<function div at 0x7fbd820d50d0>, future=<Future at 0x7fbd818be6a0 state=finished returned float>),
 Task(id='another', function=<function div at 0x7fbd820d50d0>, future=<Future at 0x7fbd820f2220 state=finished raised ZeroDivisionError>)]
"""

# Getting results
mgr.queue[0].future.result()

# Out[]: 0.5

# This will get an exception
mgr.queue[-1].future.result()
```
