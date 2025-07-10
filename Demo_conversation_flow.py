# Demo: LiaPlus AI - Nursing College Admission Chatbot

def get_user_input(prompt):
    return input(f"\n{prompt}").strip().lower()

def introduction():
    print("\n" + "="*70)
    print("Hello! Welcome to our Nursing College Admission process. I am here to help you see the details of the B.Sc Nursing program. Do you want to learn more about the admission process?")
    print("="*70)
    return get_user_input("(yes/no): ")

def eligibility_check():
    print("\n" + "-"*70)
    print("Good. To start, we will check if you meet the requirements. Can you tell us if you studied Biology in 12th grade?")
    print("-"*70)
    return get_user_input("Did you study Biology in 12th? (yes/no): ")

def program_overview():
    print("\n" + "-"*70)
    print("That is good. Because you learned Biology, you can go on. I will tell you more about the program.")
    print("The B.Sc Nursing program takes up your full time - it teaches you skills for a good job in nursing. The course teaches you facts and lets you practice.")
    print("-"*70)
    more = get_user_input("Do you want more details? (yes/no): ")
    if more in ["yes", "y"]:
        print("\n" + "-"*70)
        print("The program teaches Anatomy, Physiology along with Nursing Practice. It also covers Medical-Surgical Nursing. You will get practical training. This training involves working with real patients in hospitals. Do you want to learn about the next steps?")
        print("-"*70)

def fee_structure():
    print("\n" + "-"*70)
    print("The B.Sc Nursing program has specific charges. A tuition charge of ₹60,000 INR applies. There is also a bus charge of ₹10,000 INR. This totals ₹70,000 INR each year. The program divides the total charges into three payments. You pay the first part, which is ₹30,000, when you enroll. The second part, ₹20,000, comes after the first term. The last part, also ₹20,000, comes after the second term.")
    print("-"*70)
    get_user_input("Do you need more information about how to pay? (yes/no): ")

def hostel_and_training():
    print("\n" + "-"*70)
    print("The hostel offers water and electricity all day plus all night. Security cameras provide for safety. A warden stays on the site. The program includes clinical training. You work with actual patients in a hospital. Do you want to know more about the hostel, or do you want to know about the training?")
    print("-"*70)

def college_location():
    print("\n" + "-"*70)
    print("The college is in Delhi. This city has many people and good public transportation. Do you want to know about the college's spot or the place around it?")
    print("-"*70)

def recognition_and_accreditation():
    print("\n" + "-"*70)
    print("The college holds recognition from the Indian Nursing Council (INC), which means people in the country will accept your qualification. Would you like more information about the recognition?")
    print("The college has recognition from the Indian Nursing Council (INC), which means your qualification has acceptance throughout the country. Do you want more information about the accreditation?")
    print("-"*70)

def scholarship_options():
    print("\n" + "-"*70)
    print("We provide these scholarships: A Government Post-Matric Scholarship pays from 18,000 to 23,000 rupees. The Labour Ministry Scholarships are for people with a Labour Registration. This scholarship pays from 40,000 to 48,000 rupees.")
    print("-"*70)
    get_user_input("Do you want to learn how to apply for the scholarships? (yes/no): ")

def total_seats():
    print("\n" + "-"*70)
    print("The B.Sc Nursing program has 60 seats. Do you want to apply?")
    print("-"*70)
    get_user_input("Do you want to apply? (yes/no): ")

def eligibility_criteria():
    print("\n" + "-"*70)
    print("To get into the program, people must do a few things. They ought to take Biology in their last year of high school. They have to pass the PNT Exam. A person should be between seventeen and thirty-five years old.")
    print("-"*70)
    return get_user_input("Do you fit these requirements? Would you like to go ahead with the application? (yes/no): ")

def handle_edge_cases(response):
    print("\n" + "-"*70)
    if response in ["not sure", "maybe", "perhaps"]:
        print("You appear to need more time to decide. If a question comes up later, I will gladly offer more facts.")
    else:
        print("I will gladly offer more facts. Please tell me which part you wish to examine more closely.")
    print("-"*70)

def main():
    ans = introduction()
    if ans in ["yes", "y"]:
        bio = eligibility_check()
        if bio in ["yes", "y"]:
            program_overview()
            fee_structure()
            hostel_and_training()
            college_location()
            recognition_and_accreditation()
            scholarship_options()
            total_seats()
            fit = eligibility_criteria()
            if fit in ["yes", "y"]:
                print("\n" + "="*70)
                print("Great! Please proceed to the application form or contact us for further help.")
                print("="*70)
            elif fit in ["no", "n", "nahi"]:
                print("\n" + "="*70)
                print("I thank you for your time. If you alter your opinion later, I will help you. Have a good day!")
                print("="*70)
            else:
                handle_edge_cases(fit)
        elif bio in ["no", "n", "nahi"]:
            print("\n" + "="*70)
            print("Biology is a need for enrollment in the B.Sc Nursing program. Without Biology, a person cannot enroll in this program. A person can ask about other programs if they want.")
            print("="*70)
        else:
            handle_edge_cases(bio)
    elif ans in ["no", "n", "nahi"]:
        print("\n" + "="*70)
        print("Thank you for your time. If you change your mind, or if you need help later, contact us.")
        print("="*70)
    else:
        handle_edge_cases(ans)

if __name__ == "__main__":
    main()
