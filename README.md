# counter-demo
Demonstrates durable execution by using a simple counter in Python (before and after Temporal)

# Setup Steps (Do Before the Demo)

1. Create a virtual environment: `python -m venv .`
2. Activate virtual environment: `source ./bin/activate`
3. Install Temporal SDK: `pip install temporalio`

# Demonstrate Volatile Execution (AKA "Before Temporal")
1. Open `counter.py` in an editor and briefly explain the code
2. Execute it by running `python counter.py`
3. While it is running, press Ctrl-C in the terminal to terminate it
4. Point out the last number displayed and ask the audience what 
   number they expect to see upon restarting it. Most programmers
   should recognize that it will begin with 1, since all state from
   the previous execution is lost, though non-technical people may
   be surprised by this.
5. Repeat step 2 to restart the execution, point out that it began
   with 1 even though that repeats what was done before. Explain 
   why this would be bad (e.g., it's inefficient and could have a
   detrimental effect in some cases, such as when a customer gets
   charged twice for a single purchase).

# Demonstrate Durable Execution (AKA "With Temporal")
Note that there is no need to show the code, although technical 
audiences may benefit from seeing the Workflow code (in the 
`businesslogic.py` file), since the code is not very different
than what they saw before (though there are a few small changes)

1. Run the Temporal Service: `temporal server start-dev` (optionally 
   add the `--db-filename` option, so that the state of Workflow 
   Executions isn't lost if the service crashes).
2. Run the Worker: `python worker.py` (and be sure to explain what 
   a Worker is)
3. Run the Starter: `python start-execution.py 10` (and before you
   start it, be sure to explain that this initiates execution the 
   Workflow that does the counting and the number you want to count 
   to is being passed as input to it)
4. Switch back to the terminal where the Worker is running and 
   press Ctrl-C to terminate the process. Point out the last number
   displayed and ask what the next number will be. Unlike the volatile 
   execution shown before, this is a durable execution because of 
   Temporal, so it's going to resume where it left off as if nothing
   had happened.


