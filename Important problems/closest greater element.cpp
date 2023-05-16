// closest greater element

#include <iostream>
#include <vector>

using namespace std;

vector<int> closestGreater(vector<int>& arr) {
    vector<int> result(arr.size(), -1);
    for (int i = 0; i < arr.size(); i++) {
        int closest = -1;
        for (int j = i + 1; j < arr.size(); j++) {
            if (arr[j] > arr[i]) {
                closest = arr[j];
                break;
            }
        }
        result[i] = closest;
    }
    return result;
}

int main() {
    vector<int> arr = {4, 2, 7, 5, 8, 1, 9};
    vector<int> result = closestGreater(arr);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}

// basic n^2 algorithm

