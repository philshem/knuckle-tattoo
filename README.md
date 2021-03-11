# knuckle tattoo - a recursive word search puzzle game

generating the perfect knuckle tattoo with code and open data.

blog post -- coming soon!

## get the code

```
git@github.com:philshem/knuckle-tattoo.git
cd knucle-tattoo/
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
