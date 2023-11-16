import pyshorteners

def shorten_url(original_url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(original_url)
    return short_url

def expand_url(short_url):
    s = pyshorteners.Shortener()
    original_url = s.tinyurl.expand(short_url)
    return original_url

if __name__ == "__main__":
    while True:
        print("URL Shortener Menu:")
        print("1. Shorten a URL")
        print("2. Expand a Short URL")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            original_url = input("Enter the URL to shorten: ")
            short_url = shorten_url(original_url)
            print("Shortened URL:", short_url)

        elif choice == "2":
            short_url = input("Enter the short URL to expand: ")
            original_url = expand_url(short_url)
            print("Original URL:", original_url)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
