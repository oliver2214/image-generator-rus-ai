from translate import Translator
translator= Translator(from_lang="russian", to_lang="en")
translation = translator.translate("Кошка бежит по забору")
print(translation)
