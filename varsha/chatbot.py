import streamlit as st
from googletrans import Translator

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
            font-size: 3em;
        }
        </style>
        <div class="gradient-text">Must Visit Places</div>
        """

    st.markdown(gradient_text_html, unsafe_allow_html=True) 
    st.write(":orange[Explore the vibrant city of Bangalore with our guide to its must-visit places, featuring detailed insights and travel tips.]") 
    st.image('varsha/divider.png')

    st.write('')

    target_languages = {
        "English": "en",
        "Hindi": "hi",
        "Kannada": "kn",
        "Malayalam": "ml",
        "Telugu": "te",
        "Tamil": "ta",
        "Punjabi": "pa",
        "French": "fr",
        "Spanish": "es",
        "German": "de"
    }
    # Introduction
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        st.button('Cubbon Park')
        st.write('')
        st.write('')
        st.write('')
        st.button('Iskon')
        st.write('')
        st.write('')
        st.write('')
        st.button('Lalbagh')
        st.write('')
        st.write('')
        st.write('')
        st.button('Wonderla')

    with col2:
        st.button('Planetorium')
        st.write('')
        st.write('')
        st.write('')
        st.button('Art of Living')
        st.write('')
        st.write('')
        st.write('')
        st.button('VV Puram Food Street')
        st.write('')
        st.write('')
        st.write('')
        st.button('UB City')

    with col3:
        st.button('Orion Mall')
        st.write('')
        st.write('')
        st.write('')
        st.button('Bannerghatta Zoo')
        st.write('')
        st.write('')
        st.write('')
        st.button('Bangalore Palace')
        st.write('')
        st.write('')
        st.write('')
        st.button('Kanteerava Stadium')
    
    
    with col4:
        st.button('Madiwala Lake')
        st.write('')
        st.write('')
        st.write('')
        st.button('MG Road')
        st.write('')
        st.write('')
        st.write('')
        st.button('Yediyur lake')
        st.write('')
        st.write('')
        st.write('')
        target_language = st.selectbox("Select Language", list(target_languages.keys()))
        
    # Language selection
    

    

    def get_pedia_info(user_input, target_language='en'):
        pedia_info = {
            "cubbon park": """ :orange[Cubbon Park]  \n A lush, green space in the heart of Bangalore, perfect for morning walks, picnics, and enjoying nature.  \n :orange[Highlights]  \n - Home to a variety of flora and fauna.  \n - The park also houses historical buildings like the State Central Library.  \n - Popular for yoga, jogging, and relaxing.  \n
            Enter the name of a place from the list to know more about it.""",

            "iskcon": """ :orange[ISKCON Temple]  \n A spiritual oasis in Bangalore, the ISKCON Temple is dedicated to Lord Krishna and offers a serene atmosphere for worship and meditation.  \n :orange[Highlights]  \n - Architectural grandeur with beautiful deities.  \n - Spiritual lectures, kirtans, and prasadam (holy food).  \n - Gift shop with spiritual books and artifacts.  \n
            Enter the name of a place from the list to know more about it.""",

            "lalbagh": """ :orange[Lalbagh Botanical Garden]  \n A famous botanical garden known for its glass house, diverse plant species, and stunning flower shows.  \n :orange[Highlights]  \n - Annual flower shows during Independence Day and Republic Day.  \n - The Lalbagh Rock, one of the oldest rock formations on earth.  \n - Peaceful environment for morning walks and nature photography.  \n
            Enter the name of a place from the list to know more about it.""",

            "wonderla": """ :orange[Wonderla]  \n An amusement park with thrilling rides, water slides, and entertainment options for all ages.  \n :orange[Highlights]  \n - Exciting roller coasters and wave pools.  \n - Safe and fun environment for family outings.  \n - Variety of food options and souvenir shops.  \n
            Enter the name of a place from the list to know more about it.""",

            "mg road": """ :orange[MG Road]  \n A bustling commercial street in Bangalore, known for its shopping, dining, and nightlife.  \n :orange[Highlights]  \n - A wide range of shops from high-end boutiques to local markets.  \n - Numerous cafes, pubs, and restaurants.  \n - Popular for evening strolls and people-watching.  \n
            Enter the name of a place from the list to know more about it.""",

            "planetorium": """ :orange[Jawaharlal Nehru Planetarium]  \n A center for astronomical studies and public science education, featuring engaging exhibits and shows.  \n :orange[Highlights]  \n - Regular sky-gazing sessions and educational programs.  \n - Interactive exhibits on space and astronomy.  \n - A great place for children and adults to learn about the cosmos.  \n
            Enter the name of a place from the list to know more about it.""",

            "art of living": """ :orange[Art of Living International Center]  \n A peaceful retreat center offering yoga, meditation, and wellness programs.  \n :orange[Highlights]  \n - Beautifully landscaped gardens and serene environment.  \n - Courses on stress management and spiritual growth.  \n - Volunteer opportunities and cultural events.  \n
            Enter the name of a place from the list to know more about it.""",

            "vv puram food street": """ :orange[VV Puram Food Street]  \n A foodie’s paradise offering a variety of local and street food delicacies.  \n :orange[Highlights]  \n - Famous for traditional South Indian snacks and sweets.  \n - Bustling atmosphere, especially in the evenings.  \n - Affordable and delicious food options.  \n
            Enter the name of a place from the list to know more about it.""",

            "ub city": """ :orange[UB City]  \n A luxury commercial complex with high-end stores, fine dining, and entertainment options.  \n :orange[Highlights]  \n - Premium brands and luxury shopping.  \n - Gourmet restaurants and cafes.  \n - Regular events, art exhibitions, and performances.  \n
            Enter the name of a place from the list to know more about it.""",

            "orion mall": """ :orange[Orion Mall]  \n A large shopping mall with a mix of retail, dining, and entertainment options.  \n :orange[Highlights]  \n - Wide range of shops, from international brands to local retailers.  \n - Multiplex cinema, bowling alley, and gaming arcade.  \n - Beautiful lakeside promenade for a relaxing experience.  \n
            Enter the name of a place from the list to know more about it.""",

            "bannerghatta zoo": """ :orange[Bannerghatta Biological Park]  \n A popular wildlife park featuring a zoo, safari, and butterfly park.  \n :orange[Highlights]  \n - Home to a variety of animals, including tigers, lions, and elephants.  \n - Safari rides offering close encounters with wildlife.  \n - Conservation and educational programs for visitors.  \n
            Enter the name of a place from the list to know more about it.""",

            "bangalore palace": """ :orange[Bangalore Palace]  \n A majestic palace known for its Tudor-style architecture and lavish interiors.  \n :orange[Highlights]  \n - Guided tours showcasing the palace's history and artifacts.  \n - Beautiful gardens and courtyards.  \n - Venue for various cultural events and concerts.  \n
            Enter the name of a place from the list to know more about it.""",

            "kanteerava stadium": """ :orange[Kanteerava Stadium]  \n A multi-purpose stadium hosting various sports events, especially athletics and football.  \n :orange[Highlights]  \n - Modern facilities for athletes and spectators.  \n - Regularly hosts national and international sporting events.  \n - Accessible location with good transport links.  \n
            Enter the name of a place from the list to know more about it.""",

            "madiwala lake": """ :orange[Madiwala Lake]  \n A serene lake perfect for bird watching, boating, and leisurely walks.  \n :orange[Highlights]  \n - Rich in birdlife, especially during migratory seasons.  \n - Boating facilities and beautiful sunset views.  \n - Peaceful spot for relaxation and photography.  \n
            Enter the name of a place from the list to know more about it.""",
        }

        user_input_lower = user_input.lower()

        if user_input_lower in pedia_info:
            translator = Translator()
            translation = translator.translate(pedia_info[user_input_lower], dest=target_language)
            return translation.text
        else:
            return "I'm sorry, I'm not sure which term you're asking about. Can you please provide more details?"

    if "fest_messages" not in st.session_state:
        st.session_state.fest_messages = [{"role": "assistant", "content": "Discover must visit places with our chatbot!"}]

    for message in st.session_state.fest_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter the Place name"):
        st.session_state.fest_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        language_code = target_languages[target_language]
        response = get_pedia_info(prompt, target_language=language_code)

        with st.spinner(text="Thinking..."):
            st.session_state.fest_messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.write(response, unsafe_allow_html=True)

if __name__ == "__main__":
    app()
