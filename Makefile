# Makefile to run Main.py
.PHONY: run clean

# Define the Python interpreter
PYTHON = python3

# The main Python file and the executable name
MAIN_FILE = Main.py
EXECUTABLE = VMTranslator

# Default target: create the executable
all: $(EXECUTABLE)

# Create an executable file called VMTranslator
$(EXECUTABLE): $(MAIN_FILE)
	echo "#!/usr/bin/env $(PYTHON)" > $(EXECUTABLE)
	cat $(MAIN_FILE) >> $(EXECUTABLE)
	chmod +x $(EXECUTABLE)

# Clean target to remove the generated VMTranslator executable
clean:
	rm -f $(EXECUTABLE)
