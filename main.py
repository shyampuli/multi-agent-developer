from agents.dev_agent import DevAgent
from agents.test_agent import TestAgent
from agents.review_agent import ReviewAgent


def main():
    print("🤖 Multi-Agent AI Developer System\n")

    task = input("Enter your task: ")

    dev = DevAgent()
    tester = TestAgent()
    reviewer = ReviewAgent()

    # Step 1: Developer Agent
    print("\n👨‍💻 Dev Agent generating code...\n")
    code = dev.run(task)

    # Step 2: Test Agent
    print("\n🧪 Test Agent generating tests...\n")
    tests = tester.run(code)

    # Step 3: Review Agent (Iteration 1)
    print("\n🕵️ Reviewer improving code (Iteration 1)...\n")
    improved_code = reviewer.run(code)

    # Step 4: Review Agent (Iteration 2) 🔥
    print("\n🕵️ Reviewer improving code (Iteration 2)...\n")
    final_code = reviewer.run(improved_code)

    # Output
    print("\n" + "=" * 60)
    print("👨‍💻 DEVELOPER OUTPUT")
    print("=" * 60)
    print(code)

    print("\n" + "=" * 60)
    print("🧪 TEST CASES")
    print("=" * 60)
    print(tests)

    print("\n" + "=" * 60)
    print("🕵️ FINAL REVIEWED CODE")
    print("=" * 60)
    print(final_code)


if __name__ == "__main__":
    main()