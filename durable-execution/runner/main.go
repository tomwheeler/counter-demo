package main

import (
	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/worker"
	"context"
	example "example/durable-execution"
	"log"
)

const TASK_QUEUE_NAME = "counter-tasks" 

func main() {
	c, err := client.Dial(client.Options{})
	if err != nil {
		log.Fatalln("Unable to create client", err)
	}
	defer c.Close()

	w := worker.New(c, TASK_QUEUE_NAME, worker.Options{})

	w.RegisterWorkflow(example.CounterWorkflow)

	err = w.Start()
	if err != nil {
		log.Fatalln("Unable to start worker", err)
	}

	options := client.StartWorkflowOptions{
		ID:        "counter-workflow",
		TaskQueue: TASK_QUEUE_NAME,
	}

    we, err := c.ExecuteWorkflow(context.Background(), options, example.CounterWorkflow, 10)
	if err != nil {
		log.Fatalln("Unable to execute workflow", err)
	}

	err = we.Get(context.Background(), nil)
	if err != nil {
		log.Fatalln("Unable get workflow result", err)
	}
	w.Stop()
}

