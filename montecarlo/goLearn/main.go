package main

import (
  "fmt"
  "exampleTest/mypackage"
)

func main() {
  value := mypackage.DoMagic()
  fmt.Printf("%s", value)
}
