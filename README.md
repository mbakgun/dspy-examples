# DSPy Examples

[DSPy](https://dspy.ai/) is a framework for programming—rather than prompting—language models. It enables you to write compositional Python code to:

- Build reliable language model applications
- Create composable prompting programs
- Optimize prompts and chains automatically
- Integrate retrieval and tool use seamlessly
- Develop reproducible LLM-based systems

The framework enables developers to write declarative programs that can be optimized and improved through teleprompter learning, making it easier to create robust AI applications.


This repository contains various examples demonstrating the usage of DSPy, a framework for programming with language models. Each example showcases different capabilities and patterns.

## Setup

1. Create and activate the environment:
```bash
# Initialize project and install dependencies
uv venv --python 3.10
source .venv/bin/activate
uv pip install -U dspy
uv pip install requests
```

2. Configure Ollama:
- Make sure you have Ollama running locally
- The examples use `llama3.2:3b` model
- API base is configured to `http://localhost:11434`

## Examples

### 1. Probability Calculation
```
Question: "Three dice are tossed. What is the probability that the sum equals 3?"
Answer: 0.00462963
```
Implementation ([`getFloatAnswerExample`](basic_dspy_example.py#L17-L22))
- Uses `ChainOfThought` for mathematical reasoning
- Returns floating-point probability value
- Simple one-step calculation with direct output

### 2. Basic Question Answering
```
Question: "Turkey is a country in which continent?"
Answer: "Europe"
Reasoning: "The continent that Turkey is located on can be determined by considering its geographical position."
```
Implementation ([`GetBasicAnswer`](basic_dspy_example.py#L25-L38))
- Uses `dspy.Signature` to define input/output structure
- Provides factoid answers with reasoning
- Demonstrates basic question-answering pattern

### 3. External API Integration
```
Question: "What is the github repo of the Mj API?"
Answer: "The GitHub repository of the Mj API is https://s.akgns.com/3Aw"
```
Implementation ([`ragExampleWithMjApi`](basic_dspy_example.py#L41-L47))
- Fetches data from mj.akgns.com
- Uses RAG (Retrieval Augmented Generation)
- Processes external API response as context

### 4. Data Extraction
```
Page Size: 20
Interval Minutes: 60
Total Images: 400
```
Implementation ([`RagWithDataExtractionExample`](basic_dspy_example.py#L50-L65))
- Extracts structured data from API response
- Defines specific output fields with types
- Uses `dspy.Signature` for schema definition

### 5. Time Conversion
```
Interval in minutes: 60
Interval in seconds: 3600
```
Implementation ([`reActWithRag`](basic_dspy_example.py#L68-L85))
- Uses ReAct pattern with custom math tool
- Combines API data with calculation
- Demonstrates tool integration

### 6. String Analysis
```
Word: "strawberry"
Letter 'r' count: 3
```
Implementation ([`countLetterInWord`](basic_dspy_example.py#L88-L113))
- Custom tool for letter counting
- Uses ReAct for simple text analysis
- Shows basic tool usage pattern

### 7. Text Summarization
```
Input: Long text about DSPy framework
Output: Concise summary of DSPy's key features
```
Implementation ([`summarizeTextExample`](basic_dspy_example.py#L116-L133))
- Uses `ChainOfThought` for text summarization
- Processes multi-sentence input text
- Generates concise, coherent summaries

### 8. Text Translation
```
Input: "Hello, world! DSPy is a great tool for building AI applications."
Output: Merhaba dünya! DSPy, yapay zeka uygulamaları geliştirmek için harika bir araçtır.
```
Implementation ([`translateTextExample`](basic_dspy_example.py#L136-L144))
- Translates text to specified target language
- Uses `ChainOfThought` for accurate translation
- Maintains context and meaning

### 9. Basic Prediction
```
Question: "What is the capital of Germany?"
Answer: "Berlin"
```
Implementation ([`basicPredictExample`](basic_dspy_example.py#L147-L151))
- Simple question-answering using `dspy.Predict`
- Direct prediction without complex reasoning
- Demonstrates basic model usage

### 10. Multiple Choice Questions
```
Question: "Which planet is known as the Red Planet?"
Options: A) Venus, B) Mars, C) Jupiter, D) Saturn
```
Implementation ([`multipleChoiceExample`](basic_dspy_example.py#L154-L176))
- Custom `MultipleChoice` signature
- Uses `dspy.MultiChainComparison` and `dspy.Predict` for robust answers
- Provides reasoning for selected answer

### 11. Parallel Processing
```
Input: Multiple text snippets
Output: Category for each text
```
Implementation ([`parallelProcessingExample`](basic_dspy_example.py#L179-L194))
- Processes multiple inputs in parallel
- Uses `dspy.Parallel` for efficient execution
- Demonstrates batch processing capabilities

## DSPy Components Used

### ChainOfThought
- Used for complex reasoning tasks
- Breaks down problems into steps
- Provides transparent reasoning process

### ReAct
- Combines reasoning and actions
- Allows integration of custom tools
- Useful for interactive tasks

### Signature
- Defines input/output schemas
- Enables structured data handling
- Supports type hints and documentation

### Predict
- Simple prediction interface
- Direct question-answering
- Minimal configuration needed

### MultiChainComparison
- Compares multiple reasoning attempts
- Aggregates different model outputs
- Provides robust final answers

### Parallel
- Enables concurrent processing
- Configurable thread count
- Error handling and progress tracking

## Running Examples

Run any example using uv:
```bash
uv run basic_dspy_example.py
```

Or run specific functions by uncommenting them in the main block:
```python
if __name__ == "__main__":
    # Uncomment the example you want to run
    # getFloatAnswerExample()
    # GetBasicAnswer()
    # ...
```

## Performance Notes

All examples include execution time measurement. In our test run:
- Mac mini M4 Pro: 12-core CPU, 20-core GPU, 64GB unified memory
- Total execution time: ~27.5 seconds (Total time taken: 27593.65ms)
- Each example runs sequentially
- Performance may vary based on model and system configuration

### Parallel Execution
You can run the examples in parallel using asyncio for better performance. Note that you'll need to configure Ollama for parallel execution:

```python
import asyncio
import time

async def run_example(func):
    return await asyncio.to_thread(func)

async def main():
    start_time = time.time()
    
    tasks = [
        run_example(getFloatAnswerExample),
        run_example(GetBasicAnswer),
        run_example(ragExampleWithMjApi),
        run_example(RagWithDataExtractionExample),
        run_example(reActWithRag),
        run_example(countLetterInWord),
        run_example(summarizeTextExample),
        run_example(translateTextExample),
        run_example(basicPredictExample),
        run_example(multipleChoiceExample),
        run_example(parallelProcessingExample)
    ]
    
    await asyncio.gather(*tasks)
    
    elapsed_ms = (time.time() - start_time) * 1000
    print(f"\nTotal time taken: {elapsed_ms:.2f}ms")

if __name__ == "__main__":
    asyncio.run(main())

# Total execution time: ~25.6 seconds (25618.63ms)
```

### Ollama Configuration
To enable parallel requests in Ollama, set the following environment variable:
```bash
export OLLAMA_NUM_PARALLEL=8  # Adjust based on your system's capabilities
```

Or add to your system configuration:
```xml
<key>OLLAMA_NUM_PARALLEL</key>
<string>8</string>
```
This allows Ollama to handle multiple requests simultaneously, significantly improving performance when running examples in parallel.

DSPy provides built-in observability features for debugging and monitoring your AI systems. 
