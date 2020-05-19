import Magic
import subprocess
import random
import time



def getcomment(response):
    first_part_comment = ["Awesome", "Amazing", "Excellent", "Stunning", "Cool", "Lovely", "Wonderful",
                          "Superb", "Spectacular", "Great", "Fantastic", "Nice", "Impressive", "Fabulous",
                          "Splendid", "Captivating"]

    special_first_part = ["What{SPACE}a{SPACE}", "Love{SPACE}this{SPACE}", "Daaaamn,{SPACE}", ""]

    second_part_comment = ["{SPACE}image", "{SPACE}photo", "{SPACE}shot", "{SPACE}work", "{SPACE}picture"]

    first = random.choice(first_part_comment)
    second = random.choice(second_part_comment)

    specialfirst = random.choice(special_first_part)
    if specialfirst == "":
        specialfirst += random.choice(first_part_comment)
    else:
        specialfirst += random.choice(first_part_comment[3:]).lower()

    authorlocal = response[0]
    tags = [tag.lower() for tag in response[1]]

    if authorlocal == "":
        authorlocal = "??????"

    if '?' in authorlocal:
        return first + second
    else:
        if "portrait" in tags:
            return specialfirst + "{SPACE}portrait"
        elif "landscape" in tags:
            return specialfirst + "{SPACE}landscape"
        elif "mountain" in tags:
            return first + "{SPACE}mountains"
        else:
            return first + second


EmojiList = {
    1: "{!} :)",
    2: "{!} ;)",
    3: "{!} :D",
}

print("Vasile Sularea")
print("500px v3.1 Script")

for index in range(100):

    subprocess.call("C:/Users/sular/PycharmProjects/500pxscript/Open.exe")
    for i in range(50):
        if random.randint(1, 20) < 4:
            subprocess.call('C:/Users/sular/PycharmProjects/500pxscript/geturl.exe')
            results = Magic.GetauthorAndTags()
            if results[0] == "":
                author = "??????"
            else:
                author = results[0].split()

            firstpart = getcomment(results)

            if len(author) > 0:
                if '?' not in author[0]:
                    secondpart = ',{SPACE}' + author[0] + EmojiList[random.randint(1, 3)]
                else:
                    secondpart = EmojiList[random.randint(1, 3)]
            else:
                secondpart = EmojiList[random.randint(1, 3)]

            print("The author is " + str(author))
            print("The tags are "+str(results[1]))
            print("")

            subprocess.call(['C:/Users/sular/PycharmProjects/500pxscript/JustComment.exe', firstpart, secondpart])
            pass
        else:
            subprocess.call('C:/Users/sular/PycharmProjects/500pxscript/Like.exe')

    subprocess.call('C:/Users/sular/PycharmProjects/500pxscript/Close.exe')
    print("wait 5-6 minutes")
    time.sleep(random.randint(300, 460))
print("The End!\n")
