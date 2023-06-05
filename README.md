## Vodka Assistant

Vodka Assistant is a Python script that functions as a voice-controlled personal assistant. It utilizes various libraries and modules to perform tasks such as retrieving information from Wikipedia, performing web searches, providing system information, and more.

### Features

- Speech recognition: The assistant listens to voice commands from the user using the `speech_recognition` library.
- Text-to-speech: The assistant responds to the user's commands by converting text into speech using the `pyttsx3` library.
- Current time: The assistant can tell the current time when prompted.
- Web search: The assistant can perform web searches using the default web browser.
- Wikipedia search: The assistant can search for information on Wikipedia and provide a summary of the search query.
- Network information: The assistant can retrieve information about the network, including the hostname and IP address.
- System information: The assistant can provide information about the system, including the operating system, release, version, machine, and processor.

### Prerequisites

To run the Vodka Assistant script, you need to have the following prerequisites installed:

- Python 3.x
- Required Python packages: `speech_recognition`, `pyttsx3`, `datetime`, `wikipedia`, `webbrowser`, `os`, `subprocess`, `socket`, `platform`

### Usage

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the required Python packages by running the following command:
   ```
   pip install -r requirements.txt
   ```
4. Run the script by executing the following command:
   ```
   python assistant.py
   ```
5. The assistant will start running and will greet you with a message.
6. Start giving voice commands to the assistant and it will respond accordingly.

### Supported Commands

- "Время" (Time): Retrieves and speaks the current time.
- "Поиск [query]" (Search [query]): Performs a web search for the specified query.
- "Википедия [query]" (Wikipedia [query]): Searches for the specified query on Wikipedia and provides a summary.
- "Мой IP" (My IP): Retrieves and speaks the IP address of the current machine.
- "Информация о железе" (System information): Provides information about the system, including the operating system, release, version, machine, and processor.
- "Умри" (Exit): Exits the assistant.
