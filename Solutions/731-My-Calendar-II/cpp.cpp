class MyCalendarTwo {
public:
    MyCalendarTwo() {
        
    }
    
    bool book(int start, int end) {
        for (auto p : overlap) {
            if (((start >= p.second) || (end <= p.first)))
                continue;
            else
                return false;
        }
        for (auto k : cal) {
            if (((start >= k.second) || (end <= k.first)))
                continue;
            else
                overlap.insert({max(k.first, start), min(k.second, end)});
        }
        cal.insert({start, end});
        return true;
    }
private:
    set<pair<int, int>> cal;
    set<pair<int, int>> overlap;
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * bool param_1 = obj.book(start,end);
 */