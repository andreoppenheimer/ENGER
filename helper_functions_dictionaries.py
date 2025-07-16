phoneme_dict = {
                "p": {"consonant": True, "place": "bilabial", "manner": "plosive", "voiced": False, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 1},
                "b": {"consonant": True, "place": "bilabial", "manner": "plosive", "voiced": True, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 2},
                "t": {"consonant": True, "place": "alveolar", "manner": "plosive", "voiced": False, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 1},
                "d": {"consonant": True, "place": "alveolar", "manner": "plosive", "voiced": True, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 2},
                "k": {"consonant": True, "place": "velar", "manner": "plosive", "voiced": False, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 1},
                "g": {"consonant": True, "place": "velar", "manner": "plosive", "voiced": True, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 2},
                "θ": {"consonant": True, "place": "dental", "manner": "fricative", "voiced": False, "coda_eng": True, "onset_eng": True, "coda_ger": False, "onset_ger": False, "phoneme": True, "sonority": 3},
                "ð": {"consonant": True, "place": "dental", "manner": "fricative", "voiced": True, "coda_eng": True, "onset_eng": True, "coda_ger": False, "onset_ger": False, "phoneme": True, "sonority": 4},
                "p͡f": {"consonant": True, "place": "labiodental", "manner": "affricate", "voiced": False, "coda_eng": False, "onset_eng": False, "coda_ger": False, "onset_ger": True, "phoneme": True, "sonority": 2},
                "t͡s": {"consonant": True, "place": "alveolar", "manner": "affricate", "voiced": False, "coda_eng": False, "onset_eng": True, "coda_ger": False, "onset_ger": True, "phoneme": True, "sonority": 2},
                "t͡ʃ": {"consonant": True, "place": "postalveolar", "manner": "affricate", "voiced": False, "coda_eng": True, "onset_eng": True, "coda_ger": False, "onset_ger": False, "phoneme": True, "sonority": 2},
                "d͡ʒ": {"consonant": True, "place": "postalveolar", "manner": "affricate", "voiced": True, "coda_eng": True, "onset_eng": True, "coda_ger": False, "onset_ger": False, "phoneme": True, "sonority": 3},
                "f": {"consonant": True, "place": "labiodental", "manner": "fricative", "voiced": False, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 3},
                "v": {"consonant": True, "place": "labiodental", "manner": "fricative", "voiced": True, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 4},
                "s": {"consonant": True, "place": "alveolar", "manner": "fricative", "voiced": False, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 3},
                "z": {"consonant": True, "place": "alveolar", "manner": "fricative", "voiced": True, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 4},
                "ʃ": {"consonant": True, "place": "postalveolar", "manner": "fricative", "voiced": False, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 3},
                "ʒ": {"consonant": True, "place": "postalveolar", "manner": "fricative", "voiced": True, "coda_eng": True, "onset_eng": True, "coda_ger": False, "onset_ger": False, "phoneme": True, "sonority": 4},
                "ç": {"consonant": True, "place": "palatal", "manner": "fricative", "voiced": False, "coda_eng": False, "onset_eng": False, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 3},
                "x": {"consonant": True, "place": "velar", "manner": "fricative", "voiced": False, "coda_eng": False, "onset_eng": False, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 3},
                "h": {"consonant": True, "place": "glottal", "manner": "fricative", "voiced": False, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 3},
                "m": {"consonant": True, "place": "bilabial", "manner": "nasal", "voiced": True, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 5},
                "n": {"consonant": True,"place": "alveolar", "manner": "nasal", "voiced": True, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 5},
                "ŋ": {"consonant": True, "place": "velar", "manner": "nasal", "voiced": True, "coda_eng": True, "onset_eng": False, "coda_ger": True, "onset_ger": False, "phoneme": True, "sonority": 5},
                "l": {"consonant": True, "place": "alveolar", "manner": "lateral_approximant", "voiced": True, "coda_eng": True, "onset_eng": True, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 6},
                "j": {"consonant": True, "place": "palatal", "manner": "approximant", "voiced": True, "coda_eng": False, "onset_eng": True, "coda_ger": False, "onset_ger": True, "phoneme": True, "sonority": 7},
                "ʁ": {"consonant": True, "place": "uvular", "manner": "fricative", "voiced": True, "coda_eng": False, "onset_eng": False, "coda_ger": True, "onset_ger": True, "phoneme": True, "sonority": 6},
                "ɹ": {"consonant": True, "place": 'postalveolar', 'manner': 'approximant', 'voiced': True, "coda_eng": True, "onset_eng": True, "coda_ger": False, "onset_ger": False, "phoneme": True, "sonority": 6},
                "w": {"consonant": True, "place": "labio-velar", "manner": "approximant", "voiced": True, "coda_eng": True, "onset_eng": True, "coda_ger": False, "onset_ger": False, "phoneme": True, "sonority": 7},
                "i": {"consonant": False, "height": 'close', 'backness': 'front', 'rounded': False, 'tense': True, "sonority": 10},
                "ɪ": {"consonant": False, "height": 'close', 'backness': 'front', 'rounded': False, 'tense': False, "sonority": 10},
                "eɪ": {"consonant": False, "height": 'mid', 'backness': 'front', 'rounded': False, 'tense': True, "sonority": 10},
                "ɛ": {"consonant": False, "height": 'mid', 'backness': 'front', 'rounded': False, 'tense': False, "sonority": 10},
                "æ": {"consonant": False, "height": 'near-open', 'backness': 'front', 'rounded': False, 'tense': False, "sonority": 10},
                "ɑ": {"consonant": False, "height": 'open', 'backness': 'back', 'rounded': False, 'tense': True, "sonority": 10},
                "ɔ": {"consonant": False, 'height': 'mid', 'backness': 'back', 'rounded': True, 'tense': True, "sonority": 10},
                "oʊ": {"consonant": False, 'height': 'mid', 'backness': 'back', 'rounded': True, 'tense': True, "sonority": 10},
                "ʊ": {"consonant": False, 'height': 'close', 'backness': 'back', 'rounded': True, 'tense': False, "sonority": 10},
                "u": {"consonant": False, 'height': 'close', 'backness': 'back', 'rounded': True, 'tense': True, "sonority": 10},
                "ʌ": {"consonant": False, 'height': 'mid', 'backness': 'central', 'rounded': False, 'tense': False, "sonority": 10},
                "ə": {"consonant": False, 'height': 'mid', 'backness': 'central', 'rounded': False, 'tense': False, "sonority": 10},
                "aɪ": {"consonant": False, 'height': 'open → close', 'backness': 'front → front', 'rounded': False, 'tense': True, "sonority": 10},
                "aʊ": {"consonant": False, 'height': 'open → close', 'backness': 'back → back', 'rounded': True, 'tense': True, "sonority": 10},
                "ɔɪ": {"consonant": False, 'height': 'mid → close', 'backness': 'back → front', 'rounded': True, 'tense': True, "sonority": 10},
                "y": {"consonant": False, 'height': 'close', 'backness': 'front', 'rounded': True, 'tense': True, "sonority": 10},
                "ʏ": {"consonant": False, 'height': 'near-close', 'backness': 'front', 'rounded': True, 'tense': False, "sonority": 10},
                "e": {"consonant": False, 'height': 'close-mid', 'backness': 'front', 'rounded': False, 'tense': True, "sonority": 10},
                "ø": {"consonant": False, 'height': 'close-mid', 'backness': 'front', 'rounded': True, 'tense': True, "sonority": 10},
                "œ": {"consonant": False, 'height': 'open-mid', 'backness': 'front', 'rounded': True, 'tense': False, "sonority": 10},
                "o": {"consonant": False, 'height': 'close-mid', 'backness': 'back', 'rounded': True, 'tense': True, "sonority": 10},
                "a": {"consonant": False, 'height': 'open', 'backness': 'front', 'rounded': False, 'tense': True, "sonority": 10},
                "ɐ": {"consonant": False, "height": 'near-open', 'backness': 'central', 'rounded': False, 'tense': False, "sonority": 10}
               }

