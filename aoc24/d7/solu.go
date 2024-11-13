package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Dir struct {
	name    string
	parent  *Dir
	child   []*Dir
	content [][]string
}

func NewDir(name string, parent *Dir) *Dir {
	return &Dir{
		name:    name,
		parent:  parent,
		child:   []*Dir{},
		content: [][]string{},
	}
}

func (d *Dir) Sz() int {
	res := 0
	for _, c := range d.content {
		if len(c) > 0 {
			value, err := strconv.Atoi(c[0])
			if err == nil {
				res += value
			}
		}
	}
	for _, c := range d.child {
		res += c.Sz()
	}
	return res
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	input := []string{}
	for scanner.Scan() {
		input = append(input, scanner.Text())
	}

	if len(input) > 0 {
		input = input[1:]
	}

	testInput := input
	cdir := NewDir("/", nil)
	c1dir := cdir

	res := []int{}

	for len(testInput) > 0 {
		line := testInput[0]
		testInput = testInput[1:]
		parts := strings.Split(line, " ")
		if parts[0] == "$" {
			if parts[1] == "cd" {
				if parts[2] == ".." {
					c1dir = c1dir.parent
				} else {
					for _, c := range c1dir.child {
						if c.name == parts[2] {
							c1dir = c
							break
						}
					}
				}
			}
			continue
		}

		tp := parts[0]
		name := parts[1]
		if tp == "dir" {
			c1dir.child = append(c1dir.child, NewDir(name, c1dir))
		} else {
			c1dir.content = append(c1dir.content, []string{tp, name})
		}
	}

	NEEDED_SPACE := 30000000
	USED_SPACE := 70000000 - cdir.Sz()

	var rec func(d *Dir)
	rec = func(d *Dir) {
		sz := d.Sz()
		// if sz <= 100000 { // solu1
		//     res = append(res, sz)
		// }
		if USED_SPACE+sz >= NEEDED_SPACE { // solu2
			res = append(res, sz)
		}
		if len(d.child) > 0 {
			for _, c := range d.child {
				rec(c)
			}
		}
	}

	rec(cdir)

	fmt.Println(res)
	minVal := res[0]
	for _, val := range res {
		if val < minVal {
			minVal = val
		}
	}
	fmt.Println(minVal)
}
