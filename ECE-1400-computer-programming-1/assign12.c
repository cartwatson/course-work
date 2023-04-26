/***************************************************************************************
	Function title: Program 12
	Author: Jethro Watson

	Inputs: User
	Outputs: Print to screen

	Summary: user inputs possible dialing code, if input is a real dialing code
			 corresponding country is printed, if input is not a real dialing code
			 error message is printed

	Compile Instructions: Use Visual Studio

****************************************************************************************
									PSEUDOCODE
BEGIN
	STRUCT dialing_code
	ASK USER FOR DIALING CODE
	SEARCH FOR MATCHING DIALING CODE IN LOOP
	IF MATCHING CODE IS FOUND 
		PRINT COUNTRY AND CODE
		END
	ELSE
		PRINT ERROR
		END
***************************************************************************************/

#include <stdio.h>

#define COUNTRY_COUNT ((int) (sizeof(country_codes) / sizeof(country_codes[0])))

struct dialing_code {
	char* country;
	int code;
};

const struct dialing_code country_codes[] = 
  {{"Argentina",            54}, {"Bangladesh",      880},
   {"Brazil",               55}, {"Burma (Myanmar)",  95},
   {"China",                86}, {"Colombia",         57},
   {"Congo, Dem. Rep. of", 243}, {"Egypt",            20},
   {"Ethiopia",            251}, {"France",           33},
   {"Germany",              49}, {"India",            91},
   {"Indonesia",            62}, {"Iran",             98},
   {"Italy",                39}, {"Japan",            81},
   {"Mexico",               52}, {"Nigeria",         234},
   {"Pakistan",             92}, {"Philippines",      63},
   {"Poland",               48}, {"Russia",            7},
   {"South Africa",         27}, {"South Korea",      82},
   {"Spain",                34}, {"Sudan",           249},
   {"Thailand",             66}, {"Turkey",           90},
   {"Ukraine",             380}, {"United Kingdom",   44},
   {"United States",         1}, {"Vietnam",          84}};

int main(void) {
	int code, i;

	printf("Enter dailing code: ");
	scanf_s("%d", &code);

	for (i = 0; i < COUNTRY_COUNT; i++) {
		if (code == country_codes[i].code) {
			printf("The country with the dialing code %d is %s\n", code, country_codes[i].country);
			return 0;
		}
	}

	printf("There is no country with dialing code %d\n", code);
	return 0;
}