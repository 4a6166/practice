package main

import (
  "bufio"
  "fmt"
  "os"
  "strings"
)

func main() {
  readline();
  fmt.Println("")

  loopInput()
  fmt.Println("")

  readSingleChar()
  fmt.Println("")

  fmt.Println("scanner time")
  scanner()
  fmt.Println("")

  fmt.Println("It's finally over!")
}

func readline() {
  reader := bufio.NewReader(os.Stdin)
  fmt.Print("write something: ")

  test, _ := reader.ReadString('\n')

  // convert CRLF to LF
  test = strings.Replace(test, "\n", "", -1) //required for some reason

  fmt.Println(test)

}

//Loop over input
func loopInput() {

  fmt.Println("say 'hi' to exit")
  reader := bufio.NewReader(os.Stdin)

  for {
    fmt.Print("-> ")
    text, _ := reader.ReadString('\n')
    // convert CRLF to LF
    text = strings.Replace(text, "\n", "", -1)

    if strings.Compare("hi", text) == 0 {
      fmt.Println("hello, Yourself")
      return
    }

  }
}

// read single char
func readSingleChar() {
  fmt.Println("type as much as you want but it should only read a single char")
  fmt.Println("A or B are good options")
  reader := bufio.NewReader(os.Stdin)
  char, _, err := reader.ReadRune()

  if err != nil {
    fmt.Println(err)
  }

  // print out the unicode value i.e. A -> 65, a -> 97
  fmt.Println(char)

  switch char {
  case 'A':
    fmt.Println("A Key Pressed")
    break
  case 'a':
    fmt.Println("a Key Pressed")
    break
  default:
    fmt.Println("You didn't hit 'A' or 'B'")
    break
  }
}

// use Bufio's scanner
func scanner() {
  scanner := bufio.NewScanner(os.Stdin)
  lineread := 0
  input := ""

  for scanner.Scan() {
    input += scanner.Text() + "\n"
    lineread++

    if lineread > 3 {
      fmt.Println("Ok. That's enough.")
      fmt.Println("Here's what you wrote:")
      fmt.Println(input)
      return
    }
  }
}
