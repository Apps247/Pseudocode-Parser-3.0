#include <iostream> 
using namespace std; 
int main (int argc, char *argv[]) 
{ 
    if (argc < 2){
        printf("Usage:\n./parse filename\n");
        return 1;
    }
    char* command = ("python3 parse.py %s", argv[1]);
    system(command);
	return 0; 
} 

