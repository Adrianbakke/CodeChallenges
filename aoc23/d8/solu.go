package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readFileIntoArray(filename string) ([][]int, error) {
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return [][]int{}, err
	}
	defer file.Close() // Close the file when the function exits

	// Create a scanner to read the file line by line
	scanner := bufio.NewScanner(file)

	// Read and process each line
	var res = [][]int{}
	for scanner.Scan() {
		line := scanner.Text()
		sarr := strings.Split(line, "")

		var tmp = []int{}
		for _, i := range sarr {
			j, err := strconv.Atoi(i)
			if err != nil {
				panic(err)
			}
			tmp = append(tmp, j)
		}
		res = append(res, tmp)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}
	return res, err
}

func main() {
	filename := "input.txt"
	content, err := readFileIntoArray(filename)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	fmt.Println("File content:")
	fmt.Println(content[0])
}
