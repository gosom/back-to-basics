#ifndef GUARD_entry_h
#define GUARD_entry_h

#include <string>

class Entry{

public:
    Entry();
    Entry(const std::string &line);

    std::string name;
    std::string phone;

    std::string repr() const { return name + "\t" + phone; };

};

#endif
