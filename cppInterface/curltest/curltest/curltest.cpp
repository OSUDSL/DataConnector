#include <iostream>
#include <curl/curl.h>
#include <string>
#include <map>
#include <sstream>

std::string makeJson(std::string server, std::map<std::string, float>);

int main()
{	
	const char *putJson = "{\"Velocity\": 50, \"SimTime\": 124}";

	CURL * handle = curl_easy_init();

	struct curl_slist *slist1 = NULL;
	slist1 = curl_slist_append(slist1, "Content-Type: application/json");
	slist1 = curl_slist_append(slist1, "Accept: application/json");
	curl_easy_setopt(handle, CURLOPT_HTTPHEADER, slist1);
	curl_easy_setopt(handle, CURLOPT_URL, "http://localhost:5000/update");

	curl_easy_setopt(handle, CURLOPT_POSTFIELDS, putJson);
	curl_easy_perform(handle);
}

std::string makeJson(std::string server, std::map<std::string, float> mp) {
	std::ostringstream os;
	std::map<std::string, float>::iterator it = mp.begin();

	// Iterate through the map and print the elements
	os << "{ ";
	while (it != mp.end()) {
		os << "\"" << it->first << "\" : " << it->second << "\"";
		if (++it != mp.end()) {
			os << ", ";
		}
	}
	return os.str();
}
/*
Make a function that (uses sprintf) has a string input of server name/address, 
map of string to float
function constructs the json string for the map (using sprintf and a loop)

Make another function to execute the post request
*/
