/**
 * Gotta practice a little bit of c++
 * It is hard to draw a board, because we don't know where 0,0 should start
 * 
 * door container that has a set of connections, in the format (int, int)
 * 
 * room container, is a set of rooms in (int, int)
 * 
 * rooms will always be odd
 * 
 * doors will always be even
 * */

#include <deque>
#include <iostream>
#include <fstream>
#include <functional>
#include <utility>
#include <set>
#include <string>
#include <unordered_map>

using namespace std;

// https://stackoverflow.com/questions/32685540/unordered-map-with-pair-as-key-not-compiling
struct pair_hash
{
  template <class T1, class T2>
  std::size_t operator()(const std::pair<T1, T2> &p) const
  {
    auto h1 = std::hash<T1>{}(p.first);
    auto h2 = std::hash<T2>{}(p.second);

    // Mainly for demonstration purposes, i.e. works but is overly simple
    // In the real world, use sth. like boost.hash_combine
    return h1 ^ h2;
  }
};

bool rec_fill(int i, int j, int *c, set<pair<int, int>> &doors, set<pair<int, int>> &rooms, string input)
{
  while (*c <= input.length())
  {
    switch (input[*c])
    {
    case '(':
      do
      {
        (*c)++;
      } while (rec_fill(i, j, c, doors, rooms, input));
      break;
    case ')':
      return false;
    case '|':
      return true;
    case 'N':
      rooms.insert(make_pair(i, j - 2));
      doors.insert(make_pair(i, j - 1));
      j -= 2;
      break;
    case 'E':
      rooms.insert(make_pair(i + 2, j));
      doors.insert(make_pair(i + 1, j));
      i += 2;
      break;
    case 'W':
      rooms.insert(make_pair(i - 2, j));
      doors.insert(make_pair(i - 1, j));
      i -= 2;
      break;
    case 'S':
      rooms.insert(make_pair(i, j + 2));
      doors.insert(make_pair(i, j + 1));
      j += 2;
      break;
    }
    (*c)++;
  }

  return true;
}

int sol(string a)
{
  // get input
  string input;
  ifstream infile;
  infile.open(a);
  infile >> input;
  input = input.substr(1, input.length() - 2);
  // define board
  set<pair<int, int>> doors;
  set<pair<int, int>> rooms;
  int global_counter = 0;

  rec_fill(0, 0, &global_counter, doors, rooms, input);

  // traverse and find
  unordered_map<pair<int, int>, int, pair_hash> counts = {
      {make_pair(0, 0), 0}}; // key: coordinate, val: depth, doors

  deque<pair<int, int>> dq;
  dq.push_back(make_pair(0, 0));

  while (!dq.empty())
  {
    pair<int, int> front = dq.front();
    dq.pop_front();

    int depth_count = counts[make_pair(front.first, front.second)];

    if (doors.find(make_pair(front.first + 1, front.second)) != doors.end() && counts.find(make_pair(front.first + 2, front.second)) == counts.end())
    {
      dq.push_back(make_pair(front.first + 2, front.second));
      counts[make_pair(front.first + 2, front.second)] = depth_count + 1;
    }
    if (doors.find(make_pair(front.first - 1, front.second)) != doors.end() && counts.find(make_pair(front.first - 2, front.second)) == counts.end())
    {
      dq.push_back(make_pair(front.first - 2, front.second));
      counts[make_pair(front.first - 2, front.second)] = depth_count + 1;
    }
    if (doors.find(make_pair(front.first, front.second + 1)) != doors.end() && counts.find(make_pair(front.first, front.second + 2)) == counts.end())
    {
      dq.push_back(make_pair(front.first, front.second + 2));
      counts[make_pair(front.first, front.second + 2)] = depth_count + 1;
    }
    if (doors.find(make_pair(front.first, front.second - 1)) != doors.end() && counts.find(make_pair(front.first, front.second - 2)) == counts.end())
    {
      dq.push_back(make_pair(front.first, front.second - 2));
      counts[make_pair(front.first, front.second - 2)] = depth_count + 1;
    }
  }

  int max_val = 0;
  int sum_over_1000 = 0;
  for (auto it : counts)
  {
    if (it.second > max_val)
    {
      max_val = it.second;
    }
    if (it.second >= 1000)
    {
      sum_over_1000++;
    }
  }
  cout << "Input traversal: " << global_counter << " Correct: " << input.size() + 1 << endl;
  cout << "Rooms: " << rooms.size() << " Doors: " << doors.size() << endl;
  cout << "Part 1: " << max_val << endl;
  cout << "Part 2: " << sum_over_1000 << endl;
  return max_val;
}

int main()
{
  cout << "Max Doors: " << sol("test1.txt") << " Correct: 10" << endl
       << endl;
  cout << "Max Doors: " << sol("test2.txt") << " Correct: 18" << endl
       << endl;
  cout << "Max Doors: " << sol("test3.txt") << " Correct: 23" << endl
       << endl;
  cout << "Max Doors: " << sol("test4.txt") << " Correct: 31" << endl
       << endl;
  cout << "Max Doors: " << sol("input.txt") << endl;

  return 0;
}