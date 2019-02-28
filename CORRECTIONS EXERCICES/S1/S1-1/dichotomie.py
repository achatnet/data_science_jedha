def dich(liste, element):

    a = liste[0]
    b = liste[len(liste)-1]
    m = (a+b)/2
    while element != m:
        m = (a+b)/2
        if element < m:
            if a!=b:
                b = round(m)
                print("b vaut :{}".format(b))
            else:
                print("Element {} is not in list".format(element))
                break
        elif element > m:
            if a!=b:
                a = round(m)
                print("a vaut :{}".format(a))
            else:
                print("Element {} is not in list".format(element))
                break
    if element == m:
        print("Found Element {} at index {}".format(element, m))


dich([0,1,2,3,4,5,6,7,8,9,10], 15)
dich([0,1,2,3,4,5,6,7,8,9,10], 8)
