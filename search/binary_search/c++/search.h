#ifndef GUARD_search_h
#define GUARD_search_h

#include "Entry.h"
#include <vector>
#include <string>

int naive_search(const std::vector<Entry>& v, const std::string& name);

int binary_search(const std::vector<Entry>& v, const std::string& name);

#endif
