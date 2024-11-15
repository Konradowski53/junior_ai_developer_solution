
# Generowanie Dynamicznych Stron HTML z Treścią Artykułów i Szablonem

## Opis projektu
Aplikacja pozwala na automatyczne generowanie dynamicznych stron HTML przy użyciu modelu OpenAI GPT-3.5. Narzędzie integruje treść artykułu oraz szablon strony, tworząc kompletne i profesjonalne pliki HTML gotowe do wyświetlania w przeglądarce.

### Kluczowe funkcjonalności:
1. **Generowanie pliku `artykul.html`**:
   - Na podstawie treści z pliku `article.txt` tworzy semantyczną strukturę HTML5.
   - Uwzględnia podział treści na nagłówki, akapity i grafiki z odpowiednimi atrybutami opisowymi.

2. **Generowanie pliku `szablon.html`**:
   - Tworzy profesjonalny szablon strony z wbudowanym stylem CSS.
   - Zawiera miejsce na dynamiczne wstawienie treści artykułu.

3. **Tworzenie pliku `podglad.html`**:
   - Automatycznie łączy treść artykułu z szablonem, generując kompletną stronę do podglądu.

---

## Wymagania systemowe
- Python 3.8 lub nowszy
- Biblioteka OpenAI (`openai`)
- Aktywne połączenie z internetem
- Klucz API OpenAI (konieczny do działania modelu GPT)

---

## Instrukcja uruchomienia

1. **Klonowanie repozytorium**:
   Skopiuj projekt na swój komputer:
   ```bash
   git clone <URL_repozytorium>
   cd <nazwa_folderu_repozytorium>
   ```

2. **Zainstaluj wymagane biblioteki**:
   Zainstaluj bibliotekę OpenAI, używając menedżera pakietów `pip`:
   ```bash
   pip install openai
   ```

3. **Dodaj klucz API OpenAI**:
   - W kodzie znajdź linię:
     ```python
     openai.api_key = 'YOUR_API_KEY'
     ```
   - Zastąp `YOUR_API_KEY` swoim kluczem API OpenAI.

4. **Przygotuj plik z treścią artykułu**:
   - Utwórz plik `article.txt` w tym samym folderze co skrypt.
   - Wklej treść artykułu, który ma być przekształcony w kod HTML.

5. **Uruchom aplikację**:
   W terminalu uruchom główny skrypt:
   ```bash
   python <nazwa_skryptu>.py
   ```
   Po zakończeniu działania aplikacji zostaną wygenerowane następujące pliki:
   - `artykul.html` – zawiera wygenerowaną treść artykułu.
   - `szablon.html` – zawiera wygenerowany szablon strony.
   - `podglad.html` – kompletny plik z połączoną treścią i szablonem.

6. **Wyświetlenie strony**:
   Otwórz plik `podglad.html` w dowolnej przeglądarce internetowej, aby zobaczyć wygenerowaną stronę.

---

## Uwagi końcowe
- **Modyfikacja treści artykułu**: Aby zmienić treść artykułu, zaktualizuj plik `article.txt` i ponownie uruchom skrypt.
- **Dostosowanie szablonu**: Kod CSS i struktura szablonu mogą być modyfikowane w pliku `szablon.html`.
- **Bezpieczeństwo**: Nigdy nie udostępniaj swojego klucza API publicznie.

---

## Kontakt
W przypadku pytań lub problemów z aplikacją prosimy o kontakt:
- E-mail: konrad.ostrowski53@gmail.com