syl_dict = {
            "syl1": ["C", "V"],
            "syl2": ["C", "V", "C"],
            "syl3": ["C", "C", "V"],
            "syl4": ["C", "V", "C", "C"],
            "syl5": ["V"],
            "syl6": ["C", "C", "V", "C"],
            "syl7": ["V", "C"],
            "syl8": ["C", "C", "V", "C", "C"],
            "syl9": ["V", "C", "C"],
            "syl10": ["C", "V", "C", "C", "C", "C"]
           }

language_list = ["eng", "ger"]

import random
import ipywidgets as widgets
from IPython.display import display

def clear_log():
    clear_log = input("Clear word log? (y/n): ")
    if clear_log.lower() == "y":
        with open("word_log.txt", "w", encoding="utf-8") as file:
            file.write("Phonological Rule Log\n")
            file.write("======================\n\n")

def make_handler(rule_label, word, output):
    def handler(b):
        class Rule:
            description = rule_label
        with output:
            output.clear_output()
            on_rule_click(Rule(), word)
    return handler

def check_input():
    while True:
        try:
            user_input = input("Enter the number of syllables you would like your word to have (1–6): ")
            num_syl = int(user_input)
            if 1 <= num_syl <= 6:
                print("You entered:", num_syl)
                return num_syl  
            else:
                print(num_syl, "is not a valid number. Please enter a number from 1 to 6.")
        except ValueError:
            print(user_input, "is not a number. Please enter a whole number (1–6).")

