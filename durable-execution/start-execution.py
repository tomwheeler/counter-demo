import asyncio
import logging
import sys

from temporalio.client import Client

from businesslogic import CountingWorkflow

# This program starts the Workflow execution
async def main():
    client = await Client.connect("localhost:7233")

    if len(sys.argv) != 2:
	    print("Must specify limit argument!")
	    sys.exit(1)

    limit = int(sys.argv[1])
    await client.execute_workflow(
        CountingWorkflow.run,
        limit,
        id="counting-workflow-id",
        task_queue="counting-task-queue",
    )
    print("Workflow complete")



if __name__ == "__main__":
    asyncio.run(main())
