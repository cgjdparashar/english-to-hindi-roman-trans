#!/usr/bin/env python3
"""
Translation script to convert English text to Hindi Roman (Hinglish)
Uses a comprehensive word mapping dictionary for English to Hinglish conversion
"""
import os
import sys
import re

class HinglishConverter:
    def __init__(self):
        """Initialize the converter with common English to Hinglish mappings"""
        # Common English to Hinglish word mappings
        self.word_map = {
            # Common verbs
            'was': 'tha', 'were': 'the', 'is': 'hai', 'are': 'hain', 'am': 'hoon',
            'will': 'hoga', 'would': 'hota', 'should': 'chahiye', 'could': 'sakta',
            'can': 'sakta', 'may': 'shayad', 'must': 'zaroor',
            'do': 'karo', 'does': 'karta', 'did': 'kiya', 'done': 'kiya gaya',
            'go': 'jao', 'went': 'gaya', 'gone': 'gaya', 'going': 'ja raha',
            'come': 'aao', 'came': 'aaya', 'coming': 'aa raha',
            'see': 'dekho', 'saw': 'dekha', 'seen': 'dekha',
            'know': 'jano', 'knew': 'jaanta tha', 'known': 'jaana',
            'think': 'socho', 'thought': 'socha',
            'make': 'banao', 'made': 'banaya',
            'take': 'lo', 'took': 'liya', 'taken': 'liya',
            'find': 'dhundo', 'found': 'mila',
            'give': 'do', 'gave': 'diya', 'given': 'diya',
            'tell': 'batao', 'told': 'bataya',
            'work': 'kaam', 'worked': 'kaam kiya',
            'call': 'bulao', 'called': 'bulaya',
            'try': 'koshish karo', 'tried': 'koshish ki',
            'ask': 'pucho', 'asked': 'pucha',
            'need': 'chahiye', 'needed': 'chahiye tha',
            'feel': 'mehsoos karo', 'felt': 'mehsoos kiya',
            'become': 'bano', 'became': 'bana',
            'leave': 'chodo', 'left': 'choda',
            'put': 'rakho', 'want': 'chahiye', 'wanted': 'chahta tha',
            'look': 'dekho', 'looked': 'dekha',
            'use': 'istemaal karo', 'used': 'istemaal kiya',
            'get': 'pao', 'got': 'mila',
            'said': 'kaha', 'say': 'kaho', 'says': 'kehta hai',
            'help': 'madad', 'helped': 'madad ki',
            'keep': 'rakho', 'kept': 'rakha',
            'let': 'karne do', 'start': 'shuru karo', 'started': 'shuru kiya',
            'show': 'dikhao', 'showed': 'dikhaya',
            'hear': 'suno', 'heard': 'suna',
            'play': 'khelo', 'played': 'khela',
            'run': 'daudo', 'ran': 'dauda',
            'move': 'chalo', 'moved': 'chala',
            'live': 'raho', 'lived': 'raha',
            'believe': 'yakeen karo', 'believed': 'yakeen kiya',
            'bring': 'lao', 'brought': 'laya',
            'happen': 'ho', 'happened': 'hua',
            'write': 'likho', 'wrote': 'likha', 'written': 'likha',
            'sit': 'baitho', 'sat': 'baitha',
            'stand': 'khado', 'stood': 'khada',
            'lose': 'khona', 'lost': 'khoya',
            'pay': 'bhugtan karo', 'paid': 'bhugtan kiya',
            'meet': 'milo', 'met': 'mila',
            'include': 'shamil karo', 'including': 'shamil',
            'continue': 'jaari rakho', 'continued': 'jaari rakha',
            'set': 'set karo', 'learn': 'seekho', 'learned': 'seekha',
            'change': 'badlo', 'changed': 'badla',
            'lead': 'neta', 'led': 'neta ban',
            'understand': 'samjho', 'understood': 'samjha',
            'watch': 'dekho', 'watched': 'dekha',
            'follow': 'follow karo', 'followed': 'follow kiya',
            'stop': 'ruko', 'stopped': 'ruka',
            'create': 'banao', 'created': 'banaya',
            'speak': 'bolo', 'spoke': 'bola', 'spoken': 'bola',
            'read': 'padho', 'allow': 'ijazat do', 'allowed': 'ijazat di',
            'add': 'jodo', 'added': 'joda',
            'spend': 'kharch karo', 'spent': 'kharch kiya',
            'grow': 'badho', 'grew': 'badha',
            'open': 'kholo', 'opened': 'khola',
            'walk': 'chalo', 'walked': 'chala',
            'win': 'jeeto', 'won': 'jeeta',
            'offer': 'peshkash karo', 'offered': 'peshkash ki',
            'remember': 'yaad rakho', 'remembered': 'yaad rakha',
            'love': 'pyaar', 'loved': 'pyaar kiya',
            'consider': 'vichar karo', 'considered': 'vichar kiya',
            'appear': 'dikhna', 'appeared': 'dikha',
            'buy': 'kharido', 'bought': 'kharida',
            'wait': 'intezaar karo', 'waited': 'intezaar kiya',
            'serve': 'seva karo', 'served': 'seva ki',
            'die': 'mar jao', 'died': 'mar gaya',
            'send': 'bhejo', 'sent': 'bheja',
            'expect': 'ummeed karo', 'expected': 'ummeed ki',
            'build': 'banao', 'built': 'banaya',
            'stay': 'raho', 'stayed': 'raha',
            'fall': 'giro', 'fell': 'gira', 'fallen': 'gira',
            'cut': 'kaato', 'reach': 'pahuncho', 'reached': 'pahuncha',
            'kill': 'maaro', 'killed': 'maara',
            'remain': 'raho', 'remained': 'raha',
            'suggest': 'sujhav do', 'suggested': 'sujhav diya',
            'raise': 'uthao', 'raised': 'uthaya',
            'pass': 'paas ho', 'passed': 'paas hua',
            'sell': 'becho', 'sold': 'becha',
            'require': 'zaroorat hai', 'required': 'zaroorat thi',
            'report': 'report karo', 'reported': 'report kiya',
            'decide': 'faisla karo', 'decided': 'faisla kiya',
            'pull': 'khincho', 'pulled': 'khincha',
            
            # Pronouns
            'i': 'main', 'you': 'tum', 'he': 'woh', 'she': 'woh', 'it': 'yeh',
            'we': 'hum', 'they': 'woh', 'me': 'mujhe', 'him': 'usko', 'her': 'usko',
            'us': 'humein', 'them': 'unko',
            'my': 'mera', 'your': 'tumhara', 'his': 'uska', 'our': 'humara',
            'their': 'unka', 'mine': 'mera', 'yours': 'tumhara',
            'myself': 'khud', 'yourself': 'khud', 'himself': 'khud', 'herself': 'khud',
            'itself': 'khud', 'ourselves': 'hum khud', 'themselves': 'woh khud',
            
            # Common nouns
            'man': 'aadmi', 'woman': 'aurat', 'child': 'bachcha', 'children': 'bachche',
            'people': 'log', 'person': 'vyakti',
            'day': 'din', 'night': 'raat', 'morning': 'subah', 'evening': 'shaam',
            'year': 'saal', 'month': 'mahina', 'week': 'hafte',
            'time': 'samay', 'hour': 'ghanta', 'minute': 'minute',
            'way': 'tarika', 'place': 'jagah', 'thing': 'cheez', 'things': 'cheezon',
            'world': 'duniya', 'life': 'zindagi', 'hand': 'haath', 'eye': 'aankh', 'eyes': 'aankhein',
            'face': 'chehra', 'head': 'sir', 'body': 'sharir',
            'door': 'darwaza', 'room': 'kamra', 'house': 'ghar',
            'name': 'naam', 'work': 'kaam', 'word': 'shabd', 'words': 'shabd',
            'water': 'paani', 'food': 'khana', 'money': 'paisa',
            'father': 'pita', 'mother': 'mata', 'friend': 'dost', 'friends': 'dost',
            'book': 'kitaab', 'story': 'kahani',
            'city': 'sheher', 'country': 'desh',
            'road': 'sadak', 'street': 'gali',
            'car': 'gaadi', 'tree': 'ped',
            'school': 'school', 'teacher': 'teacher',
            'question': 'sawal', 'answer': 'jawab',
            'problem': 'samasya', 'idea': 'vichar',
            'number': 'sankhya', 'group': 'group',
            'fact': 'tathya', 'family': 'parivaar',
            'government': 'sarkar', 'company': 'company',
            'party': 'party', 'office': 'office',
            'power': 'shakti', 'information': 'jaankari',
            'business': 'business', 'system': 'system',
            'program': 'program', 'area': 'kshetra',
            'level': 'star', 'point': 'point',
            'reason': 'kaaran', 'result': 'natija',
            'change': 'badlav', 'state': 'rajya',
            'moment': 'pal', 'end': 'ant',
            'law': 'kanoon', 'war': 'jung',
            'history': 'itihaas', 'case': 'mamla',
            'service': 'seva', 'side': 'taraf',
            'part': 'hissa', 'form': 'roop',
            'mind': 'dimag', 'heart': 'dil',
            'light': 'roshni', 'voice': 'awaaz',
            'chance': 'mauka', 'effect': 'prabhav',
            'color': 'rang', 'sound': 'awaaz',
            'age': 'umar', 'job': 'naukri',
            'death': 'maut', 'figure': 'aankda',
            'view': 'drishti', 'church': 'church',
            'course': 'course', 'wife': 'patni',
            'experience': 'anubhav', 'action': 'kaarya',
            'issue': 'mudda', 'force': 'bal',
            'education': 'shiksha', 'art': 'kala',
            'foot': 'pair', 'health': 'swasthya',
            'value': 'moolya', 'truth': 'sach',
            'attention': 'dhyan', 'interest': 'ruchi',
            'fire': 'aag', 'blood': 'khoon',
            'matter': 'vishay', 'feeling': 'ehsaas',
            'line': 'line', 'kind': 'prakar',
            'sun': 'suraj', 'decision': 'faisla',
            'air': 'hawa', 'hope': 'asha',
            'control': 'niyantran', 'evidence': 'sabut',
            'baby': 'bachcha', 'society': 'samaj',
            'plan': 'yojana', 'sense': 'samajh',
            'student': 'vidyarthi', 'purpose': 'uddeshya',
            'bed': 'palang', 'arm': 'baazu',
            'peace': 'shanti', 'knowledge': 'gyan',
            'girl': 'ladki', 'boy': 'ladka',
            'table': 'mez', 'sea': 'samundar',
            'language': 'bhasha', 'image': 'chhavi',
            'paper': 'kaagaz', 'ground': 'zameen',
            'responsibility': 'zimmedaari', 'activity': 'gatividhi',
            'situation': 'sthiti', 'development': 'vikas',
            
            # Adjectives
            'good': 'acha', 'bad': 'bura', 'great': 'mahan', 'small': 'chhota', 'large': 'bada',
            'big': 'bada', 'little': 'thoda',
            'new': 'naya', 'old': 'purana', 'young': 'jawan',
            'different': 'alag', 'same': 'same',
            'own': 'apna', 'other': 'dusra', 'another': 'ek aur',
            'long': 'lamba', 'short': 'chhota',
            'high': 'uncha', 'low': 'neeche',
            'right': 'sahi', 'wrong': 'galat',
            'important': 'important', 'best': 'sabse acha',
            'better': 'behtar', 'worse': 'kharab',
            'early': 'jaldi', 'late': 'der se',
            'happy': 'khush', 'sad': 'udaas',
            'easy': 'aasaan', 'hard': 'mushkil',
            'free': 'free', 'real': 'asli',
            'strong': 'majboot', 'weak': 'kamzor',
            'full': 'poora', 'empty': 'khaali',
            'sure': 'pakka', 'possible': 'sambhav',
            'impossible': 'asambhav', 'ready': 'taiyaar',
            'beautiful': 'khoobsurat', 'true': 'sach',
            'false': 'jhooth', 'clear': 'saaf',
            'dark': 'andhera', 'white': 'safed',
            'black': 'kaala', 'red': 'lal',
            'blue': 'neela', 'green': 'hara',
            'hot': 'garam', 'cold': 'thanda',
            'fast': 'tez', 'slow': 'dheema',
            'rich': 'ameer', 'poor': 'gareeb',
            'heavy': 'bhaari', 'light': 'halka',
            'nice': 'acha', 'perfect': 'perfect',
            'simple': 'simple', 'common': 'aam',
            'difficult': 'mushkil', 'serious': 'serious',
            'special': 'special', 'certain': 'kuch',
            'available': 'uplabdh', 'recent': 'haal hi ka',
            'various': 'alag alag', 'similar': 'milta julta',
            'particular': 'khaas', 'social': 'samajik',
            'political': 'rajneeti', 'public': 'public',
            'private': 'private', 'personal': 'personal',
            'national': 'rashtriya', 'natural': 'prakritik',
            'human': 'maanav', 'general': 'aam',
            'whole': 'poora', 'local': 'sthaaniya',
            'several': 'kai', 'single': 'ek',
            'final': 'antim', 'medical': 'medical',
            'current': 'vartman', 'financial': 'vitteey',
            'able': 'saksham', 'main': 'mukhya',
            'international': 'antarrashtriya', 'alone': 'akela',
            'military': 'sainik', 'economic': 'aar thik',
            'former': 'poorva', 'enough': 'kaafi',
            
            # Adverbs & Others
            'not': 'nahi', 'no': 'nahi', 'yes': 'haan',
            'very': 'bahut', 'so': 'isliye', 'just': 'bas',
            'now': 'ab', 'then': 'tab', 'here': 'yahan', 'there': 'wahan',
            'when': 'kab', 'where': 'kahan', 'why': 'kyun', 'how': 'kaise',
            'what': 'kya', 'who': 'kaun', 'which': 'kaunsa',
            'all': 'sab', 'each': 'har', 'every': 'har',
            'both': 'dono', 'few': 'kuch', 'more': 'aur', 'most': 'sabse zyada',
            'many': 'bahut', 'much': 'bahut', 'some': 'kuch',
            'any': 'koi', 'only': 'sirf', 'also': 'bhi',
            'too': 'bhi', 'well': 'acha', 'even': 'bhi',
            'back': 'wapas', 'up': 'upar', 'down': 'neeche',
            'out': 'bahar', 'about': 'ke baare mein', 'over': 'upar',
            'after': 'baad', 'before': 'pehle',
            'through': 'ke zariye', 'during': 'ke dauraan',
            'again': 'phir se', 'always': 'hamesha', 'never': 'kabhi nahi',
            'today': 'aaj', 'yesterday': 'kal', 'tomorrow': 'kal',
            'still': 'abhi bhi', 'however': 'lekin',
            'perhaps': 'shayad', 'almost': 'lagbhag',
            'really': 'sachme', 'already': 'pehle se',
            'together': 'saath', 'around': 'ke aas paas',
            'once': 'ek baar', 'often': 'aksar',
            'probably': 'shayad', 'usually': 'aamtaur par',
            'sometimes': 'kabhi kabhi', 'soon': 'jald',
            'maybe': 'shayad', 'actually': 'asal mein',
            'quite': 'kaafi', 'rather': 'balki',
            'ago': 'pehle', 'away': 'door',
            'far': 'door', 'near': 'paas',
            'behind': 'peeche', 'among': 'ke beech',
            'between': 'ke beech', 'within': 'ke andar',
            'without': 'bina', 'against': 'ke khilaf',
            'toward': 'ki taraf', 'above': 'upar',
            'below': 'neeche', 'inside': 'andar',
            'outside': 'bahar', 'forward': 'aage',
            'since': 'jab se', 'until': 'jab tak',
            'although': 'haalaanki', 'whether': 'chahe',
            'unless': 'jab tak nahi', 'if': 'agar',
            'because': 'kyunki', 'while': 'jabki',
            'though': 'haalaanki', 'unless': 'jab tak nahi',
            
            # Prepositions
            'in': 'mein', 'on': 'par', 'at': 'par', 'to': 'ko',
            'for': 'ke liye', 'with': 'ke saath', 'from': 'se',
            'by': 'dwara', 'of': 'ka', 'as': 'jaise',
            
            # Numbers
            'one': 'ek', 'two': 'do', 'three': 'teen', 'four': 'char',
            'five': 'paanch', 'six': 'chhah', 'seven': 'saat', 'eight': 'aath',
            'nine': 'nau', 'ten': 'das', 'hundred': 'sau', 'thousand': 'hazaar',
            'first': 'pehla', 'second': 'doosra', 'third': 'teesra',
            'last': 'aakhri', 'next': 'agla',
        }
    
    def convert_to_hinglish(self, text):
        """
        Convert English text to Hinglish using word mapping
        """
        # Convert to lowercase for matching, but preserve original case structure
        words = text.split()
        converted_words = []
        
        for word in words:
            # Remove punctuation for matching
            clean_word = re.sub(r'[^\w\s]', '', word.lower())
            
            # Check if word exists in mapping
            if clean_word in self.word_map:
                hinglish_word = self.word_map[clean_word]
                
                # Preserve original punctuation
                if word != clean_word:
                    # Get punctuation
                    punct = word[len(clean_word):]
                    hinglish_word = hinglish_word + punct
                
                converted_words.append(hinglish_word)
            else:
                # Keep original word if no mapping exists
                converted_words.append(word)
        
        return ' '.join(converted_words)