def build_word():
    word = []
    num_syl = check_input()
    syl_list = list(syl_dict.keys())
    while num_syl > 0:
        syl_choice = random.choice(syl_list)
        syl_structure = syl_dict[syl_choice]
        word += build_syl(syl_structure)
        num_syl -= 1
    word.pop()
    return word

def syl_slicer(syl_structure):
    v_index = syl_structure.index('V')  # Find the index of 'V'
    onset_structure = syl_structure[:v_index]     # Everything before 'V'
    coda_structure = syl_structure[v_index+1:]   # Everything after 'V'
    return onset_structure, coda_structure

def build_syl(syl_structure):
    syl = []
    onset_structure, coda_structure = syl_slicer(syl_structure)
    if len(onset_structure) > 0:
        syl += (build_onset(onset_structure))
    syl += (build_nucleus())
    if len(coda_structure) > 0:
        syl += (build_coda(coda_structure))
    syl.append('.')
    return syl

def build_onset(onset_structure):
    language = random.choice(language_list)
    onset = []
    i = 0
    while i < len(onset_structure):
        if language == "eng":
            if i == 0:
                filtered_list = [k for k, v in phoneme_dict.items() if v.get("onset_eng") ==  True and v.get("sonority") <= (8 - len(onset_structure) + i)]
                c = random.choice(filtered_list)
                onset.append(c)
                i += 1
            else:
                last_phoneme = onset[-1]
                last_sonority = phoneme_dict[last_phoneme]["sonority"]
                filtered_list = [k for k, v in phoneme_dict.items() if ((v.get("onset_eng") ==  True and v.get("sonority") > last_sonority) or (last_phoneme == "s" and k in ["t", "p", "k"])) and v.get("sonority") <= (8 - len(onset_structure) + i)]
                c = random.choice(filtered_list)
                onset.append(c)
                i += 1
        if language == "ger":
            if i == 0:
                filtered_list = [k for k, v in phoneme_dict.items() if v.get("onset_ger") ==  True and v.get("sonority") <= (8 - len(onset_structure) + i)]
                c = random.choice(filtered_list)
                onset.append(c)
                i += 1
            else:
                last_phoneme = onset[-1]
                last_sonority = phoneme_dict[last_phoneme]["sonority"]
                filtered_list = [k for k, v in phoneme_dict.items() if ((v.get("onset_ger") ==  True and v.get("sonority") > last_sonority) or (last_phoneme == "s" and k in ["k"]) or (last_phoneme == "ʃ" and k in ["t", "p"])) and v.get("sonority") <= (8 - len(onset_structure) + i)]
                c = random.choice(filtered_list)
                onset.append(c)
                i += 1
    return onset

def build_nucleus():
    filtered_list = [k for k, v in phoneme_dict.items() if v.get("consonant") == False]
    n = random.choice(filtered_list)
    return n

def build_coda(coda_structure):
    language = random.choice(language_list)
    coda = []
    i = 0
    while i < len(coda_structure):
        if language == "eng":
            if i == 0:
                filtered_list = [k for k, v in phoneme_dict.items() if v.get("coda_eng") ==  True and v.get("sonority") >= (len(coda_structure) - i)]
                c = random.choice(filtered_list)
                coda.append(c)
                i += 1
            else:
                last_phoneme = coda[-1]
                last_sonority = phoneme_dict[last_phoneme]["sonority"]
                filtered_list = [k for k, v in phoneme_dict.items() if v.get("coda_eng") ==  True and v.get("sonority") < last_sonority and v.get("sonority") >= (len(coda_structure) - i)]
                c = random.choice(filtered_list)
                coda.append(c)
                i += 1
        if language == "ger":
            if i == 0:
                filtered_list = [k for k, v in phoneme_dict.items() if v.get("coda_ger") ==  True and v.get("sonority") >= (len(coda_structure) - i)]
                c = random.choice(filtered_list)
                coda.append(c)
                i += 1
            else:
                last_phoneme = coda[-1]
                last_sonority = phoneme_dict[last_phoneme]["sonority"]
                filtered_list = [k for k, v in phoneme_dict.items() if v.get("coda_ger") ==  True and v.get("sonority") < last_sonority and v.get("sonority") >= (len(coda_structure) - i)]
                c = random.choice(filtered_list)
                coda.append(c)
                i += 1
    return coda

