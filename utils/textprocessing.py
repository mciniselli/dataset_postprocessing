import re
import os

from utils.input_output import read_file

from utils.utilities import run_command

class TextProcessing:
    def __init__(self, java_path):
        self.java_path = java_path
        self.raw_text = read_file(java_path)
        self.text = None


    def srcml_process(self):

        self.xml_path = self.java_path.replace(".java", ".xml")

        path_list = self.java_path.split("/")

        self.cwd = "/".join(path_list[:-1])

        run_command("srcml {} -o {}".format(self.java_path, self.xml_path), self.cwd)

        f = open(self.xml_path, "r")
        textxml = ""
        skip_line = True
        for x in f:
            # print(x)
            if skip_line == True:
                skip_line = False
                continue
            if len(x.strip()) == 0:
                continue
            textxml += x.strip() + " "

        f.close()
        self.text = textxml

    def remove_comments(self):

        text = self.text

        self.text = re.sub("(?s)<comment.*?</comment>", "", text);

    def remove_tags(self):

        text = self.text

        text = text.replace("<if", "|||IF___START|||<if").replace("</if>",
                                                                                    "|||IF___END|||")
        text = text.replace("<condition>", "|||CONDITION___START|||<condition>").replace("</condition>",
                                                                                       "|||CONDITION___END|||")
        text = text.replace("<name>", "|||NAME___START|||<name>").replace("</name>",
                                                                                       "|||NAME___END|||")
        text = text.replace("<operator>", "|||OPERATOR___START|||<operator>").replace("</operator>",
                                                                                       "|||OPERATOR___END|||")

        text = text.replace("<call>", "|||CALL___START|||<call>").replace("</call>",
                                                                                       "|||CALL___END|||")

        text = text.replace("<literal", "|||LITERAL___START|||<literal>").replace("</literal>",
                                                                                       "|||LITERAL___END|||")

        text = text.replace("<argument>", "|||ARGUMENT___START|||<argument>").replace("</argument>",
                                                                                       "|||ARGUMENT___END|||")

        res = (re.sub(r'\<[^>]*\>', '|_|', text))

        res = res.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;",
                                                                    "&")  # these characters are replaced with HTML version => we replace them all

        # if there are some comments, once removed it remains an empty line. We want to remove all empty lines
        while "\n    \n    " in res:
            res = res.replace("\n    \n    ", "\n    ")

        res = res.replace("\n    ", "|_|")

        # while "|_| |_|" in res:
        #     res = res.replace("|_| |_|", "|_|")
        while "|_||_|" in res:
            res = res.replace("|_||_|", "|_|")

        res = (res).replace("\t", " ")

        self.text = res

