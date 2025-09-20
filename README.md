# AI Interview Simulator

An intelligent interview practice tool powered by Google's Gemini AI that provides personalized questions and detailed feedback.

## Features

- **4 Interview Types**: Behavioral, Technical, General, Case Study
- **AI-Powered Questions**: Generated based on your position and interview type
- **Real-time Analysis**: Get feedback on each answer with scores and suggestions
- **Comprehensive Report**: Detailed analysis at the end
- **Session Saving**: Export your interview results to JSON
- **Automatic API Key Loading**: No manual input required

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up API Key** (Optional - works in demo mode without it):
   - Get a free API key from: https://makersuite.google.com/app/apikey
   - Add it to `InterviewerAI.env` file:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

3. **Run the Interview Simulator**:
   ```bash
   python Interviewer2.py
   ```

## API Key Setup

The script automatically loads your API key from the `InterviewerAI.env` file. No manual input required!

### Option 1: Use .env file (Recommended)
1. Edit `InterviewerAI.env` and add your API key:
   ```
   GEMINI_API_KEY=AIzaSyC...
   ```

### Option 2: Environment Variable
Set the environment variable:
- **Windows**: `set GEMINI_API_KEY=your_key_here`
- **Linux/Mac**: `export GEMINI_API_KEY=your_key_here`

## Demo Mode

If no API key is provided, the script runs in demo mode with:
- 32+ unique fallback questions
- Varied analysis responses
- Full interview functionality
- Session saving

## Usage

1. Run the script
2. Enter your name and desired position
3. Choose interview type (1-4)
4. Answer questions naturally
5. Type `next` to skip, `feedback` for detailed analysis, or `end` to finish
6. Get your complete AI analysis report!

## Troubleshooting

Run the diagnostic script to check your setup:
```bash
python diagnose_gemini.py
```

## Files

- `Interviewer2.py` - Main interview simulator
- `InterviewerAI.env` - API key configuration
- `diagnose_gemini.py` - Diagnostic tool
- `requirements.txt` - Python dependencies

## Requirements

- Python 3.7+
- google-generativeai
- python-dotenv