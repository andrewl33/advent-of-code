#include <algorithm>
#include <fstream>
#include <functional>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

using namespace std;

typedef void (*OpCodeFunction)(int, int, int, int[]);

unordered_map<string, OpCodeFunction>
    opCodes({{"addr", [](int a, int b, int c, int l[]) {
                l[c] = l[a] + l[b];
              }},
             {"addi", [](int a, int b, int c, int l[]) {
                l[c] = l[a] + b;
              }},
             {"mulr", [](int a, int b, int c, int l[]) {
                l[c] = l[a] * l[b];
              }},
             {"muli", [](int a, int b, int c, int l[]) {
                l[c] = l[a] * b;
              }},
             {"banr", [](int a, int b, int c, int l[]) {
                l[c] = l[a] & l[b];
              }},
             {"bani", [](int a, int b, int c, int l[]) {
                l[c] = l[a] & b;
              }},
             {"borr", [](int a, int b, int c, int l[]) {
                l[c] = l[a] | l[b];
              }},
             {"bori", [](int a, int b, int c, int l[]) {
                l[c] = l[a] | b;
              }},
             {"setr", [](int a, int b, int c, int l[]) {
                l[c] = l[a];
              }},
             {"seti", [](int a, int b, int c, int l[]) {
                l[c] = a;
              }},
             {"gtir", [](int a, int b, int c, int l[]) {
                l[c] = a > l[b] ? 1 : 0;
              }},
             {"gtri", [](int a, int b, int c, int l[]) {
                l[c] = l[a] > b ? 1 : 0;
              }},
             {"gtrr", [](int a, int b, int c, int l[]) {
                l[c] = l[a] > l[b] ? 1 : 0;
              }},
             {"eqir", [](int a, int b, int c, int l[]) {
                l[c] = a == l[b] ? 1 : 0;
              }},
             {"eqri", [](int a, int b, int c, int l[]) {
                l[c] = l[a] == b ? 1 : 0;
              }},
             {"eqrr", [](int a, int b, int c, int l[]) {
                l[c] = l[a] == l[b] ? 1 : 0;
              }}});

void by_index_sol()
{
  // get data
  string input;
  ifstream infile;
  infile.open("input.txt");
  infile >> input;
  infile >> input;
  int ip = stoi(input);
  vector<vector<int>> res;
  vector<string> op_names(
      {"addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr",
       "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"});
  vector<function<void(int, int, int, int[])>> fns({[](int a, int b, int c, int l[]) {
                                                      l[c] = l[a] + l[b];
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = l[a] + b;
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = l[a] * l[b];
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = l[a] * b;
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = l[a] & l[b];
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = l[a] & b;
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = l[a] | l[b];
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = l[a] | b;
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = l[a];
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = a;
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = a > l[b] ? 1 : 0;
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = l[a] > b ? 1 : 0;
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = l[a] > l[b] ? 1 : 0;
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = a == l[b] ? 1 : 0;
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = l[a] == b ? 1 : 0;
                                                    },
                                                    [](int a, int b, int c, int l[]) {
                                                      l[c] = l[a] == l[b] ? 1 : 0;
                                                    }});
  while (getline(infile, input))
  {
    string title;
    vector<int> codes;
    istringstream iss(input);
    for (string s; iss >> s;)
    {
      vector<string>::iterator idx = find(op_names.begin(), op_names.end(), s);
      if (idx != op_names.end())
      {
        codes.push_back(idx - op_names.begin());
      }
      else
      {
        codes.push_back(stoi(s));
      }
    }
    res.push_back(codes);
  }
  res.erase(res.begin());
  int registers[6] = {0, 0, 0, 0, 0, 0};

  set<int> repeat_set;
  int top_set = 0;
  int count = 0;
  while (registers[ip] < res.size())
  {
    int inst = registers[ip];
    fns[res[inst][0]](res[inst][1], res[inst][2], res[inst][3], registers);

    registers[ip] += 1;
    if (registers[2] == 28)
    {
      if (repeat_set.find(registers[3]) == repeat_set.end())
      {
        cout << count << endl;
        count++;
        repeat_set.insert(registers[3]);
        top_set = registers[3];
      }
      else
      {
        cout << top_set << endl;
        break;
      }
    }
  }
}

// void sol()
// {
//   // get data
//   string input;
//   ifstream infile;
//   infile.open("input.txt");
//   infile >> input;
//   infile >> input;
//   int ip = stoi(input);
//   vector<pair<string, vector<int>>> res;
//   while (getline(infile, input))
//   {
//     string title;
//     vector<int> codes;
//     istringstream iss(input);
//     string s;
//     iss >> title;
//     for (string s; iss >> s;)
//     {
//       codes.push_back(stoi(s));
//     }
//     res.push_back(make_pair(title, codes));
//   }
//   res.erase(res.begin());
//   int registers[6] = {0, 0, 0, 0, 0, 0};

//   set<int> repeat_set;
//   int top_set = 0;
//   int count = 0;
//   while (registers[ip] < res.size())
//   {
//     pair<string, vector<int>> instructions = res[registers[ip]];
//     opCodes[instructions.first](instructions.second[0], instructions.second[1], instructions.second[2], registers);

//     registers[ip] += 1;
//     if (registers[2] == 28)
//     {
//       if (repeat_set.find(registers[3]) == repeat_set.end())
//       {
//         cout << count << endl;
//         count++;
//         repeat_set.insert(registers[3]);
//         top_set = registers[3];
//       }
//       else
//       {
//         cout << top_set << endl;
//         break;
//       }
//     }
//   }
// }

int main()
{
  by_index_sol();
  // sol();
  return 1;
}