# Math
A couple of scripts related to mathematics. Some really old, some recent.

## Harmonic Series Subsequence
Is the sum of all reciprocals, basically.

![image](https://github.com/more-joao/math/assets/67847521/2f59fb6c-a533-4858-b475-72829ae3ff8e)

Now, there is a question that can be posed, which is what the script (and future tests with it) may help answer. Before anything else, let us define a couple of things.

> Def 1: a **harmonic number** is any sum within the harmonic series, given by some upper bound k >= 1. We can denote a harmonic number by H(k).

```
def harmonic_number(k):
    sum = 0
    for i in range(1,k+1):
        sum = sum + 1/i
    return sum
```

> Def 2: given some real (or natural) number a, there exists a set of all harmonic numbers H(k) such that H(k) < a. Be this set the **harmonic set for the given a**.

```
def generate_harmonic_set(a, hset):
        m = len(hset)+1
        while True:
            h = harmonic_number(m)
            if h <= a:
                hset.append(h)
            elif harmonic_number(m+1) > a:
                break
            m = m+1
        return hset
```

We also have a somewhat important propostion that can be proved (note that, here, we restrict ourselves to natural numbers):
> Proposition: being A the harmonic set for some natural number a, |A| = k if max(A) = H(k). In other words, the cardinality of a harmonic set is equal to the upper bound of the greatest harmonic number that is less than the given number a.

Lastly, the topic of exploration, the mentioned subsequence, is given by:
> Target subsequence: the greatest number m of terms such that H(m) < a<sub>k</sub>, for all a<sub>k</sub> in the natural (or real) numbers set.

However, we can make the definition of this sequence clearer using the proposition above:
> The sequence of all cardinalities of the harmonic sets for every a<sub>k</sub> in {a0, ..., a<sub>k</sub>, with naturals a<sub>k</sub> > a<sub>k-1</sub>}.

The big question is: can we find a general formula for this sequence? The script tries to expose certain relations.
