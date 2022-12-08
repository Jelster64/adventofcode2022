#!/bin/zsh

today=6
here=$PWD
frens="$here/../aocfrens"

jelle() {
    cd $here
    cd day$1
    echo "Jelle:"
    [ $1 -ne 2 ] && for pythonfile in *.py; do
        time python $pythonfile >/dev/null
    done
    cd ..
}

stan() {
    cd "$frens/stan"
    echo "Stan:"
    for pythonfile in day$1/*.py; do
        time python $pythonfile >/dev/null
    done
}

jens() {
    cd "$frens/jens"
    echo "Jens:"
    time ./day$1 >/dev/null
}

cd "$frens/jens"
for day in $(seq 1 $today); do
    ghc -dynamic day$day.hs
done
rm *.hi *.o
cd "$here"

for day in $(seq 1 $today); do
    echo "Day $day"
    jelle $day
    stan $day
    jens $day
    echo "\n"
done


