import json
import random
import time
from datetime import datetime
from typing import List, Dict

class InterviewBot:
    def __init__(self):
        self.candidate_name = ""
        self.position = ""
        self.current_question_index = 0
        self.responses = []
        self.interview_started = False
        
        # Question banks for different types of interviews
        self.question_banks = {
            "general": [
                "Tell me about yourself.",
                "Why are you interested in this position?",
                "What are your greatest strengths?",
                "What's a weakness you're working to improve?",
                "Where do you see yourself in 5 years?",
                "Why should we hire you?",
                "Tell me about a challenging situation you faced and how you handled it.",
                "What motivates you in your work?",
                "How do you handle stress and pressure?",
                "Do you have any questions for us?"
            ],
            "technical": [
                "Walk me through your technical background.",
                "Describe a complex project you've worked on.",
                "How do you approach debugging a difficult problem?",
                "What's your experience with version control?",
                "How do you stay updated with new technologies?",
                "Explain a time when you had to learn a new technology quickly.",
                "How do you ensure code quality in your projects?",
                "Describe your development workflow.",
                "What's your experience with testing?",
                "How do you handle technical disagreements with teammates?"
            ],
            "behavioral": [
                "Tell me about a time you disagreed with a colleague.",
                "Describe a situation where you had to meet a tight deadline.",
                "Give an example of when you went above and beyond.",
                "Tell me about a mistake you made and how you handled it.",
                "Describe a time you had to work with a difficult person.",
                "How do you handle constructive criticism?",
                "Tell me about a time you had to adapt to change.",
                "Describe a situation where you showed leadership.",
                "Give an example of when you had to prioritize multiple tasks.",
                "Tell me about a time you had to learn something completely new."
            ]
        }
        
    def start_interview(self):
        print("🤖 AI Interview Simulator")
        print("=" * 40)
        print("Welcome! I'm your interview practice bot.")
        print("I'll help you practice for your upcoming interview.\n")
        
        self.candidate_name = input("What's your name? ").strip()
        self.position = input("What position are you interviewing for? ").strip()
        
        print(f"\nGreat to meet you, {self.candidate_name}!")
        print(f"Let's practice for your {self.position} interview.\n")
        
        # Choose interview type
        print("What type of interview practice would you like?")
        print("1. General interview questions")
        print("2. Technical interview questions") 
        print("3. Behavioral interview questions")
        print("4. Mixed (all types)")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            self.questions = self.question_banks["general"].copy()
        elif choice == "2":
            self.questions = self.question_banks["technical"].copy()
        elif choice == "3":
            self.questions = self.question_banks["behavioral"].copy()
        elif choice == "4":
            self.questions = (self.question_banks["general"] + 
                            self.question_banks["technical"] + 
                            self.question_banks["behavioral"])
        else:
            print("Invalid choice. Using general questions.")
            self.questions = self.question_banks["general"].copy()
            
        random.shuffle(self.questions)
        self.interview_started = True
        
        print(f"\n{'='*50}")
        print("🎯 INTERVIEW SIMULATION STARTING")
        print(f"{'='*50}")
        print(f"Candidate: {self.candidate_name}")
        print(f"Position: {self.position}")
        print(f"Questions prepared: {len(self.questions)}")
        print("\nInstructions:")
        print("- Answer each question naturally")
        print("- Type 'skip' to move to the next question")
        print("- Type 'end' to finish the interview")
        print("- Type 'feedback' to get tips on your last answer")
        print(f"{'='*50}\n")
        
        input("Press Enter when you're ready to begin...")
        
    def ask_question(self):
        if self.current_question_index >= len(self.questions):
            self.end_interview()
            return
            
        question = self.questions[self.current_question_index]
        print(f"\n🎤 Question {self.current_question_index + 1}:")
        print(f"   {question}")
        print("-" * 50)
        
        start_time = time.time()
        response = input("Your answer: ").strip()
        end_time = time.time()
        
        if response.lower() == 'end':
            self.end_interview()
            return
        elif response.lower() == 'skip':
            print("⏭️  Skipped question.")
            self.current_question_index += 1
            self.ask_question()
            return
        elif response.lower() == 'feedback':
            self.provide_feedback()
            return
            
        response_time = round(end_time - start_time, 2)
        
        # Store the response
        self.responses.append({
            "question": question,
            "answer": response,
            "response_time": response_time,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
        
        # Provide immediate encouragement
        encouragements = [
            "Great answer! 👍",
            "Nice response! 🌟",
            "Well said! ✨",
            "Good thinking! 💡",
            "Excellent! 🎯"
        ]
        print(f"\n{random.choice(encouragements)}")
        
        if response_time > 30:
            print("💡 Tip: Try to be more concise in your responses.")
        elif response_time < 5:
            print("💡 Tip: Take a moment to think before answering.")
            
        self.current_question_index += 1
        
        # Ask if they want to continue
        if self.current_question_index < len(self.questions):
            continue_choice = input("\nReady for the next question? (y/n/end): ").lower()
            if continue_choice == 'n':
                print("Take your time. Press Enter when ready...")
                input()
            elif continue_choice == 'end':
                self.end_interview()
                return
                
        self.ask_question()
        
    def provide_feedback(self):
        if not self.responses:
            print("❌ No previous answers to provide feedback on.")
            self.ask_question()
            return
            
        last_response = self.responses[-1]
        print(f"\n📝 Feedback on your last answer:")
        print(f"Question: {last_response['question']}")
        print(f"Your answer: {last_response['answer']}")
        print(f"Response time: {last_response['response_time']} seconds")
        
        # Simple feedback based on answer length and keywords
        answer_length = len(last_response['answer'].split())
        
        if answer_length < 10:
            print("💡 Consider providing more detailed examples in your answer.")
        elif answer_length > 100:
            print("💡 Try to be more concise while still being comprehensive.")
        else:
            print("✅ Good answer length!")
            
        # Check for positive keywords
        positive_keywords = ['achieved', 'successful', 'improved', 'led', 'created', 'solved']
        if any(keyword in last_response['answer'].lower() for keyword in positive_keywords):
            print("✅ Great use of action-oriented language!")
            
        input("\nPress Enter to continue...")
        self.ask_question()
        
    def end_interview(self):
        print(f"\n{'='*50}")
        print("🏁 INTERVIEW SIMULATION COMPLETE")
        print(f"{'='*50}")
        
        if self.responses:
            print(f"Questions answered: {len(self.responses)}")
            
            total_time = sum(r['response_time'] for r in self.responses)
            avg_time = total_time / len(self.responses) if self.responses else 0
            
            print(f"Total time: {total_time:.1f} seconds")
            print(f"Average response time: {avg_time:.1f} seconds")
            
            # Generate summary
            self.generate_summary()
            
            # Ask if they want to save the session
            save_choice = input("\nWould you like to save this interview session? (y/n): ")
            if save_choice.lower() == 'y':
                self.save_session()
        else:
            print("No questions were answered.")
            
        print("\nThank you for practicing! Good luck with your real interview! 🍀")
        
    def generate_summary(self):
        print(f"\n📊 INTERVIEW SUMMARY")
        print("-" * 30)
        
        # Calculate stats
        word_counts = [len(r['answer'].split()) for r in self.responses]
        avg_words = sum(word_counts) / len(word_counts) if word_counts else 0
        
        print(f"Average answer length: {avg_words:.1f} words")
        
        # Quick response analysis
        quick_responses = sum(1 for r in self.responses if r['response_time'] < 10)
        thoughtful_responses = sum(1 for r in self.responses if 10 <= r['response_time'] <= 30)
        slow_responses = sum(1 for r in self.responses if r['response_time'] > 30)
        
        print(f"Quick responses (< 10s): {quick_responses}")
        print(f"Thoughtful responses (10-30s): {thoughtful_responses}")
        print(f"Longer responses (> 30s): {slow_responses}")
        
        # Recommendations
        print(f"\n💡 RECOMMENDATIONS:")
        if avg_words < 20:
            print("- Try to provide more detailed examples and explanations")
        if slow_responses > len(self.responses) // 2:
            print("- Practice common questions to improve response speed")
        if quick_responses > len(self.responses) // 2:
            print("- Take more time to think through your answers")
            
        print("- Use the STAR method (Situation, Task, Action, Result) for behavioral questions")
        print("- Practice speaking your answers out loud")
        print("- Research the company and role thoroughly")
        
    def save_session(self):
        filename = f"interview_session_{self.candidate_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        session_data = {
            "candidate_name": self.candidate_name,
            "position": self.position,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_questions": len(self.responses),
            "responses": self.responses
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(session_data, f, indent=2, ensure_ascii=False)
            print(f"✅ Session saved as: {filename}")
        except Exception as e:
            print(f"❌ Error saving session: {e}")

def main():
    print("🚀 Starting Interview Simulation Bot...")
    bot = InterviewBot()
    
    try:
        bot.start_interview()
        if bot.interview_started:
            bot.ask_question()
    except KeyboardInterrupt:
        print("\n\n👋 Interview simulation interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please restart the program and try again.")

if __name__ == "__main__":
    main()