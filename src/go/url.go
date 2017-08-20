package main

import "os"
import "fmt"
import "net"
import "net/url"



func main() {
    var xx = os.Args[1]
    u, err := url.Parse(xx)
    if err != nil {
        os.Exit(-1)
    }

    host, port, _ := net.SplitHostPort(u.Host)
    if (port == ""){
        host = u.Host
    }
    fmt.Printf("scheme=%s, host=%s, port=%s\n", u.Scheme, host, port);

}
