import asyncio
import logging
import sys

from temporalio.client import Client
from temporalio.worker import Worker

from businesslogic import CountingWorkflow

async def main():
    if len(sys.argv) != 2:
        print("Must specify limit argument!")
        sys.exit(1)

    limit = int(sys.argv[1])

    # Customize the logger output to match the print statement
    logging.basicConfig(
        level=logging.INFO,
        format= '%(message)s',
    )

    # Catch Ctrl-C so we can limit excessive output in terminal
    try:
        client = await Client.connect("localhost:7233")
        worker = Worker(
             client,
             task_queue="counter-demo",
             workflows=[CountingWorkflow],
        )

        await worker.run()
        await client.execute_workflow(
            CountingWorkflow.run,
            limit,
            id="counting-workflow-id",
            task_queue="counter-demo",
        )

        handle = client.get_workflow_handle(  
            workflow_id="counting-workflow-id",
        )
        results = await handle.result()
    except asyncio.exceptions.CancelledError:
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)



if __name__ == "__main__":
    asyncio.run(main())

