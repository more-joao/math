def harmonic_number(k):
    sum = 0
    for i in range(1,k+1):
        sum = sum + 1/i
    return sum

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
        
# usando o teorema de que a cardinalidade do conjunto harmonico e igual ao maior m que procuramos

this = []
for x in range(1, 4):
    this = generate_harmonic_set(x, this)         
    #print(f"cardinality: {len(this)} | growth: {abs(this[len(this)-1]-this[len(this)-2])} | limit: {x} | max h. number: {this[len(this)-1]} | distance to limit: {x-this[len(this)-1]}")
    print(this)