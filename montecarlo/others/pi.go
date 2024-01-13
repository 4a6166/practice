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

  const points = 1_000_000
  fmt.Printf("Estimating pi with %d point(s).\n\n", points)

  var success int
  for i := 0; i < points; i++ {
    x, y := getRandomPoint()

    if x*x + y*y <= 1 {
      success++
    }
  }

  piApprox := 4.0 * float64(success) / float64(points)
  errorPct := 100.0 * math.Abs(piApprox-math.Pi) / math.Pi

  fmt.Printf("Estimated pi: %9f \n", piApprox)
  fmt.Printf("pi: %9f \n", math.Pi)
  fmt.Printf("Error: %9f%%\n", errorPct)
}

// not sure why the math around the rand float. got error of 0.02% without, compared to Gabriel's published 0.04%
// func getRandomPoint() (x, y float64) {
//   x = 2.0 * rand.Float64() - 1.0
//   y = 2.0 * rand.Float64() - 1.0
//   return x, y
// }

func getRandomPoint() (x, y float64) {
  x = rand.Float64()
  y = rand.Float64()
  return x, y
}