def strident_cluster_simplification(word):
    strident_set = {"s", "z", "ʃ", "ʒ", "ts", "tʃ", "dʒ"}
    result = []
    for i in range(len(word)):
        result.append(word[i])
        if i < len(word) - 1 and word[i] in strident_set and word[i+ 1] in strident_set:
            result.append("ə")
    return result

def postnasal_t_deletion(word):
    nasal_consonants_set = {"m", "n", "ŋ"}
    result = []
    for i in range(len(word)):
        result.append(word[i])
        if i > len(word) -1 and word[i] == "t" and word[i - 1] in nasal_consonants_set:
            word.pop(i)
    return result

def alveolar_place_enforcement(word):
    alveolar_dict = { "p": "t", "b": "d" ,"k": "t", "g": "d"}
    stop_set = {k for k, v in phoneme_dict.items() if v.get("manner") == "plosive"}
    result = []
    for i in range(len(word)):
        result.append(word[i])
        if i < len(word) - 1 and word[-1] in alveolar_dict.keys() and word[-2] in stop_set:
            word[-1] = alveolar_dict[word[-1]]
    return result

def l_velarisation(word):
    velarised_dict = {"l": "ɫ"}
    syll_count = 0
    result = []
    
    for i in range(len(word)):
        char = word[i]
        if char == ".":
            syll_count += 1
        if syll_count >= 3 and char == "l":
            result.append(velarised_dict["l"])
        else:
            result.append(char)
    return result

def tapping(word):
    vowels_set = {k for k, v in phoneme_dict.items() if not v.get("consonant")}
    glides_set = {"w", "j"}
    td_dict = {"t": "ɾ", "d": "ɾ"}
    result = word[:]  
    for i in range(1, len(word) - 1):  
        if word[i] in td_dict:
            before = word[i - 1]
            after = word[i + 1]
            if (before in vowels_set or before in glides_set) and after in vowels_set:
                result[i] = td_dict[word[i]]
    return result

def vowel_nasalization(word):
    nasal_vowels_dict = {
        "i": "ĩ", "ɪ": "ɪ̃", "eɪ": "eɪ̃", "ɛ": "ɛ̃", "æ": "æ̃", "ɑ": "ɑ̃", "ɔ": "ɔ̃",
        "oʊ": "oʊ̃", "ʊ": "ʊ̃", "u": "ũ", "ʌ": "ʌ̃", "ə": "ə̃", "aɪ": "aɪ̃",
        "aʊ": "aʊ̃", "ɔɪ": "ɔɪ̃", "y": "ỹ", "ʏ": "ʏ̃", "e": "ẽ", "ø": "ø̃",
        "œ": "œ̃", "o": "õ", "a": "ã", "ɐ": "ɐ̃"
    }
    nasal_consonants_set = {"m", "n", "ŋ"}
    result = word[:]
    for i in range(len(word) - 1):
        if word[i] in nasal_vowels_dict and word[i + 1] in nasal_consonants_set:
            result[i] = nasal_vowels_dict[word[i]]
    return result

def final_devoicing(word):
    obstruent_pairs = {"b": "p", "d": "t", "g": "k", "v": "f", "z": "s", "ʒ": "ʃ"}
    if not word:
        return word  
    result = word[:]  
    if result[-1] in obstruent_pairs:
        result[-1] = obstruent_pairs[result[-1]]
    return result

def nasal_assimilation(word):
    velar_set = {k for k, v in phoneme_dict.items() if v.get("place") == "velar" and k != "ŋ"}
    labial_set = {k for k, v in phoneme_dict.items() if v.get("place") in ("bilabial", "labiodental") and k != "m"}
    result = word[:]  
    for i in range(len(result) - 1):
        if result[i] == "n":
            next_seg = result[i + 1]
            if next_seg in velar_set:
                result[i] = "ŋ"
            elif next_seg in labial_set:
                result[i] = "m"
    return result

