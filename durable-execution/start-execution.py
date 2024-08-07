import asyncio
import logging
import sys
from datetime import timedelta

from temporalio.client import Client, WorkflowExecutionStatus
from temporalio.worker import Worker
from temporalio import exceptions

from businesslogic import CounterWorkflow


async def main():
    # Customize the logger output to match the print statement
    logging.basicConfig(
        level=logging.WARN,
        format="%(message)s",
    )

    try:
        client = await Client.connect("localhost:7233")
        async with Worker(
            client, 
            task_queue="counter", 
            workflows=[CounterWorkflow],
        ):
            result = await client.execute_workflow(
                CounterWorkflow.run,
				10, # value of 'limit' argument
                id="counterwf",
                task_queue="counter",
                task_timeout=timedelta(seconds=3),
            )
    except asyncio.exceptions.CancelledError:
        sys.exit(0)
    except exceptions.WorkflowAlreadyStartedError as err:
        async with Worker(
            client, 
            task_queue="counter", 
            workflows=[CounterWorkflow]
        ):
            workflow_handle = client.get_workflow_handle("counterwf")
            description = await workflow_handle.describe()
            while description.status != WorkflowExecutionStatus.COMPLETED:
                description = await workflow_handle.describe()
                await asyncio.sleep(1)
    # Catch Ctrl-C so we can limit excessive output in terminal
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
