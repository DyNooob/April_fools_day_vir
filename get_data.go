package main


import (
	"bufio"
	"fmt"
	"golang.org/x/net/html/charset"
	"golang.org/x/text/encoding"
	"golang.org/x/text/transform"
	"io"
	"io/ioutil"
	"net/http"
)

func main() {
	resp,err := http.Get("你的api")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	e := DetermineEncoding(resp.Body)
	utf8Reader := transform.NewReader(resp.Body,e.NewDecoder())
	if resp.StatusCode == http.StatusOK {
		all,err := ioutil.ReadAll(utf8Reader)
		if err != nil {
			panic(err)
		}
		fmt.Printf("%s\n",all)
	}
}

func DetermineEncoding(r io.Reader)encoding.Encoding  {
	bytes,err := bufio.NewReader(r).Peek(1024)
	if err != nil{
		panic(err)
	}
	encode,_,_ := charset.DetermineEncoding(bytes,"")
	return encode
}
