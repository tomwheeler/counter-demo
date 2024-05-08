package example

import (
	"log"
	"strings"
)

type MinimalLogger struct {}

func NewMinimalLogger() *MinimalLogger {
	return &MinimalLogger{}
}

func (ml *MinimalLogger) Debug(msg string, keyvals ...interface{}) {
	log.Println(msg)
}

func (ml *MinimalLogger) Info(msg string, keyvals ...interface{}) {
	if strings.Contains(msg, "NewTimer") {
		return
	}
	log.Println(msg)
}

func (ml *MinimalLogger) Warn(msg string, keyvals ...interface{}) {
	log.Println(msg)
}

func (ml *MinimalLogger) Error(msg string, keyvals ...interface{}) {
	log.Println(msg)
}
