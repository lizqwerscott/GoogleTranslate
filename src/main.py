from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])
a = translator.translate('Toradora!', dest='ja')
print(a)
