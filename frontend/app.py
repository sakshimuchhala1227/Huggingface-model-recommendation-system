import streamlit as st
import requests

# Title and description for the Streamlit app
st.title("Hugging Face Model Recommender")
st.write("Enter a prompt, and we'll recommend the best models for you.")

# Input for user to enter task description
user_prompt = st.text_input("Enter your task description here:")

# Button to trigger the recommendation process
if st.button("Recommend Models"):
    if user_prompt:
        # Send the prompt to the Flask API for recommendation
        response = requests.post("http://127.0.0.1:8000/recommend_models/", json={"user_prompt": user_prompt})
        
        # Check if the response is successful
        if response.status_code == 200:
            recommendations = response.json()
            
            # Display the recommended models
            st.write("Recommended Models:")
            for rec in recommendations:
                # Display each model's details
                st.write(f"**Model ID:** {rec['model_id']}")
                st.write(f"**Description:** {rec['description']}")
                st.write(f"**Tags:** {rec['tags']}")
                st.write(f"**Downloads:** {rec['downloads']}")
                st.write(f"**Likes:** {rec['likes']}")
                st.write(f"**Language:** {rec['language']}")
                st.write("---")  # Separator between models
        else:
            st.write("Error: Could not retrieve recommendations.")
    else:
        st.write("Please enter a task description.")



# import streamlit as st
# import requests

# # Title and description for the Streamlit app
# st.title("Hugging Face Model Recommender")
# st.write("Enter a prompt, and we'll recommend the best models for you.")

# # Input for user to enter task description
# user_prompt = st.text_input("Enter your task description here:")

# # Initialize session state to keep track of the start index for recommendations
# if "start_index" not in st.session_state:
#     st.session_state.start_index = 0

# # Button to trigger the recommendation process
# if st.button("Recommend Models"):
#     if user_prompt:
#         # Prepare data for POST request
#         request_data = {
#             "user_prompt": user_prompt,
#             "start_index": st.session_state.start_index,
#             "num_recommendations": 5
#         }

#         try:
#             # Send POST request to the FastAPI server
#             response = requests.post("http://127.0.0.1:8000/recommend_models/", json=request_data)

#             # Check if the response is successful (status code 200)
#             if response.status_code == 200:
#                 recommendations = response.json()
                
#                 # Display the recommended models
#                 st.write("Recommended Models:")
#                 for rec in recommendations:
#                     st.write(f"**Model ID:** {rec['model_id']}")
#                     st.write(f"**Description:** {rec['description']}")
#                     st.write(f"**Tags:** {rec['tags']}")
#                     st.write(f"**Downloads:** {rec['downloads']}")
#                     st.write(f"**Likes:** {rec['likes']}")
#                     st.write(f"**Language:** {rec['language']}")
#                     st.write("---")  # Separator between models

#                 # Pagination buttons
#                 if len(recommendations) == 5:  # Only show the "Next" button if there are more models
#                     if st.button("Next 5 models"):
#                         st.session_state.start_index += 5  # Move to the next page
#                         st.experimental_rerun()  # Rerun to update the recommendations with new start_index

#                 if st.session_state.start_index > 0:
#                     if st.button("Previous 5 models"):
#                         st.session_state.start_index -= 5  # Go back to the previous set
#                         st.experimental_rerun()  # Rerun to update the recommendations with new start_index

#             else:
#                 st.write("Error: Could not retrieve recommendations.")
#         except Exception as e:
#             st.write(f"An error occurred: {e}")
#     else:
#         st.write("Please enter a task description.")
