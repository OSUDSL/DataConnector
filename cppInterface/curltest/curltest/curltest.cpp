#include <iostream>
#include <curl/curl.h>
#include <string>
#include <map>
#include <sstream>
#include <profileapi.h>

std::string makeJson(std::map<std::string, float>);
CURL* curlHandleInit(const char* server);
void curlHandleCleanup(CURL* handle);
CURLcode sendRequest(CURL* handle, const char* jsonData);

int main()
{	
	//std::map<std::string, float> mp = { {"Velocity", (float)434}, {"SimTime", (float)654} };
	std::map<std::string, float> mp = {};
	std::string str = makeJson(mp);
	const char * putJson = str.c_str();

	CURL * handle = curlHandleInit("http://127.0.0.1:500/update");
	CURLcode res = sendRequest(handle, putJson);
	if (res != CURLE_OK) {
		fprintf(stderr, "failed: %s", curl_easy_strerror(res));
	}

	curlHandleCleanup(handle);
	return 0;
}

std::string makeJson(std::map<std::string, float> mp) {
	std::ostringstream os;
	std::map<std::string, float>::iterator it = mp.begin();

	// Iterate through the map and print the elements
	os << "{ ";
	while (it != mp.end()) {
		os << "\"" << it->first << "\" : " << it->second;
		if (++it != mp.end()) {
			os << ", ";
		}
	}
	os << " }";
	return os.str();
}

CURL* curlHandleInit(const char* server) {
	CURL * handle = curl_easy_init();

	struct curl_slist *slist1 = NULL;
	slist1 = curl_slist_append(slist1, "Content-Type: application/json");
	slist1 = curl_slist_append(slist1, "Accept: application/json");
	
	curl_easy_setopt(handle, CURLOPT_HTTPHEADER, slist1);
	curl_easy_setopt(handle, CURLOPT_URL, server);
	curl_easy_setopt(handle, CURLOPT_CONNECTTIMEOUT_MS, 50);
	curl_easy_setopt(handle, CURLOPT_HAPPY_EYEBALLS_TIMEOUT_MS, 10);
	return handle;
}

void curlHandleCleanup(CURL* handle) {
	curl_easy_cleanup(handle);
}

CURLcode sendRequest(CURL* handle, const char* jsonData) {
	curl_easy_setopt(handle, CURLOPT_POSTFIELDS, jsonData);
	return curl_easy_perform(handle);
}