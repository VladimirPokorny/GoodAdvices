from utils.translator import Translator
from utils.advice import Advice


def main():
    translator = Translator()
    advice = Advice()
    
    advice_text = advice.get_random_advice()
    print(translator.translate_text(advice_text, "CS"))


if __name__ == "__main__":
    main()
