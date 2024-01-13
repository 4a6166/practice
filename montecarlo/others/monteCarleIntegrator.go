package monteCarlo

type Export struct {
}

func (c Export) Integrate(f func(float64) float64, a float64, b float64, n int) float64 {
   var s float64
   for i := 0; i < n; i++ {
     ui := rand.Float64()
     ux := a + (b-a)*ui
     s += f(xi)
   }

   s = ((b - a) / float64(n) *s
   return s
}
