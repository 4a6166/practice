// from https://ggcarvalho.dev/posts/montecarlo/

package main

import (
  "fmt"
  "math"
  "math/rand"
  "time"
)

func main() {
  rand.Seed(time.Now().UTC().UnixNano())

  const simulations = 10_000_000
  fmt.Printf("Estimating the probability of winning by switching doors with %d game(s).\n\n", simulations)

  var success int
  printResults := false
  results := []string{}

  for i:=0; i< simulations; i++ {
    var guestWon, result = runSim()
    results = append(results, result)
    if guestWon == 1 {
      success++
    }
  }
    
  probability := float64(success)/float64(simulations)
  const theoryValue = 2. / 3.
  errorPct := 100. * math.Abs(probability - theoryValue)/theoryValue

  fmt.Printf("Estimated probability: %9f\n", probability)
  fmt.Printf("Theoretical value: %9f\n", theoryValue)
  fmt.Printf("Error: %9f\n", errorPct)

  if printResults {
    fmt.Println(results)
  }

}

func runSim()(int, string) {

  doors := [3]string{"goat", "goat", "prize"}

  guestDoor := rand.Intn(3)

  remainingDoors := []string{}
  for index, element := range doors {
    if index != guestDoor {
      remainingDoors = append(remainingDoors, element)
    }
  }

  // Monty removes one of the remaining two doors, which is guaranteed to have a goat

  // result is correct uses logic that we would not necessarily know if we were doing this as part of a business process
  // if remainingDoors[0] == "prize" || remainingDoors[1] == "prize" {
  //   return 1
  // }

  // This is slower and can be condensed with logic, but better follows the "business" process of the game
  if remainingDoors[1] == "goat" {
    remainingDoors = remainingDoors[:1]
  } else if remainingDoors[0] == "goat" {
    remainingDoors[0] = remainingDoors[1]
    remainingDoors = remainingDoors[:1]
  }

  if remainingDoors[0] == "prize" {
    return 1, remainingDoors[0]
  } else {
    return 0, remainingDoors[0]
  }
}