def Ich_Ach_rule(word):
    front_vowels_set = {k for k, v in phoneme_dict.items() if v.get("backness") == "front"}
    back_vowels_set = {k for k, v in phoneme_dict.items() if v.get("backness") == "back"}
    sonorants_set = {k for k, v in phoneme_dict.items() if v.get("manner") in ("nasal", "approximant", "lateral_approximant")}
    result = word[:]
    for i in range(1, len(result)):
        if result[i] == "x" and (result[i - 1] in front_vowels_set or result[i - 1] in sonorants_set):
            result[i] = "ç"
        elif result[i] == "ç" and result[i - 1] in back_vowels_set:
            result[i] = "x"
    return result

def long_final_e(word):
    if word and word[-1] == "e":
        result = word[:]
        result[-1] = "e:"
        return result
    return word

def glide_insertion(word):
    vowels_set = {k for k, v in phoneme_dict.items() if v.get("consonant") == False}
    result = []
    i = 0
    while i < len(word):
        if word[i] == "aɪ" and i + 1 < len(word) and word[i + 1] in vowels_set:
            result.append("a")
            result.append("j")
            i += 1  
        else:
            result.append(word[i])
        i += 1
    return result

def schwa_deletion_before_sonorants(word):
    sonorants_set = {k for k, v in phoneme_dict.items() if v.get("manner") in ("nasal", "approximant", "lateral_approximant")}
    result = []
    i = 0
    while i < len(word):
        if word[i] == "ə" and i + 1 < len(word) and word[i + 1] in sonorants_set:
            i += 1
        else:
            result.append(word[i])
        i += 1
    return result

def prevocalic_aspiration(word):
    vowels_set = {k for k, v in phoneme_dict.items() if not v.get("consonant")}
    aspirated_dict = {"p": "pʰ", "t": "tʰ", "k": "kʰ"}
    result = word[:]  
    for i in range(len(word) - 1):
        if word[i] in aspirated_dict and word[i + 1] in vowels_set:
            result[i] = aspirated_dict[word[i]]
    return result

def schwa_deletion_between_consonants(word):
    consonants_set = {k for k, v in phoneme_dict.items() if v.get("consonant") == True}
    result = []
    i = 0
    while i < len(word):
        if (
            word[i] == "ə"
            and i > 0
            and i + 1 < len(word)
            and word[i - 1] in consonants_set
            and word[i + 1] in consonants_set
        ):
            i += 1 
        else:
            result.append(word[i])
        i += 1
    return result

def regressive_assimilation(word):
    result = word[:]  
    for i in range(len(result) - 1):
        if result[i] == "s" and result[i + 1] == "ʃ":
            result[i] = "ʃ"
    return result

