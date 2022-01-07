# Request for Sentence or Word
word = input("What is the word? ")

# Counting number of letters for future use
a = word.count("a")
b = word.count("b")
c = word.count("c")
d = word.count("d")
e = word.count("e")
f = word.count("f")
g = word.count("g")
h = word.count("h")
i = word.count("i")
j = word.count("j")
k = word.count("k")
l = word.count("l")
m = word.count("m")
n = word.count("n")
o = word.count("o")
p = word.count("p")
q = word.count("q")
r = word.count("r")
s = word.count("s")
t = word.count("t")
u = word.count("u")
v = word.count("v")
w = word.count("w")
x = word.count("x")
y = word.count("y")
z = word.count("z")

# Converting original sentence to stage one encryption
word = word.replace("a", "z", a)
word = word.replace("b", "y", b)
word = word.replace("c", "x", c)
word = word.replace("d", "w", d)
word = word.replace("e", "v", e)
word = word.replace("f", "u", f)
word = word.replace("g", "t", g)
word = word.replace("h", "s", h)
word = word.replace("i", "r", i)
word = word.replace("j", "q", j)
word = word.replace("k", "p", k)
word = word.replace("l", "o", l)
word = word.replace("m", "n", m)
word = word.replace("n", "m", n)
word = word.replace("o", "l", o)
word = word.replace("p", "k", p)
word = word.replace("q", "j", q)
word = word.replace("r", "i", r)
word = word.replace("s", "h", s)
word = word.replace("t", "g", t)
word = word.replace("u", "f", u)
word = word.replace("v", "e", v)
word = word.replace("w", "d", w)
word = word.replace("x", "c", x)
word = word.replace("y", "b", y)
word = word.replace("z", "a", z)

####################################################################

# swap characters in string
def swap(string):
   return string[-1: ] + string[1: -1] + string[: 1]

word = swap(word)

####################################################################



# Result
print(word)
