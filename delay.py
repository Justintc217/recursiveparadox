def delay(t):
    w = 0               # pause begin
    while w <(10**4) * 100*t:
        w = w + 1       # pause end
    return(t)
