
#include "Entry.h"
#include <string>
#include <vector>
#include <boost/algorithm/string.hpp>


Entry::Entry(const std::string &line){
    std::vector<std::string> v;
    boost::split(v, line, boost::is_any_of("\t"));
    name = v[0];
    phone = v[1];
}
