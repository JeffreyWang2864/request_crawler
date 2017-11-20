class output:
    def __init__(self, e):
        self.data = dict()
        self.data_count = int()
        self.total_data_count = int()
        self.buffer_trigger = e
        self.buffer_size = 50
        self.end_writing = False
    def collectData(self, data):
        assert data is not None
        self.data_count += len(data)
        self.total_data_count += len(data)
        self.data.update(data)
    def writeHTML(self, path):
        file = open(path, 'w')
        file.write("<!DOCTYPE HTML>\n")
        file.write("<html>\n")

        file.write("\t<head>\n")
        file.write('\t\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n')
        file.write('\t\t<title> crawl result </title>\n')
        file.write("\t</head>\n")

        while not self.end_writing:
            self.buffer_trigger.wait()
            file.write("\t<body>\n")
            for sentence, rating in zip(self.data.values(), self.data.keys()):
                file.write("\t\t<p>\n")
                file.write("\t\t\t%s"%rating)
                file.write(" <br>\n")
                file.write("\t\t\t<em>rating:</em>&nbsp;")
                file.write("%s\n" % sentence)
                file.write("\t\t</p>\n")
                file.write("\t\t<hr>\n")
            print("\n***\nwrote %d lines of file on %s\n***\n"%(len(self.data), path))
            self.data = dict()
            self.data_count = int()
            self.buffer_trigger.clear()

        file.write("\t</body>\n")
        file.write("</html>")
        file.close()
    def writeTXT(self, path):
        file = open(path, 'w')

        while not self.end_writing:
            self.buffer_trigger.wait()
            for sentence, rating in zip(self.data.values(), self.data.keys()):
                file.write(rating)
                file.write("\t")
                file.write(str(sentence))
                file.write("\n")
            print("\n***\nwrote %d lines of file on %s\n***\n" % (len(self.data), path))
            self.data = dict()
            self.data_count = int()
            self.buffer_trigger.clear()
        file.close()
