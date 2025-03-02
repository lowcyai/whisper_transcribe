# Transcribe Whisper Turbo

Projekt ten służy do transkrypcji mediów (audio/wideo) za pomocą modelu Whisper Turbo.  
Kod sprawdza czy FFmpeg jest zainstalowany, pobiera model, a następnie zapisuje transkrypcję w formacie napisów SRT.

## Funkcjonalności
- Wykrywanie systemu operacyjnego.
- Weryfikacja obecności FFmpeg.
- Automatyczne pobieranie modelu Whisper Turbo.
- Transkrypcja plików audio/wideo.
- Zapis wyników w formacie SRT.

## Jak uruchomić?
1. Upewnij się, że masz zainstalowany FFmpeg.  
   - macOS: `brew install ffmpeg`  
   - Windows: `choco install ffmpeg` lub `scoop install ffmpeg`, ewentualnie zainstaluj z oficjalnej strony ffmpeg i ustaw zmienną środowiskową na plik exe
   - Linux: `sudo apt install ffmpeg`
2. Uruchom skrypt:
   ```bash
   python transcribe_whisper.py
   ```
3. Postępuj zgodnie z instrukcjami w konsoli.

## O projekcie
Kod został stworzony dla bloga [lowcyai.pl](https://lowcyai.pl).  
Zapraszamy do odwiedzin i dzielenia się opiniami na temat tego rozwiązania.
