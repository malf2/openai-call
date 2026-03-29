# OpenAI Call

Welcome to the **openai-call** repository! This project contains a collection of Python scripts that I created while learning how to interact with the OpenAI API. I focused on the quickstart guide, text generation, and maintaining conversation state.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Installation

To use the scripts in this repository, you'll need to have Python and uv installed. Follow these steps to set up your environment:

1. Clone the repository:

   ```bash
   git clone https://github.com/malf2/openai-call.git
   ```

2. Change to the project directory:

   ```bash
   cd openai-call
   ```

3. Install the required packages:

   ```bash
   uv sync
   ```

4. Set your OpenAI API key as an environment variable:

   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

## Usage

After installation, you can run the scripts to interact with the OpenAI API. Here are some examples:

- To generate text using the GPT model, run:

  ```bash
  python text_prompt.py
  ```

- For maintaining conversation state, execute:

  ```bash
  python multiturn_conversation.py
  ```

Check the individual Python files for more details on specific functionalities and options.

## Features

- Text generation using the OpenAI API.
- Conversation state management for maintaining context in dialogues.
- Easy-to-follow examples for rapid learning and experimentation.

## Acknowledgments

- Thanks to OpenAI for providing an extensive and informative API.
- Special thanks to the community for support and resources that helped in learning.