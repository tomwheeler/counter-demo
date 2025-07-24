# counter-demo
Demonstrates durable execution by using a simple counter in Python (before and after Temporal)

# Setup Steps (Do Before the Demo)

1. Create a virtual environment: `python -m venv .`
2. Activate virtual environment: `source ./bin/activate`
3. Install Temporal SDK: `pip install temporalio`

# Demonstrate Normal Execution (AKA "Before Temporal")
1. `cd normal-execution`
2. Open `businesslogic.py` in an editor and briefly explain the code, 
   and then explain `start-execution.py`, which calls it.
3. Execute by running `python start-execution.py`
4. While it is running, press Ctrl-C in the terminal to terminate it
5. Point out the last number displayed and ask the audience what 
   number they expect to see upon restarting it. Most programmers
   should recognize that it will begin with 1, since all state from
   the previous execution is lost, though non-technical people may
   be surprised by this.
6. Repeat step 2 to restart the execution, point out that it began
   with 1 even though that repeats what was done before. Explain 
   why this would be bad (e.g., it's inefficient and could have a
   detrimental effect in some cases, such as when a customer gets
   charged twice for a single purchase).

# Demonstrate Durable Execution (AKA "With Temporal")
Note that there is no need to show the code, although technical 
audiences may benefit from seeing the Workflow code (in the 
`businesslogic.py` file), since the code is not very different
than what they saw before (though there are a few small changes)

1. `cd durable-execution`
2. Run the Temporal Service: `temporal server start-dev` (optionally 
   add the `--db-filename` option, so that the state of Workflow 
   Executions isn't lost if the service crashes).
3. Run `python start-execution.py` (this launches a Worker, submits 
   the Workflow for execution, and shuts down the Worker when that 
   execution is complete.
4. Press Ctrl-C to terminate the process while the count is underway. 
   Point out the last number displayed and ask what the next number 
   will be. Unlike the normal execution shown before, this is a 
   durable execution because of Temporal, so it's going to resume 
   where it left off as if nothing had happened.


# Teardown Steps (Do After the Demo)

1. Deactivate the virtual environment: `cd ..; deactivate`
