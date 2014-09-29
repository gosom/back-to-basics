#include "Entry.h"
#include "search.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>

using std::cout;        using std::ifstream;
using std::to_string;    using std::string;
using std::endl;    using std::getline;
using std::cerr;    using std::vector;
using std::sort;


bool compare(const Entry& x, const Entry& y){
    return x.name < y.name;
}



float get_elapsed(const std::clock_t& begin_time,
                  const std::clock_t&end_time){
    return 1000 * (end_time - begin_time) / CLOCKS_PER_SEC;
}


int main(int argc, const char** argv){

    const string name = argv[1];

    for(int i=1; i<11; ++i){
        const string fname = "../data/" + to_string(i) + "_catalog.txt";
        ifstream infile(fname);

        if(!infile){
            cerr << "File " << fname << " does not exist" << endl;
            return 1;
        }

        vector<Entry> phonebook;

        string line;
        while(getline(infile, line)){
            Entry e = Entry(line);
            phonebook.push_back(e);
        }

        // sort the phonebook by name
        sort(phonebook.begin(), phonebook.end(), compare);

        // let' search for a non existing name using naive search
        std::clock_t begin_time = std::clock();
        int idx = naive_search(phonebook, name);
        std::clock_t end_time = std::clock();
        float elapsed = get_elapsed(begin_time, end_time);

        // the same using binary search
        begin_time = std::clock();
        idx = binary_search(phonebook, name);
        end_time = std::clock();
        float belapsed = get_elapsed(begin_time, end_time);

        cout << phonebook.size() << " - naive: " << elapsed;
        cout << " - binary: " << belapsed << " - position: " << idx << endl;
    }

    return 0;
}
