#!/usr/bin/env python3
"""
Gemini API Diagnostic Script
This script helps diagnose common Gemini API issues
"""

import os
import sys
import google.generativeai as genai
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('InterviewerAI.env')

def test_gemini_api():
    """Test Gemini API connection and functionality"""
    print("🔍 Gemini API Diagnostic Tool")
    print("=" * 50)
    
    # Check if .env file exists
    env_file = "InterviewerAI.env"
    if os.path.exists(env_file):
        print(f"✅ Found .env file: {env_file}")
    else:
        print(f"⚠️  .env file not found: {env_file}")
        print("   The script will look for environment variables instead")
    
    # Check if API key is set
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ No GEMINI_API_KEY found in environment or .env file")
        print("💡 To set it up:")
        print("   1. Add GEMINI_API_KEY=your_key_here to InterviewerAI.env file")
        print("   2. Or set environment variable: GEMINI_API_KEY=your_key_here")
        print("   3. Get a free API key from: https://makersuite.google.com/app/apikey")
        return False
    
    print(f"✅ API Key found: {api_key[:10]}...{api_key[-5:]}")
    print("   (Loaded from .env file or environment variable)")
    
    try:
        # Test API configuration
        print("\n🔌 Testing API configuration...")
        genai.configure(api_key=api_key)
        print("✅ API configuration successful")
        
        # Test model creation
        print("\n🤖 Testing model creation...")
        model = genai.GenerativeModel('gemini-1.5-flash')
        print("✅ Model creation successful")
        
        # Test simple content generation
        print("\n📝 Testing content generation...")
        test_prompt = "Say 'Hello, API test successful!'"
        print(f"   Prompt: {test_prompt}")
        
        response = model.generate_content(test_prompt)
        
        if response and response.text:
            print(f"✅ Content generation successful!")
            print(f"   Response: {response.text.strip()}")
            
            # Test JSON generation (for interview questions)
            print("\n📋 Testing JSON generation...")
            json_prompt = """
            Generate a simple JSON response with this structure:
            {
                "question": "What is your greatest strength?",
                "category": "general"
            }
            Return ONLY the JSON, no additional text.
            """
            
            json_response = model.generate_content(json_prompt)
            if json_response and json_response.text:
                print("✅ JSON generation successful!")
                print(f"   JSON Response: {json_response.text.strip()}")
                
                # Try to parse the JSON
                try:
                    import json
                    parsed = json.loads(json_response.text.strip())
                    print("✅ JSON parsing successful!")
                    print(f"   Parsed: {parsed}")
                except json.JSONDecodeError as e:
                    print(f"⚠️  JSON parsing failed: {e}")
                    print("   This might cause issues with interview analysis")
            
            print("\n🎉 All tests passed! Your Gemini API is working correctly.")
            return True
        else:
            print("❌ Content generation failed - no response received")
            return False
            
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Error: {error_msg}")
        
        # Provide specific error guidance
        if "API_KEY_INVALID" in error_msg or "API key not valid" in error_msg:
            print("\n🔑 API Key Issue:")
            print("   • Your API key is invalid or expired")
            print("   • Get a new key from: https://makersuite.google.com/app/apikey")
            print("   • Make sure to copy the entire key without extra spaces")
        elif "quota" in error_msg.lower() or "limit" in error_msg.lower():
            print("\n📊 Quota Issue:")
            print("   • You may have exceeded your API usage limits")
            print("   • Check your Google AI Studio dashboard")
            print("   • Wait for quota to reset or upgrade your plan")
        elif "network" in error_msg.lower() or "connection" in error_msg.lower():
            print("\n🌐 Network Issue:")
            print("   • Check your internet connection")
            print("   • Try again in a few moments")
            print("   • Check if your firewall is blocking the connection")
        else:
            print("\n🔧 General Error:")
            print("   • Check your API key format")
            print("   • Ensure you have access to Gemini API")
            print("   • Try creating a new API key")
        
        return False

def test_interview_bot():
    """Test the interview bot with debug mode"""
    print("\n" + "=" * 50)
    print("🤖 Testing Interview Bot with Debug Mode")
    print("=" * 50)
    
    try:
        from Interviewer2 import AIInterviewBot
        
        # Create bot in debug mode
        bot = AIInterviewBot(debug_mode=True)
        
        if bot.model:
            print("✅ Bot created with API connection")
            
            # Test question generation
            print("\n📝 Testing question generation...")
            question = bot.generate_question("Test context for question generation")
            print(f"✅ Generated question: {question}")
            
            # Test response analysis
            print("\n🧠 Testing response analysis...")
            analysis = bot.analyze_response(question, "This is a test answer for analysis.")
            print(f"✅ Analysis result: {analysis}")
            
        else:
            print("⚠️  Bot created in demo mode (no API key)")
            print("   This is normal if you don't have a valid API key")
            
    except Exception as e:
        print(f"❌ Error testing interview bot: {e}")

if __name__ == "__main__":
    print(f"🕐 Diagnostic started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Test basic API functionality
    api_works = test_gemini_api()
    
    # Test interview bot
    test_interview_bot()
    
    print("\n" + "=" * 50)
    if api_works:
        print("🎉 Diagnosis complete - API is working!")
    else:
        print("🔧 Diagnosis complete - API issues detected")
        print("   Check the error messages above for solutions")
    print("=" * 50)
