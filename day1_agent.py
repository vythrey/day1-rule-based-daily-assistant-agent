class MemoryAgent:
    def __init__(self):
        self.memory = {}

    def store(self, key, value):
        self.memory[key] = value

    def recall(self, key):
        return self.memory.get(key, "No memory found.")


class DailyAssistantAgent:
    def __init__(self):
        self.memory = MemoryAgent()

    def respond(self, user_input):
        cleaned_input = user_input.lower().strip()

        if "last question" in cleaned_input:
            return self.memory.recall("last_query")

        self.memory.store("last_query", user_input)

        if "plan my day" in cleaned_input:
            answer = "Start with one important task, take a short break, finish your second priority task, and review your day in the evening."

        elif "healthy meal" in cleaned_input:
            answer = "Try a balanced meal with rice or roti, dal, vegetables, and a protein source like paneer, eggs, or chickpeas."

        elif "motivate me" in cleaned_input:
            answer = "Do not wait for motivation. Start with 10 minutes of focused work. Action creates momentum."

        elif "help me focus" in cleaned_input:
            answer = "Keep your phone away, choose one task, set a 25-minute timer, and work only on that task."

        else:
            answer = "I am still learning. Try asking me to plan your day, suggest a healthy meal, motivate you, or help you focus."

        self.memory.store("last_response", answer)
        return answer


if __name__ == "__main__":
    agent = DailyAssistantAgent()

    print("Daily Assistant Agent is running. Type 'exit' to stop.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower().strip() == "exit":
            print("Goodbye!")
            break

        response = agent.respond(user_input)
        print("\nAgent:", response)