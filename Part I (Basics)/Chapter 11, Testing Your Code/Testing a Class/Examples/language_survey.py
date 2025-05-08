from survey import AnonymousSurvey

# Define a question and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question and store the responses
my_survey.show_question()
print("Enter 'q' at anytime to exit. \n")

while True:
    response = input('Language: ')
    if response.lower().strip() == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to Everyone who participated in the survey!")
my_survey.show_results()