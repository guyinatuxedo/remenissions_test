#include <stdio.h>
#include <string.h>


#define ROWS 8
#define COLS 8

#define C_RED "31"
#define C_YELLOW "33"
#define C_GREEN "32"
#define C_BLUE "34"
#define C_WHITE "37"
#define B_RED "101"

#define T_ESC(body) "\x1b[" body "m"
#define T_END "m"
#define T_BRIGHT ";1"
#define TC_RESET T_ESC()
#define TC_WHITE T_ESC(C_WHITE T_BRIGHT)
#define TC_ERROR T_ESC(B_RED T_BRIGHT ";" C_WHITE)


const char* row_colors[] = {
  [0 ... 3] = C_GREEN,
  [4 ... 5] = C_YELLOW,
  [6]       = C_WHITE,
  [7]       = C_RED,
};

char expected[ROWS*COLS];

void init_visualize(char* buff) {
  for (int i = 0; i < ROWS * COLS; i++) 
    expected[i] = buff[i];
}

void visualize(char* buff) {
  int i = 0;
  char format_str[20];

  puts("");
  puts("Legend: "T_ESC(C_GREEN) "buff " T_ESC(C_GREEN T_BRIGHT) "MODIFIED "
       TC_RESET T_ESC(C_YELLOW) "padding " T_ESC(C_YELLOW T_BRIGHT) "MODIFIED\n  "
       TC_RESET T_ESC(C_BLUE) "notsecret " T_ESC(C_BLUE T_BRIGHT) "MODIFIED "
       TC_RESET T_ESC(C_BLUE) "secret " T_ESC(C_BLUE T_BRIGHT) "MODIFIED\n  " 
       TC_RESET T_ESC(C_RED) "return address " T_ESC(C_RED T_BRIGHT) "MODIFIED" 
       TC_RESET);
  for (int r = 0; r < ROWS; r++) {
    printf("%p "TC_WHITE"| ", buff + r * COLS);
    for (int c = 0; c < COLS; c++) {
      if (row_colors[r] == C_RED && c < 4) {
        sprintf(format_str, T_ESC("0;%s%s"), C_WHITE,
          (buff[i] == expected[i]) ? "" : T_BRIGHT);
      } else {
        sprintf(format_str, T_ESC("0;%s%s"), row_colors[r],
          (buff[i] == expected[i]) ? "" : T_BRIGHT);
      }
      
      printf("%s%02x"TC_RESET" ", format_str, buff[i] & 0xff);
      i++;
    }
    puts(TC_WHITE"|"TC_RESET);
  }

  printf("Return address: 0x%08x\n", *(int*)((buff + 7*8 + 4)));
  puts("");
}
