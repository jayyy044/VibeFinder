import React, { useState } from "react";
import './HomePage.css';
import LogoPng from '../../assets/logo.png'

const HomePage = () => {
    const GrabImage = async () => {
        try{
            const response = await fetch('/api/image');
            const blob = await response.blob();  
            if(!response.ok){
                console.log("There was an error recieving image")
            }
            const url = URL.createObjectURL(blob);
            console.log("Url Recieved", url)

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
                        <img src={LogoPng}/>
                    </div>
                </div>
            </div>
        </>
    )

}

export default HomePage;
