from src.config import *
import enchant
import re
import pdf2image

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

engl = enchant.Dict("en_UK")
dutch = enchant.Dict("nl")


# with open("DutchBook_0-60.txt", "r") as f:
#     text = f.read()


def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)


def ocr_core(file):
    text = pytesseract.image_to_string(file, lang="nld")
    return text


def print_pages(pdf_file):
    s = ''
    images = pdf_to_img(pdf_file)
    for pg, img in enumerate(images):
        s += ocr_core(img)
    return s


if __name__ == "__main__":

    OCR = False

    if OCR or not os.path.isfile(ALL_TEXT_FILE):
        text = print_pages('DutchBookWordlistChapter0-10.pdf')
        with open(ALL_TEXT_FILE, "w") as f:
            text = re.sub("\n\n", "", text)
            f.write(text)
    else:
        with open(ALL_TEXT_FILE, 'r') as f:
            text = f.read()

    text = re.sub("\n", ",", text).split(",")
    text = [i for i in text if i != ""]
    print(text)
    s = ''
    for line in text:
        s += line + '\n'
    print(s)

    with open(ALL_TEXT_FILE, "w") as f:
        f.write(s)

    # d = []
    # e = []
    # dutch_text = ""
    #
    # # go through the text. if change from dutch to english put a comma
    #
    # for line in text[:2]:
    #     print(line)
    #
    #     was_dutch = None
    #     was_engl = None
    #
    #     dutch_line = ''
    #
    #     words = re.findall("\S+", line)
    #
    #     for i in range(len(words)):
    #         word = words[i]
    #         print(i, word)
    #         nextWord = None
    #         if i < len(words) - 1:
    #             print(i, len(words))
    #             nextWord = words[i+1]
    #
    #         if dutch.check(word) and engl.check(nextWord):
    #             dutch_line += word + ","
    #         else:
    #             dutch_line += word + " "
    #
    #         #     if word == "":
    #         #         continue
    # #         is_dutch = dutch.check(word)
    # #         is_engl = engl.check(word)
    # #         print(word)
    # #
    # #         if is_dutch and is_engl:
    # #             dutch_line += word + " "
    # #         elif is_dutch and (was_dutch or was_dutch is None):
    # #             dutch_line += word + " "
    # #         elif is_engl and (was_engl or was_engl is None):
    # #             dutch_line += word + " "
    # #         elif was_dutch and (is_engl or was_engl is None):
    # #             dutch_line += "," + word + " "
    # #
    # #         was_dutch = is_dutch
    # #         was_engl = is_engl
    # #
    #     dutch_text += dutch_line + "\n"
    # #
    # # # d.append([s + " " for s in dutch_line])
    # print(dutch_text)

# d = [i[0].strip() for i in d if i != []]

# print(d)

# if is_engl and is_dutch:
#     if
#     dutch.append(word)
#     e.append(word)

#     isFirstEnglWord = is_engl and prev_is_engl is None
#     isFirstdutchWord = is_dutch and prev_is_dutch is None
#
#     prev_is_dutch = is_dutch
#     prev_is_engl = is_engl
