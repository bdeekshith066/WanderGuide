import google.generativeai as genai
import streamlit as st
import time
import toml

# Load the API key from the config file
config = toml.load('config.toml')
api_key = config['api_keys']['gemini']

# Streamlit app layout configuration
def app():
    gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 2.9em;
        }
        </style>
        <div class="gradient-text">Travel Assistant</div>
        """

    # Render the gradient text
    st.markdown(gradient_text_html, unsafe_allow_html=True)
    
    st.image('divider.png')

    st.write("""
    Please provide the following details in the text area below:
    1. Place you want to visit
    2. Number of people
    3. Budget
    4. Number of days
    5. Interests and preferences (e.g., adventure, relaxation, historical sites)
    6. Accommodation preferences (e.g., hotel, hostel, Airbnb)
    7. Mode of travel (e.g., flight, train, car)
    """)

    # Text area for user input
    user_input = st.text_area("Enter your travel details here:")

    # Configure the Gemini API with the loaded API key
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat()

    def generate_travel_itinerary(user_input):
        prompt = f"""
        Travel Information:
        {user_input}
        
        Please act as a professional travel assistant and provide the following:
        1. A brief assessment based on the provided information.
        2. A detailed travel itinerary in a table format, including daily activities, accommodations, and travel arrangements.
        3. Recommendations and precautions for the traveler to ensure a safe and enjoyable trip.

        The itinerary should cover:
        - Daily activities
        - Suggested places to visit
        - Accommodation options
        - Dining recommendations
        - Travel arrangements

        Ensure that the activities and accommodations are appropriate based on the provided budget and preferences.
        """

        full_response = ""
        try:
            for chunk in chat.send_message(prompt, stream=True):
                full_response += chunk.text
        except genai.types.generation_types.BlockedPromptException as e:
            st.exception(e)
        except Exception as e:
            st.exception(e)

        return full_response

    if st.button("Generate Travel Itinerary"):
        with st.spinner("Generating travel itinerary..."):
            time.sleep(4)
            generated_itinerary = generate_travel_itinerary(user_input)
            st.success(generated_itinerary)

if __name__ == "__main__":
    app()
