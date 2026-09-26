        for (char c : s) {
            if (c == '(') {
                addKey = true;
            } else if (c == ')') {
                if (dict.count(key) > 0) {
                    res += dict[key];
                } else {
                    res.push_back('?');
                }
                addKey = false;
                key.clear();
            } else if (addKey) {
                key.push_back(c);
            } else {
                res.push_back(c);
            }
        }
    }
};
        string key, res;
