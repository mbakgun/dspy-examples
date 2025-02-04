import time
import warnings
import requests
from pydantic import BaseModel, Field

warnings.filterwarnings(
    "ignore", category=UserWarning, module="pydantic._internal._config"
)
import dspy

model_name = "llama3.2:3b"
lm = dspy.LM(
    "ollama_chat/" + model_name,
    api_base="http://localhost:11434",
    api_key="",
    cache=False,
)
dspy.configure(lm=lm)


def getFloatAnswerExample():
    math = dspy.ChainOfThought("question -> answer: float")
    result = math(
        question="Three dice are tossed. What is the probability that the sum equals 3?"
    )
    print(f"Answer: {result.answer}")


class GetBasicAnswer(dspy.Signature):
    """Answer questions with short factoid answers."""

    question = dspy.InputField()
    answer = dspy.OutputField(desc="often between 1 and 5 words")

    def __init__(self):
        question = "Turkey is a country in which continent?"
        answer = dspy.ChainOfThought(GetBasicAnswer)
        prediction = answer(question=question)

        print(f"Question: {question}")
        print(f"Answer: {prediction.answer}")
        print(f"Reasoning: {prediction.reasoning}")


def ragExampleWithMjApi(question: str = "What is the github repo of the Mj API?"):
    response = requests.get("https://mj.akgns.com")
    context = [response.text]
    rag = dspy.ChainOfThought("context, question -> response")
    result = rag(context=context, question=question)
    print(f"Question: {question}")
    print(f"Answer: {result.response}")


class RagWithDataExtractionExample(dspy.Signature):
    """Extract structured information about image generation."""

    text: str = dspy.InputField()
    pageSize: int = dspy.OutputField(desc="number of images per page", format="int")
    intervalInMinutes: int = dspy.OutputField(desc="interval in minutes", format="int")
    totalImages: int = dspy.OutputField(desc="total number of images to generate")

    def __init__(self):
        response = requests.get("https://mj.akgns.com")
        extractor = dspy.ChainOfThought(RagWithDataExtractionExample)
        result = extractor(text=response.text)

        print(f"Page Size: {result.pageSize}")
        print(f"Interval Minutes: {result.intervalInMinutes}")
        print(f"Total Images: {result.totalImages}")


def reActWithRag():
    def evaluate_math(expression: str):
        print(f"Evaluating math expression: {expression}")
        return dspy.PythonInterpreter({}).execute(expression)

    def getMjApiInterval():
        response = requests.get("https://mj.akgns.com")
        extractor = dspy.ChainOfThought(RagWithDataExtractionExample)
        result = extractor(text=response.text)
        return result.intervalInMinutes

    react = dspy.ReAct("question -> answer: int", max_iters=1, tools=[evaluate_math])
    intervalInMinutes = getMjApiInterval()
    result = react(question=f"What is {intervalInMinutes} minutes in seconds?")

    print(f"Interval in minutes: {intervalInMinutes}")
    print(f"Interval in seconds: {result.answer}")
    return result.answer


def countLetterInWord():
    def count_letter(word: str, letter: str) -> int:
        """Counts occurrences of a letter in a word"""
        if not word or not letter or len(letter) != 1:
            return 0
        return word.lower().count(letter.lower())

    class LetterCounter(dspy.Signature):
        """Count occurrences of a letter in a word."""

        word = dspy.InputField(desc="the word to search in")
        letter = dspy.InputField(desc="single letter to count")
        answer = dspy.OutputField(
            desc="number of occurrences of the letter in the word", format="int"
        )

    react = dspy.ReAct(LetterCounter, tools=[count_letter], max_iters=1)

    word = "strawberry"
    letter = "r"
    result = react(word=word, letter=letter)

    print(f"Word: {word}")
    print(f"Letter '{letter}' count: {result.answer}")

    return result.answer


def summarizeTextExample():
    summ_model = dspy.ChainOfThought("text -> summary")
    sample_text = (
        "DSPy is a framework that simplifies the process of constructing machine learning problems "
        "that are based on chains of thought and require fewer steps because of its structure. "
        "The incorporation of specialist tools into language models is another feature of this system. "
        "The creation of applications, including those using artificial intelligence, can benefit greatly "
        "from the utilization of this instrument. "
        "It provides a declarative approach to building LLM applications through Python code rather than prompts. "
        "The framework enables optimization of prompts and chains automatically while maintaining reproducibility. "
        "Integration with external tools and retrieval systems is seamless, making it ideal for production deployments."
    )
    result = summ_model(text=sample_text)
    print(f"Original text: {sample_text}")
    print(f"Summary: {result.summary}")


