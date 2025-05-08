class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Show a question and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the given responses."""
        print("The survey results are as follows:")
        for response in self.responses:
            print(f' - {response.title().strip()}')