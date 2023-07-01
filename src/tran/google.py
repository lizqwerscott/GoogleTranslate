from googletrans import Translator

def translate(data, dest):
    R_dict = dict()
    try:
        translator = Translator(service_urls=[
            'translate.google.com',
            'translate.google.co.kr',
        ])
        outcome = translator.translate(data, dest=dest)
        R_dict["data"] = outcome.text
    except RuntimeError:
        R_dict["code"] = 444
        R_dict["msg"] = "翻译错误！！"
    finally:
        R_dict["code"] = 200
        R_dict["msg"] = "翻译正常"

    return R_dict
