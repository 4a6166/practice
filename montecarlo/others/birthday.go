// from https://ggcarvalho.dev/posts/montecarlo/
// modified to accept input

// In a group of N people, randomly assign birthday and mark success for each time two are the same.
// Divide by number of trials to get probability.

package main

import (
  "bufio"
  "os"
  "fmt"
  "math/rand"
  "time"
  "strconv"
  "strings"
)

func main() {
  rand.Seed(time.Now().UnixNano())

  const trials = 1_000_000
  success := 0

  reader := bufio.NewReader(os.Stdin)
  fmt.Println("Enter number of people:")

  numPeople_input, _ := reader.ReadString('\n')
  numPeople_input = strings.Replace(numPeople_input, "\n", "", -1) //required for some reason

  // If this was a real program, I would have to do something to deal with the input-calc lag allowing too many entries
  // if len(numPeople_input) > 1 {
  //   os.Stdin.SetDeadline(time.Now())
  // }
  numPeople, err := strconv.Atoi(numPeople_input)

  if err != nil {
    fmt.Print("bad input")
    return
  }

  // each loop is a separate MC simulation
  for i:= 0; i < trials; i++ {
    bdays := genBdayList(numPeople)
    uniques := uniqueSlice(bdays)

    // uniques is a list of each unique birthday from the bday list
    if len(uniques) != numPeople {
      success++
    }
  }

  probability := float64(success) / float64(trials)
  fmt.Printf("The probability of at least 2 people in a group of %d sharing a birthday is %.2f%%\n", numPeople, probability*100)

}

// fairly common algorithm to generate a list of unique items from another list
func uniqueSlice(s []int) []int {
  keys := make(map[int]bool)
  list := []int{}
  for _, entry := range s {
    if _, value := keys[entry]; !value {
      keys[entry] = true
      list = append(list, entry)
    }
  }
  return list
}

//generates a list of birthdays 
func genBdayList(n int) []int {
  var bdays = make([]int, n)
  for i := 0; i < n; i++ {
    bdays[i] = rand.Intn(365) //ignoring leap years
  }
  return bdays
}
