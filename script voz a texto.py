import speech_recognition as sr

def voz_a_texto(ruta_audio=None, idioma='es-ES', tiempo_limite=30):
    """
    Convierte audio a texto usando Google Speech Recognition.

    Parámetros:
    - ruta_audio: ruta del archivo de audio (formato WAV recomendado). Si es None, usa micrófono.
    - idioma: código de idioma para el reconocimiento (por defecto español de España).
    - tiempo_limite: duración máxima de escucha en segundos para micrófono.

    Retorna:
    - Texto reconocido o None si no fue posible reconocer.
    """
    r = sr.Recognizer()

    try:
        if ruta_audio:
            with sr.AudioFile(ruta_audio) as source:
                print(f"Procesando archivo: {ruta_audio}")
                audio = r.record(source)
        else:
            with sr.Microphone() as source:
                print("Ajustando ruido ambiente... Por favor espera.")
                r.adjust_for_ambient_noise(source, duration=2)  # Ajuste para ruido ambiental, muy recomendable
                print("Escuchando... Por favor habla ahora.")
                audio = r.listen(source, timeout=None, phrase_time_limit=tiempo_limite)

        print("Procesando audio...")   
        texto = r.recognize_google(audio, language=idioma)
        print("Texto reconocido:")
        print(texto)
        return texto

    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print(f"Error con el servicio de reconocimiento: {e}")
    except sr.WaitTimeoutError:
        print("No se detectó audio a tiempo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    return None


if __name__ == "__main__":
    # Usar micrófono
    voz_a_texto()

    # Para usar archivo de audio (WAV)
    # voz_a_texto("ruta/a/tu/audio.wav")
