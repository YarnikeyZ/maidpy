try:
    from os import get_terminal_size as gts
    from os.path import abspath
    from subprocess import getoutput as gout
    from sys import argv
except KeyboardInterrupt:
    exit()

def backslash(text: str, encrypt: bool):
    if encrypt:
        if "\\_" in text:
            text = text.replace("\\_", "{~}")
        if "\\*" in text:
            text = text.replace("\\*", "{~~}")
        if "\\#" in text:
            text = text.replace("\\#", "{~~~}")
        if "\\\\" in text:
            pass
    else:
        if "{~}" in text:
            text = text.replace("{~}", "_")
        if "{~~}" in text:
            text = text.replace("{~~}", "*")
        if "{~~~}" in text:
            text = text.replace("{~~~}", "#")
        if "\\\\" in text:
            pass
    return text


def style(text_in: str):
    before = backslash(text_in.replace("\n", ""), True)
    result = before

    c_has = before[:3].count("#")
    c_und = before[:4].count("_")+before[4:].count("_")
    c_ast = before[:4].count("*")+before[4:].count("*")
    
    if before == "_ _ _" or before == "* * *" or before == "- - -":
        return "="*gts()[0]
    before = before.replace("_ ", "").replace("_", "").replace("* ", "").replace("*", "").replace("# ", "").replace("#", "")
    result = backslash(before, False)

    if c_has == 1:
        result = gout(f"figlet -f Big -t -k '{result}'")+"\n"+"="*gts()[0]
    elif c_has == 2:
        result = gout(f"figlet -f standard -t -k '{result}'")
    elif c_has == 3:
        result = gout(f"figlet -f Small -t -k '{result}'")

    if c_ast%2 != 0:
        result = "  *  " + result
    
    if c_und == 2 or c_ast == 2:
        result = "\033[1m" + result + "\033[0m"
    if c_und == 4 or c_ast == 4:
        result = "\033[3m" + result + "\033[0m"
    if c_und == 6 or c_ast == 6:
        result = "\033[1m\033[3m" + result + "\033[0m"
    
    return result + "\n"


def main():
    try:
        result = ""
        with open(f"{abspath('')}/{argv[1]}", 'r', encoding='utf-8') as file:
            for line in list(file):
                line = style(line)
                result += line
        print(f"\033[0m{result}")
    except IndexError:
        print("Missing file operand")
    except FileNotFoundError:
        print("No such file")


if __name__ == "__main__":
    main()
