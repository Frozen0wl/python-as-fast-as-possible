import googletrans

# class translator:
#     def __init__(self, languageto, languagefrom):
#         self.languageto = languageto
#         self.languagefrom = languagefrom

translate = googletrans.Translator()

print(translate.detect("merhaba"))