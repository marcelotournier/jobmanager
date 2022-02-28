"""
This is an example of how to instantiate a very
simple python "job manager" using only the concurrent.futures
library, without any external dependencies.
"""
from concurrent.futures import ThreadPoolExecutor
from collections import namedtuple


class JobManager:
    """
    Simple abstraction to run functions in a linear or concurrent queue.
    
    Example:
    from jobmanager import JobManager

    # creating the function to run 
    def div(a, b): 
        return a/b

    # Constructing a manager
    mgr = JobManager()

    # submitting a task
    mgr.submit(id="mk I", func=div, args={"a":1,"b":2})
    mgr.submit(id="test", func=div, args={"a":2,"b":2})
    mgr.submit(id="bad task", func=div, args={"a":1,"b":0})
    mgr.submit(id="blahblah", func=div, args={"a":2,"b":5})

    # Checking the queue
    mgr.queue

    # Getting results for a task from queue
    mgr.queue[-1].future.result()
    """
    _Task = namedtuple("Task", ["id", "function", "future"])
    
    def submit(self, id, func, args):
        """
        Submits a job to the queue.
        :param `id`: a string identifier for your job
        :param `func`: function to run
        :param `args`: a dictionary with the function arguments to run 
        """
        return self.queue.append(self._Task(id, func, self.executor.submit(func, **args)))

    def __init__(self, max_workers=1):
        """
        Starts the job manager.
        :param `max_workers`: Maximum amount of concurrent tasks running in the queue.
            You can use any int value > 1 to use concurrent jobs in different threads
        """
        self.queue = []
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
