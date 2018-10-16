class MyCalendar {
public:
    MyCalendar() {
        
    }
    
    bool book(int start, int end) {
        auto it = time.lower_bound(start);
        if (it != time.end() && it->first < end)    return false;
        if (it != time.begin() && prev(it)->second > start) return false;
        time[start] = end;
        return true;
    }
private:
    map<int, int>time; // use map here because map is sorted
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * bool param_1 = obj.book(start,end);
 */