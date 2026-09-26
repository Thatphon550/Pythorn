import urllib.request

def main():
    url = "http://warframe.com"
    infile = urllib.request.urlopen(url)
    s = infile.read().decode()
    count = 0
    for _ in s.split():
        count += 1

    print(f"Total word count: {count}")

main()
