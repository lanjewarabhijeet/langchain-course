from dotenv import load_dotenv
import os
load_dotenv()

def main():
    print("Hello, World!")
    print(os.getenv("GROQ_API_KEY"))
    #hi 

if __name__ == "__main__":
    main()