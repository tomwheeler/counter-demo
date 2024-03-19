import asyncio
import logging
import sys

from temporalio.client import Client
from temporalio.worker import Worker

from businesslogic import CountingWorkflow


async def main():
    # Customize the logger output to match the print statement
    logging.basicConfig(
        level=logging.INFO,
        format= '%(message)s',
    )


    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="counting-task-queue",
        workflows=[CountingWorkflow],
    )

    # Catch Ctrl-C so we can limit excessive output in terminal
    try:
        await worker.run()
    except asyncio.exceptions.CancelledError:
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)



if __name__ == "__main__":
    asyncio.run(main())
