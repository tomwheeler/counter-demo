package main

import (
	"log"
	"time"
)

func countTo(limit int) {
	number := 1

	for number <= limit {
		log.Println("Current number is:", number)
		number = number + 1
		time.Sleep(time.Second * 1)
	}
}

func main() {
	countTo(10)
}
