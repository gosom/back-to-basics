#include "search.h"
#include "Entry.h"
#include <vector>
#include <string>

using std::string;  using std::vector;


int naive_search(const vector<Entry>& v, const string& name){
    for(vector<Entry>::size_type i=0; i!=v.size(); ++i){
        Entry e = v[i];
        if(e.name == name)
            return i;
    }
    return -1;
}

int binary_search(const vector<Entry>& v, const string& name){
    int low = 0;
    int high = v.size() - 1;
    int mid;
    while(low <= high){
        mid = (int) ((low + high) / 2);
        Entry e = v[mid];
        if(name == e.name)
            return mid;

        if(name < e.name)
            high = mid -1;
        else
            low = mid + 1;
    }
    return -(low + 1);
}

