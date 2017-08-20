package main
import "net/http"
import "fmt"
import "os"
import "io/ioutil"


func main() {

    var xx = os.Args[1]
    resp, err := http.Get(xx)
    if err != nil {
        os.Exit(-1)
    }
    
    defer resp.Body.Close()
    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        os.Exit(-1)
    }
 
    fmt.Print(string(body))

}