def rule_possible_check(word):
    phonological_rules_temp = set()

    consonants_set = {k for k, v in phoneme_dict.items() if v.get("consonant")}
    vowels_set = {k for k, v in phoneme_dict.items() if not v.get("consonant")}
    sonorants_set = {k for k, v in phoneme_dict.items() if v.get("manner") in ("nasal", "approximant", "lateral_approximant")}
    front_vowels_set = {k for k, v in phoneme_dict.items() if v.get("backness") == "front"}
    back_vowels_set = {k for k, v in phoneme_dict.items() if v.get("backness") == "back"}
    labial_set = {k for k, v in phoneme_dict.items() if v.get("place") in ("bilabial", "labiodental") and k != "m"}
    velar_set = {k for k, v in phoneme_dict.items() if v.get("place") == "velar" and k != "ŋ"}
    stop_set = {k for k, v in phoneme_dict.items() if v.get("manner") == "plosive"}
    obstruent_pairs = {"b": "p", "d": "t", "g": "k", "v": "f", "z": "s", "ʒ": "ʃ"}
    aspirated_dict = {"p": "pʰ", "t": "tʰ", "k": "kʰ"}
    strident_set = {"s", "z", "ʃ", "ʒ", "ts", "tʃ", "dʒ"}
    alveolar_dict = {"p": "t", "b": "d", "k": "t", "g": "d"}
    nasal_consonants_set = {"m", "n", "ŋ"}
    glides_set = {"w", "j"}
    nasal_vowels_set = {
        "i", "ɪ", "eɪ", "ɛ", "æ", "ɑ", "ɔ", "oʊ", "ʊ", "u", "ʌ", "ə",
        "aɪ", "aʊ", "ɔɪ", "y", "ʏ", "e", "ø", "œ", "o", "a", "ɐ"
    }

    for i in range(len(word)):
        # Nasal Assimilation
        if word[i] == "n" and i + 1 < len(word):
            if word[i + 1] in velar_set or word[i + 1] in labial_set:
                phonological_rules_temp.add("Nasal Assimilation")

        # Ich-Ach Rule
        if word[i] == "x" and i > 0 and (word[i - 1] in front_vowels_set or word[i - 1] in sonorants_set):
            phonological_rules_temp.add("Ich-Ach Rule")
        if word[i] == "ç" and i > 0 and word[i - 1] in back_vowels_set:
            phonological_rules_temp.add("Ich-Ach Rule")

        # Regressive Assimilation
        if word[i] == "s" and i + 1 < len(word) and word[i + 1] == "ʃ":
            phonological_rules_temp.add("Regressive Assimilation")

        # Schwa Deletion before Sonorants
        if word[i] == "ə" and i + 1 < len(word) and word[i + 1] in sonorants_set:
            phonological_rules_temp.add("Schwa Deletion before Sonorants")

        # Schwa Deletion between Consonants
        if word[i] == "ə" and 0 < i < len(word) - 1:
            if word[i - 1] in consonants_set and word[i + 1] in consonants_set:
                phonological_rules_temp.add("Schwa Deletion between Consonants")

        # Glide Insertion
        if word[i] == "aɪ" and i + 1 < len(word) and word[i + 1] in vowels_set:
            phonological_rules_temp.add("Glide Insertion")

        # Prevocalic Aspiration
        if word[i] in aspirated_dict and i + 1 < len(word) and word[i + 1] in vowels_set:
            phonological_rules_temp.add("Prevocalic Aspiration")

        # Postnasal T Deletion
        if word[i] == "t" and i > 0 and word[i - 1] in nasal_consonants_set:
            phonological_rules_temp.add("Postnasal T Deletion")

        # Strident Cluster Simplification
        if i < len(word) - 1 and word[i] in strident_set and word[i + 1] in strident_set:
            phonological_rules_temp.add("Strident Cluster Simplification")

        # Tapping
        if 0 < i < len(word) - 1 and word[i] in {"t", "d"}:
            if (word[i - 1] in vowels_set or word[i - 1] in glides_set) and word[i + 1] in vowels_set:
                phonological_rules_temp.add("Tapping")

        # Vowel Nasalization
        if i < len(word) - 1 and word[i] in nasal_vowels_set and word[i + 1] in nasal_consonants_set:
            phonological_rules_temp.add("Vowel Nasalization")

    # Final Devoicing
    if word and word[-1] in obstruent_pairs:
        phonological_rules_temp.add("Final Devoicing")

    # Long word-final e
    if word and word[-1] == "e":
        phonological_rules_temp.add("Long word final e")

    # Alveolar Place Enforcement
    if len(word) >= 2 and word[-1] in alveolar_dict and word[-2] in stop_set:
        phonological_rules_temp.add("Alveolar Place Enforcement")

    # L-Velarisation (3 or more syllables → count at least 2 dots)
    if word.count(".") >= 2 and "l" in word:
        phonological_rules_temp.add("L-Velarisation")

    return phonological_rules_temp

def on_rule_click(rule, word):
    phonological_rules_actual = {
        "Final Devoicing": final_devoicing,
        "Nasal Assimilation": nasal_assimilation,
        "Ich-Ach Rule": Ich_Ach_rule,
        "Glide Insertion": glide_insertion,
        "Schwa Deletion before Sonorants": schwa_deletion_before_sonorants,
        "Prevocalic Aspiration": prevocalic_aspiration,
        "Schwa Deletion between Consonants": schwa_deletion_between_consonants,
        "Regressive Assimilation": regressive_assimilation,
        "Long word final e": long_final_e,
        "Postnasal T Deletion": postnasal_t_deletion,
        "Strident Cluster Simplification": strident_cluster_simplification,
        "Alveolar Place Enforcement": alveolar_place_enforcement,
        "L-Velarisation": l_velarisation,
        "Tapping": tapping,
        "Vowel Nasalization": vowel_nasalization,
    }

    print(f"You chose: {rule.description}")

    word_copy = word[:]

    rule_function = phonological_rules_actual.get(rule.description)
    if rule_function:
        result = rule_function(word_copy)
        if result is None:  
            result = word_copy
    else:
        print(f"Rule '{rule.description}' not found.")
        return

    print(f"Your new word is: {' '.join(result)}")

    with open("word_log.txt", "a", encoding="utf-8") as file:
        file.write(f"Rule applied: {rule.description}\n")
        file.write(f"Resulting word: {' '.join(result)}\n\n")
