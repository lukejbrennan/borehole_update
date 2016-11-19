from rapidsms.contrib.handlers import KeywordHandler

class Test(KeywordHandler):
    keyword = "hey"
    def help(self):
        self.respond("hi")
    def handle(self, text):
        self.help()
