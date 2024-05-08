import asyncio

from temporalio import workflow

@workflow.defn
class CounterWorkflow:
    # Make the logging output look more like that of print()
    workflow.logger.workflow_info_on_message = False

    @workflow.run
    async def run(self) -> None:
        limit = 10
        workflow.logger.info("*** Starting Workflow - Will count to %d" % limit)

        number = 1
        while number <= 10:
            workflow.logger.info(number)
            number = number + 1
            await asyncio.sleep(1)

        workflow.logger.info("*** Finished workflow - Counted to %d" % limit)
