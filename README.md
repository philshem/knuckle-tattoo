# knuckle tattoo - a recursive word search puzzle game

generating the perfect knuckle tattoo with code and open data.

blog post -- coming soon!

## get the code

```
git@github.com:philshem/knuckle-tattoo.git
cd knuckle-tattoo/
```

code requires python3 but otherwise no non-standard libraries

## run the code

```
python3 find_knuckle_tattoos.py $input > $output
```

for example, with the input file from the [most common 20k word list](https://github.com/first20hours/google-10000-english):

```
wget https://raw.githubusercontent.com/first20hours/google-10000-english/master/20k.txt
python3 find_knuckle_tattoos.py 20k.txt > 20k.csv
```

## how to cheat

Once you've generated the `20k.csv` file, you can do a lookup to find solutions to the first published puzzles.

```
echo "A E E K N O P S
A B D D E E I T
B E E E F R T U
A E E I L L R S
A D E F H I L T
E E L N O O P S
A E L N O S S T
D E E E N R T U
D E E F I L S T
A E E I L L M S
A D H K L O O Y
E E G I K N N S
A E E I L L S S
D E I I K N S T" > puzzle-set.txt


grep -f puzzle-set.txt 20k.csv
```