def translateTextExample():
    trans_model = dspy.ChainOfThought("text, target_language -> translation")
    text_to_translate = (
        "Hello, world! DSPy is a great tool for building AI applications."
    )
    target_language = "Turkish"
    result = trans_model(text=text_to_translate, target_language=target_language)
    print(f"Original text: {text_to_translate}")
    print(f"Translation ({target_language}): {result.translation}")


def basicPredictExample():
    predictor = dspy.Predict("question -> answer")
    result = predictor(question="What is the capital of Germany?")
    print(f"Question: What is the capital of Germany?")
    print(f"Answer: {result.answer}")


def multipleChoiceExample():
    class MultipleChoice(dspy.Signature):
        """Answer multiple choice questions by comparing options."""

        question = dspy.InputField()
        options = dspy.InputField()
        answer = dspy.OutputField(desc="The best answer choice (A, B, C, or D)")
        reasoning = dspy.OutputField(desc="Explanation for the answer")

    predictor = dspy.Predict(MultipleChoice)

    mc_solver = dspy.MultiChainComparison(MultipleChoice, M=3)

    question = "Which planet is known as the Red Planet?"
    options = {"A": "Venus", "B": "Mars", "C": "Jupiter", "D": "Saturn"}

    completions = [predictor(question=question, options=options) for _ in range(3)]

    result = mc_solver(completions=completions, question=question, options=options)

    print(f"Question: {question}")
    print(f"Options: {options}")
    print(f"Selected Answer: {result.answer}")
    print(f"Reasoning: {result.rationale}")


def parallelProcessingExample():
    predictor = dspy.Predict("text -> category")
    parallel_processor = dspy.Parallel()

    texts = [
        "The stock market saw significant gains today",
        "Scientists discover new species in Amazon rainforest",
        "New smartphone model released with advanced features",
    ]

    exec_pairs = [(predictor, {"text": text}) for text in texts]
    results = parallel_processor(exec_pairs)

    for text, result in zip(texts, results):
        print(f"\nText: {text}")
        print(f"Category: {result.category}")


def typedChainOfThoughtExample():

    class NarutoCharacter(BaseModel):
        name: str = Field()
        clanName: str = Field(
            description="The name of the clan the character belongs to"
        )

    class KonohaFriends(dspy.Signature):
        """Given a question about Naruto's friends, return a list of their names and clans"""

        question: str = dspy.InputField()
        friends: list[NarutoCharacter] = dspy.OutputField(
            desc="List of Naruto's friends with their names and clans"
        )

    predict = dspy.ChainOfThought(KonohaFriends)
    result = predict(question="Who were Naruto's school friends from Konoha?")

    print("\nNaruto's Friends from Konoha:")
    print([friend.model_dump() for friend in result.friends])  # Convert to JSON


def stackedLLMCallsExample():
    """Example of stacking multiple LLM calls in sequence"""

    class DoubleChainModule(dspy.Module):
        def __init__(self):
            super().__init__()
            self.cot1 = dspy.ChainOfThought("question -> step_by_step_thought")
            self.cot2 = dspy.ChainOfThought("question, thought -> one_word_answer")

        def forward(self, question):
            thought = self.cot1(question=question).step_by_step_thought
            answer = self.cot2(question=question, thought=thought).one_word_answer
            return dspy.Prediction(thought=thought, answer=answer)

    multi_step_question = "What is the total years between the Roman Empire's founding and the fall of Rome?"

    doubleCot = DoubleChainModule()
    output = doubleCot(question=multi_step_question)

    print(f"\nQuestion: {multi_step_question}")
    print(f"Thought Process: {output.thought}")
    print(f"Final Answer: {output.answer}")


if __name__ == "__main__":
    start_time = time.time()
    # getFloatAnswerExample()
    # GetBasicAnswer()
    # ragExampleWithMjApi()
    # RagWithDataExtractionExample()
    # reActWithRag()
    # countLetterInWord()
    # summarizeTextExample()
    # translateTextExample()
    # basicPredictExample()
    # multipleChoiceExample()
    # parallelProcessingExample()
    # typedChainOfThoughtExample()
    # stackedLLMCallsExample()

    elapsed_ms = (time.time() - start_time) * 1000
    print(f"\nTotal time taken: {elapsed_ms:.2f}ms")
