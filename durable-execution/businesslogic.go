package example 

import (
	"go.temporal.io/sdk/workflow"
	"fmt"
	"time"
)

func CounterWorkflow(ctx workflow.Context, limit int) error {
	logger := workflow.GetLogger(ctx)
	logger.Info("Executing Workflow")

	number := 1

	for number <= limit {
		logger.Info(fmt.Sprintf("Current Number: %d", number))
		number = number + 1
		workflow.Sleep(ctx, time.Second*1)
	}
	return nil
}
