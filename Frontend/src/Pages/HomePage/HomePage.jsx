import React, { useState } from "react";
import './HomePage.css';
import LogoPng from '../../assets/logo.png'

const HomePage = () => {
    const [srcImg, setSrcImg] = useState(LogoPng)
    const GrabImage = async () => {
        try{
            const response = await fetch('/api/image');
            const blob = await response.blob();  
            if(!response.ok){
                console.log("There was an error recieving image")
            }
            const url = URL.createObjectURL(blob);
            console.log("Url Recieved", url)
            // Your OpenAI API key
            const API_KEY = import.meta.env.VITE_API_BASE_URL;
            const API_URL = "https://api.openai.com/v1/chat/completions";


            // Function to call the OpenAI API
            async function callOpenAI(prompt) {
                const headers = {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${API_KEY}`
                };


                const data = {
                    model: "gpt-4-turbo",
                    messages: [
                        {
                            role: "user",
                            content: prompt
                        }
                    ],
                    max_tokens: 200,
                    temperature: 0.7,
                    n: 1,
                    stop: null
                };


                try {
                    const response = await fetch(API_URL, {
                        method: "POST",
                        headers: headers,
                        body: JSON.stringify(data)
                    });


                    if (!response.ok) {
                        throw new Error(`Error: ${response.status} - ${response.statusText}`);
                    }


                    const result = await response.json();
                    const reply = result.choices[0]?.message?.content;


                    console.log("OpenAI Response:", reply);
                    return reply;
                } catch (error) {
                    console.error("API Error:", error);
                    return null;
                }
            }

            const genres = [
                "acoustic", "afrobeat", "alt-rock", "alternative", "ambient", "anime", "black-metal", "bluegrass", 
                "blues", "bossanova", "brazil", "breakbeat", "british", "cantopop", "chicago-house", "children", 
                "chill", "classical", "club", "comedy", "country", "dance", "dancehall", "death-metal", "deep-house", 
                "detroit-techno", "disco", "disney", "drum-and-bass", "dub", "dubstep", "edm", "electro", 
                "electronic", "emo", "folk", "forro", "french", "funk", "garage", "german", "gospel", "goth", 
                "grindcore", "groove", "grunge", "guitar", "happy", "hard-rock", "hardcore", "hardstyle", 
                "heavy-metal", "hip-hop", "holidays", "honky-tonk", "house", "idm", "indian", "indie", "indie-pop", 
                "industrial", "iranian", "j-dance", "j-idol", "j-pop", "j-rock", "jazz", "k-pop", "kids", "latin", 
                "latino", "malay", "mandopop", "metal", "metal-misc", "metalcore", "minimal-techno", "movies", 
                "mpb", "new-age", "new-release", "opera", "pagode", "party", "philippines-opm", "piano", "pop", 
                "pop-film", "post-dubstep", "power-pop", "progressive-house", "psych-rock", "punk", "punk-rock", 
                "r-n-b", "rainy-day", "reggae", "reggaeton", "road-trip", "rock", "rock-n-roll", "rockabilly", 
                "romance", "sad", "salsa", "samba", "sertanejo", "show-tunes", "singer-songwriter", "ska", 
                "sleep", "songwriter", "soul", "soundtracks", "spanish", "study", "summer", "swedish", "synth-pop", 
                "tango", "techno", "trance", "trip-hop", "turkish", "work-out", "world-music"
            ];
            
           
            callOpenAI(`Based on the image above, give me 3 genres from this list that best describe the image: ${genres.join(', ')}  Make sure the three song genres you return are in this list. An example output would look like this; hip-hop%2ctrip-hop%2cromance`);
            

        }
        catch(error){
            console.log("An error occrured while fetching image", error.message)
        }
       


    }
    return(
        <>
            <div className="HomePageContainer">
                <div className="TextContainer">
                    <div className="Welcome">
                        <p>Certifed Compiler Boys Bring You:</p>
                        <p className="CompanyName">Vybe-Fynd3r</p>
                    </div>
                    <div class="CatchPhrase">
                        Vision To Vibes
                    </div>
                </div>
                <div className="ImageContainer">
                    <div className="ImgCont" onClick={GrabImage}>
                        <img src={srcImg}/>
                    </div>
                </div>
            </div>
        </>
    )

}

export default HomePage;
