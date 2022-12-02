package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func toNum(letter string) int {
	switch letter {
	case "X":
		fallthrough
	case "A":
		return 0
	case "Y":
		fallthrough
	case "B":
		return 1
	case "Z":
		fallthrough
	case "C":
		return 2
	default:
		return 900000
	}
}

func decide(opponent string, outcome string) string {
	//     A   B   C
	// L   2   0   1
	// d   0   1   2
	// W   1   2   0
	decideMatrix := [3][3]string{
		{"Z", "X", "Y"},
		{"X", "Y", "Z"},
		{"Y", "Z", "X"},
	}
	return decideMatrix[toNum(outcome)][toNum(opponent)]
}

func calculateScore(opponent string, you string) int {
	//     A   B   C
	// X   d   L   W
	// Y   W   d   L
	// Z   L   W   d
	winLossMatrix := [3][3]int{
		{3, 0, 6},
		{6, 3, 0},
		{0, 6, 3},
	}
	return winLossMatrix[toNum(you)][toNum(opponent)] + toNum(you) + 1
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal()
	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	score := 0

	for scanner.Scan() {
		s := strings.Split(scanner.Text(), " ")
		score += calculateScore(s[0], decide(s[0], s[1]))
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "reading standard input:", err)
	}
	file.Close()
	fmt.Println(score)
}
