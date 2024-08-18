def count(string, substr):
    count = 0
    start = 0

    while True:
        start = string.find(substr, start)
        if start == -1:
            break
        count += 1
        start += len(substr)  

    return count


text = "hello world world world"
print(count(text, "world"))

