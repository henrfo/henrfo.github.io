norwegian_stopwords = [
    "jeg", "du", "han", "hun", "det", "de", "er", "en", "og", "på", "som", "med", "til", "fra",
    "for", "av", "var", "vi", "kan", "ha", "nå", "har", "om", "et", "seg", "mot", "ut", "får",
    "ble", "ikke", "bare", "alle", "må", "den", "så", "sin", "man", "og", "i", "kunne", "hva",
    "hvordan", "der", "når", "alt", "år", "vil", "igjen", "skal", "noen", "deg", "meg", "dette",
    "andre", "bli", "sa", "ved", "etter", "hvor", "selv", "noe", "disse", "opp", "men", "oss",
    "over", "nå", "vårt", "nye", "helt", "få", "gjør", "blir", "hver", "ut", "inn", "da", "før",
    "veldig", "min", "ny", "litt", "vår", "si", "kommer", "rundt", "hvem", "hvorfor", "være",
    "aldri", "fikk", "gå", "gjøre", "dere", "flere", "mest", "bare", "først", "eller", "gikk",
    "ned", "dette", "slik", "jo", "skulle", "vil", "nok", "mens", "egentlig", "sånn", "enn",
    "alle", "andre", "at", "av", "bare", "begge", "ble", "blei", "bli", "blir",
    "blitt", "bort", "bra", "bruke", "både", "båe", "da", "de", "deg", "dei", "deim", "deira",
    "deires", "dem", "den", "denne", "der", "dere", "deres", "det", "dette", "di", "din", "disse",
    "ditt", "du", "dykk", "dykkar", "då", "eg", "ein", "eit", "eitt", "eller", "elles", "en",
    "ene", "eneste", "enhver", "enn", "er", "et", "ett", "etter", "folk", "for", "fordi",
    "forsûke", "fra", "få", "før", "fûr", "fûrst", "gjorde", "gjûre", "god", "gå", "ha", "hadde",
    "han", "hans", "har", "hennar", "henne", "hennes", "her", "hjå", "ho", "hoe", "honom", "hoss",
    "hossen", "hun", "hva", "hvem", "hver", "hvilke", "hvilken", "hvis", "hvor", "hvordan",
    "hvorfor", "i", "ikke", "ikkje", "ingen", "ingi", "inkje", "inn", "innen", "inni", "ja",
    "jeg", "kan", "kom", "korleis", "korso", "kun", "kunne", "kva", "kvar", "kvarhelst", "kven",
    "kvi", "kvifor", "lage", "lang", "lik", "like", "makt", "man", "mange", "me", "med", "medan",
    "meg", "meget", "mellom", "men", "mens", "mer", "mest", "mi", "min", "mine", "mitt", "mot",
    "mye", "mykje", "må", "måte", "navn", "ned", "nei", "no", "noe", "noen", "noka", "noko",
    "nokon", "nokor", "nokre", "ny", "nå", "når", "og", "også", "om", "opp", "oss", "over",
    "part", "punkt", "på", "rett", "riktig", "samme", "sant", "seg", "selv", "si", "sia",
    "sidan", "siden", "sin", "sine", "sist", "sitt", "sjøl", "skal", "skulle", "slik", "slutt",
    "so", "som", "somme", "somt", "start", "stille", "så", "sånn", "tid", "til", "tilbake",
    "tilstand", "um", "under", "upp", "ut", "uten", "var", "vart", "varte", "ved", "verdi",
    "vere", "verte", "vi", "vil", "ville", "vite", "vore", "vors", "vort", "vår", "være",
    "vært", "vöre", "vört", "å", "gang", "første", "fortsatt", "se", "stor", "går", "dagens",
 "les", "n", "frå", "nær", "ser", "en", "to", "tre", "fire", "fem", "seks", "syv", "åtte",
"ni", "elleve", "tolv", "egen", "nrk", "blant", "sett", "hatt", "ham", "han", "ifølge", "følge", "hele",
"fått", "radio", "radioprogrammer", "podkast", "podcast", "podkaster", "podcaster", "våre", "Hallo", "hallo"
]

# Added a function to remove stop words in data cleaning

def remove_stopwords(text, stopwords):
    """
    Remove stopwords from the text.
    
    Parameters:
        text (str): input text for processing.
        stopwords (list): list of stopwords to remove.
        
    Returns:
        str: Text without stopwords.
    """
    words = text.split()
    return " ".join(word for word in words if word.lower() not in stopwords)
