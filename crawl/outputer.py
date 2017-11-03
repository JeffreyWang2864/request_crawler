class output:
    def __init__(self):
        self.data = dict()
    def collectData(self, data):
        assert data is not None
        self.data.update(data)
    def writeHTML(self, path):
        file = open(path, 'w')
        file.write("<!DOCTYPE HTML>\n")
        file.write("<html>\n")

        file.write("\t<head>\n")
        file.write('\t\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n')
        file.write('\t\t<title> crawl result </title>\n')
        file.write("\t</head>\n")

        file.write("\t<body>\n")
        for sentence, rating in zip(self.data.values(), self.data.keys()):
            file.write("\t\t<p>\n")
            file.write("\t\t\t%s"%rating)
            file.write(" <br>\n")
            file.write("\t\t\t<em>rating:</em>&nbsp;")
            file.write("%s\n" % sentence)
            file.write("\t\t</p>\n")
            file.write("\t\t<hr>\n")
        file.write("\t</body>\n")

        file.write("</html>")
    def writeTXT(self, path):
        file = open(path, 'w')
        for sentence, rating in zip(self.data.values(), self.data.keys()):
            file.write(rating)
            file.write("\t")
            file.write(str(sentence))
            file.write("\n")