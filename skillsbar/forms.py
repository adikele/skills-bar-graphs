from django import forms

# from .utilities import list_all_countries

"""
give the form:
(i) a list of skills and 
(ii) a list of percentage - 10%, 20%
Let me have the list in utilities
"""

dict_lang_raw = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Bengali": "bn",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Chinese (Simplified)": "zh",
    "Chinese (Traditional)": "zh-TW",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da ",
    "Dari": "fa-AF",
    "Dutch": "nl ",
    "English": "en",
    "Estonian": "et",
    "Farsi (Persian)": "fa",
    "Filipino Tagalog": "tl",
    "Finnish": "fi",
    "French": "fr",
    "French (Canada)": "fr-CA",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Haitian Creole": "ht",
    "Hausa": "ha",
    "Hebrew": "he ",
    "Hindi": "hi",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id ",
    "Italian": "it",
    "Japanese": "ja",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Konkani": "ka",
    "Korean": "ko",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Macedonian": "mk",
    "Malay": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Marathi": "mr",
    "Mongolian": "mn",
    "Norwegian": "no",
    "Persian": "fa",
    "Pashto": "ps",
    "Polish": "pl",
    "Portuguese": "pt",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Spanish": "es",
    "Spanish (Mexico)": "es-MX",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tagalog": "tl",
    "Tamil": "ta",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
}

list_lang_raw = dict_lang_raw.keys()

list_lang_processed = []

for i in list_lang_raw:
    list_lang_processed.append((i, i))

"""
list_skills_raw = ['python','java', 'C', 'C++']

list_skills_processed = []

for i in list_skills_raw:
    list_skills_processed.append((i,i))
"""

list_levels_raw = ["25%", "50%", "75%", "100%"]

list_levels_processed = []

for i in list_levels_raw:
    list_levels_processed.append((i, i))


class SkillsSelectForm(forms.Form):
    selected_skill1 = forms.CharField(
        label="Select skill 1:",
        initial="Marathi",
        widget=forms.Select(choices=list_lang_processed),
    )
    selected_level_skill1 = forms.CharField(
        label="Level - skill 1:", widget=forms.Select(choices=list_levels_processed)
    )

    selected_skill2 = forms.CharField(
        label="Select skill 2:",
        initial="Konkani",
        widget=forms.Select(choices=list_lang_processed),
    )
    selected_level_skill2 = forms.CharField(
        label="Level - skill 2:", widget=forms.Select(choices=list_levels_processed)
    )

    selected_skill3 = forms.CharField(
        label="Select skill 3:",
        initial="Hindi",
        widget=forms.Select(choices=list_lang_processed),
    )
    selected_level_skill3 = forms.CharField(
        label="Level - skill 3:", widget=forms.Select(choices=list_levels_processed)
    )

    name = forms.CharField(label="Your name")


"""  
class CountrySelectForm(forms.Form):
    selected_country = forms.CharField(label='Select country:', widget=forms.Select(choices=LIST_COUNTRIES_processed )) 



    selected_skill2 = forms.CharField(label='Select skill 2:', widget=forms.Select(choices=list_skills_processed )) 
    selectedlevel_skill2 =  forms.CharField(label='Level - skill 2:', widget=forms.Select(choices=list_levels_processed )) 
    
    selected_skill3 = forms.CharField(label='Select skill 3:', widget=forms.Select(choices=list_skills_processed )) 
    selectedlevel_skill3 =  forms.CharField(label='Level - skill 3:', widget=forms.Select(choices=list_levels_processed ))    
"""
