from googletrans import Translator

def translate_text(text, target_lang='ko'):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

done = False

while not done:
    option = input(""" 
      옵션을 입력해 주세요
      실습1 : 한국어로 번역할지, 영어로 번역할지
      실습2 : 입력을 받아서 번역 진행
      실습3 : 일본어로 번역
      실습4 : 동시에 2개 이상의 번역 (선택 안할시 영어, 일본어 기본)
      도전1 : 4개 국어 이상의 번역기
      도전2 : github 연결 및 README 출력
      종료 : 프로그램 종료
      """)
    

    if option == "실습1":
        lang = "ko"
        temp = input("""
                     1 : 영어로 번역하기
                     2 : 한국어로 번역하기
                     """)
        if temp == "1": lang = "en"
        elif temp == "2": lang = "ko"
    elif option == "실습2":
        text = input("번역할 텍스트를 입력해주세요")
        print(translate_text(text,lang))
    elif option == "실습3":
        japText = input("일본어로 번역합니다, 텍스트를 입력해주세요")
        print(translate_text(japText,"ja"))
    elif option == "실습4":
        print("두개의 언어로 번역합니다, 예시) en, ko, ja, es, de")
        firstLang = input("첫번째 언어를 입력해주세요")
        secondLang = input("두번째 언어를 입력해주세요")
        twoText = input("번역할 텍스트를 입력해주세요")
        print(translate_text(twoText,firstLang))
        print(translate_text(twoText,secondLang))
    elif option == "도전1":
        multiLang = input("여러 언어로 번역할 텍스트를 입력해주세요")
        print(translate_text(multiLang,"ko"))
        print(translate_text(multiLang,"en"))
        print(translate_text(multiLang,"ja"))
        print(translate_text(multiLang,"es"))        
        print(translate_text(multiLang,"de"))
    elif option == "도전2":
        print("제 github를 소개합니다.")
    elif option == "종료":
        reply = input("프로그램을 종료할까요? [y/n]")
        if reply == "y":
            done = True
            print("프로그램을 종료합니다.")
        else:
            print("처음 화면으로 돌아갑니다.")

