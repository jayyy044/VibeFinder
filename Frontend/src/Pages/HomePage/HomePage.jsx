import React, { useState } from "react";
import './HomePage.css';
import LogoPng from '../../assets/logo.png'

const HomePage = () => {
    const [Page, setPage] = useState(false)
    const [apiResonse, setapiResponse] = useState()
    const GrabImage = async () => {
        try{
            const response = await fetch('/api');
            const data = await response.json();  
            if(!response.ok){
                console.log("There was an error recieving image")
            }
            console.log("Music Data", data)
            setapiResponse(data)
            setPage(true)

        }
        catch(error){
            console.log("An error occrured while fetching image", error.message)
        }
       


    }
    return(
        <>
            {!Page && (
                <div className="HomePageContainer">
                    <div className="TextContainer">
                        <div className="Welcome">
                            <p>Certified Compiler Boys Bring You:</p>
                            <p className="CompanyName">Vybe-Fynd3r</p>
                        </div>
                        <div className="CatchPhrase">
                            Vision To Vibes
                        </div>
                    </div>
                    <div className="ImageContainer">
                        <div className="ImgCont" onClick={GrabImage}>
                            <img src={LogoPng} alt="Logo" />
                        </div>
                    </div>
                </div>
            )}

            {Page && 
                 <div className="DataContainer">
                    {apiResonse.map((track, index) => (
                        <div key={index} className="TrackCard">
                            <img src={track[2]} alt={`${track[1]} cover`} /> {/* Image */}
                            <h1>{track[1]}</h1>
                            <h1>{`Artist: ${track[0]}`}</h1> {/* Artist Name */}
                             {/* Track Title */}
                            
                        </div>
                    ))}
                 </div>
            }
        </>
    )

}

export default HomePage;
