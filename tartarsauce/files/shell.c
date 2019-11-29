#include <unistd.h>
#include <sys/types.h>
#include <grp.h>
#include <stdio.h>

int main (int argc, char** argv) {
  gid_t newGrp = 0;

  if (setuid(0) != 0) {
    perror("ERROR");
    return 1;
  }
  setgid(0);
  seteuid(0);
  setegid(0);
  setgroups(1, &newGrp);

  execvp("/bin/bash", argv);

  return 0;
}
