# Quick VS Code Python Test
print("🎉 VS Code Python Test")
print("=" * 30)

# Test Python version
import sys
print(f"✅ Python Version: {sys.version.split()[0]}")
print(f"✅ Python Path: {sys.executable}")

# Test imports
try:
    import json, os, time
    print("✅ Core modules: Working")
except ImportError as e:
    print(f"❌ Import error: {e}")

# Test your project imports
try:
    from dotenv import load_dotenv
    print("✅ dotenv: Working")
except ImportError:
    print("❌ dotenv: Not installed")

try:
    import google.generativeai as genai
    print("✅ Google AI: Working")
except ImportError:
    print("❌ Google AI: Not installed")

try:
    import speech_recognition as sr
    print("✅ Speech Recognition: Working")
except ImportError:
    print("❌ Speech Recognition: Not installed")

try:
    import pyttsx3
    print("✅ Text-to-Speech: Working")
except ImportError:
    print("❌ Text-to-Speech: Not installed")

print("\n🚀 Ready to run InterviewerSpeech.py!")
print("Press F5 or run: python InterviewerSpeech.py")
