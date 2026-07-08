import requests

def main():
    name = input('Enter your name: ').strip()
    print(f'Hello, {name}, from my amazing uv project!')
    r = requests.get('https://python.org')
    print(r.text[:100])

def test_main():
    assert 10 > 5

if __name__ == '__main__':
    main()
