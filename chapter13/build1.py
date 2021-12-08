class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"
    
    def public_method():
        #client が使ってもよい
        pass #pass文は文が必要だが何もしない文に使用する

    def _unsafe_method(self):
        #clientは使うべきじゃない
        pass #pass文は文が必要だが何もしない文に使用する

