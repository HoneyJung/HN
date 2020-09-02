#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int get_cheat_score(string answer, string first, string second) {
   int total_chear = 0;
   int tmp_long = 0, longest = 0;
   int sheet_size = answer.size();

   for (int i = 0; i < sheet_size; i++) {
      if (first.at(i) == second.at(i)) { // 학생 답안지 비교
         if (answer.at(i) != first.at(i)) { // 정답과 비교
            tmp_long++;
            total_chear++;
         }
         else {
            if (tmp_long > longest) // 길게 연결된 답안 길이
               longest = tmp_long;
            tmp_long = 0;
         }
      }
      else {
         if (tmp_long > longest) 
            longest = tmp_long;
         tmp_long = 0;
      }

   }

   if (tmp_long > longest)
      longest = tmp_long;

   return total_chear + longest * longest;
}

int solution(string answer_sheet, vector<string> sheets) {
   int answer = -1;
   int longest = -1;
   int num_students = sheets.size();

   for (int i = 0; i < num_students; i++) {
      for (int j = i + 1; j < num_students; j++) {
         int tmp = get_cheat_score(answer_sheet, sheets.at(i), sheets.at(j));
         if (tmp > answer)   
            answer = tmp;
      }
   }

   return answer;
}