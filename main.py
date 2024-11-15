import openai

# Wprowadź swój klucz API OpenAI 
openai.api_key = 'YOUR_API_KEY'

# Funkcja odczytująca treść z pliku
def read_file_content(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku '{filename}'. Upewnij się, że plik znajduje się w tym samym folderze co skrypt.")
        exit()

# Funkcja generująca szablon strony
def generate_template_with_ai():
    prompt = (
        "Jako profesjonalny web designer, zaprojektuj kompletny szablon strony internetowej. "
    "Szablon powinien być estetyczny, funkcjonalny i zgodny z najnowszymi standardami projektowania stron internetowych.\n\n"
    "### Wytyczne do stworzenia szablonu:\n"
    "1. **Struktura strony**:\n"
    "   - Nagłówek (<header>) ma zawierać miejsce na logo, nazwę strony i uproszczoną nawigację.\n"
    "   - Główna sekcja (<main>) powinna być przeznaczona na treść artykułu, z oznaczeniem `<!-- CONTENT GOES HERE -->` w miejscu, gdzie dynamicznie zostanie wstawiona treść.\n"
    "   - Stopka (<footer>) musi zawierać prawa autorskie i opcjonalnie linki do mediów społecznościowych lub dodatkowych zasobów.\n\n"
    "2. **Estetyka i styl**:\n"
    "   - Osadź style CSS wewnątrz tagu <style>, z wyraźnym podziałem na sekcje (np. dla nagłówka, treści, stopki).\n"
    "   - Projekt powinien wykorzystywać elastyczne układy, takie jak Flexbox lub Grid, zapewniające responsywność i optymalny wygląd na różnych urządzeniach.\n"
    "   - Zadbaj o odpowiednie marginesy, odstępy, czytelne czcionki (preferowane: sans-serif) oraz kontrast kolorów zgodny z WCAG (Web Content Accessibility Guidelines).\n\n"
    "3. **Responsywność i dostępność**:\n"
    "   - Zapewnij poprawne działanie szablonu na urządzeniach mobilnych i desktopowych, stosując techniki RWD (Responsive Web Design).\n"
    "   - Uwzględnij dostępność (accessibility), np. przez stosowanie czytelnych kolorów, odpowiednich rozmiarów tekstu oraz nawigacji przyjaznej użytkownikom korzystającym z czytników ekranowych.\n\n"
    "4. **Dodatkowe funkcje**:\n"
    "   - Dodaj miejsce na dodatkowe elementy, takie jak banery, sidebar lub sekcja „o nas”, które można opcjonalnie włączyć w przyszłości.\n"
    "   - Uwzględnij sekcję z przyciskiem CTA (Call to Action), np. „Skontaktuj się z nami” lub „Przeczytaj więcej”.\n\n"
    "5. **Cel i przeznaczenie**:\n"
    "   - Twój szablon ma być prosty do integracji z dynamiczną treścią artykułu. W miejscu przeznaczonym na treść umieść wyraźny komentarz `<!-- CONTENT GOES HERE -->`.\n\n"
    "Wygeneruj kompletny dokument HTML zawierający wbudowane style CSS i zachowujący najlepsze praktyki projektowe."
    )
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Błąd podczas komunikacji z API OpenAI: {e}")
        exit()

# Funkcja generująca HTML dla artykułu
def generate_article_html(article_content):
    prompt = (
       "Jako profesjonalny web developer, opracuj semantyczny kod HTML na podstawie poniższego artykułu(użyj całego tekstu zawartego w pliku i tylko i wyłącznie jego). "
    "Kod powinien być zgodny z najnowszymi standardami HTML5 i uwzględniać dostępność (accessibility) oraz najlepsze praktyki w zakresie organizacji i czytelności treści.\n\n"
    
    " Wytyczne do generowania kodu HTML:\n"
    "1. **Semantyczna struktura HTML5**:\n"
    "   - Zorganizuj treść w logicznej strukturze, używając odpowiednich semantycznych tagów, takich jak <header>, <section>, <article>, <footer>.\n"
    "   - W nagłówku dokumentu (<header>) umieść tytuł artykułu, a w stopce (<footer>) miejsce na dodatkowe informacje, np. prawa autorskie .\n\n"
    "2. **Hierarchia i czytelność treści**:\n"
    "   - Podziel treść na sekcje z odpowiednimi nagłówkami (h1, h2, h3), aby nadać jej przejrzystość.\n"
    "   - Użyj akapitów (<p>) do wyraźnego oddzielenia tekstu.\n"
    "   - Jeśli treść zawiera listy, zastosuj znaczniki <ul>/<ol> oraz <li>, aby zwiększyć czytelność.\n\n"
    "3. **Obsługa grafik i multimediów**:\n"
    "   - Zintegruj miejsce na grafiki, dodając znaczniki <img src='image_placeholder.jpg' alt='Opis obrazu'> w odpowiednich miejscach artykułu.\n"
    "   - Zadbaj o to, aby atrybut `alt` dokładnie opisywał treść lub kontekst obrazu dla użytkowników korzystających z czytników ekranowych.\n"
    "   - Każdy obraz opatrz podpisem (<figcaption>), który opisuje znaczenie grafiki w kontekście treści artykułu.\n\n"
    "4. **Zakres generowanego kodu**:\n"
    "   - Twój kod ma być przeznaczony do wstawienia między  znacznikami <body> i </body>, bez uwzględniania tagów <html> i <head>.\n"
    "   - Skup się wyłącznie na strukturze wizualnej i organizacyjnej treści artykułu.\n\n"
    "5. **Dodatkowe uwagi**:\n"
    "   - Kod HTML musi być w pełni walidowalny i zoptymalizowany pod kątem przejrzystości oraz edytowalności.\n"
    "   - Nie uwzględniaj zewnętrznych stylów CSS ani JavaScript – kod ma być skoncentrowany na strukturze HTML.\n\n"
    "### Tekst artykułu:\n\n" + article_content
    )
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Błąd podczas komunikacji z API OpenAI: {e}")
        exit()

# Pobranie treści artykułu
article_content = read_file_content("article.txt")

# Generowanie pliku artykułowego
article_html = generate_article_html(article_content)
with open("artykul.html", "w", encoding="utf-8") as article_file:
    article_file.write(article_html)
print("Wygenerowano plik 'artykul.html'.")

# Generowanie szablonu strony
template_html = generate_template_with_ai()
with open("szablon.html", "w", encoding="utf-8") as template_file:
    template_file.write(template_html)
print("Wygenerowano plik 'szablon.html'.")

# Generowanie pliku podglądu
try:
    # Wczytaj treści szablonu i artykułu
    template_content = read_file_content("szablon.html")
    article_content = read_file_content("artykul.html")
    
    # Wstaw treść artykułu w miejsce <!-- CONTENT GOES HERE -->
    preview_content = template_content.replace("<!-- CONTENT GOES HERE -->", article_content)
    
    # Zapisz do pliku podglądu
    with open("podglad.html", "w", encoding="utf-8") as preview_file:
        preview_file.write(preview_content)
    print("Wygenerowano plik 'podglad.html'.")
except Exception as e:
    print(f"Błąd podczas generowania pliku podglądu: {e}")