def process_file(input_file, output_file):
    """
    Process the input file line by line
    """
    print(f"Starting Hinglish conversion of {input_file}...")
    print(f"Output will be saved to {output_file}\n")
    
    # Count total lines
    with open(input_file, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for _ in f)
    
    print(f"Total lines: {total_lines}")
    
    converter = HinglishConverter()
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            line_count = 0
            
            for line in infile:
                line_count += 1
                line = line.strip()
                
                if not line:
                    outfile.write('\n')
                    continue
                
                # Convert to Hinglish
                hinglish_line = converter.convert_to_hinglish(line)
                outfile.write(hinglish_line + '\n')
                
                # Progress indicator
                if line_count % 100 == 0:
                    progress = (line_count / total_lines) * 100
                    print(f"Progress: {line_count}/{total_lines} ({progress:.1f}%)")
    
    print(f"\n✓ Conversion complete! Processed {line_count} lines")
    print(f"✓ Output saved to: {output_file}")

def main():
    input_file = 'story_31_10.txt'
    output_file = 'story_31_10_hinglish.txt'
    
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found!")
        sys.exit(1)
    
    size = os.path.getsize(input_file)
    print(f"File size: {size:,} bytes ({size/1024:.1f} KB)\n")
    
    process_file(input_file, output_file)

if __name__ == '__main__':
    main()
