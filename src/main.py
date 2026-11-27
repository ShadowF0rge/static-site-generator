from textnode import * 



def main(text, text_type, url):
    test = TextNode(text, text_type, url)
    print(test)



if __name__ == "__main__":
    main("This is some anchor text", TextType.LINKS, "https://www.boot.dev")