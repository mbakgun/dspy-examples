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

<details>
<summary><strong>1. Probability Calculation: getFloatAnswerExample</strong></summary>

```
Question: "Three dice are tossed. What is the probability that the sum equals 3?"
Answer: 0.00462963
```
Implementation ([`getFloatAnswerExample`](basic_dspy_example.py#L21-L26))
- Uses `ChainOfThought` for mathematical reasoning
- Returns floating-point probability value
- Simple one-step calculation with direct output
</details>

<details>
<summary><strong>2. Basic Question Answering: GetBasicAnswer</strong></summary>

```
Question: "Turkey is a country in which continent?"
Answer: "Europe"
Reasoning: "The continent that Turkey is located on can be determined by considering its geographical position."
```
Implementation ([`GetBasicAnswer`](basic_dspy_example.py#L29-L42))
- Uses `dspy.Signature` to define input/output structure
- Provides factoid answers with reasoning
- Demonstrates basic question-answering pattern
</details>

<details>
<summary><strong>3. External API Integration: ragExampleWithMjApi</strong></summary>

```
Question: "What is the github repo of the Mj API?"
Answer: "The GitHub repository of the Mj API is https://s.akgns.com/3Aw"
```
Implementation ([`ragExampleWithMjApi`](basic_dspy_example.py#L45-L51))
- Fetches data from mj.akgns.com
- Uses RAG (Retrieval Augmented Generation)
- Processes external API response as context
</details>

<details>
<summary><strong>4. Data Extraction: RagWithDataExtractionExample</strong></summary>

```
Page Size: 20
Interval Minutes: 60
Total Images: 400
```
Implementation ([`RagWithDataExtractionExample`](basic_dspy_example.py#L54-L69))
- Extracts structured data from API response
- Defines specific output fields with types
- Uses `dspy.Signature` for schema definition
</details>

<details>
<summary><strong>5. Time Conversion: reActWithRag</strong></summary>

```
Interval in minutes: 60
Interval in seconds: 3600
```
Implementation ([`reActWithRag`](basic_dspy_example.py#L72-L89))
- Uses ReAct pattern with custom math tool
- Combines API data with calculation
- Demonstrates tool integration
</details>

<details>
<summary><strong>6. String Analysis: countLetterInWord</strong></summary>

```
Word: "strawberry"
Letter 'r' count: 3
```
Implementation ([`countLetterInWord`](basic_dspy_example.py#L92-L117))
- Custom tool for letter counting
- Uses ReAct for simple text analysis
- Shows basic tool usage pattern
</details>

<details>
<summary><strong>7. Text Summarization: summarizeTextExample</strong></summary>

```
Input: Long text about DSPy framework
Output: Concise summary of DSPy's key features
```
Implementation ([`summarizeTextExample`](basic_dspy_example.py#L120-L134))
- Uses `ChainOfThought` for text summarization
- Processes multi-sentence input text
- Generates concise, coherent summaries
</details>

<details>
<summary><strong>8. Text Translation: translateTextExample</strong></summary>

```
Input: "Hello, world! DSPy is a great tool for building AI applications."
Output: Merhaba dünya! DSPy, yapay zeka uygulamaları geliştirmek için harika bir araçtır.
```
Implementation ([`translateTextExample`](basic_dspy_example.py#L137-L145))
- Translates text to specified target language
- Uses `ChainOfThought` for accurate translation
- Maintains context and meaning
</details>

<details>
<summary><strong>9. Basic Prediction: basicPredictExample</strong></summary>

```
Question: "What is the capital of Germany?"
Answer: "Berlin"
```
Implementation ([`basicPredictExample`](basic_dspy_example.py#L148-L152))
- Simple question-answering using `dspy.Predict`
- Direct prediction without complex reasoning
- Demonstrates basic model usage
</details>

<details>
<summary><strong>10. Multiple Choice Questions: multipleChoiceExample</strong></summary>

```
Question: "Which planet is known as the Red Planet?"
Options: A) Venus, B) Mars, C) Jupiter, D) Saturn
```
Implementation ([`multipleChoiceExample`](basic_dspy_example.py#L155-L178))
- Custom `MultipleChoice` signature
- Uses `dspy.MultiChainComparison` and `dspy.Predict` for robust answers
- Provides reasoning for selected answer
</details>

<details>
<summary><strong>11. Parallel Processing: parallelProcessingExample</strong></summary>

```
Input: Multiple text snippets
Output: Category for each text
```
Implementation ([`parallelProcessingExample`](basic_dspy_example.py#L181-L196))
- Processes multiple inputs in parallel
- Uses `dspy.Parallel` for efficient execution
- Demonstrates batch processing capabilities
</details>

<details>
<summary><strong>12. Typed Chain of Thought with JSON: typedChainOfThoughtExample</strong></summary>

```
Input: Question about Naruto's friends
Output: Structured JSON data with character names and clans
```
Implementation ([`typedChainOfThoughtExample`](basic_dspy_example.py#L199-L219))
- Uses `ChainOfThought` for structured reasoning
- Processes JSON input and generates structured output
- Demonstrates complex reasoning with JSON
</details>

<details>
<summary><strong>13. Stacked LLM Calls: stackedLLMCallsExample</strong></summary>

```
Question: "What is the total years between the Roman Empire's founding and the fall of Rome?"
Thought Process: Step-by-step historical analysis
Final Answer: 503
```
Implementation ([`stackedLLMCallsExample`](basic_dspy_example.py#L222-L243))
- Uses multiple LLM calls to answer a complex question
- Demonstrates the ability to integrate multiple models
- Shows how to handle multi-step reasoning
</details>

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

### Prediction
- Stores and manages LLM response outputs
- Provides access to step-by-step reasoning process
- Captures intermediate thoughts and final answers
- Supports accessing multiple model completions

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

Example console outputs can be found in [console_logs.txt](console_logs.txt).

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
- Total execution time: ~31.6 seconds (Total time taken: 31654.63ms)
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
        run_example(parallelProcessingExample),
        run_example(typedChainOfThoughtExample),
        run_example(stackedLLMCallsExample)
    ]
    
    await asyncio.gather(*tasks)
    
    elapsed_ms = (time.time() - start_time) * 1000
    print(f"\nTotal time taken: {elapsed_ms:.2f}ms")

if __name__ == "__main__":
    asyncio.run(main())

# Total execution time: ~29.7 seconds (29714.53ms)
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
