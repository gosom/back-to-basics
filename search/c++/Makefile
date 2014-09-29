CC=g++
CFLAGS=-c -Wall -std=c++11 -O
LDFLAGS=
SOURCES=main.cpp Entry.cpp search.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=search

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -rf *o $(EXECUTABLE)
