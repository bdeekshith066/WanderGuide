import streamlit as st
import streamlit.components.v1 as components




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
        <div class="gradient-text">Welcome to WanderGuide</div>
        """

    # Render the gradient text
    st.markdown(gradient_text_html, unsafe_allow_html=True)
    st.write(":orange[Your Banglore travel companion]")

    

    st.write('Planning a trip has never been easier with WanderGuide, your ultimate travel companion designed to simplify every step of your journey. Our platform provides comprehensive travel planning services that cater to your unique needs and preferences. Whether you are looking to explore exotic destinations, plan a family vacation, or embark on a solo adventure, WanderGuide ensures a seamless and enjoyable travel experience. With personalized itineraries, budget-friendly options, and expert recommendations, we take the hassle out of travel planning, allowing you to focus on making unforgettable memories.')
    
    
    col4, col5,col7, col6, col7 = st.columns([0.06,0.45,0.07,0.5, 0.06])
    with col5:
        st.write('')
        st.write('')
        st.write('')
        
        components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
  margin: 0; /* Remove default margin */
  padding: 0; /* Remove default padding */
}
body {
  font-family: Verdana, sans-serif;
}
.mySlides {
  display: none;
}
img {
  vertical-align: middle;
  width: 100%; /* Make images fill their containers */
  margin: 0; /* Remove any margin */
  padding: 0; /* Remove any padding */
}
/* Slideshow container */
.slideshow-container {
  max-width: 400px;
  max-height : 400px;
  position: 100%;
  margin: 0;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}
/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.9s;
}
@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}
</style>
</head>
<body>
<div class="slideshow-container">
  <div class="mySlides fade">
    <div class="numbertext">1 / 4</div>
    <img src="https://static.toiimg.com/photo/54559212.cms">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">2 / 4</div>
    <img src="https://bangaloreepicure.com/wp-content/uploads/2016/06/ub_city.jpg">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">3 / 4</div>
    <img src="https://www.fabhotels.com/blog/wp-content/uploads/2020/03/Cubbon-Park-Bangalore-600.jpg">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">4 / 4</div>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBgRiaIKTD7cuuzBOORQMAP0QCvY_wc1wxfQ&s">
    
  </div>
</div>
<script>
  let slideIndex = 0;
  showSlides();

  function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    slides[slideIndex-1].style.display = "block";  
    setTimeout(showSlides, 2000); // Change image every 2 seconds
  }
</script>
</body>
</html>
    """,
    height=300, width=400
)
    

    with col6:
        st.write('')
        st.write('')
        tab0, tab1= st.tabs(["WanderGuide", "About Us"])

        with tab0:
            st.write(" - :orange[Multilingual Support]: Chatbots assist users in their preferred language for seamless travel planning.")
            st.write(" - :orange[Personalized Itineraries]: Get custom travel plans based on your interests and preferences. ")
            st.write(" - :orange[Real-Time Assistance]: Available 24/7 to adapt and update travel plans as needed.")
            st.write(" - :orange[Local Insights]: Receive valuable tips on local attractions and customs.")
            st.write(" - :orange[Budget-Friendly Solutions]: Optimize travel expenses while ensuring a great experience.")
                


   
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.image('divider.png')
    st.write('')
    st.write('')
    col1,col2,col3 = st.columns([0.5,1,0.5])
    with col2:
        st.write('   Project by team - : - Varsha , Yashaswini, Vinti ')
    
    
if __name__ == "__main__":
    app()
    
