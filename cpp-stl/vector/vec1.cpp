#include <vector>
#include <iostream>
using namespace std;

vector<int> get_vec();

int main() {
    vector<int> nums1 {4, 5, 8};
    nums1.push_back(9);
    nums1.insert(begin(nums1) + 2, 6);
    nums1.insert(nums1.end()-2, 7);
    cout << "nums1: ";
    for (auto it = nums1.begin(); it != nums1.end(); it++) {
        cout << *it << " ";
    }    // nums1 = {4, 5, 6, 7, 8, 9}
    cout << endl;

    vector<string> ss {"cpp", "stl"};
    string s_arr[] = {"zhihu", "zhuanlan"};
    cout << "ss: ";
    ss.insert(ss.begin(), begin(s_arr), end(s_arr));
    for (const auto& s : ss) {
        cout << s << " ";
    }  // ss = {"zhihu", "zhuanlan", "cpp", "stl"}
    cout << endl;

    vector<int> nums2 = get_vec();
    nums2.reserve(10);
    cout << "nums2: ";
    nums2.insert(nums2.end(), nums1.begin(), nums1.end());
    for (const int& t : nums2) {
        cout << t << " ";
    }
    cout << endl;
}

vector<int> get_vec() {
    return {1, 2, 3};
}
