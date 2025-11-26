from app.server import app

print(f"Edge TTS (Free Azure TTS) Replacement for OpenAI's TTS API")
print(f"")
print(f"* Serving OpenAI Edge TTS")
print(f"")

if __name__ == '__main__':
    app.run()
