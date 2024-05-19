# import requests

# response = requests.get('https://devapi.beyondchats.com/api/get_message_with_sources')
# print(response.status_code)
# print(response.json())

# # success=response.json()['status'][0]['success']
# # print(success)



# import requests
# import streamlit as st

# # Step 1: Fetch Data from the API
# def fetch_data(api_url):
#     data = []
#     page = 1

#     while True:
#         response = requests.get(f"{api_url}?page={page}")
#         if response.status_code != 200:
#             print("Error:", response.status_code)
#             break
#         page_data = response.json()
#         if not page_data:
#             break
#         data.extend(page_data)
#         page += 1

#     return data

# # Step 2: Identify Citations
# def identify_citations(data):
#     citations = []

#     for item in data:
#         response_text = item['response']
#         sources = item['sources']
#         matched_sources = []

#         for source in sources:
#             if source['context'] in response_text:
#                 matched_sources.append(source)

#         citations.append(matched_sources)

#     return citations

# # Step 3: Create a User-Friendly UI using Streamlit
# def display_citations(citations):
#     st.title("Response Citations")

#     for index, citation in enumerate(citations, start=1):
#         st.subheader(f"Response {index}")
#         if citation:
#             for source in citation:
#                 st.write(f"Source ID: {source['id']}")
#                 st.write(f"Source Context: {source['context']}")
#                 if 'link' in source:
#                     st.write(f"Source Link: {source['link']}")
#                 st.write("---")
#         else:
#             st.write("No citations found for this response")
#         st.write("===")

# # Main function
# def main():
#     api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
#     data = fetch_data(api_url)
#     citations = identify_citations(data)
#     display_citations(citations)

# if __name__ == "__main__":
#     main()





import requests
import streamlit as st

# Step 1: Fetch Data from the API
def fetch_data(api_url):
    data = []
    page = 1

    while True:
        response = requests.get(f"{api_url}?page={page}")
        if response.status_code != 200:
            print("Error:", response.status_code)
            break
        page_data = response.json()
        if not page_data:
            break
        data.extend(page_data)
        page += 1

    return data

# Step 2: Identify Citations
def identify_citations(data):
    citations = []

    for item in data:
        response_text = item.get('response', '')  # Ensure response_text is a string
        sources = item.get('sources', [])        # Ensure sources is a list
        matched_sources = []

        for source in sources:
            if source.get('context', '') in response_text:
                matched_sources.append(source)

        citations.append(matched_sources)

    return citations

# Step 3: Create a User-Friendly UI using Streamlit
def display_citations(citations):
    st.title("Response Citations")

    for index, citation in enumerate(citations, start=1):
        st.subheader(f"Response {index}")
        if citation:
            for source in citation:
                st.write(f"Source ID: {source.get('id', '')}")
                st.write(f"Source Context: {source.get('context', '')}")
                st.write(f"Source Link: {source.get('link', '')}")
                st.write("---")
        else:
            st.write("No citations found for this response")
        st.write("===")

# Main function
def main():
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    data = fetch_data(api_url)
    citations = identify_citations(data)
    display_citations(citations)

if '__name__' == "_main_":
    main()